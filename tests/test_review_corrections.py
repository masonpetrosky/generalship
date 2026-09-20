import copy
from pathlib import Path
import shutil
import tempfile
import unittest

from generalship.evidence import validate_dossier
from generalship.sources import (read_json, source_document_date, source_registry,
                                validate_source_metadata, write_json)
from scripts.migrate_shiloh_review_corrections import (
    ARCHIVE, BUNDLE, DOSSIER, LEDGER, REGISTRY, REVIEW, SOURCE_IDS,
    expected_outputs, migrate,
)

ROOT = Path(__file__).resolve().parents[1]


class ReviewCorrectionTests(unittest.TestCase):
    def test_estimation_status_is_distinct_from_printed_precision(self):
        dossier = read_json(ROOT / DOSSIER)
        q = next(q for q in dossier['quantities'] if q['id'] == 'reed-mccook-detail-engaged')
        self.assertEqual((q['lower'], q['upper'], q['estimate_kind'], q['estimation_status']),
                         (7553, 7553, 'reported_exact', 'explicit_estimate'))
        for status in ['explicit_estimate', 'aggregate_includes_estimates',
                       'reported_without_explicit_estimation_qualifier', 'unknown']:
            q['estimation_status'] = status
            validate_dossier(ROOT, dossier)
        q['estimation_status'] = 'unknown'
        q['estimation_citations'] = []
        validate_dossier(ROOT, dossier)  # An unknown needs a rationale, not an invented quote.

    def test_estimation_provenance_cannot_be_dropped_or_fabricated(self):
        for changes in [{'estimation_status': None}, {'estimation_status': 'measured_exact'},
                        {'estimation_note': ' '}, {'estimation_citations': []}]:
            with self.subTest(changes=changes):
                dossier = read_json(ROOT / DOSSIER)
                dossier['quantities'][0].update(changes)
                with self.assertRaises(ValueError): validate_dossier(ROOT, dossier)
        dossier = read_json(ROOT / DOSSIER)
        q = next(q for q in dossier['quantities'] if q['id'] == 'reed-eighteenth-wisconsin-estimate')
        q['estimation_citations'][-1]['section'] = 'p93'  # Its asterisk means detachment, not Estimated.
        with self.assertRaisesRegex(ValueError, 'Estimation qualifier passage'): validate_dossier(ROOT, dossier)
        dossier = read_json(ROOT / DOSSIER)
        dossier['schema_version'] = 2
        with self.assertRaisesRegex(ValueError, 'schema version 3'): validate_dossier(ROOT, dossier)

    def test_legacy_dossier_still_validates_without_new_fields(self):
        validate_dossier(ROOT, read_json(ROOT / ARCHIVE))

    def test_section_dates_preserve_nulls_and_do_not_fall_back(self):
        sources = source_registry(ROOT)
        ammen = sources['or-ammen-crossing-v2']
        nelson = sources['or-nelson-reinforcements-v2']
        self.assertIsNone(ammen['document_date'])
        self.assertEqual(source_document_date(ammen, 'p328-report'), '1862-04-10')
        self.assertEqual(source_document_date(nelson, 'p325-strength'), '1862-04-10')
        for section in ['p329-diary-heading', 'p330-diary', 'p333-diary', 'p334-diary', 'transcription-scope']:
            self.assertIsNone(source_document_date(ammen, section))
        for section in ['p326-return', 'p327-march-return']:
            self.assertIsNone(source_document_date(nelson, section))
        for section in [None, 'p999']:
            with self.assertRaises(ValueError): source_document_date(nelson, section)
        self.assertEqual(source_document_date(sources['or-ammen-crossing-v1']), '1862-04-10')

    def test_section_date_contract_rejects_missing_sections_and_invented_dates(self):
        for mode in ['missing', 'extra', 'invalid_date', 'event_date_fallback', 'missing_note', 'editorial_in_map']:
            with self.subTest(mode=mode):
                sources = source_registry(ROOT)
                source = sources['or-ammen-crossing-v2']
                if mode == 'missing': del source['document_dates_by_section']['p334-diary']
                if mode == 'extra': source['document_dates_by_section']['p999'] = None
                if mode == 'invalid_date': source['document_dates_by_section']['p334-diary'] = '1862-02-30'
                if mode == 'event_date_fallback': source['document_date'] = '1862-04-10'
                if mode == 'missing_note': source['document_date_note'] = ' '
                if mode == 'editorial_in_map': source['document_dates_by_section']['transcription-scope'] = None
                with self.assertRaises(ValueError): validate_source_metadata(ROOT, sources)

    def test_source_metadata_versions_bind_old_records_and_unchanged_raw_bytes(self):
        for mode in ['old_metadata_changed', 'new_raw_changed', 'missing_predecessor']:
            with self.subTest(mode=mode):
                sources = source_registry(ROOT)
                if mode == 'old_metadata_changed': sources['or-ammen-crossing-v1']['document_date'] = None
                if mode == 'new_raw_changed': sources['or-ammen-crossing-v2']['sha256'] = '0' * 64
                if mode == 'missing_predecessor': sources['or-ammen-crossing-v2']['supersedes']['source_id'] = 'missing'
                with self.assertRaises(ValueError): validate_source_metadata(ROOT, sources)

    def test_same_return_and_scan_cannot_be_independent(self):
        sources = source_registry(ROOT)
        current = sources['or-union-return-detail-v3']
        self.assertEqual(current['independence_group'], 'or-union-returns')
        self.assertEqual(current['facsimile_source_id'], 'or-union-return-scan')
        for field, value in [('independence_group', 'or-grant'), ('facsimile_source_id', 'missing'),
                             ('facsimile_source_id', 'or-confederate-return-scan')]:
            with self.subTest(field=field):
                changed = copy.deepcopy(sources)
                changed['or-union-return-detail-v3'][field] = value
                with self.assertRaises(ValueError): validate_source_metadata(ROOT, changed)

    def test_bounded_migration_preserves_numbers_events_unknowns_and_old_sources(self):
        outputs = expected_outputs(ROOT)
        for path, blob in outputs.items():
            self.assertEqual((ROOT / path).read_bytes(), blob, path)
        old = read_json(ROOT / ARCHIVE)
        current = read_json(ROOT / DOSSIER)
        self.assertEqual(old['events'], current['events'])
        self.assertEqual(old['open_questions'], current['open_questions'])
        for before, after in zip(old['quantities'], current['quantities'], strict=True):
            self.assertEqual(before, {k: v for k, v in after.items() if not k.startswith('estimation_')})
        for before, after in zip(old['claims'], current['claims'], strict=True):
            restored = copy.deepcopy(after)
            for citation in restored['citations']:
                reverse = {new: prior for prior, new in SOURCE_IDS.items()}
                citation['source_id'] = reverse.get(citation['source_id'], citation['source_id'])
            if before['id'] == 'crittenden-arrival-phases': restored['value'] = before['value']
            self.assertEqual(before, restored)
        config = read_json(ROOT / f'reviews/{BUNDLE}/config.json')
        original_registry = read_json(ROOT / config['snapshot_copies'][REGISTRY])
        current_registry = read_json(ROOT / REGISTRY)
        self.assertEqual(original_registry['sources'], current_registry['sources'][:50])
        self.assertEqual(len(current_registry['sources']), 53)

    def test_migration_is_idempotent_and_rejects_divergence_before_writing(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copytree(ROOT / 'data', root / 'data')
            config_path = f'reviews/{BUNDLE}/config.json'
            config = read_json(ROOT / config_path)
            paths = [config_path, config['snapshot_copies'][DOSSIER], config['snapshot_copies'][REGISTRY],
                     f'{REVIEW}/dispatch.json', f'{REVIEW}/review-result.json']
            for path in paths:
                (root / path).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / path, root / path)
            # Replay the original transition, not just a comparison to its output.
            shutil.copyfile(root / config['snapshot_copies'][DOSSIER], root / DOSSIER)
            shutil.copyfile(root / config['snapshot_copies'][REGISTRY], root / REGISTRY)
            (root / ARCHIVE).unlink()
            self.assertEqual(migrate(root)['files_written'], 4)
            self.assertEqual(migrate(root)['files_written'], 0)
            divergent = read_json(root / DOSSIER)
            divergent['boundary_note'] += ' divergent local edit'
            write_json(root / DOSSIER, divergent)
            (root / LEDGER).unlink()
            before = (root / REGISTRY).read_bytes()
            with self.assertRaisesRegex(ValueError, 'Refusing to replace divergent'): migrate(root)
            self.assertEqual(before, (root / REGISTRY).read_bytes())
            self.assertFalse((root / LEDGER).exists())


if __name__ == '__main__':
    unittest.main()
