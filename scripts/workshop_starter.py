#!/usr/bin/env python3
"""Workshop adapter for the pinned Claude Work Starter; no global setup or scheduler."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sqlite3
import sys

from participant_git import project_root, work_root, git, Refused

ROOT = Path(__file__).resolve().parents[1]
COLLECTION = "moja-naloga"


def components(project):
    folder = project / ".claude/skills/delavnica-dokumenti"
    manifest = json.loads((folder / "source.json").read_text(encoding="utf-8"))
    for name, digest in manifest["files"].items():
        file = folder / name
        if file.is_symlink() or hashlib.sha256(file.read_bytes()).hexdigest() != digest:
            raise Refused("Komponente starterja so spremenjene; najprej preglej različico.")
    # Use the bundled reader, even if another document module was imported earlier.
    for name in ("dokumenti", "indeks"):
        spec = importlib.util.spec_from_file_location(name, folder / "scripts" / (name + ".py"))
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules["indeks"]


def context(project):
    project = project_root(project)
    work_root(project)
    for name in ("local/", ".obsidian/"):
        if git(project, "check-ignore", "--no-index", name, check=False).returncode:
            raise Refused("Gradiva morajo izključevati lokalne nastavitve; najprej posodobi gradiva.")
        if git(project, "ls-files", "--", name).stdout.strip():
            raise Refused("Lokalne nastavitve so že v skupnem Gitu; najprej razreši stanje.")
    index = components(project)
    state = index.safe_path(project / "local/starter")
    return project, index, state


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=ROOT)
    subs = parser.add_subparsers(dest="command", required=True)
    init = subs.add_parser("pripravi")
    init.add_argument("--source", type=Path, required=True)
    init.add_argument("--approve-cloud", action="store_true")
    init.add_argument("--verify-private", action="store_true")
    init.add_argument("--exclude", action="append", default=[])
    for cmd in ("preveri", "stanje", "pregled", "osvezi", "paket", "kazalo"):
        subs.add_parser(cmd)
    subs.add_parser("najdi").add_argument("query")
    read = subs.add_parser("preberi")
    read.add_argument("path")
    read.add_argument("--chunk", type=int, default=1)
    read.add_argument("--pages")
    subs.add_parser("vkljuci").add_argument("path")
    subs.add_parser("potrdi").add_argument("answers", type=Path)
    args = parser.parse_args(argv)
    try:
        project, index, state = context(args.project)
        if args.command == "preveri":
            with sqlite3.connect(":memory:") as db:
                db.execute("create virtual table proof using fts5(content)")
            import pypdf
            import openpyxl
            print(json.dumps({"status": "ok", "python": sys.executable,
                              "state": str(state), "pypdf": pypdf.__version__,
                              "openpyxl": openpyxl.__version__, "global_setup_changed": False}))
            return 0
        if args.command == "pripravi":
            source = args.source if args.source.is_absolute() else project / args.source
            source = index.safe_path(source)
            if not args.approve_cloud or not args.verify_private:
                raise Refused("Najprej potrdi dovoljeno zbirko, obdelavo pri Claudu in zasebno lokacijo indeksa.")
            # Register performs its own containment, symlink and overlapping-collection checks.
            # The whole chosen small folder is explicitly authorised, including older files.
            return index.main(["--state-dir", str(state), "--collection", COLLECTION,
                               "--root", str(source),
                               *[v for e in args.exclude for v in ("--exclude", e)],
                               "nastavi", "--since", "1970-01-01", "--approve-cloud", "--verify-private"])
        if not (state / "nastavitve.json").is_file():
            raise Refused("Indeks delavnice še ni pripravljen. Osebnega starterja ne uporabim samodejno.")
        forwarded = ["--state-dir", str(state), "--collection", COLLECTION, args.command]
        if args.command == "najdi":
            forwarded.append(args.query)
        elif args.command in ("preberi", "vkljuci"):
            forwarded.append(args.path)
            if args.command == "preberi":
                forwarded += ["--chunk", str(args.chunk)]
                if args.pages:
                    forwarded += ["--pages", args.pages]
        elif args.command == "potrdi":
            answers = index.safe_path(args.answers if args.answers.is_absolute() else project / args.answers)
            if not answers.is_relative_to(state):
                raise Refused("Odgovori za indeks morajo biti v zasebni mapi local/starter.")
            forwarded.append(str(answers))
        return index.main(forwarded)
    except (ValueError, OSError, ImportError, KeyError) as exc:
        print("STOP: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
