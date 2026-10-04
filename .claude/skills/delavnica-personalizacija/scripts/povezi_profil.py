#!/usr/bin/env python3
"""Inspect or append one personal-profile router, preserving other global instructions."""
import argparse
import difflib
import os
from pathlib import Path
import subprocess
import tempfile
from datetime import datetime, timezone

START = '<!-- delavnica-profil:start -->'
END = '<!-- delavnica-profil:end -->'

def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], stderr=subprocess.PIPE).decode().strip()

def make_block(profile):
    def imp(name):
        value = (profile / name).as_posix()
        if any(c in value for c in '\n\r\t'):
            raise ValueError('Pot vsebuje nedovoljen prelom ali tabulator.')
        return '@' + value.replace(' ', '\\ ')
    return '\n'.join([START, '## Osebni profil za delo', imp('PERSON.md'), imp('INDEX.md'),
        'Pred vsebinsko nalogo uporabi osebni profil. Podjetje in znamko izberi po potrjeni povezavi trenutne mape v kazalu ali po uporabnikovi nalogi. Če je izbira nejasna, vprašaj. Preberi navedene COMPANY.md, BRAND.md in PRIMERI.md; pravil različnih podjetij ne mešaj.',
        'Popravke loči na trajnejše pravilo, posebnost naloge in primer z razlogom. Ob nasprotju preveri dogovor. Če profil ali pot manjka, to povej in popravi povezavo po preverjanju dejanske mape.', END])

def merged(original, block):
    if original.count(START) != original.count(END) or original.count(START) > 1:
        raise ValueError('Neveljaven ali podvojen povezovalni blok; najprej preglej obstoječa navodila.')
    if START in original:
        a, b = original.index(START), original.index(END) + len(END)
        if b <= a:
            raise ValueError('Neveljaven vrstni red oznak.')
        return original[:a] + block + original[b:]
    return original + ('\n\n' if original and not original.endswith('\n\n') else '') + block + '\n'

def prepare(workspace, global_path):
    root = workspace.resolve()
    inner = root / 'moje-delo'
    if inner.is_symlink() or Path(git(inner, 'rev-parse', '--show-toplevel')).resolve() != inner.resolve():
        raise ValueError('Zasebni Gitov koren mora biti točno moje-delo/.')
    git(root, 'check-ignore', 'moje-delo/napredek.md')
    profile = inner / 'rezultati/profil'
    for name in ['PERSON.md', 'INDEX.md']:
        p = profile / name
        if not p.is_file() or p.is_symlink() or not p.resolve().is_relative_to(inner.resolve()) or not p.read_text().strip():
            raise ValueError(f'Manjka pravi pregledani profil: {name}')
    if global_path.is_symlink():
        raise ValueError('Globalna navodila so simbolna povezava; cilj preglej in uredi izrecno.')
    old = global_path.read_text() if global_path.exists() else ''
    return old, merged(old, make_block(profile.resolve()))

def apply(global_path, old, new):
    if old == new:
        return None
    global_path.parent.mkdir(parents=True, exist_ok=True)
    backup = None
    if global_path.exists():
        folder = global_path.parent / 'workshop-backups'
        folder.mkdir(mode=0o700, exist_ok=True)
        os.chmod(folder, 0o700)
        fd, filename = tempfile.mkstemp(prefix='CLAUDE-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S-'), suffix='.md', dir=folder)
        with os.fdopen(fd, 'w') as f:
            f.write(old)
        backup = Path(filename)
    mode = global_path.stat().st_mode & 0o777 if global_path.exists() else 0o600
    fd, name = tempfile.mkstemp(dir=global_path.parent, prefix='.workshop-profile-')
    try:
        with os.fdopen(fd, 'w') as f: f.write(new)
        os.chmod(name, mode)
        # Avoid overwriting an edit made since the preview/read.
        current = global_path.read_text() if global_path.exists() else ''
        if current != old: raise ValueError('Globalna navodila so se med pripravo spremenila; ponovi pregled.')
        os.replace(name, global_path)
    finally:
        if Path(name).exists(): Path(name).unlink()
    return backup

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('command', choices=['pregled', 'povezi'])
    p.add_argument('--workspace', type=Path, default=Path.cwd())
    p.add_argument('--global-file', type=Path, default=Path.home() / '.claude/CLAUDE.md')
    a = p.parse_args()
    try:
        old, new = prepare(a.workspace, a.global_file)
        if a.command == 'pregled':
            print(''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile='sedanja navodila', tofile='predlog navodil')) or 'Povezava je že aktualna.')
        else:
            backup = apply(a.global_file, old, new)
            print('Povezava je že aktualna.' if old == new else 'Povezava dodana. Preveri uporabo v novem pogovoru Code.')
            if backup: print(f'Zasebna kopija: {backup}')
    except (ValueError, OSError, subprocess.CalledProcessError) as e:
        print(f'STOP: {e}')
        return 1
    return 0

if __name__ == '__main__': raise SystemExit(main())
