"""Saved prediction presentation: orientation, ranking and frozen-run integrity."""

import copy
from pathlib import Path
import unittest
from unittest.mock import patch

from generalship import baseline, napoleonic_benchmark_run
from generalship import napoleonic_surprises as surprises
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]
FRAME = {e['id']: e for e in read_json(ROOT / 'data/napoleonic/frame-v1.json')['entries']}


class SurpriseTests(unittest.TestCase):
    def test_saved_predictions_only_and_exact_development_coverage(self):
        with patch.object(baseline, 'fit_logistic') as base, patch.object(napoleonic_benchmark_run, 'fit_logistic') as fit:
            rows = surprises.load_rows(ROOT, FRAME)
        base.assert_not_called(); fit.assert_not_called()
        self.assertEqual(len(rows), 194)
        self.assertEqual(sum(r['opponent_ratio'] > 1 for r in rows), 54)
        reserved = set(read_json(ROOT / 'data/napoleonic/methods-v1/evaluation.json')['reserved_final'])
        self.assertFalse(reserved & {r['battle_id'] for r in rows})

    def test_losing_a_side_probability_is_complemented_for_actual_winner(self):
        rows = {r['battle_id']: r for r in surprises.load_rows(ROOT, FRAME)}
        pressburg = rows['B406c']; graz = rows['B409a']
        self.assertEqual(pressburg['winner_side'], 'B')
        self.assertEqual((pressburg['winner_troops'], pressburg['other_troops']), (5000, 18000))
        self.assertAlmostEqual(pressburg['winner_probability'], 1 - pressburg['a_probability'])
        self.assertEqual(graz['winner_side'], 'A')
        self.assertEqual(graz['winner_probability'], graz['a_probability'])
        self.assertEqual(graz['opponent_ratio'], 4.4)
        self.assertEqual(rows['B431c']['winner'], 'Prussia')

    def test_two_orders_answer_different_questions(self):
        rows = surprises.load_rows(ROOT, FRAME)
        self.assertEqual(rows[0]['battle_id'], 'B406c')
        self.assertEqual(max(rows, key=lambda r: r['opponent_ratio'])['battle_id'], 'B409a')
        self.assertTrue(all(a['winner_probability'] <= b['winner_probability'] for a, b in zip(rows, rows[1:])))

    def test_changed_dataset_and_duplicate_forecasts_cannot_be_presented_as_saved_run(self):
        with patch.object(surprises, 'digest', return_value='0'*64):
            with self.assertRaisesRegex(ValueError, 'unchanged development-only'):
                surprises.load_rows(ROOT, FRAME)
        original = read_json(ROOT / surprises.RUN); changed = copy.deepcopy(original)
        preds = changed['populations']['primary']['leave_campaign_out']['predictions']
        preds.append(copy.deepcopy(preds[0]))
        with patch.object(surprises, 'read_json', side_effect=lambda p: changed if p == ROOT / surprises.RUN else read_json(p)):
            with self.assertRaisesRegex(ValueError, 'Duplicate saved forecasts'):
                surprises.load_rows(ROOT, FRAME)


if __name__ == '__main__':
    unittest.main()
