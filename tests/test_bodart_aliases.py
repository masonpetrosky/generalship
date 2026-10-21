"""Explicit identity scope, orientation and provenance; historical fitting is blocked."""

import copy
import math
from pathlib import Path
import unittest
from unittest.mock import patch

from generalship import bodart_aliases as aliases
from generalship import bodart_ratings as v1
from generalship import bodart_ratings_v2 as v2
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


class AliasTests(unittest.TestCase):
    def test_scoped_preparation_preserves_all_battle_readings_and_reservation(self):
        with patch.object(v1, 'fit', side_effect=AssertionError('no historical fit')), \
                patch('urllib.request.urlopen', side_effect=AssertionError('no fetch')):
            prepared = aliases.prepare(ROOT)
        self.assertEqual(prepared, read_json(ROOT / aliases.COHORT))
        original = read_json(ROOT / v1.COHORT)
        self.assertEqual(prepared['ledger'], original['ledger'])
        self.assertEqual(len(prepared['rows']), 542)
        self.assertEqual(prepared['alias_occurrences'], 111)
        self.assertEqual(len(prepared['groups']), 8)
        self.assertEqual(prepared['before']['labels'] - prepared['after']['labels'], 14)
        reserved = set(read_json(ROOT / v1.RESERVATION)['reserved_final'])
        for old, new in zip(original['rows'], prepared['rows']):
            self.assertEqual(old['id'], new['id'])
            self.assertNotIn(new['id'], reserved)
            self.assertLess(new['a'], new['b'])
            self.assertAlmostEqual(new['x'], math.log(new['personnel_a'] / new['personnel_b']))
            self.assertEqual(new['y'], 1 - old['y'] if new['orientation_flipped'] else old['y'])
            for key in ('year', 'decade', 'personnel_checked', 'record_status', 'source_id', 'source_sha256', 'locator'):
                self.assertEqual(new[key], old[key])
            self.assertEqual(sorted((old['a_raw'], old['b_raw'])), sorted((new['a_raw'], new['b_raw'])))
            self.assertEqual(sorted((old['personnel_a'], old['personnel_b'])), sorted((new['personnel_a'], new['personnel_b'])))

    def test_alias_flip_changes_both_sides_and_does_not_merge_a_similar_surname(self):
        rows = [{'id': 'toy', 'a': 'bonaparte', 'b': 'colli', 'a_raw': 'Gen. Bonaparte', 'b_raw': 'Gen. Colli',
                 'personnel_a': 20000, 'personnel_b': 10000, 'x': math.log(2), 'y': 1},
                {'id': 'other', 'a': 'bonaparte junior', 'b': 'colli', 'a_raw': 'Bonaparte junior', 'b_raw': 'Colli',
                 'personnel_a': 5000, 'personnel_b': 8000, 'x': math.log(5 / 8), 'y': 0}]
        group = {'canonical_unit': 'napoleon i', 'members': ['bonaparte', 'napoleon i']}
        first, other = aliases.migrate(rows, [group])
        self.assertTrue(first['orientation_flipped'])
        self.assertEqual((first['a'], first['b']), ('colli', 'napoleon i'))
        self.assertEqual(first['a_raw'], 'Gen. Colli')
        self.assertEqual(first['personnel_a'], 10000)
        self.assertEqual(first['y'], 0)
        self.assertEqual(other['a'], 'bonaparte junior')
        self.assertEqual(rows[0]['a'], 'bonaparte')

    def test_mapping_cannot_put_one_identity_on_both_sides(self):
        row = {'id': 'bad', 'a': 'bonaparte', 'b': 'napoleon i'}
        with self.assertRaisesRegex(ValueError, 'both sides'):
            aliases.migrate([row], [{'canonical_unit': 'napoleon i', 'members': ['bonaparte', 'napoleon i']}])

    def test_changed_source_bytes_and_occurrence_scope_are_rejected(self):
        parent = read_json(ROOT / v1.COHORT)
        with patch.object(aliases, 'digest', return_value='0' * 64):
            with self.assertRaisesRegex(ValueError, 'changed source'):
                aliases.load(ROOT, parent)
        real_read = aliases.read_json
        def altered(path):
            data = real_read(path)
            if path == ROOT / aliases.ALIASES:
                data['groups'][0]['scoped_occurrences'][0]['year'] += 1
            return data
        with patch.object(aliases, 'read_json', side_effect=altered):
            with self.assertRaisesRegex(ValueError, 'occurrence scope changed'):
                aliases.load(ROOT, parent)

    def test_index_omissions_are_retained_and_titles_are_not_silently_corrected(self):
        manifest = read_json(ROOT / aliases.ALIASES)
        groups = {g['id']: g for g in manifest['groups']}
        self.assertEqual(groups['karl']['index_unlisted_battle_ids'], ['B312c', 'B312d'])
        self.assertEqual(groups['melas']['index_unlisted_battle_ids'], ['B355c'])
        self.assertIn('Marquis-Wellesley', groups['wellington']['interpretation'])
        self.assertTrue(any('Marquis Wellesley' in o['raw_label'] for o in groups['wellington']['scoped_occurrences']))

    def test_force_predictions_are_equivalent_after_reorientation(self):
        rows = [{'id': str(i), 'a': 'bonaparte', 'b': 'colli', 'a_raw': 'Bonaparte', 'b_raw': 'Colli',
                 'personnel_a': 10000 + i * 1000, 'personnel_b': 12000, 'x': math.log((10 + i) / 12),
                 'y': int(i % 3 != 0)} for i in range(6)]
        migrated = aliases.migrate(rows, [{'canonical_unit': 'napoleon i', 'members': ['bonaparte', 'napoleon i']}])
        old, new = v1.fit(rows, commanders=False), v1.fit(migrated, commanders=False)
        self.assertAlmostEqual(old['beta'], new['beta'], places=10)
        for a, b in zip(rows, migrated):
            self.assertAlmostEqual(v1.predict(old, a), 1 - v1.predict(new, b), places=12)

    def test_saved_rerun_checks_without_historical_fitting(self):
        if not (ROOT / v2.RUN).is_file():
            self.skipTest('explicit historical job has not run yet')
        cohort, saved = read_json(ROOT / aliases.COHORT), read_json(ROOT / v2.RUN)
        with patch.object(v1, 'fit', side_effect=AssertionError('no historical fit')):
            v2.verify(ROOT, cohort, saved)
        altered = copy.deepcopy(saved)
        altered['folds'][0]['train_ids'].append(altered['folds'][0]['test_ids'][0])
        with self.assertRaisesRegex(ValueError, 'training scope'):
            v2.verify(ROOT, cohort, altered)


if __name__ == '__main__':
    unittest.main()
