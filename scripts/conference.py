#!/usr/bin/env python3
"""Lokalni učni simulator. Brez omrežja, pravega CRM-ja ali pošiljanja."""
import argparse
import csv
import hashlib
import json
from collections import Counter
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
import re
import sqlite3
import sys
from urllib.parse import urlsplit
import uuid

ROOT = Path(__file__).resolve().parents[1]
APP = "tp-conference-simulator-v1"
REQUIRED = ("source_row_id", "conference", "company", "contact_name", "business_email", "assigned_salesperson")


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def normalized(value):
    return " ".join(value.strip().lower().split())


def host(value):
    if not value.strip():
        return ""
    url = value.strip()
    return (urlsplit(url if "://" in url else "https://" + url).hostname or "").lower().removeprefix("www.")


def classify(rows, crm):
    """Vrstni red je poslovno pravilo: validacija, vhodni dvojnik, CRM, podjetje."""
    ids = Counter(row.get("source_row_id", "").strip() for row in rows)
    seen = {}
    results, actions = [], []
    for raw in rows:
        row = {key: (value or "").strip() for key, value in raw.items()}
        source_id = row.get("source_row_id", "")
        email = row.get("business_email", "").lower()
        result = {"source_row_id": source_id, "status": "needs_review", "reason": "", "evidence": {}}
        missing = [key for key in REQUIRED if not row.get(key)]
        if missing:
            result.update(reason="missing_required", evidence={"fields": missing})
        elif ids[source_id] > 1:
            result.update(reason="duplicate_source_id")
        elif not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
            result.update(reason="invalid_email")
        elif email in seen:
            result.update(status="duplicate", reason="duplicate_in_input", evidence={"first_source_row_id": seen[email]})
        else:
            seen[email] = source_id
            contacts = [contact for contact in crm["contacts"] if contact["email"].strip().lower() == email]
            if len(contacts) == 1:
                result.update(status="existing", reason="contact_exists", evidence={"crm_contact_id": contacts[0]["id"]})
            elif len(contacts) > 1:
                result.update(reason="ambiguous_contact", evidence={"candidates": [c["id"] for c in contacts]})
            else:
                website = host(row.get("company_website", ""))
                by_name = [company for company in crm["companies"] if normalized(company["name"]) == normalized(row["company"])]
                candidates = ([company for company in crm["companies"] if host(company.get("website", "")) == website] if website else by_name)
                if len(candidates) > 1:
                    result.update(reason="ambiguous_company", evidence={"candidates": [c["id"] for c in candidates]})
                elif website and not candidates and by_name:
                    result.update(reason="company_domain_conflict", evidence={"candidates": [c["id"] for c in by_name]})
                else:
                    company = {"mode": "link", "id": candidates[0]["id"]} if candidates else {"mode": "create", "name": row["company"], "website": row.get("company_website", "")}
                    action = {"source_row_id": source_id, "company": company,
                              "contact": {"name": row["contact_name"], "email": email, "role": row.get("role", ""), "country": row.get("country", "")},
                              "conference": row["conference"], "meeting_note": row.get("meeting_note", ""),
                              "assigned_salesperson": row["assigned_salesperson"], "next_action_text": row.get("next_action", "")}
                    result.update(status="ready", reason="new_contact", evidence={"company_match": company})
                    actions.append(action)
        results.append(result)
    return results, actions


def workspace(path, create=False):
    selected = Path(path).expanduser()
    if selected.is_symlink():
        raise ValueError("Delovna mapa ne sme biti simbolna povezava.")
    directory = selected.resolve()
    if directory == ROOT or directory in ROOT.parents:
        raise ValueError("Izberi namensko delovno mapo, na primer moje-delo/konferenca.")
    if directory.is_relative_to(ROOT) and not directory.is_relative_to(ROOT / "moje-delo"):
        raise ValueError("Znotraj repozitorija uporabljaj samo mapo moje-delo/.")
    marker = directory / ".conference-simulator.json"
    if create and not marker.exists():
        directory.mkdir(parents=True, exist_ok=True)
        if any(directory.iterdir()):
            raise ValueError("Mapa ni prazna in ni označena za ta simulator; ničesar nisem prepisal.")
        write_json(marker, {"application": APP, "created_at": now()})
    if not marker.is_file() or marker.is_symlink() or read_json(marker).get("application") != APP:
        raise ValueError("Ni veljavne delovne mape simulatorja; najprej uporabi preview.")
    for name in ("state.sqlite3", "runs"):
        if (directory / name).is_symlink():
            raise ValueError("Stanje simulatorja ne sme biti simbolna povezava.")
    return directory


