import copy
from pathlib import Path
import shutil
import tempfile
import unittest

from generalship.dataset import build_dataset, number, unique
from generalship.evidence import validate_all, validate_dossier
from generalship.sources import digest, read_json, safe_path, verify_sources

ROOT = Path(__file__).resolve().parents[1]


class EvidenceTests(unittest.TestCase):
    def test_repository_dossiers_have_resolvable_passages(self):
        dossiers = validate_all(ROOT)
        self.assertEqual({d['battle_id'] for d in dossiers},
                         {'TN027', 'TN028', 'TN029', 'VA044', 'TN024', 'GA005', 'TN023', 'TN025', 'TN026', 'WV012', 'TN022', 'TN021', 'VA039', 'VA040', 'VA041', 'VA042', 'VA043', 'TN019', 'TN020', 'TN018', 'GA003', 'GA004', 'IN001', 'OH001', 'OH002', 'TN017', 'VA035', 'VA107', 'VA036', 'VA037', 'VA038', 'PA001', 'PA002', 'MD004', 'MD006', 'VA108', 'AL001', 'VA032', 'VA033', 'VA034', 'MS004', 'MS005', 'MS006', 'MS007', 'MS008', 'MS010', 'MS011', 'LA011', 'LA014', 'AR008', 'VA029', 'NC010', 'NC011', 'VA030', 'VA031', 'TN012', 'TN013', 'TN014', 'TN015', 'TN016', 'MS003', 'AR006', 'TN009', 'TN011', 'NC007', 'NC008', 'NC009', 'VA028', 'TN008', 'TN010', 'MS001', 'MS002', 'TN007', 'WV010', 'MD002', 'WV016', 'VA022', 'VA023', 'VA024', 'VA025', 'VA026', 'VA027', 'TN005', 'TN006', 'KY007', 'KY008', 'KY009', 'VA101', 'VA102', 'WV009', 'VA103', 'VA104', 'VA105', 'VA106', 'VA008', 'VA009', 'VA010', 'VA011', 'VA012', 'VA013', 'VA014', 'VA015', 'VA016', 'VA017', 'VA018', 'VA019', 'VA020', 'VA020A', 'VA020B', 'VA021', 'MO012', 'TN004', 'NC002', 'NC003', 'NC004', 'NC005', 'NC006', 'KY005', 'KY006', 'TN001', 'TN002', 'TN003', 'MD001', 'MD003', 'MS009', 'MS016', 'VA100'})
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

    def test_quote_on_another_page_is_not_valid_support(self):
        dossier = read_json(ROOT / 'data/evidence/TN003.json')
        claim = next(c for c in dossier['claims'] if c['id'] == 'command-transfer')
        citation = next(c for c in claim['citations'] if c['source_id'] == 'or-beauregard-shiloh-report')
        citation['section'] = 'p385'  # Correct document, wrong page.
        with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_section_cannot_be_missing_or_invented(self):
        for section in (None, '', 'p999', 'p387\n## p385'):
            with self.subTest(section=section):
                dossier = read_json(ROOT / 'data/evidence/TN003.json')
                citation = next(c for c in dossier['claims'] if c['id'] == 'union-return-strength')['citations'][0]
                citation['section'] = section
                with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_quantity_requires_specific_evidenced_strength_claim(self):
        for changes in ({'claim_id': 'missing'}, {'claim_id': 'logistics-unknown'},
                        {'claim_id': 'result'}, {'citation_index': 100}, {'citation_index': True},
                        {'entity_id': 'missing'}, {'entity_id': 'grant'}):
            with self.subTest(changes=changes):
                dossier = read_json(ROOT / 'data/evidence/TN003.json')
                dossier['quantities'][0].update(changes)
                with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_quantity_cannot_erase_population_or_precision(self):
        for changes in ({'basis': 'troops'}, {'scope': ''}, {'location': ''}, {'note': ''},
                        {'lower': -1}, {'upper': float('nan')}, {'lower': True},
                        {'lower': 70000}, {'upper': 70000}, {'unit': 'regiments'}):
            with self.subTest(changes=changes):
                dossier = read_json(ROOT / 'data/evidence/TN003.json')
                dossier['quantities'][0].update(changes)
                with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_unstated_muster_date_stays_unknown(self):
        dossier = read_json(ROOT / 'data/evidence/TN003.json')
        q = next(q for q in dossier['quantities'] if q['id'] == 'confederate-after')
        self.assertIsNone(q['period']['start'])
        self.assertIsNone(q['period']['end'])
        self.assertEqual(q['recorded_at'], '1862-04-21')
        validate_dossier(ROOT, dossier)
        q['period']['start'] = '1862-04-07'
        with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_reversed_quantity_dates_fail(self):
        dossier = read_json(ROOT / 'data/evidence/TN003.json')
        dossier['quantities'][0]['period']['end'] = '1862-04-05'
        with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_events_require_evidence_and_known_entities(self):
        for changes in ({'claim_ids': ['missing']}, {'claim_ids': ['logistics-unknown']},
                        {'entity_ids': ['missing']}, {'time_label': ''}, {'date': 'yesterday'}):
            with self.subTest(changes=changes):
                dossier = read_json(ROOT / 'data/evidence/TN003.json')
                dossier['events'][0].update(changes)
                with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_phase_records_cannot_silently_downgrade_schema(self):
        dossier = read_json(ROOT / 'data/evidence/TN003.json')
        dossier['schema_version'] = 1
        with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_duplicate_phase_record_ids_fail(self):
        for key in ('entities', 'events', 'quantities'):
            with self.subTest(key=key):
                dossier = read_json(ROOT / 'data/evidence/TN003.json')
                dossier[key].append(copy.deepcopy(dossier[key][0]))
                with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)

    def test_archived_dossier_is_preserved_and_bound_to_revision(self):
        dossier = read_json(ROOT / 'data/evidence/TN003.json')
        previous = read_json(ROOT / dossier['supersedes']['path'])
        self.assertTrue({c['id'] for c in previous['claims']}.issubset(
            {c['id'] for c in dossier['claims']}))
        # Evidence revisions can keep the same schema. Follow their hash-bound
        # archive chain rather than assuming the immediate predecessor is v1.
        revision, seen = dossier, set()
        while revision.get('supersedes'):
            reference = revision['supersedes']
            self.assertNotIn(reference['path'], seen)
            seen.add(reference['path'])
            path = safe_path(ROOT, reference['path'])
            self.assertEqual(digest(path), reference['sha256'])
            revision = read_json(path)
            self.assertEqual(revision['battle_id'], dossier['battle_id'])
        self.assertEqual(revision['schema_version'], 1)
        self.assertEqual(len(revision['claims']), 7)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copytree(ROOT / 'data', root / 'data')
            path = root / dossier['supersedes']['path']
            path.write_bytes(path.read_bytes()+b'\n')
            with self.assertRaises(ValueError): validate_dossier(root, dossier)

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



class ResearchFrameTests(unittest.TestCase):
    def test_cohort_v2_contains_v1_and_every_source_battle(self):
        root = Path(__file__).resolve().parents[1]
        v1 = read_json(root / 'data/pilot/cohort.json')['battle_ids']
        v2 = read_json(root / 'data/pilot/cohort-v2.json')['battle_ids']
        self.assertTrue(set(v1) <= set(v2))
        self.assertEqual(len(v2), 384)


if __name__ == '__main__':
    unittest.main()
