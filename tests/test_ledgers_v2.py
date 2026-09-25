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
