"""Bound views for replaying frozen ledgers (docs/ledger-replay.md §5)."""

import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from generalship import command, estimates, estimates_v2
from generalship.replay import ReplayError, _mirror, bound_dossier, bound_view, substitutions
from generalship.sources import digest, read_json

ROOT = Path(__file__).resolve().parents[1]
FROZEN = [(estimates.DEFAULT_LEDGER, estimates.check), (command.DEFAULT_LEDGER, command.check),
          (estimates_v2.DEFAULT_LEDGER, estimates_v2.check), ('data/command/responsibility-v2.json', command.check)]
LIVE = 'data/evidence/X001.json'


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(value if isinstance(value, bytes) else (json.dumps(value) + '\n').encode())
    return digest(path)


def ledger(sha, path=LIVE):
    return {'bindings': {'dossiers': {'X001': {'path': path, 'sha256': sha}}}}


class SyntheticTree(unittest.TestCase):
    """X001 corrected twice: live v3 supersedes archive v2, which supersedes archive v1."""

    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix='replay-test-'))
        self.addCleanup(shutil.rmtree, self.root, True)
        history = self.root / 'data/evidence/history'
        self.v1 = write(history / 'X001.v1.json', {'battle_id': 'X001', 'note': 'v1'})
        self.v2 = write(history / 'X001.v2.json', {'battle_id': 'X001', 'note': 'v2', 'supersedes': {
            'path': 'data/evidence/history/X001.v1.json', 'sha256': self.v1}})
        self.v3 = self.relink({'path': 'data/evidence/history/X001.v2.json', 'sha256': self.v2})

    def relink(self, supersedes, battle='X001'):
        return write(self.root / LIVE, {'battle_id': battle, 'note': 'live', 'supersedes': supersedes})

    def resolve(self, sha):
        return bound_dossier(self.root, {'path': LIVE, 'sha256': sha})


class ResolutionTests(SyntheticTree):
    def test_live_match_and_archive_chains(self):
        self.assertEqual(self.resolve(self.v3), (self.root / LIVE).resolve())
        self.assertEqual(self.resolve(self.v2), (self.root / 'data/evidence/history/X001.v2.json').resolve())
        self.assertEqual(self.resolve(self.v1), (self.root / 'data/evidence/history/X001.v1.json').resolve())
        self.assertIsNone(self.resolve('0' * 64))

    def test_broken_archive_hash(self):
        write(self.root / 'data/evidence/history/X001.v2.json', b'{"battle_id": "X001", "note": "edited"}\n')
        self.assertIsNone(self.resolve(self.v1))

    def test_wrong_battle(self):
        other = write(self.root / 'data/evidence/history/X002.v1.json', {'battle_id': 'X002'})
        self.relink({'path': 'data/evidence/history/X002.v1.json', 'sha256': other})
        self.assertIsNone(self.resolve(other))

    def test_repeated_path(self):
        loop = self.root / 'data/evidence/history/X001.loop.json'
        sha = write(loop, {'battle_id': 'X001', 'supersedes': {'path': 'data/evidence/history/X001.loop.json',
                                                               'sha256': 'f' * 64}})
        self.relink({'path': 'data/evidence/history/X001.loop.json', 'sha256': sha})
        self.assertIsNone(self.resolve('f' * 64))

    def test_paths_outside_history_or_root(self):
        outside = write(self.root / 'data/evidence/X001-old.json', {'battle_id': 'X001'})
        for path in ('data/evidence/X001-old.json', 'data/evidence/history/../X001-old.json', '../outside.json'):
            self.relink({'path': path, 'sha256': outside})
            self.assertIsNone(self.resolve(outside), path)

    def test_missing_or_unreadable_files(self):
        self.relink({'path': 'data/evidence/history/X001.v9.json', 'sha256': self.v1})
        self.assertIsNone(self.resolve(self.v1))
        self.assertIsNone(bound_dossier(self.root, {'path': 'data/evidence/X999.json', 'sha256': self.v1}))
        write(self.root / LIVE, b'not json')
        self.assertIsNone(self.resolve(self.v1))
        self.assertIsNone(bound_dossier(self.root, None))


