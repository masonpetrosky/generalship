"""Bulk extraction boundaries, column safety, provenance and explicit OCR errors."""

import csv
import gzip
import hashlib
import io
from pathlib import Path
import unittest
from unittest.mock import patch

from generalship import bodart_bulk as bulk
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


class BodartBulkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.meta = bulk.build(ROOT)
        cls.by = {r['id']: r for r in cls.rows}

    def test_scope_preserves_checked_entries_and_denominators(self):
        c = self.meta['coverage']
        self.assertEqual(c['page_range'], [49, 600])
        self.assertEqual(c['detail_pages'], 552)
        self.assertEqual(c['entries'], 1682)
        self.assertEqual(c['existing_checked_entries'], 708)
        self.assertEqual(c['new_ocr_candidates'], 974)
        self.assertEqual(c['new_entries_with_sample_field_checks'], 34)
        self.assertEqual(len(self.by), len(self.rows))
        self.assertTrue(all(49 <= r['page'] <= 600 for r in self.rows))
        frame = read_json(ROOT / bulk.FRAME)['entries']
        self.assertEqual({r['id'] for r in self.rows if r['source_id'] == bulk.MANUAL_SOURCE},
                         {r['id'] for r in frame})
        reserved = read_json(ROOT / 'data/napoleonic/cohort-v1.json')['battle_ids']
        self.assertEqual(len(reserved), 325)  # Broad source rows are not a cohort migration.

    def test_saved_files_reproduce_without_fit_or_network(self):
        with patch('generalship.baseline.fit_logistic', side_effect=AssertionError('no fit')), \
                patch('urllib.request.urlopen', side_effect=AssertionError('no fetch')):
            rows, meta = bulk.build(ROOT)
        self.assertFalse(meta['historical_outcomes_fitted'])
        self.assertTrue(meta['independent_of_arsht_inputs_and_code'])
        self.assertEqual(read_json(ROOT / bulk.META), meta)
        self.assertEqual((ROOT / bulk.CSV).read_text(), bulk.table_csv(rows))
        self.assertEqual((ROOT / bulk.REPORT).read_text(), bulk.report(rows, meta))

    def test_known_ocr_errors_survive_in_check_record(self):
        row = self.by['B369c']  # Austerlitz: the existing transcription wins over OCR.
        self.assertEqual(row['winner_personnel'], 65000)
        replay = next(r for r in self.meta['extraction_replay']['rows'] if r['checked_id'] == 'B369c')
        self.assertEqual(replay['fields']['winner_personnel'], {'checked': 65000, 'ocr': 66000, 'status': 'disagree'})
        row = self.by['BL595-002']
        self.assertEqual((row['winner_personnel'], row['loser_personnel']), (20000, 24000))
        self.assertIn('90.000', row['winner_strength_reading'])
        self.assertEqual(row['record_status'], 'ocr_candidate_with_checked_fields')
        sample = next(r for r in self.meta['primary_image_checks']['rows'] if r['row_id'] == row['id'])
        self.assertEqual(sample['fields']['loser_personnel']['ocr'], 84000)
        self.assertNotIn('winner_commander_text', row['image_checked_fields'])
        self.assertEqual(sum(self.meta['primary_image_checks']['personnel_fields_before_image_corrections'].values()), 68)

    def test_unknowns_and_different_populations_are_not_zeroes(self):
        self.assertEqual(self.by['BL516-011']['winner_personnel'], 50000)  # Not the engaged-only 40,000.
        self.assertIsNone(self.by['BL187-025']['loser_personnel'])  # Explicit later state: "noch 1.000".
        self.assertIsNone(self.by['BL595-016']['winner_personnel'])  # 900 below the prose is a loss.
        row = next(r for r in csv.DictReader(io.StringIO(bulk.table_csv(self.rows))) if r['id'] == 'BL595-016')
        self.assertEqual(row['winner_personnel'], '')
        for text in ['5.500 Inft., 1.500 Reiter', 'noch 1.000 M.', '300 Gesch.', '1 Gen. 31 Offz.']:
            self.assertIsNone(bulk.parenthetical_strength('(' + text + ')')[1]['primary_value'], text)
        self.assertEqual(bulk.parenthetical_strength('(7.700 Inft., 300 Reiter = 8.000 M.)')[1]['primary_value'], 8000)

    def test_column_blocks_merge_by_position_without_selecting_outer_guns(self):
        def line(i, tokens, y=100):
            words = [{'text': t, 'box': (x, y, x + 60, y + 35), 'confidence': 100} for x, t in tokens]
            return {'line': i, 'text': '', 'words': words,
                    'box': (words[0]['box'][0], y, words[-1]['box'][2], y + 35)}
        merged = bulk.visual_lines([line(0, [(720, '118.000')]), line(1, [(1050, 'Gesamt'), (1250, 'Stärke')]),
                                    line(2, [(2040, 'Gesch.'), (2240, '224')])])[0]
        merged['width'] = 2500
        self.assertEqual(merged['line_ids'], [0, 1, 2])
        values = bulk.table_value(merged, (1, 2))
        self.assertEqual(values[0][2], 118000)
        self.assertIsNone(values[1])  # Missing right personnel cannot become 224 guns.
        malformed = bulk.visual_lines([line(0, [(720, '500OO'), (1050, 'Gesamt'), (1250, 'Stärke'), (1600, '50.000')])])[0]
        malformed['width'] = 2500
        values = bulk.table_value(malformed, (1, 2))
        self.assertIsNone(values[0][2])  # OCR letters must not be stripped into a plausible 500.
        self.assertEqual(values[1][2], 50000)

    def test_corrupt_source_is_rejected_and_xml_matches_pinned_metadata(self):
        with patch.object(bulk, 'digest', return_value='changed'):
            with self.assertRaisesRegex(ValueError, 'changed bulk raw source'):
                bulk.build(ROOT)
        raw = gzip.decompress((ROOT / bulk.LAYOUT).read_bytes())
        metadata = read_json(ROOT / 'data/raw/bodart-1908-v1/ia-metadata.json')
        original = next(f for f in metadata['files'] if f['name'].endswith('_djvu.xml'))
        self.assertEqual(hashlib.sha1(raw).hexdigest(), original['sha1'])

    def test_provenance_and_verification_scope_remain_visible(self):
        registry = bulk.source_registry_with_bulk(ROOT)
        for r in self.rows:
            self.assertEqual(r['source_sha256'], registry[r['source_id']]['sha256'])
            self.assertTrue(r['locator'] and r['source_quote'])
            if r['image_source_id']:
                self.assertEqual(r['image_source_sha256'], registry[r['image_source_id']]['sha256'])
                self.assertEqual(set(r['image_checked_fields']), {'year', 'place', 'winner_personnel', 'loser_personnel'})
        report = bulk.report(self.rows, self.meta)
        self.assertIn('not a blind accuracy estimate', report)
        self.assertIn('No model was fitted', report)
        self.assertIn('Unknown values stay blank', report)
        self.assertGreater(self.meta['extraction_replay']['personnel_fields']['disagree'], 0)


if __name__ == '__main__':
    unittest.main()