def connect(directory):
    db_path = directory / "state.sqlite3"
    exists = db_path.exists()
    db = sqlite3.connect(db_path, timeout=15)
    db.row_factory = sqlite3.Row
    if exists:
        try:
            owned = db.execute("SELECT value FROM metadata WHERE key='application'").fetchone()
            if not owned or owned[0] != APP:
                raise ValueError("Datoteka stanja ne pripada simulatorju.")
        except sqlite3.DatabaseError as error:
            db.close()
            raise ValueError("Obstoječa datoteka ni veljavno stanje simulatorja.") from error
    else:
        with db:
            db.executescript("""
            CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
            CREATE TABLE runs (id TEXT PRIMARY KEY, status TEXT NOT NULL, original_hash TEXT NOT NULL, plan TEXT NOT NULL, approved_hash TEXT, reviewer TEXT);
            CREATE TABLE effects (source_id TEXT PRIMARY KEY, email TEXT UNIQUE NOT NULL, payload_hash TEXT NOT NULL, record_id TEXT UNIQUE NOT NULL, payload TEXT NOT NULL, created_run TEXT NOT NULL);
            CREATE TABLE receipts (run_id TEXT NOT NULL, source_id TEXT NOT NULL, status TEXT NOT NULL, record_id TEXT NOT NULL, PRIMARY KEY(run_id, source_id));
            CREATE TABLE events (id INTEGER PRIMARY KEY, run_id TEXT NOT NULL, at TEXT NOT NULL, event TEXT NOT NULL, detail TEXT NOT NULL);
            """)
            db.execute("INSERT INTO metadata VALUES ('application', ?)", (APP,))
    return db


def event(db, run_id, kind, detail=""):
    db.execute("INSERT INTO events (run_id, at, event, detail) VALUES (?, ?, ?, ?)", (run_id, now(), kind, detail))


def run_record(db, run_id):
    if not re.fullmatch(r"run-[0-9a-f]{32}", run_id):
        raise ValueError("Neveljaven ID poskusa.")
    record = db.execute("SELECT * FROM runs WHERE id=?", (run_id,)).fetchone()
    if not record:
        raise ValueError("Poskus ne obstaja v tej delovni mapi.")
    return record


def plan_file(directory, run_id):
    file = directory / "runs" / run_id / "plan.json"
    if file.is_symlink() or file.parent.is_symlink():
        raise ValueError("Načrt ne sme biti simbolna povezava.")
    return file


def preview(args):
    directory = workspace(args.workdir, create=True)
    with Path(args.input).open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or any(field not in reader.fieldnames for field in REQUIRED):
            raise ValueError("CSV nima vseh zahtevanih stolpcev.")
        rows = list(reader)
    if any(None in row for row in rows):
        raise ValueError("CSV vsebuje nepravilno število stolpcev.")
    crm = read_json(args.crm)
    results, actions = classify(rows, crm)
    run_id = "run-" + uuid.uuid4().hex
    plan = {"application": APP, "mode": "LOCAL_SIMULATOR_ONLY", "run_id": run_id, "created_at": now(), "rules_version": 1,
            "input_sha256": hashlib.sha256(Path(args.input).read_bytes()).hexdigest(), "crm_sha256": digest(crm),
            "destination": "local SQLite; no network", "input_count": len(rows), "results": results, "actions": actions}
    fingerprint = digest(plan)
    folder = directory / "runs" / run_id
    folder.mkdir(parents=True)
    write_json(folder / "plan.json", plan)
    with closing(connect(directory)) as db, db:
        db.execute("INSERT INTO runs (id, status, original_hash, plan) VALUES (?, 'PREVIEW', ?, ?)", (run_id, fingerprint, canonical(plan)))
        event(db, run_id, "PREVIEW", fingerprint)
    return {"mode": "LOCAL_SIMULATOR_ONLY", "run_id": run_id, "status": "PREVIEW", "sha256": fingerprint,
            "plan": str(folder / "plan.json"), "counts": dict(Counter(row["status"] for row in results))}


