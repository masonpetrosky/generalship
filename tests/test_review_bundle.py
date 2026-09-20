import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

from scripts.prepare_shiloh_review import BUNDLE_ID, OUTPUT, RECIPE, build

ROOT = Path(__file__).resolve().parents[1]


class ReviewBundleTests(unittest.TestCase):
    def test_bundle_is_complete_deterministic_and_explicitly_unreviewed(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / 'output'
            first = build(ROOT, output)
            second = build(ROOT, output)
            self.assertEqual(first['sha256'], second['sha256'])
            with zipfile.ZipFile(first['bundle']) as archive:
                manifest = json.loads(archive.read(f'{OUTPUT}/MANIFEST.json'))
                expected = set(manifest['payload_sha256']) | {f'{OUTPUT}/MANIFEST.json'}
                self.assertEqual(set(archive.namelist()), expected)
                self.assertEqual(len(archive.namelist()), len(expected))
                for name, checksum in manifest['payload_sha256'].items():
                    self.assertEqual(hashlib.sha256(archive.read(name)).hexdigest(), checksum)
                dossier = json.loads(archive.read('data/evidence/TN003.json'))
                coverage = json.loads(archive.read(f'{OUTPUT}/REVIEW-COVERAGE.json'))
                self.assertFalse(coverage['review_completed'])
                self.assertIsNone(coverage['reviewer']['identity'])
                for category in ('claims', 'quantities', 'events'):
                    self.assertEqual([r['id'] for r in coverage[category]],
                                     [r['id'] for r in dossier[category]])
                    self.assertTrue(all(r['decision'] == 'not_reviewed' for r in coverage[category]))
                self.assertEqual(len(coverage['scan_checks']), 26)
                sources = json.loads(archive.read('data/sources.json'))['sources']
                for source in sources:
                    self.assertEqual(hashlib.sha256(archive.read(source['path'])).hexdigest(), source['sha256'])
                self.assertNotIn(b'{{DOSSIER_SHA256}}', archive.read(f'{OUTPUT}/PROMPT.md'))

    def test_extracted_verifier_detects_tampering(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            result = build(ROOT, root / 'output')
            with zipfile.ZipFile(result['bundle']) as archive:
                archive.extractall(root / 'extracted')
            verifier = root / 'extracted/verify_bundle.py'
            good = subprocess.run([sys.executable, str(verifier)], capture_output=True, text=True)
            self.assertEqual(good.returncode, 0, good.stderr)
            # A later live dossier must not make this frozen review impossible to reproduce.
            live_dossier = root / 'extracted/data/evidence/TN003.json'
            prior = live_dossier.read_bytes()
            live_dossier.write_text('{}')
            rebuilt = build(root / 'extracted', root / 'rebuilt')
            self.assertEqual(rebuilt['sha256'], result['sha256'])
            live_dossier.write_bytes(prior)
            (root / 'extracted/data/raw/shiloh/or-nelson-reinforcements-v1.txt').write_text('changed')
            bad = subprocess.run([sys.executable, str(verifier)], capture_output=True, text=True)
            self.assertNotEqual(bad.returncode, 0)
            self.assertIn('Checksum mismatch', bad.stderr)

    def test_changed_frozen_evidence_cannot_replace_existing_handoff(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            config = json.loads((ROOT / RECIPE / 'config.json').read_text())
            # Only inputs encountered before the changed dossier are needed for this failure.
            for name in config['expected_input_sha256']:
                origin = config['snapshot_copies'].get(name, name)
                target = root / origin
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / origin, target)
                if name == 'data/evidence/TN003.json':
                    target.write_text('{}')
                    break
            (root / RECIPE).mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / RECIPE / 'config.json', root / RECIPE / 'config.json')
            output = root / 'output'
            output.mkdir()
            previous = output / f'{BUNDLE_ID}.zip'
            previous.write_bytes(b'previous-handoff')
            with self.assertRaisesRegex(ValueError, 'Frozen input changed: data/evidence/TN003.json'):
                build(root, output)
            self.assertEqual(previous.read_bytes(), b'previous-handoff')


if __name__ == '__main__':
    unittest.main()
