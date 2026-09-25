"""Cohort-v2 ledger scaffolding (docs/ledgers-v2.md): successor checks leave the v1 ledgers frozen."""

import copy
from pathlib import Path
import unittest

from generalship import command, estimates, estimates_v2
from generalship.sources import digest, read_json

ROOT = Path(__file__).resolve().parents[1]


class V2CheckerTests(unittest.TestCase):
    def test_v1_strength_ledger_still_binds_the_unchanged_engine(self):
        ledger = read_json(ROOT / estimates.DEFAULT_LEDGER)
        self.assertEqual(ledger['bindings']['script']['sha256'], digest(ROOT / 'generalship/estimates.py'))
        self.assertEqual(ledger['bindings']['cohort']['path'], 'data/pilot/cohort.json')

    def test_v2_strength_checker_requires_a_version_2_ledger(self):
        ledger = copy.deepcopy(read_json(ROOT / estimates.DEFAULT_LEDGER))
        with self.assertRaisesRegex(estimates.EstimateError, 'Ledger version'):
            estimates_v2.check(ROOT, ledger=ledger)

    def test_v2_strength_checker_shares_the_v1_engine(self):
        self.assertIs(estimates_v2.estimate_side, estimates.estimate_side)
        self.assertIs(estimates_v2.CONSTANTS, estimates.CONSTANTS)

    def test_unbound_registry_is_only_for_subset_checks(self):
        ledger = read_json(ROOT / command.DEFAULT_LEDGER)
        registry = read_json(ROOT / command.DEFAULT_REGISTRY)
        with self.assertRaisesRegex(command.CommandError, 'draft subset checks only'):
            command.check(ROOT, ledger=ledger, registry=registry)

    def test_command_checker_reads_the_cohort_its_ledger_binds(self):
        ledger = copy.deepcopy(read_json(ROOT / command.DEFAULT_LEDGER))
        ledger['bindings']['cohort'] = {'path': 'data/pilot/cohort-v2.json', 'sha256': digest(ROOT / 'data/pilot/cohort-v2.json')}
        with self.assertRaisesRegex(command.CommandError, 'Coverage'):
            command.check(ROOT, ledger=ledger)


if __name__ == '__main__':
    unittest.main()


class V2RuleTests(unittest.TestCase):
    def test_v2_rank_order_extends_v1_without_reordering_it(self):
        for service in ('army', 'navy'):
            v1, v2 = command.RANK_ORDER[service], command.RANK_ORDER_V2[service]
            self.assertEqual([r for r in v2 if r in v1], v1)
        self.assertLess(command.rank_level('Major', '0', command.RANK_ORDER_V2),
                        command.rank_level('Captain', '0', command.RANK_ORDER_V2))
        self.assertEqual(command.rank_level('Acting Master', '1', command.RANK_ORDER_V2),
                         command.rank_level('Master', '1', command.RANK_ORDER_V2))
        with self.assertRaises(command.CommandError):
            command.rank_level('Major', '0')

    def test_v1_ledger_rejects_the_v2_rank_order(self):
        ledger = copy.deepcopy(read_json(ROOT / command.DEFAULT_LEDGER))
        ledger['rank_order'] = command.RANK_ORDER_V2
        with self.assertRaisesRegex(command.CommandError, 'Rank order'):
            command.check(ROOT, ledger=ledger)


class PassageMergeTests(unittest.TestCase):
    def test_a_passage_merge_needs_a_listed_target(self):
        ledger = read_json(ROOT / command.DEFAULT_LEDGER)
        registry = copy.deepcopy(read_json(ROOT / command.DEFAULT_REGISTRY))
        target = next(c for c in registry['commanders'] if c.get('passage_citation'))
        target['passage_merges'] = [{'passage_id': 'x', 'name': 'x', 'basis': 'test',
                                     'citation': dict(target['passage_citation'])}]
        bid = target['passage_citation']['battle_id']
        with self.assertRaisesRegex(command.CommandError, 'listed target'):
            command.check(ROOT, ledger=ledger, only=[bid], registry=registry)


class V2LedgerReplayTests(unittest.TestCase):
    def test_committed_v2_ledgers_replay(self):
        if (ROOT / estimates_v2.DEFAULT_LEDGER).is_file():
            result = estimates_v2.check(ROOT)
            self.assertEqual(result['in_scope'], 305)
            self.assertFalse(result['fitted'])
        path = 'data/command/responsibility-v2.json'
        if (ROOT / path).is_file():
            result = command.check(ROOT, path)
            self.assertEqual(result['engagements'], 305)
            self.assertFalse(result['rated'])
