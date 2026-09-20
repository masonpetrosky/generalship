from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from generalship.cli import run_build
from generalship.sources import digest, read_json, write_json

ROOT = Path(__file__).resolve().parents[1]


class WorkflowTests(unittest.TestCase):
    def test_draft_quantities_do_not_change_baseline(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copytree(ROOT / 'data', root / 'data')
            run_build(root, write=True)
            before = read_json(root / 'artifacts/baseline.json')
            path = root / 'data/evidence/TN003.json'
            dossier = read_json(path)
            # Valid structural mutation is NOT historical validation. This test
            # verifies that the research layer cannot silently become a feature.
            q = dossier['quantities'][0]
            q['lower'] = q['upper'] = 1
            write_json(path, dossier)
            run_build(root, write=True)
            self.assertEqual(before, read_json(root / 'artifacts/baseline.json'))

    def test_offline_build_is_reproducible_and_receipt_matches(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for directory in ('data', 'generalship'):
                shutil.copytree(ROOT / directory, root / directory)
            first = run_build(root, write=True)
            receipt = read_json(root / 'artifacts/receipt.json')
            second = run_build(root, write=True)
            self.assertEqual(first, second)
            self.assertEqual(receipt, read_json(root / 'artifacts/receipt.json'))
            for name, sha in receipt['output_sha256'].items():
                self.assertEqual(digest(root/'artifacts'/name), sha)
            self.assertTrue((root / 'artifacts/pilot-report.md').is_file())

    def test_cli_bad_root_exits_nonzero_without_traceback(self):
        with tempfile.TemporaryDirectory() as temp:
            process = subprocess.run([sys.executable, '-m', 'generalship', '--root', temp, 'check'],
                                     cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(process.returncode, 1)
        self.assertIn('generalship:', process.stderr)
        self.assertNotIn('Traceback', process.stderr)
