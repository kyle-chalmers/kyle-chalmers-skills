#!/usr/bin/env python3
"""Check migrated tutorial files, relative links and optional description URLs."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'!?\[[^\]]*\]\(([^\s)]+)\)')
OLD = re.compile(r'https://github\.com/kyle-chalmers/(?:data-ai-reference|data-ai-tickets-template)', re.I)


def check(spec=None):
    failures = []
    documents = list((ROOT / 'tutorials').rglob('*.md')) + list((ROOT / 'examples').rglob('*.md'))
    for path in documents:
        text = path.read_text()
        if OLD.search(text):
            failures.append(f'{path.relative_to(ROOT)}: retired repository URL')
        for target in LINK.findall(text):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith('#'):
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                failures.append(f'{path.relative_to(ROOT)}: missing relative link {target}')
    provenance = json.loads((ROOT / 'catalog/tutorial-provenance.json').read_text())
    for item in provenance['files']:
        path = ROOT / item['destination_path']
        if not path.is_file():
            failures.append(f'missing import: {item["destination_path"]}')
        elif hashlib.sha256(path.read_bytes()).hexdigest() != item['destination_sha256']:
            failures.append(f'import hash mismatch: {item["destination_path"]}')
    count = 0
    if spec:
        for item in json.loads(Path(spec).read_text())['changes']:
            text = item['new_description']
            count += 1
            if OLD.search(text) or len(text) > 5000:
                failures.append(f'{item["video_id"]}: retired URL or description over 5000 characters')
            for target in re.findall(r'https://github.com/kyle-chalmers/kyle-chalmers-skills/[^\s)]+', text):
                parsed = urlsplit(target)
                parts = parsed.path.split('/')
                if len(parts) >= 6 and parts[3] in ('blob', 'tree') and parts[4] == 'main':
                    relative = unquote('/'.join(parts[5:]))
                    if not (ROOT / relative).exists():
                        failures.append(f'{item["video_id"]}: missing proposed destination {relative}')
    if failures:
        raise SystemExit('\n'.join(failures))
    print(f'Validated {len(documents)} tutorial documents, {len(provenance["files"])} imports and {count} proposed descriptions.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--description-spec', help='Optional local JSON proposal with changes and new_description fields')
    check(parser.parse_args().description_spec)