def decide(args):
    directory = workspace(args.workdir)
    with closing(connect(directory)) as db, db:
        run = run_record(db, args.run_id)
        if run["status"] != "PREVIEW":
            raise ValueError("Odločitev je mogoča samo za PREVIEW; za spremembe ustvari nov preview.")
        fingerprint = digest(read_json(plan_file(directory, args.run_id)))
        if fingerprint != run["original_hash"] or args.hash != fingerprint:
            raise ValueError("Prstni odtis ne ustreza nespremenjenemu načrtu. Ustvari nov preview.")
        if not args.reviewer.strip():
            raise ValueError("Navedi pregledovalca.")
        state = "APPROVED" if args.decision == "approve" else "REJECTED"
        db.execute("UPDATE runs SET status=?, approved_hash=?, reviewer=? WHERE id=?", (state, fingerprint if state == "APPROVED" else None, args.reviewer.strip(), args.run_id))
        event(db, args.run_id, state, args.reviewer.strip())
    return {"mode": "LOCAL_SIMULATOR_ONLY", "run_id": args.run_id, "status": state}


def execute(args):
    directory = workspace(args.workdir)
    with closing(connect(directory)) as db:
        run = run_record(db, args.run_id)
        if run["status"] not in ("APPROVED", "RUNNING", "INTERRUPTED", "COMPLETED"):
            raise ValueError("Izvedba zahteva veljavno odobritev; stanje je " + run["status"] + ".")
        fingerprint = digest(read_json(plan_file(directory, args.run_id)))
        if fingerprint != run["approved_hash"]:
            with db:
                db.execute("UPDATE runs SET status='INVALIDATED' WHERE id=?", (args.run_id,))
                event(db, args.run_id, "INVALIDATED", "Načrt spremenjen po odobritvi; pretekli učinki ostanejo zabeleženi.")
            raise ValueError("Načrt se je po odobritvi spremenil. Odobritev razveljavljena; ustvari nov preview.")
        if run["status"] == "COMPLETED":
            return report(directory, args.run_id)
        # Izvajamo pregledani nespremenljivi posnetek iz baze, ne spreminjajoče se datoteke.
        plan = json.loads(run["plan"])
        with db:
            db.execute("UPDATE runs SET status='RUNNING' WHERE id=?", (args.run_id,))
            event(db, args.run_id, "RUNNING")
        created = 0
        for action in plan["actions"]:
            source_id = action["source_row_id"]
            payload_hash = digest(action)
            # BEGIN IMMEDIATE zagotovi enega lokalnega pisca tudi pri sočasnem zagonu.
            db.execute("BEGIN IMMEDIATE")
            try:
                existing = db.execute("SELECT * FROM effects WHERE source_id=? OR email=?", (source_id, action["contact"]["email"])).fetchall()
                if existing:
                    match = existing[0]
                    if len(existing) != 1 or match["payload_hash"] != payload_hash:
                        db.execute("UPDATE runs SET status='CONFLICT' WHERE id=?", (args.run_id,))
                        event(db, args.run_id, "CONFLICT", source_id + ": obstaja učinek z drugačno vsebino; ročni pregled.")
                        db.commit()
                        raise ValueError("Obstoječi učinek z drugačno vsebino; ustavitev za pregled: " + source_id)
                    record_id, receipt_status = match["record_id"], "recovered_existing"
                else:
                    record_id = "SIM-" + uuid.uuid4().hex
                    db.execute("INSERT INTO effects VALUES (?, ?, ?, ?, ?, ?)", (source_id, action["contact"]["email"], payload_hash, record_id, canonical(action), args.run_id))
                    event(db, args.run_id, "EFFECT_SAVED", source_id + ":" + record_id)
                    receipt_status = "created"
                    created += 1
                db.commit()
            except Exception:
                db.rollback()
                raise
            # Prekinitev se zgodi PO trajnem shranjevanju učinka, PRED potrdilom.
            if args.interrupt_after and created == args.interrupt_after and receipt_status == "created":
                with db:
                    db.execute("UPDATE runs SET status='INTERRUPTED' WHERE id=?", (args.run_id,))
                    event(db, args.run_id, "INTERRUPTED", source_id + ": učinek shranjen, potrdilo še manjka.")
                return report(directory, args.run_id)
            with db:
                db.execute("INSERT OR IGNORE INTO receipts VALUES (?, ?, ?, ?)", (args.run_id, source_id, receipt_status, record_id))
        with db:
            db.execute("UPDATE runs SET status='COMPLETED' WHERE id=?", (args.run_id,))
            event(db, args.run_id, "COMPLETED")
    return report(directory, args.run_id)


