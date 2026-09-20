import copy
from pathlib import Path
import shutil
import tempfile
import unittest

from generalship.dataset import build_dataset, number, unique
from generalship.evidence import validate_all, validate_dossier
from generalship.sources import read_json, safe_path, verify_sources

ROOT = Path(__file__).resolve().parents[1]


class EvidenceTests(unittest.TestCase):
    def test_repository_dossiers_have_resolvable_passages(self):
        dossiers = validate_all(ROOT)
        self.assertEqual({d['battle_id'] for d in dossiers}, {'TN003', 'MD003', 'MS009'})
        self.assertTrue(all(d['status']=='draft' for d in dossiers))

    def test_invented_quote_fails(self):
        dossier = read_json(ROOT / 'data/evidence/TN003.json')
        dossier['claims'][0]['citations'][0]['quote'] = 'This is not a historical quotation.'
        with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_unsupported_known_claim_fails(self):
        dossier = read_json(ROOT / 'data/evidence/TN003.json')
        dossier['claims'][0]['citations'] = []
        with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_unknown_is_null_not_zero(self):
        dossier = read_json(ROOT / 'data/evidence/TN003.json')
        unknown = next(c for c in dossier['claims'] if c['status']=='unknown')
        unknown['value'] = 0
        with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_incomplete_dimension_coverage_fails(self):
        dossier = read_json(ROOT / 'data/evidence/TN003.json')
        dossier['claims'] = [c for c in dossier['claims'] if c['dimension'] != 'logistics']
        with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_review_requires_an_actual_record(self):
        dossier = read_json(ROOT / 'data/evidence/TN003.json')
        dossier['status'] = 'reviewed'
        with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_citation_requires_full_key(self):
        dossier = read_json(ROOT / 'data/evidence/MS009.json')
        dossier['claims'][0]['citations'][0]['row_key'] = {}
        with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_duplicate_claim_ids_fail(self):
        dossier = read_json(ROOT / 'data/evidence/MS009.json')
        dossier['claims'].append(copy.deepcopy(dossier['claims'][0]))
        with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_checksum_tampering_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copytree(ROOT / 'data', root / 'data')
            path = root / 'data/raw/cwsac_forces.csv'
            path.write_bytes(path.read_bytes()+b'\n')
            with self.assertRaises(ValueError): verify_sources(root)

    def test_frozen_cohort_tampering_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copytree(ROOT / 'data', root / 'data')
            path = root / 'data/pilot/cohort.json'
            path.write_text(path.read_text().replace('"IN001",', ''))
            with self.assertRaises(ValueError): build_dataset(root)

    def test_paths_cannot_escape_repository(self):
        with self.assertRaises(ValueError): safe_path(ROOT, '../elsewhere')

    def test_duplicate_join_keys_rejected(self):
        with self.assertRaises(ValueError): unique([{'id':'a'}, {'id':'a'}], ['id'], 'example')

    def test_missing_numeric_is_distinct_from_zero(self):
        self.assertIsNone(number(''))
        self.assertEqual(number('0'), 0)
        for value in ['nan', 'inf', '-1']:
            with self.assertRaises(ValueError): number(value)

    def test_coverage_denominator_retains_unscorable_battles(self):
        records, profile = build_dataset(ROOT)
        self.assertEqual(profile['pilot_battles'], 127)
        self.assertEqual(profile['pilot_campaigns'], 36)
        self.assertEqual(profile['baseline_eligible'], 23)
        antietam = next(r for r in records if r['battle_id']=='MD003')
        self.assertFalse(antietam['baseline_eligible'])
        self.assertIn('missing_numeric_strength', antietam['exclusion_reasons'])
        self.assertIn('inconclusive_outcome', antietam['exclusion_reasons'])
        self.assertIsNone(antietam['strengths']['US']['low'])


if __name__ == '__main__':
    unittest.main()
