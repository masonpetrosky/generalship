from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from generalship.cli import run_build
from generalship.sources import digest, read_json, write_json

ROOT = Path(__file__).resolve().parents[1]


def copy_methods_design(root):
    """Bound research designs also need to exist in temporary offline data fixtures."""
    (root / 'docs').mkdir(exist_ok=True)
    shutil.copyfile(ROOT / 'docs/napoleonic-methods-v1.md', root / 'docs/napoleonic-methods-v1.md')
    shutil.copyfile(ROOT / 'docs/napoleonic-ledgers-v1.md', root / 'docs/napoleonic-ledgers-v1.md')


class WorkflowTests(unittest.TestCase):
    def test_draft_quantities_do_not_change_baseline(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copytree(ROOT / 'data', root / 'data')
            copy_methods_design(root)
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
            copy_methods_design(root)
            if (ROOT / 'artifacts/napoleonic-methods-v1.json').is_file():
                (root / 'artifacts').mkdir()
                shutil.copyfile(ROOT / 'artifacts/napoleonic-methods-v1.json',
                                root / 'artifacts/napoleonic-methods-v1.json')
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