def report(directory, run_id):
    with closing(connect(directory)) as db:
        run = run_record(db, run_id)
        results = json.loads(run["plan"])["results"]
        receipts = {row["source_id"]: dict(row) for row in db.execute("SELECT * FROM receipts WHERE run_id=?", (run_id,))}
        effects = {row["source_id"]: row["record_id"] for row in db.execute("SELECT source_id, record_id FROM effects")}
        output = []
        for item in results:
            row = dict(item)
            if item["source_row_id"] in receipts:
                row["execution"] = receipts[item["source_row_id"]]
            elif item["source_row_id"] in effects and item["status"] == "ready":
                row["execution"] = {"status": "effect_saved_receipt_pending", "record_id": effects[item["source_row_id"]]}
            else:
                row["execution"] = {"status": "not_executed"}
            output.append(row)
        result = {"mode": "LOCAL_SIMULATOR_ONLY", "run_id": run_id, "status": run["status"], "approved_sha256": run["approved_hash"],
                  "simulated_effects_total": db.execute("SELECT COUNT(*) FROM effects").fetchone()[0], "rows": output,
                  "events": [dict(row) for row in db.execute("SELECT at, event, detail FROM events WHERE run_id=? ORDER BY id", (run_id,))]}
    write_json(directory / "runs" / run_id / "report.json", result)
    return result




def parser():
    command = argparse.ArgumentParser(description="Lokalni učni simulator konference. Ne dostopa do omrežja ali pravega CRM-ja. Za pomoč koraku dodaj --help.")
    subs = command.add_subparsers(dest="command", required=True)
    for name, description in (("preview", "Razvrsti vrstice in shrani predlog brez učinka."), ("decide", "Zabeleži odobritev ali zavrnitev natančnega načrta."), ("execute", "Izvedi odobreni načrt v lokalni simulaciji."), ("status", "Pokaži trajne rezultate in dogodke poskusa.")):
        sub = subs.add_parser(name, help=description, description=description)
        sub.add_argument("--workdir", required=True, help="Namenska mapa, npr. moje-delo/konferenca; ob prvi uporabi prazna.")
        if name != "preview":
            sub.add_argument("--run-id", required=True, help="ID iz rezultata preview.")
        if name == "preview":
            sub.add_argument("--input", default=str(ROOT / "exercises/conference/prospects.csv"), help="Vhodni CSV.")
            sub.add_argument("--crm", default=str(ROOT / "exercises/conference/existing-crm.json"), help="Izmišljeni posnetek CRM v JSON.")
        elif name == "decide":
            sub.add_argument("--decision", choices=("approve", "reject"), required=True)
            sub.add_argument("--hash", required=True, help="SHA-256 iz nespremenjenega pregledanega načrta.")
            sub.add_argument("--reviewer", required=True, help="Ime učnega pregledovalca; ni preverjena avtentikacija.")
        elif name == "execute":
            sub.add_argument("--interrupt-after", type=int, default=0, help="Učno prekini po N novih shranjenih učinkih, pred potrdilom.")
    return command


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        if getattr(args, "interrupt_after", 0) < 0:
            raise ValueError("Število za prekinitev ne sme biti negativno.")
        result = {"preview": preview, "decide": decide, "execute": execute, "status": lambda a: report(workspace(a.workdir), a.run_id)}[args.command](args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, sqlite3.Error, KeyError, TypeError) as error:
        print(json.dumps({"mode": "LOCAL_SIMULATOR_ONLY", "status": "STOPPED", "error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
