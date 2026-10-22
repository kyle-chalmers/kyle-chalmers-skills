import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class InstallTests(unittest.TestCase):
    def run_installer(self, destination, *args):
        return subprocess.run([sys.executable, str(ROOT / 'scripts/install.py'), '--dest', str(destination), *args], capture_output=True, text=True)

    def test_copies_review_scripts_and_metadata(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / 'skills'
            result = self.run_installer(destination, '--skill', 'ai-friend-review')
            self.assertEqual(result.returncode, 0, result.stderr)
            for source in (ROOT / 'skills/ai-friend-review').rglob('*'):
                if source.is_file() and '__pycache__' not in source.parts and source.suffix != '.pyc':
                    installed = destination / 'ai-friend-review' / source.relative_to(ROOT / 'skills/ai-friend-review')
                    self.assertEqual(installed.read_bytes(), source.read_bytes())

    def test_conflict_stops_all_without_writing(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp)
            existing = destination / 'skill-chain'
            existing.mkdir()
            (existing / 'custom.txt').write_text('keep my changes')
            result = self.run_installer(destination, '--all')
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual((existing / 'custom.txt').read_text(), 'keep my changes')
            self.assertEqual({p.name for p in destination.iterdir()}, {'skill-chain'})

    def test_unknown_name_cannot_escape_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / 'skills'
            result = self.run_installer(destination, '--skill', '../unexpected')
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(destination.exists())

    def test_all_installs_every_catalog_entry(self):
        with tempfile.TemporaryDirectory() as temp:
            result = self.run_installer(temp, '--all')
            self.assertEqual(result.returncode, 0, result.stderr)
            expected = {s['name'] for s in json.loads((ROOT / 'catalog/skills.json').read_text())['skills']}
            self.assertEqual({p.name for p in Path(temp).iterdir()}, expected)

    def test_broken_symlink_is_protected(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp)
            link = destination / 'next-session-prompt'
            link.symlink_to(destination / 'missing')
            result = self.run_installer(destination, '--skill', 'next-session-prompt')
            self.assertNotEqual(result.returncode, 0)
            self.assertTrue(link.is_symlink())


if __name__ == '__main__':
    unittest.main()

