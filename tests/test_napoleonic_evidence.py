"""Napoleonic draft dossiers and research packets (generalship/evidence.py, generalship/napoleonic_packet.py)."""

from pathlib import Path
import json
import shutil
import tempfile
import unittest

from generalship.evidence import NAPOLEONIC_CODES, NAPOLEONIC_COHORT, NAPOLEONIC_EVIDENCE, NAPOLEONIC_SIDES, \
    validate_dossier, validate_napoleonic
import generalship.napoleonic_packet as packet
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]
BODART = 'bodart-1908-transcription-v1'


def dossier(battle_id='B369c'):
    cite = {'source_id': BODART, 'section': 'p369', 'locator': 'Bodart (1908), p. 369, Austerlitz',
            'quote': 'Franzosen | Russen und Österreicher'}
    claims = [{'id': f'{d}-unknown', 'dimension': d, 'value': None, 'status': 'unknown', 'phase': 'unresolved',
               'rationale': 'Not read in this test.', 'citations': []}
              for d in ('strength', 'terrain', 'logistics', 'information', 'objectives', 'responsibility',
                        'posture', 'fortification')]
    claims.append({'id': 'bodart-winner', 'dimension': 'outcome', 'value': 'Bodart puts the French on the winning side.',
                   'status': 'supported', 'phase': 'post_outcome', 'rationale': 'Winner on the left (p. 46).',
                   'citations': [cite]})
    return {'schema_version': 1, 'battle_id': battle_id, 'status': 'draft', 'tactical_replacement_at': None,
            'campaign_replacement_at': None, 'boundary_note': 'Test.', 'claims': claims,
            'open_questions': ['Everything beyond Bodart.']}


class NapoleonicEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        registry = read_json(ROOT / 'data/sources.json')['sources']
        cls.sources = {s['id']: s for s in registry if s['id'] == BODART}
        cls.cohort = read_json(ROOT / NAPOLEONIC_COHORT)['battle_ids']

    def check(self, d):
        return validate_dossier(ROOT, d, self.sources, self.cohort, NAPOLEONIC_SIDES, NAPOLEONIC_CODES)

    def test_a_cohort_entry_with_a_resolvable_quote_passes(self):
        self.assertEqual(self.check(dossier())['claims'], 9)

    def test_posture_and_fortification_are_required_dimensions(self):
        for dimension in NAPOLEONIC_CODES:
            d = dossier()
            d['claims'] = [c for c in d['claims'] if c['dimension'] != dimension]
            with self.assertRaisesRegex(ValueError, 'Every research dimension'):
                self.check(d)
        with self.assertRaisesRegex(ValueError, 'Every research dimension'):  # the Civil War path has seven
            validate_dossier(ROOT, dossier(), self.sources, self.cohort, NAPOLEONIC_SIDES)

    def test_a_known_coded_claim_takes_one_listed_code(self):
        d = dossier()
        posture = next(c for c in d['claims'] if c['dimension'] == 'posture')
        posture.update(value='A test proposition.', status='supported', citations=[d['claims'][-1]['citations'][0]])
        for code in (None, 'attacker', ['A_attacked'], 'none_named'):  # none_named belongs to fortification
            posture['code'] = code
            with self.assertRaisesRegex(ValueError, 'takes one listed code'):
                self.check(d)
        posture['code'] = 'A_attacked'
        self.assertEqual(self.check(d)['unknown_claims'], 7)

    def test_an_unknown_coded_claim_takes_no_code(self):
        d = dossier()
        next(c for c in d['claims'] if c['dimension'] == 'fortification')['code'] = 'none_named'
        with self.assertRaisesRegex(ValueError, 'takes one listed code'):
            self.check(d)

    def test_only_coded_dimensions_take_a_code(self):
        d = dossier()
        d['claims'][0]['code'] = None  # strength
        with self.assertRaisesRegex(ValueError, 'Only coded dimensions'):
            self.check(d)

    def test_an_entry_outside_cohort_v1_fails(self):
        with self.assertRaisesRegex(ValueError, 'not in the research frame'):
            self.check(dossier('B269c'))  # Valmy, 1792: in the frame, not in cohort v1

    def test_a_quote_from_another_page_fails(self):
        d = dossier()
        d['claims'][-1]['citations'][0]['section'] = 'p370'
        with self.assertRaisesRegex(ValueError, 'Supporting passage not found'):
            self.check(d)

    def test_dossiers_are_named_by_frame_id_and_checked_against_cohort_v1(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for rel in (NAPOLEONIC_COHORT, 'data/raw/bodart-1908-v1/transcription.txt'):
                (root / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(ROOT / rel, root / rel)
            self.assertEqual(validate_napoleonic(root, self.sources), [])
            (root / NAPOLEONIC_EVIDENCE).mkdir(parents=True)
            (root / NAPOLEONIC_EVIDENCE / 'B369a.json').write_text(json.dumps(dossier()), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'named by its frame ID'):
                validate_napoleonic(root, self.sources)
            (root / NAPOLEONIC_EVIDENCE / 'B369a.json').rename(root / NAPOLEONIC_EVIDENCE / 'B369c.json')
            self.assertEqual([r['battle_id'] for r in validate_napoleonic(root, self.sources)], ['B369c'])

    def test_packet_lists_the_group_with_each_printed_entry(self):
        text = packet.packet(ROOT, 'third-coalition 1805')
        self.assertEqual(text.count('\n### B'), 22)
        self.assertIn('1805 2./12. SCHLACHT bei Austerlitz (1.)', text)
        self.assertIn('[1] hiev. 21 Btln., 28 Esk. = 16.000 Österreicher.', text)  # its footnotes travel with it
        with self.assertRaisesRegex(ValueError, 'Not a cohort v1 campaign group'):
            packet.packet(ROOT, 'first-coalition 1796')

    def test_compact_packet_preserves_access_without_embedding_every_draft(self):
        compact = packet.packet(ROOT, 'fourth-coalition 1806')
        full = packet.packet(ROOT, 'fourth-coalition 1806', full=True)
        one = packet.packet(ROOT, 'fourth-coalition 1806', battle_id='B377c')
        self.assertIn('data/napoleonic/evidence/B377c.json', compact)
        self.assertIn('SHA-256', compact)
        self.assertNotIn('"bodart-strength"', compact)
        self.assertIn('"bodart-strength"', full)
        self.assertIn('"bodart-strength"', one)
        self.assertEqual(one.count('\n### B'), 1)
        self.assertLess(len(compact), len(full) / 5)
        with self.assertRaisesRegex(ValueError, 'is not in'):
            packet.packet(ROOT, 'fourth-coalition 1806', battle_id='B363a')


if __name__ == '__main__':
    unittest.main()
