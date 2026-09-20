#!/usr/bin/env python3
"""Ordinary Git helpers for an outer course clone and private moje-delo repository.

No course updater: check-update is a read-only preflight, followed by git pull
--ff-only. Files are selected explicitly; the helper cannot judge whether a
reviewed business result is suitable for the participant's private backup.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys

PUBLIC_REPO = "LukaLeskovsek/tovarna-podjemov-delavnica-ai-udelezenci"
ROOT_DOCS = {
    "napredek.md", "workflow-brief.md", "context-map.md", "run-log.md",
    "verification-report.md", "improvement-proposal.md", "access-matrix.md",
    "operating-guide.md",
}
BLOCKED_PARTS = {
    "zasebno", "raw", "raw-inputs", "inputs", "vhodi", "transcripts", "transkripti",
    "credentials", "poverilnice", "secrets", "local", "node_modules", "__pycache__",
}
IGNORE = """# Raw business inputs and local connection information never enter this backup.
zasebno/
**/raw/
**/raw-inputs/
**/inputs/
**/vhodi/
**/transcripts/
**/transkripti/
**/credentials/
**/poverilnice/
**/secrets/
**/local/
.env
.env.*
*.pem
*.key
*.p12
*.pfx
*.sqlite*
*.db
.mcp.json
.claude/
.DS_Store
__pycache__/
*.pyc
node_modules/
"""
SECRET_PATTERNS = [
    rb"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----",
    rb"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b",
    rb"\bAKIA[0-9A-Z]{16}\b",
    rb"\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{20,}\b",
    rb"(?im)^\s*[\"']?(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)[\"']?\s*[:=]\s*[\"']?[^\s\"']{8,}",
]


class Refused(ValueError):
    """An expected condition requiring a participant decision or correction."""


class SavedLocally(Refused):
    """Checkpoint exists locally; remote backup did not complete."""


def run(args: list[str], cwd: Path, *, check: bool = True, binary: bool = False) -> subprocess.CompletedProcess:
    env = os.environ.copy()
    for key in list(env):
        if key.startswith("GIT_") and key not in {"GIT_SSH_COMMAND", "GIT_TERMINAL_PROMPT"}:
            env.pop(key)
    if args[0] == "gh" and not shutil.which("gh"):
        fallback = Path.home() / ".local/bin/gh"
        if fallback.is_file():
            args = [str(fallback), *args[1:]]
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=not binary, env=env)
    if check and result.returncode:
        # Avoid echoing remote URLs/credential-bearing subprocess output.
        raise Refused(f"Ukaz {args[0]} {args[1]} ni uspel; preveri prijavo, Git in nastavitve.")
    return result


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return run(["git", *args], root, check=check)


def paths(output: str) -> list[str]:
    return [part for part in output.split("\0") if part]


def reject_symlinks(path: Path) -> None:
    for part in [path, *path.parents]:
        if part.is_symlink():
            raise Refused("Simbolne povezave niso dovoljene za projekt ali izbrane datoteke.")


def project_root(project: Path) -> Path:
    project = project.absolute()
    reject_symlinks(project)
    if not project.is_dir():
        raise Refused("Mapa projekta ne obstaja.")
    top = git(project, "rev-parse", "--show-toplevel").stdout.strip()
    if Path(top).resolve() != project.resolve():
        raise Refused("Projekt mora biti koren zunanjega repozitorija.")
    return project.resolve()


def work_root(project: Path) -> Path:
    project = project_root(project)
    work = project / "moje-delo"
    reject_symlinks(work)
    if not (work / ".git").is_dir() or (work / ".git").is_symlink():
        raise Refused("Najprej inicializiraj moje-delo/ kot samostojen repozitorij; zunanji ni osebna shramba.")
    if Path(git(work, "rev-parse", "--show-toplevel").stdout.strip()).resolve() != work:
        raise Refused("Koren osebnega repozitorija mora biti natanko moje-delo/.")
    if git(project, "ls-files", "--", "moje-delo").stdout.strip():
        raise Refused("Zunanji repozitorij že sledi moje-delo/; najprej razreši to stanje.")
    if git(project, "check-ignore", "--no-index", "moje-delo/", check=False).returncode:
        raise Refused("Zunanji repozitorij mora ignorirati celotno moje-delo/.")
    return work


def initialise(project: Path) -> dict:
    project = project_root(project)
    if git(project, "ls-files", "--", "moje-delo").stdout.strip():
        raise Refused("Zunanji repozitorij že sledi moje-delo/.")
    if git(project, "check-ignore", "--no-index", "moje-delo/", check=False).returncode:
        raise Refused("Pred začetkom mora zunanji .gitignore vključevati moje-delo/.")
    work = project / "moje-delo"
    reject_symlinks(work)
    if (work / ".git").exists():
        work_root(project)
        return {"status": "already_initialised", "remote_created": False}
    if (work / ".gitignore").exists() and (work / ".gitignore").read_text() != IGNORE:
        raise Refused("moje-delo/.gitignore že obstaja; preveri ga pred inicializacijo, brez prepisovanja.")
    for name in ("skills", "rezultati", "zasebno"):
        reject_symlinks(work / name)
        if (work / name).exists() and not (work / name).is_dir():
            raise Refused(f"moje-delo/{name} mora biti mapa.")
    work.mkdir(exist_ok=True)
    (work / ".gitignore").write_text(IGNORE, encoding="utf-8")
    for name in ("skills", "rezultati", "zasebno"):
        (work / name).mkdir(exist_ok=True)
    git(work, "init", "-b", "main")
    return {"status": "initialised_locally", "remote_created": False, "files_committed": False}


def allowed_path(name: str) -> bool:
    p = PurePosixPath(name)
    if name == ".gitignore":
        return True
    if not name or p.as_posix() != name or p.is_absolute() or ".." in p.parts or "\\" in name or ":" in name or any(ord(c) < 32 for c in name):
        return False
    for part in p.parts:
        lower = part.lower()
        if lower in BLOCKED_PARTS or lower.startswith("."):
            return False
        if re.search(r"(?:^|[-_.])(?:credentials?|secrets?|transcripts?|raw|passwords?|tokens?|local-config)(?:$|[-_.])", lower):
            return False
        if lower.endswith((".pem", ".key", ".p12", ".pfx", ".db", ".pyc")) or ".sqlite" in lower:
            return False
    return (len(p.parts) == 1 and name in ROOT_DOCS) or (
        len(p.parts) > 1 and p.parts[0] in {"skills", "rezultati"}
    ) or (len(p.parts) > 1 and p.parts[0] == "decisions" and p.suffix == ".md")


def inspect_content(name: str, content: bytes) -> None:
    if name == ".gitignore":
        required = set(IGNORE.splitlines()) - {"", IGNORE.splitlines()[0]}
        if not required.issubset(set(content.decode("utf-8").splitlines())):
            raise Refused("Osebni .gitignore ne vsebuje obveznih izključitev.")
    if any(re.search(pattern, content) for pattern in SECRET_PATTERNS):
        raise Refused(f"Datoteka {name} vsebuje možne poverilnice; odstrani jih in preveri zgodovino.")


def validate_tracked(work: Path) -> None:
    for name in paths(git(work, "ls-files", "-z").stdout):
        if not allowed_path(name):
            raise Refused(f"Osebni repozitorij že sledi nedovoljeni datoteki: {name}.")
        reject_symlinks(work / name)
    # Removed secrets/raw inputs are still published with Git history. Check all
    # reachable historical blobs, not only the current working directory.
    objects = git(work, "rev-list", "--objects", "--all").stdout.splitlines()
    for entry in objects:
        oid, _, name = entry.partition(" ")
        if not name or git(work, "cat-file", "-t", oid).stdout.strip() != "blob":
            continue
        if not allowed_path(name):
            raise Refused(f"Git zgodovina vsebuje nedovoljeno datoteko: {name}; ne bo objavljena.")
        content = run(["git", "cat-file", "blob", oid], work, binary=True).stdout
        inspect_content(name, content)


def origin_identity(url: str) -> str:
    match = re.fullmatch(r"(?:https://github\.com/|git@github\.com:|ssh://git@github\.com/)([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?:\.git)?/?", url)
    if not match:
        raise Refused("Origin mora biti neposreden HTTPS ali SSH naslov repozitorija na github.com.")
    return match.group(1)


def origin_url(work: Path) -> str:
    fetch = git(work, "remote", "get-url", "--all", "origin").stdout.splitlines()
    push = git(work, "remote", "get-url", "--push", "--all", "origin").stdout.splitlines()
    if len(fetch) != 1 or len(push) != 1 or origin_identity(fetch[0]).lower() != origin_identity(push[0]).lower():
        raise Refused("Origin mora imeti en sam cilj za branje in zapis v isti repozitorij.")
    return push[0]


def verify_remote(work: Path) -> dict:
    endpoint = origin_url(work)
    name = origin_identity(endpoint)
    login = run(["gh", "api", "user", "--hostname", "github.com", "--jq", ".login"], work).stdout.strip()
    metadata = json.loads(run(["gh", "repo", "view", f"https://github.com/{name}", "--json", "owner,name,isPrivate,url,sshUrl,isArchived"], work).stdout)
    full_name = f"{metadata['owner']['login']}/{metadata['name']}"
    if full_name.lower() != name.lower() or metadata["owner"]["login"].lower() != login.lower():
        raise Refused("Ciljni repozitorij mora pripadati trenutno prijavljenemu osebnemu računu gh.")
    if metadata.get("isPrivate") is not True or metadata.get("isArchived") is True:
        raise Refused("Ciljni repozitorij mora biti zaseben in omogočati zapise.")
    if origin_identity(metadata["url"]).lower() != name.lower() or origin_identity(metadata["sshUrl"]).lower() != name.lower():
        raise Refused("GitHub podatki in naslov origin se ne ujemajo.")
    return {"login": login, "repo": full_name, "url": endpoint}


def clean_index(work: Path) -> None:
    if paths(git(work, "diff", "--cached", "--name-only", "-z").stdout):
        raise Refused("Indeks že vsebuje pripravljene spremembe; najprej jih preglej, ničesar ne dodajam.")
    if git(work, "symbolic-ref", "--quiet", "--short", "HEAD").stdout.strip() != "main":
        raise Refused("Osebne kontrolne točke shrani na veji main.")


def tag_exists(work: Path, tag: str) -> bool:
    return git(work, "show-ref", "--verify", "--quiet", f"refs/tags/{tag}", check=False).returncode == 0


def valid_tag(tag: str) -> None:
    if not re.fullmatch(r"session-[0-9]{2,}(?:-v[1-9][0-9]*)?", tag):
        raise Refused("Osebna oznaka naj bo session-01 oziroma session-01-v2.")


def selected_files(work: Path, files: list[str]) -> tuple[list[str], list[dict]]:
    selected = sorted(set(files))
    if not selected:
        raise Refused("Izberi konkretne datoteke z --files.")
    tracked = set(paths(git(work, "ls-files", "-z").stdout))
    if ".gitignore" not in tracked:
        selected = sorted(set(selected) | {".gitignore"})
    report = []
    for name in selected:
        if not allowed_path(name):
            raise Refused(f"Datoteka ni dovoljena za izbrani pregledani izhod: {name}.")
        path = work / name
        reject_symlinks(path)
        if path.exists() and not path.is_file():
            raise Refused("--files sprejme samo konkretne datoteke, ne celotnih map.")
        if path.exists():
            content = path.read_bytes()
            inspect_content(name, content)
            if git(work, "check-ignore", "--no-index", "--quiet", "--", name, check=False).returncode == 0:
                raise Refused(f"Izbrana datoteka je izključena iz Gita: {name}.")
            report.append({"path": name, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()})
        elif name in tracked:
            report.append({"path": name, "deleted": True})
        else:
            raise Refused(f"Izbrana datoteka ne obstaja: {name}.")
    return selected, report


def push_checkpoint(work: Path, tag: str, remote: dict) -> dict:
    commit = git(work, "rev-parse", f"refs/tags/{tag}^{{commit}}").stdout.strip()
    head = git(work, "rev-parse", "HEAD").stdout.strip()
    if commit != head:
        raise Refused("Oznaka ni na trenutnem HEAD; ne premikam oznake ali veje. Preveri osebno zgodovino.")
    result = git(work, "-c", "push.followTags=false", "push", "--atomic", "--no-follow-tags", remote["url"],
                 f"{commit}:refs/heads/main", f"refs/tags/{tag}:refs/tags/{tag}", check=False)
    if result.returncode:
        raise SavedLocally(f"saved locally, not backed up — {tag} ({commit[:12]}). Ponovi z retry --tag {tag}; oznaka ostane nespremenjena.")
    return {"status": "backed_up", "tag": tag, "commit": commit, "repository": remote["repo"]}


def checkpoint(project: Path, files: list[str], tag: str, *, preview: bool = False) -> dict:
    valid_tag(tag)
    work = work_root(project)
    clean_index(work)
    if tag_exists(work, tag):
        raise Refused(f"Oznaka {tag} že obstaja; za ponoven prenos uporabi retry --tag {tag}.")
    validate_tracked(work)
    selected, report = selected_files(work, files)
    remote = verify_remote(work)
    if preview:
        return {"status": "preview_only", "tag": tag, "repository": remote["repo"], "files": report,
                "review": "Preberi točno navedene datoteke; preverjanje vzorcev ne prepozna vseh zaupnih podatkov."}
    git(work, "var", "GIT_AUTHOR_IDENT")
    git(work, "var", "GIT_COMMITTER_IDENT")
    git(work, "add", "--", *selected)
    staged = set(paths(git(work, "diff", "--cached", "--name-only", "-z").stdout))
    if not staged:
        raise Refused("Izbrane datoteke nimajo sprememb; ni nove kontrolne točke.")
    if not staged.issubset(set(selected)):
        raise Refused("Pripravljene spremembe vsebujejo neizbrane datoteke; ne ustvarim commita.")
    for name in staged:
        if git(work, "cat-file", "-e", f":{name}", check=False).returncode == 0:
            content = run(["git", "show", f":{name}"], work, binary=True).stdout
            inspect_content(name, content)
    git(work, "commit", "-m", f"Shrani {tag}")
    committed = set(paths(git(work, "diff-tree", "--root", "--no-commit-id", "--name-only", "-r", "-z", "HEAD").stdout))
    if not committed.issubset(set(selected)):
        raise Refused("Commit vsebuje neizbrane datoteke, morda po posegu lokalnega Git hooka; ostane lokalno, brez oznake ali prenosa.")
    validate_tracked(work)
    git(work, "tag", "-a", tag, "-m", f"Osebna kontrolna točka {tag}")
    result = push_checkpoint(work, tag, remote)
    result["files"] = sorted(staged)
    return result


def retry(project: Path, tag: str) -> dict:
    valid_tag(tag)
    work = work_root(project)
    clean_index(work)
    if not tag_exists(work, tag):
        raise Refused("Oznaka ne obstaja; retry ne ustvarja novih kontrolnih točk.")
    validate_tracked(work)
    return push_checkpoint(work, tag, verify_remote(work))


def check_update(project: Path) -> dict:
    project = project_root(project)
    if origin_identity(origin_url(project)).lower() != PUBLIC_REPO.lower():
        raise Refused("Zunanji origin ni uradni javni repozitorij gradiv.")
    if git(project, "symbolic-ref", "--quiet", "--short", "HEAD").stdout.strip() != "main":
        raise Refused("Posodobitve gradiv uporabljajo vejo main.")
    if git(project, "status", "--porcelain", "--untracked-files=all").stdout:
        raise Refused("Gradiva imajo lokalne spremembe; najprej jih preglej. Ne prepisujem in ne skrivam sprememb.")
    upstream = git(project, "rev-parse", "--abbrev-ref", "@{upstream}").stdout.strip()
    if upstream != "origin/main":
        raise Refused("Veja main mora spremljati origin/main.")
    if git(project, "merge-base", "--is-ancestor", "HEAD", "origin/main", check=False).returncode:
        raise Refused("Lokalna zgodovina gradiv je odstopila od origin/main; najprej razreši stanje.")
    return {"status": "ready_for_plain_pull", "next_command": "git pull --ff-only",
            "note": "Predhodni pregled ne prenaša sprememb; pull preveri tudi novo oddaljeno zgodovino."}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init")
    commands.add_parser("check-update")
    save = commands.add_parser("checkpoint")
    save.add_argument("--files", nargs="+", required=True)
    save.add_argument("--tag", required=True)
    save.add_argument("--preview", action="store_true")
    again = commands.add_parser("retry")
    again.add_argument("--tag", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            result = initialise(args.project)
        elif args.command == "check-update":
            result = check_update(args.project)
        elif args.command == "retry":
            result = retry(args.project, args.tag)
        else:
            result = checkpoint(args.project, args.files, args.tag, preview=args.preview)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (Refused, OSError, json.JSONDecodeError, subprocess.SubprocessError) as error:
        status = "saved_locally_not_backed_up" if isinstance(error, SavedLocally) else "stopped"
        print(json.dumps({"status": status, "message": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
