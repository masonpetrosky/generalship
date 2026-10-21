"""Saved-run verification checks every holdout without historical refitting."""

import copy
from pathlib import Path
import unittest
from unittest.mock import patch

from generalship import bodart_ratings as br
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


class SavedBodartRatingsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cohort = read_json(ROOT / br.COHORT)
        cls.saved = read_json(ROOT / br.RUN)

    def test_saved_run_verifies_offline_without_fit_and_preserves_limits(self):
        with patch.object(br, 'fit', side_effect=AssertionError('no historical fit')), \
                patch('urllib.request.urlopen', side_effect=AssertionError('no network')):
            br.verify(ROOT, self.cohort, self.saved)
            report = br.report(self.cohort, self.saved)
        self.assertEqual(len(self.cohort['rows']), 542)
        self.assertEqual(len(self.saved['estimates']), 669)
        self.assertEqual(sum(e['rank'] is not None for e in self.saved['estimates']), 72)
        self.assertEqual(len(self.saved['folds']), 28)
        self.assertEqual((ROOT / br.REPORT).read_text(), report)
        self.assertEqual((ROOT / br.CSV).read_text(), br.csv_text(self.saved))
        self.assertIn('OCR years can place a record in the wrong evaluation decade', report)
        self.assertIn('No cross-component or causal', report)
        self.assertGreater(self.saved['metrics']['decade_weighted']['commander']['log_loss'],
                           self.saved['metrics']['decade_weighted']['equal_odds']['log_loss'])

    def test_holdout_cannot_enter_training_or_be_duplicated(self):
        altered = copy.deepcopy(self.saved)
        fold = altered['folds'][0]
        fold['train_ids'].append(fold['test_ids'][0])
        with self.assertRaisesRegex(ValueError, 'fold membership'):
            br.verify(ROOT, self.cohort, altered)

    def test_prediction_cannot_silently_change(self):
        altered = copy.deepcopy(self.saved)
        altered['predictions'][0]['commander'] = .99
        with self.assertRaisesRegex(ValueError, 'predictions differ'):
            br.verify(ROOT, self.cohort, altered)

    def test_bound_input_changes_are_rejected(self):
        altered = copy.deepcopy(self.saved)
        altered['input_sha256'][br.TABLE] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'binding population'):
            br.verify(ROOT, self.cohort, altered)


if __name__ == '__main__':
    unittest.main()
