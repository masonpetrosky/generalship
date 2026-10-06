"""Profile-driven grade E (docs/commander-ratings-v4.md §2): reproduction of run 3 and the pre-start view."""

from pathlib import Path
import unittest

from generalship import imputation as v1
from generalship import imputation_v2 as v2
from generalship.estimates import input_rows
from generalship.frame import CIVIL_WAR
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]
LEDGER_V2 = 'data/estimates/side-strength-v2.json'


def as_v1(out):
    """The v2 output in v1's shape: v2 adds a profile, options and the pre-start view and names grade D 'modelled'."""
    out = {k: v for k, v in out.items() if k not in {'version', 'profile', 'options', 'pre_start_view'}}
    out['composition'] = {k: {'training': v['training'], 'grade_D': v['modelled']} for k, v in out['composition'].items()}
    out['selection_descriptive'] = {k.replace('modelled_', 'grade_D_'): v for k, v in out['selection_descriptive'].items()}
    return out


class ReproductionTests(unittest.TestCase):
    def test_run_3_settings_reproduce_imputation_v1_exactly(self):
        for options in ({}, {'train_grades': 'AB'}, {'all_bounds': True}, {'joint_ledger_echelon': True}):
            with self.subTest(**options):
                old = v1.impute(ROOT, verify=False, **options)
                old.pop('version')
                new = v2.impute(ROOT, CIVIL_WAR, strength=LEDGER_V2, prestart=False, **options)
                self.assertEqual(as_v1(new), old)

    def test_the_committed_v1_output_is_reproduced(self):
        stored = read_json(ROOT / 'artifacts/strength-imputation-v1.json')
        for k in ('bindings', 'version'):
            stored.pop(k)
        self.assertEqual(as_v1(v2.impute(ROOT, CIVIL_WAR, strength=LEDGER_V2, prestart=False)), stored)


class PrestartViewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = read_json(ROOT / CIVIL_WAR['strength_ledger'])
        cls.view = v2.prestart_view(cls.ledger)

    def test_every_post_start_side_is_re_estimated_without_post_start_groups(self):
        post = {(e['battle_id'], s) for e in self.ledger['engagements'] for s in CIVIL_WAR['sides']
                if 'post_start_information' in e['sides'][s]['estimate']['labels']}
        self.assertEqual(set(self.view), post)
        for key, v in self.view.items():
            self.assertNotIn('post_start_information', v['estimate']['labels'], key)
            self.assertFalse(any(input_rows(i)['row3'] for i in v['inputs']), key)
            self.assertTrue(v['removed_inputs'], key)

    def test_pre_start_evidence_is_kept(self):
        # VA111 US: two grade A counts; only the opponent's post-start figure, which raised the range, is removed.
        v = self.view[('VA111', 'US')]
        self.assertEqual(v['removed_inputs'], ['us-vaughn-june6'])
        self.assertEqual((v['estimate']['grade'], v['estimate']['point']), ('A', 8500))
        self.assertLess(v['estimate']['high'], v['ledger_estimate']['high'])

    def test_a_dependence_group_is_removed_whole(self):
        # VA017 Confederate: the CWSAC and NPS figures reproduce Livermore's post-start figure.
        v = self.view[('VA017', 'Confederate')]
        self.assertEqual(v['removed_inputs'], ['cs-cw', 'cs-lv', 'cs-nps'])
        self.assertEqual(v['estimate']['grade'], 'D')

    def test_post_start_sides_without_pre_start_evidence_are_modelled(self):
        out = v2.impute(ROOT, CIVIL_WAR)
        modelled = {(s['battle_id'], s['side']) for s in out['sides'] if 'post_start_modelled' in s['labels']}
        expected = {k for k, v in self.view.items() if v['estimate']['grade'] == 'D'}
        self.assertEqual(modelled, expected)
        self.assertEqual(len(out['pre_start_view']), len(self.view))
        graded_d = sum(e['sides'][s]['estimate']['grade'] == 'D' for e in self.ledger['engagements'] for s in CIVIL_WAR['sides'])
        self.assertEqual(len(out['sides']), graded_d + len(expected))


class ProfileTests(unittest.TestCase):
    def test_levels_come_from_the_profile(self):
        profile = {'echelons': ('army', 'unknown'), 'sides': ('X', 'Y'), 'periods': (('early', 1, 2), ('late', 3, 4)),
                   'theaters': ('North', 'Centre', 'South'),
                   'reference': {'echelon': 'unknown', 'side': 'X', 'period': 'early', 'theater': 'North'}}
        rows = ([{'echelon': 'army', 'side': 'X', 'period': 'early', 'theater': 'North'}] * 6
                + [{'echelon': 'unknown', 'side': 'Y', 'period': 'late', 'theater': 'South'}] * 6
                + [{'echelon': 'army', 'side': 'Y', 'period': 'late', 'theater': 'Centre'}] * 2)
        mapping, levels, merges = v2.levels_for(rows, profile)
        self.assertEqual(levels, {'echelon': ['army'], 'side': ['Y'], 'period': ['late'], 'theater': ['South']})
        # Centre has 2 rows: merged into an adjacent level of the declared order (North is first in a tie).
        self.assertEqual(mapping['theater']['Centre'], 'North')
        self.assertEqual(merges, {'theater=Centre': {'into': 'North', 'training_rows': 2}})


if __name__ == '__main__':
    unittest.main()
