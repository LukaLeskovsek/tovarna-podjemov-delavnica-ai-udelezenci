#!/usr/bin/env python3
"""Verify a released participant snapshot; standard library, no network."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import unquote, urlsplit
import zipfile

LOCAL_DIRS = {'.git', 'moje-delo', 'local', '__pycache__', '.venv', '.gstack'}
FORBIDDEN_PARTS = {'facilitator', 'tests', 'validation', 'programme', 'releases',
                   'release-content', 'zasebno', 'node_modules', 'dist'}
PRIVATE_REPO = re.compile(r'https://github\.com/LukaLeskovsek/tovarna-podjemov-delavnica-ai(?:[/?#\s)"\']|$)')
SECRET = re.compile(r'\bgh[pousr]_[A-Za-z0-9]{20,}\b|\bsk-ant-[A-Za-z0-9_-]{20,}\b|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|/Users/[A-Za-z0-9._-]+/')


def safe_path(value):
    if not isinstance(value, str) or not value or '\\' in value or any(ord(c) < 32 for c in value):
        raise ValueError(f'Invalid relative path: {value!r}')
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {'', '.', '..'} for part in value.split('/')):
        raise ValueError(f'Unsafe path: {value}')
    if any(part.casefold() in LOCAL_DIRS | FORBIDDEN_PARTS for part in path.parts):
        raise ValueError(f'Private/local path cannot be released: {value}')
    if re.search(r'expected-output|answer[-_]key|\.env(?:\.|$)|\.pem$|\.key$|\.mcp\.json$|settings\.local\.json$|\.gitmodules$', value, re.I):
        raise ValueError(f'Private/answer file cannot be released: {value}')
    return path


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_text(name, text, errors):
    if SECRET.search(text):
        errors.append(f'Local path or credential marker in {name}')
    # Source code contains the validator's own deny expressions; Markdown/metadata must not link private source.
    if name.endswith(('.md', '.json', '.yml', '.yaml')) and PRIVATE_REPO.search(text):
        errors.append(f'Private preparation repository link in {name}')


def verify(root):
    root = Path(root).resolve()
    errors = []
    try:
        metadata = json.loads((root / 'release.json').read_text())
        if metadata.get('schema_version') != 1 or not re.fullmatch(r'(?:start|meeting-\d{2})-v[1-9]\d*', metadata['release_tag']):
            raise ValueError('Invalid release version')
        expected = metadata['files']
        if not isinstance(expected, dict) or not expected or 'release.json' in expected:
            raise ValueError('Invalid released file list')
        modules = metadata['modules']
        if not isinstance(modules, list) or not modules or any(type(n) is not int or n not in range(1, 11) for n in modules):
            raise ValueError('Invalid module selection')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f'Invalid release.json: {exc}']
    for name, digest in expected.items():
        try:
            safe_path(name)
            path = root / name
            if any(p.is_symlink() for p in [path, *path.parents] if p != root and root in p.parents):
                raise ValueError(f'Symlink cannot be released: {name}')
            if not path.is_file() or not re.fullmatch(r'[0-9a-f]{64}', str(digest)) or sha256(path) != digest:
                errors.append(f'Missing or changed course file: {name}')
        except ValueError as exc:
            errors.append(str(exc))
    actual = set()
    for path in root.rglob('*'):
        relative = path.relative_to(root)
        if any(part in LOCAL_DIRS for part in relative.parts):
            continue
        if path.is_symlink():
            errors.append(f'Unexpected symlink: {relative}')
        if path.is_file():
            actual.add(relative.as_posix())
    for name in sorted(actual - set(expected) - {'release.json'}):
        errors.append(f'Unlisted file in course snapshot: {name}')
    if metadata['release_tag'].startswith('start-'):
        if modules != [1]:
            errors.append('Starter must expose only module 1')
        for name in expected:
            if (name.startswith('.claude/skills/') or name == 'scripts/conference.py'
                    or re.match(r'koraki/(?!01-)[0-9]{2}-', name)):
                errors.append(f'Later material in starter: {name}')
    for name in sorted(actual & (set(expected) | {'release.json'})):
        path = root / name
        if path.suffix in {'.md', '.json', '.yml', '.yaml', '.py', '.csv', '.txt'}:
            try:
                text = path.read_text(encoding='utf-8')
            except UnicodeError:
                errors.append(f'Invalid text file: {name}')
                continue
            check_text(name, text, errors)
            if path.suffix == '.md':
                prose = re.sub(r'```.*?```', '', text, flags=re.S)
                for href in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', prose):
                    href = href.strip().strip('<>').split(' "', 1)[0]
                    parsed = urlsplit(href)
                    if parsed.scheme or href.startswith('#'):
                        continue
                    target = (path.parent / unquote(parsed.path)).resolve()
                    if not target.is_relative_to(root) or not target.exists():
                        errors.append(f'Missing or external local link: {name} -> {href}')
        elif path.suffix in {'.docx', '.pptx', '.xlsx'}:
            try:
                with zipfile.ZipFile(path) as archive:
                    for entry in archive.namelist():
                        if entry.endswith(('.xml', '.rels')):
                            check_text(name + ':' + entry, archive.read(entry).decode('utf-8'), errors)
            except (OSError, ValueError, zipfile.BadZipFile) as exc:
                errors.append(f'Invalid Office archive {name}: {exc}')
        elif path.suffix == '.zip':
            errors.append(f'Nested ZIP packages need a separately reviewed release artifact: {name}')
    ignore = root / '.gitignore'
    if not ignore.is_file() or 'moje-delo/' not in ignore.read_text().splitlines():
        errors.append('Outer repository must ignore moje-delo/')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = verify(args.root)
    if errors:
        print('\n'.join(errors))
        return 1
    print('OK: released file hashes, selected scope, links and private-content exclusions.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
