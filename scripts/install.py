#!/usr/bin/env python3
"""Copy complete portable skills into an explicitly selected agent directory."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--skill', action='append', help='Skill name; repeat to select several.')
    selection.add_argument('--all', action='store_true', help='Install every portable skill.')
    destination = parser.add_mutually_exclusive_group(required=True)
    destination.add_argument('--agent', choices=['claude', 'codex'])
    destination.add_argument('--dest', type=Path, help='Parent skill directory for another loader.')
    args = parser.parse_args()

    catalog = json.loads((ROOT / 'catalog/skills.json').read_text())
    available = {s['name']: ROOT / s['path'] for s in catalog['skills']}
    names = sorted(available) if args.all else list(dict.fromkeys(args.skill))
    unknown = set(names) - available.keys()
    if unknown:
        parser.error('Unknown skill: ' + ', '.join(sorted(unknown)))
    target = args.dest.expanduser() if args.dest else Path.home() / ('.claude' if args.agent == 'claude' else '.codex') / 'skills'

    # Preflight the whole request before creating any destination folders.
    for name in names:
        source = available[name]
        if not (source / 'SKILL.md').is_file():
            parser.error(f'Incomplete source skill: {name}')
        if any(p.is_symlink() for p in source.rglob('*')):
            parser.error(f'Source contains a symlink: {name}')
        output = target / name
        if output.exists() or output.is_symlink():
            parser.error(f'Refusing to overwrite {output}. Back it up and remove it deliberately first.')
    target.mkdir(parents=True, exist_ok=True)
    for name in names:
        shutil.copytree(available[name], target / name, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        print(f'Installed {name}: {target / name}')
    print('Start a new agent session to load the installed skills.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

