"""Command-responsibility ledger checker (docs/commander-ratings.md §2)."""

import copy
from pathlib import Path
import unittest

from generalship.command import CommandError, check, contained_pairs, rank_level
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


class RuleTests(unittest.TestCase):
    def test_rank_order_and_brevet_or_acting_ranks(self):
        self.assertLess(rank_level('General', '0'), rank_level('Lieutenant General', '0'))
        self.assertEqual(rank_level('Brevet Colonel', '0'), rank_level('Colonel', '0'))
        self.assertEqual(rank_level('Acting Rear Admiral', '1'), rank_level('Rear Admiral', '1'))
        with self.assertRaises(CommandError):
            rank_level('Major', '0')

    def test_contained_pairs_need_same_campaign_and_a_strictly_inner_interval(self):
        battles = {'A': {'campaign': 'c', 'start_date': '1863-05-01', 'end_date': '1863-05-06'},
                   'B': {'campaign': 'c', 'start_date': '1863-05-03', 'end_date': '1863-05-03'},
                   'C': {'campaign': 'd', 'start_date': '1863-05-03', 'end_date': '1863-05-03'}}
        self.assertEqual(contained_pairs(battles, ['A', 'B', 'C']), [('A', 'B')])


class LedgerTests(unittest.TestCase):
    base = None

    @classmethod
    def setUpClass(cls):
        cls.base = read_json(ROOT / 'data/command/responsibility-v1.json')

    def test_committed_ledger_replays(self):
        result = check(ROOT)
        self.assertEqual((result['engagements'], result['sides']), (91, 182))
        self.assertFalse(result['rated'])

    def tampered(self, message, change):
        ledger = copy.deepcopy(self.base)
        change({e['battle_id']: e for e in ledger['engagements']}, ledger)
        with self.assertRaisesRegex(CommandError, message):
            check(ROOT, ledger=ledger)

    def test_tampered_ledgers_fail(self):
        self.tampered('grade D if and only if', lambda E, L: E['TN003']['sides']['US'].update(grade='D', rule='3c'))
        self.tampered('grade B cites only the listing', lambda E, L: E['IN001']['sides']['US'].update(
            citations=E['IN001']['sides']['US']['citations'] + E['IN001']['sides']['Confederate']['citations'][1:]))
        self.tampered('not accounted for', lambda E, L: E['TN003']['sides']['US'].update(candidates=[]))
        self.tampered('mixed services require rule 5', lambda E, L: E['TN001']['sides']['US'].update(
            rule='3a', labels=['joint_command', 'responsibility_unresolved']))
        self.tampered('rule 3\\(c\\) needs a tie', lambda E, L: E['VA026']['sides']['Confederate'].update(
            rule='3c', grade='D', commander_id=None, candidates=['cs-robert-e-lee', 'cs-thomas-j-jackson']))
        self.tampered('quote not in passage', lambda E, L: E['NC003']['sides']['Confederate']['citations'][1].update(quote='commanded by nobody'))
        self.tampered('Nesting', lambda E, L: L['nesting'].pop())
        self.tampered('superior_directing names a superior', lambda E, L: E['MS001']['sides']['US'].update(superior=None))
        self.tampered('Coverage', lambda E, L: L['engagements'].pop())


if __name__ == '__main__':
    unittest.main()