class ViewTests(SyntheticTree):
    def test_nothing_to_substitute_yields_the_root_and_keeps_it(self):
        with bound_view(self.root, ledger(self.v3)) as view:
            self.assertEqual(view, self.root)
        with self.assertRaises(RuntimeError):
            with bound_view(self.root, ledger(self.v3), 'data/no-such-ledger.json'):
                raise RuntimeError
        self.assertEqual(digest(self.root / LIVE), self.v3)

    def test_substitution_presents_the_bound_bytes_and_leaves_the_tree(self):
        with bound_view(self.root, ledger(self.v1)) as view:
            self.assertNotEqual(view, self.root)
            self.assertEqual(digest(view / LIVE), self.v1)
            self.assertEqual(digest(view / 'data/evidence/history/X001.v2.json'), self.v2)
        self.assertFalse(view.exists())
        self.assertEqual(digest(self.root / LIVE), self.v3)
        self.assertEqual(digest(self.root / 'data/evidence/history/X001.v1.json'), self.v1)

    def test_view_is_removed_after_an_error(self):
        views = []
        with self.assertRaises(RuntimeError):
            with bound_view(self.root, ledger(self.v1)) as view:
                views.append(view)
                raise RuntimeError
        self.assertFalse(views[0].exists())
        self.assertEqual(digest(self.root / LIVE), self.v3)

    def test_conflicting_bindings(self):
        for pair in ((self.v1, self.v2), (self.v3, self.v1)):  # two archives; a live match and an archive
            with self.assertRaises(ReplayError):
                with bound_view(self.root, ledger(pair[0]), ledger(pair[1])):
                    pass

    def test_unreachable_bindings_fail_closed_and_never_conflict(self):
        self.assertEqual(substitutions(self.root, ledger('0' * 64)), {})
        with bound_view(self.root, ledger('0' * 64), ledger(self.v1)) as view:
            self.assertEqual(digest(view / LIVE), self.v1)


class FrozenLedgerTests(unittest.TestCase):
    def test_every_frozen_binding_is_reachable(self):
        for path, _ in FROZEN:
            for bid, binding in read_json(ROOT / path)['bindings']['dossiers'].items():
                self.assertIsNotNone(bound_dossier(ROOT, binding), f'{path} {bid}')

    def test_a_corrected_bound_dossier_replays_through_a_view(self):
        tmp = Path(tempfile.mkdtemp(prefix='replay-simulation-'))
        self.addCleanup(shutil.rmtree, tmp, True)
        mirror = tmp / 'repo'
        mirror.mkdir()
        _mirror(ROOT, mirror)
        bindings = [read_json(ROOT / path)['bindings']['dossiers'] for path, _ in FROZEN]
        bid = next(b for b in sorted(set.intersection(*map(set, bindings)))
                   if all(digest(ROOT / bs[b]['path']) == bs[b]['sha256'] for bs in bindings))
        live, before = f'data/evidence/{bid}.json', digest(ROOT / f'data/evidence/{bid}.json')
        versions = [int(m) for m in re.findall(rf'{bid}\.v(\d+)\.json', ' '.join(
            p.name for p in (ROOT / 'data/evidence/history').glob(f'{bid}.v*.json')))]
        archive = f'data/evidence/history/{bid}.v{max(versions, default=0) + 1}.json'
        corrected = read_json(ROOT / live)
        corrected['boundary_note'] += ' (simulated correction)'
        corrected['supersedes'] = {'path': archive, 'sha256': before}
        shutil.copyfile(ROOT / live, mirror / archive)  # a new file in the mirror
        (mirror / live).unlink()  # never write through a hard link
        (mirror / live).write_text(json.dumps(corrected, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        for path, check in FROZEN:
            with self.assertRaisesRegex(ValueError, 'Dossier binding'):
                check(mirror, path)
        with bound_view(mirror, *(path for path, _ in FROZEN)) as view:
            for path, check in FROZEN:
                check(view, path)
        self.assertEqual(digest(ROOT / live), before)
        self.assertFalse((ROOT / archive).exists())


if __name__ == '__main__':
    unittest.main()
