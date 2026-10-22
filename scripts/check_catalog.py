#!/usr/bin/env python3
"""Validate catalog coverage, provenance, manifests, and packaged resources offline."""

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check() -> None:
    catalog = json.loads((ROOT / 'catalog/skills.json').read_text())
    names = [s['name'] for s in catalog['skills']]
    assert len(names) == len(set(names)), 'Duplicate catalog names'
    actual = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
    assert set(names) == actual, 'Catalog and skill directories differ'
    for skill in catalog['skills']:
        folder = ROOT / skill['path']
        assert folder == ROOT / 'skills' / skill['name']
        text = (folder / 'SKILL.md').read_text()
        assert text.startswith('---\n') and '\n---\n' in text[4:]
        frontmatter = text.split('---', 2)[1]
        assert re.search(r'^name:\s*' + re.escape(skill['name']) + r'\s*$', frontmatter, re.M)
        assert re.search(r'^description:\s*\S', frontmatter, re.M)
        assert skill['category'] in catalog['categories']
        assert not any(p.is_symlink() for p in folder.rglob('*')), 'Packaged symlink'
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if '://' not in link and not link.startswith(('#', '<')):
                assert (folder / link.split('#')[0]).exists(), f'Missing resource: {skill["name"]}/{link}'
    provenance = json.loads((ROOT / 'catalog/provenance.json').read_text())
    assert {s['name'] for s in provenance['skills']} == set(names)
    for source in provenance['skills']:
        for file in source['files']:
            data = (ROOT / file['destination_path']).read_bytes()
            git_sha = hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()
            if file['destination_path'] not in source.get('changed_files', []):
                assert git_sha == file['original_blob_sha'], f'Undocumented change: {file["destination_path"]}'
    marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    plugin = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
    assert marketplace['plugins'][0]['name'] == plugin['name']
    assert marketplace['plugins'][0]['source'] == './'
    assert {p['name'] for p in marketplace['plugins'][1:]} == {s['name'] for s in catalog['external_suites']}
    print(f'Validated {len(names)} portable skills, {len(catalog["external_suites"])} external suites, provenance, and plugin manifests.')


if __name__ == '__main__':
    check()

