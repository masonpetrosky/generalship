"""The v3 strength ledger (docs/ledgers-v3.md): carried forward, re-derived and replayed."""

import copy
from pathlib import Path
import unittest

from generalship import estimates_v3 as e3
from generalship.estimates import EstimateError
from generalship.replay import bound_view
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


class V3LedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = read_json(ROOT / e3.DEFAULT_LEDGER)

    def check(self, ledger):
        with bound_view(ROOT, e3.DEFAULT_LEDGER) as view:
            return e3.check(view, e3.DEFAULT_LEDGER, ledger)

    def test_committed_ledger_replays_and_rebuilds(self):
        result = self.check(self.ledger)
        self.assertEqual(sum(result['side_grades'].values()), 2 * result['in_scope'])
        self.assertEqual(e3.build(ROOT), self.ledger)

    def test_only_grade_d_sides_gain_inputs(self):
        v2 = read_json(ROOT / e3.PREDECESSOR)
        v2_by = {e['battle_id']: e for e in v2['engagements']}
        for e in self.ledger['engagements']:
            for s in ('US', 'Confederate'):
                old = v2_by[e['battle_id']]['sides'][s]
                if old['estimate']['grade'] != 'D':
                    self.assertEqual(e['sides'][s]['inputs'], old['inputs'])

    def test_tampering_fails(self):
        led = copy.deepcopy(self.ledger)
        graded = next(e for e in led['engagements'] if e['sides']['US']['estimate']['grade'] == 'A')
        graded['sides']['US']['inputs'].append(copy.deepcopy(graded['sides']['US']['inputs'][0]) | {'id': 'us-extra'})
        with self.assertRaises(EstimateError):
            self.check(led)
        led = copy.deepcopy(self.ledger)
        e = next(e for e in led['engagements'] for s in ('US', 'Confederate')
                 if any(i['id'].endswith('-cws2') for i in e['sides'][s]['inputs']))
        side = next(s for s in ('US', 'Confederate') if any(i['id'].endswith('-cws2') for i in e['sides'][s]['inputs']))
        inp = next(i for i in e['sides'][side]['inputs'] if i['id'].endswith('-cws2'))
        inp['printed'] = {'lower': inp['printed']['lower'] + 1, 'upper': inp['printed']['upper'] + 1}
        with self.assertRaises(EstimateError):
            self.check(led)
        led = copy.deepcopy(self.ledger)
        e = next(e for e in led['engagements'] if any(e['inventory'].get('upstream', {}).get(s) for s in ('US', 'Confederate')))
        s = next(s for s in ('US', 'Confederate') if e['inventory']['upstream'].get(s))
        e['inventory']['upstream'][s] = e['inventory']['upstream'][s][1:]
        with self.assertRaises(EstimateError):
            self.check(led)

    def test_links_and_zero_cells(self):
        links = {'A1': [('7', 'eq', ['A1'])], 'B1': [('8', 'eq', ['B1', 'B2'])], 'C1': [('9', 'neq', ['C1'])],
                 'D1': [('1', 'eq', ['D1']), ('2', 'eq', ['D1'])]}
        self.assertEqual(e3.link_status(links, 'A1'), [('7', 'ok')])
        self.assertIn('covers 2 records', e3.link_status(links, 'B1')[0][1])
        self.assertIn("'neq'", e3.link_status(links, 'C1')[0][1])
        self.assertTrue(all(st != 'ok' for _, st in e3.link_status(links, 'D1')))
        self.assertIsNone(e3._value('0'))
        self.assertIsNone(e3._value(''))
        self.assertEqual(e3._value('4100'), 4100)
