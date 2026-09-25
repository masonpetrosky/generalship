"""Tier-2 validator tests. All evidence here is explicitly invented and test-only."""

from copy import deepcopy
from pathlib import Path
import shutil
import tempfile
import unittest

from generalship.admission import AdmissionError, canonical_hash
from generalship.sources import digest, source_metadata_digest, write_json
from generalship.strength_admission import (IMPLEMENTATION, SCOPE, audit_release, check,
                                            generate_scenarios, review_bindings, validate_proposal)

ROOT = Path(__file__).resolve().parents[1]


def ref(root, path):
    return {'path': path, 'sha256': digest(root / path)}


FIGURES = [  # id, side, section, value, basis, period
    ('tab-us', 'US', 'table', 1000, 'reported_engaged', ('2000-01-02', '2000-01-03')),
    ('tab-cs', 'CS', 'table', 800, 'reported_engaged', ('2000-01-02', '2000-01-03')),
    ('rep-us', 'US', 'us-report', 1100, 'reported_engaged', ('2000-01-02', '2000-01-03')),
    ('rep-cs', 'CS', 'cs-report', 700, 'reported_engaged', ('2000-01-02', '2000-01-03')),
]


class Synthetic:
    def __init__(self, root):
        self.root = root
        for p in IMPLEMENTATION:
            dest = root / p; dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / p, dest)
        (root / 'data').mkdir(exist_ok=True)
        shutil.copyfile(ROOT / 'docs/feature-admission.md', root / 'data/contract.md')
        shutil.copyfile(ROOT / 'docs/feature-admission-reported-strength.md', root / 'data/design.md')
        (root / 'data/battles.csv').write_text(
            'battle,start_date,end_date\nSYN001,2000-01-02,2000-01-03\nSYN002,2000-02-01,2000-02-01\n'
            'SYN003,2000-03-01,2000-03-01\n')
        self.figures = deepcopy(FIGURES)
        self.phase = 'unresolved'
        self.estimation = 'reported_without_explicit_estimation_qualifier'
        self.candidates = [self.candidate(f[0]) for f in self.figures]
        self.screened = []
        self.outcomes = {'SYN001': 'Union', 'SYN002': 'Union', 'SYN003': 'Inconclusive'}
        self.write()

    def candidate(self, qid, role=None, codes=()):
        side = next(f[1] for f in self.figures if f[0] == qid)
        return {'id': qid, 'battle_id': 'SYN001', 'side': 'US' if side == 'US' else 'Confederate',
                'entity_id': f'{side.lower()}-force', 'quantity_id': qid,
                'source_role': role or ('compiled_total' if qid.startswith('tab') else 'own_report'),
                'codes': list(codes), 'rationale': 'SYNTHETIC TEST MAPPING; no historical claim.', 'citations': []}

    def write(self):
        root = self.root
        raw = '# SYNTHETIC TEST DATA\n'
        raw += '\n## table\nSYNTHETIC table: US 1000 engaged; CS 800 engaged.\n'
        raw += '\n## us-report\nSYNTHETIC US report: 1100 engaged.\n'
        raw += '\n## cs-report\nSYNTHETIC CS report: 700 engaged.\n'
        raw += '\n## other\nSYNTHETIC other figures: 500 engaged; about 2000 by the enemy.\n'
        (root / 'data/raw.txt').write_text(raw)
        text_source = {'id': 'synthetic-text', 'path': 'data/raw.txt', 'sha256': digest(root / 'data/raw.txt'),
                       'format': 'text', 'sectioned': True, 'source_kind': 'test_only_invented',
                       'independence_group': 'synthetic', 'document_date': None,
                       'document_date_note': 'Synthetic.', 'retrieved_at': '2026-09-20'}
        table_raw = '# SYNTHETIC TABLE\n\n## table\nSYNTHETIC table: US 1000 engaged; CS 800 engaged.\n'
        (root / 'data/table.txt').write_text(table_raw)
        table_source = dict(text_source, id='synthetic-table', path='data/table.txt', sha256=digest(root / 'data/table.txt'))
        battles = {'id': 'arnold-cwsac-battles', 'path': 'data/battles.csv', 'sha256': digest(root / 'data/battles.csv'),
                   'format': 'csv', 'primary_key': ['battle'], 'source_kind': 'test_only_invented',
                   'independence_group': 'synthetic-frame', 'document_date': None,
                   'document_date_note': 'Synthetic.', 'retrieved_at': '2026-09-20'}
        quotes = {'table': 'SYNTHETIC table: US 1000 engaged; CS 800 engaged.',
                  'us-report': 'SYNTHETIC US report: 1100 engaged.', 'cs-report': 'SYNTHETIC CS report: 700 engaged.'}
        citations = []
        for fid, side, section, value, basis, period in self.figures:
            src = 'synthetic-table' if section == 'table' else 'synthetic-text'
            citations.append({'source_id': src, 'section': section, 'locator': section,
                              'quote': quotes.get(section, 'SYNTHETIC other figures: 500 engaged; about 2000 by the enemy.')})
        claims = [{'id': 'strength', 'dimension': 'strength', 'value': 'Synthetic counts', 'status': 'supported',
                   'phase': self.phase, 'rationale': 'Only test data.', 'citations': citations},
                  {'id': 'outcome', 'dimension': 'outcome', 'value': 'Union', 'status': 'supported', 'phase': 'post_outcome',
                   'rationale': 'Only test data.', 'citations': [citations[0]]}]
        for dim in ['terrain', 'logistics', 'information', 'objectives', 'responsibility']:
            claims.append({'id': dim, 'dimension': dim, 'value': None, 'status': 'unknown', 'phase': 'unresolved',
                           'rationale': 'Not supplied.', 'citations': []})
        quantities = []
        for i, (fid, side, section, value, basis, period) in enumerate(self.figures):
            quantities.append({'id': fid, 'claim_id': 'strength', 'citation_index': i, 'entity_id': f'{side.lower()}-force',
                               'unit': 'people', 'lower': value, 'upper': value, 'basis': basis,
                               'estimate_kind': 'reported_exact',
                               'period': {'start': period[0], 'end': period[1], 'label': 'Synthetic'} if period[0]
                               else {'start': None, 'end': None, 'label': 'Synthetic undated'},
                               'location': 'Synthetic', 'scope': 'Synthetic whole side', 'recorded_at': None,
                               'note': 'Synthetic.', 'estimation_status': self.estimation,
                               'estimation_note': 'Synthetic.',
                               'estimation_citations': [] if self.estimation == 'unknown' else [citations[i]]})
        dossier = {'schema_version': 3, 'battle_id': 'SYN001', 'status': 'draft', 'tactical_replacement_at': None,
                   'campaign_replacement_at': None, 'boundary_note': 'Synthetic.', 'claims': claims,
                   'open_questions': ['Synthetic fixture is not historical evidence.'],
                   'entities': [{'id': 'us-force', 'name': 'US', 'kind': 'formation', 'side': 'US'},
                                {'id': 'cs-force', 'name': 'CS', 'kind': 'formation', 'side': 'CS'}],
                   'events': [{'id': 'interval', 'date': '2000-01-02', 'time_label': 'Date only',
                               'entity_ids': ['us-force'], 'claim_ids': ['strength'], 'note': 'Synthetic.'}],
                   'quantities': quantities}
        sources = [text_source, table_source, battles]
        snapshot = {'schema_version': 1, 'test_only': True, 'cohort': {'battle_ids': sorted(self.outcomes)},
                    'frame': [{'id': b, 'campaign': f'C-{b}', 'outcome': o, 'operation': False,
                               'baseline_eligible': b == 'SYN001'} for b, o in sorted(self.outcomes.items())],
                    'registry': {'sources': sources}, 'dossiers': [dossier],
                    'source_bindings': {s['id']: {'metadata_sha256': source_metadata_digest(s), 'raw_sha256': s['sha256']}
                                        for s in sources}}
        write_json(root / 'data/snapshot.json', snapshot)
        profile = {'id': 'reported_side_strength_v1', 'use': 'retrospective_whole_engagement_strength_diagnostic',
                   'target': 'recorded_decisive_union_outcome', 'field': 'reported_side_strength', 'unit': 'people',
                   'population_rule': 'Synthetic.', 'interval_rule': 'Synthetic.',
                   'uncertainty_policy': 'preserve_bounds_no_imputation', 'scenario_policy': 'generated_pair_ranking_v1',
                   'selection_policy': 'locked_without_outcomes_or_scores', 'contract': ref(root, 'data/contract.md'),
                   'design': ref(root, 'data/design.md'),
                   'evaluation_plan': {'research_cutoff': '2026-09-25', 'grouping': 'whole_campaign_holdout',
                                       'comparison': 'common_new_and_all_rows_per_scenario', 'fitting': 'not_performed',
                                       'source_selection': 'no_outcome_or_score_selection',
                                       'output_name': 'diagnostic_union_score'}}
        self.proposal = {'schema_version': 2, 'kind': 'admission_proposal', 'test_only': True, 'profile': profile,
                         'snapshot': ref(root, 'data/snapshot.json'), 'candidates': self.candidates,
                         'screened': self.screened, 'scenarios': []}
        write_json(root / 'data/proposal.json', self.proposal)
        # Declare exactly the generated scenarios, as an author following the rule would.
        report = validate_proposal(root, 'data/proposal.json', allow_test_only=True)
        decisions = {d['candidate_id']: d for d in report['decisions']}
        frame = {r['id']: r for r in snapshot['frame']}
        self.proposal['scenarios'] = [{'id': k, 'assignments': v, 'rationale': 'Generated by the design §4 rule.'}
                                      for k, v in sorted(generate_scenarios(frame, decisions).items())]
        write_json(root / 'data/proposal.json', self.proposal)

    def run(self):
        return validate_proposal(self.root, 'data/proposal.json', allow_test_only=True)

    def release(self):
        report = self.run()
        (self.root / 'data/response.md').write_text('# SYNTHETIC TEST-ONLY REVIEW STUB\n')
        review = {'kind': 'separate_evidence_use_review', 'test_only': True, 'bindings': review_bindings(report),
                  'scope': sorted(SCOPE), 'reviewer': {'identity': 'synthetic-reviewer', 'kind': 'test_stub',
                                                       'model': None, 'effort': None},
                  'date': '2026-09-25', 'verdict': 'accept', 'findings': [], 'response': ref(self.root, 'data/response.md')}
        write_json(self.root / 'data/review.json', review)
        primary = {'kind': 'primary_evidence_use_reconciliation', 'test_only': True,
                   'proposal_sha256': report['proposal_sha256'], 'review_sha256': digest(self.root / 'data/review.json'),
                   'actor': 'synthetic-primary', 'date': '2026-09-25', 'decision': 'accept', 'unresolved_findings': [],
                   'rationale': 'Synthetic test stub, not a historical admission.'}
        write_json(self.root / 'data/primary.json', primary)
        manifest = {'schema_version': 2, 'kind': 'strength_admission_release_audit', 'test_only': True,
                    'proposal': ref(self.root, 'data/proposal.json'),
                    'implementation_sha256': {p: digest(self.root / p) for p in IMPLEMENTATION},
                    'review': ref(self.root, 'data/review.json'), 'reconciliation': ref(self.root, 'data/primary.json'),
                    'rows_sha256': canonical_hash(report['preview_rows_by_scenario']),
                    'coverage_sha256': canonical_hash(report['coverage'])}
        write_json(self.root / 'data/release.json', manifest)
        return manifest


class StrengthAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.s = Synthetic(Path(self.temp.name))

    def decision(self, report, cid):
        return next(d for d in report['decisions'] if d['candidate_id'] == cid)

    def codes(self, report, cid):
        return {r['code'] for r in self.decision(report, cid)['reasons']}

    def test_pair_classes_orderings_and_rows(self):
        r = self.s.run()
        self.assertEqual(r['scenario_issues'], [])
        rows = r['preview_rows_by_scenario']
        first = rows['compiled_first'][0]['sides']
        self.assertEqual((first['US']['candidate_id'], first['Confederate']['candidate_id']), ('tab-us', 'tab-cs'))
        reports = rows['reports_first'][0]['sides']
        self.assertEqual((reports['US']['candidate_id'], reports['Confederate']['candidate_id']), ('rep-us', 'rep-cs'))
        # Four same-basis pairs give alternate_2..alternate_4; every pair appears somewhere.
        self.assertEqual(r['generated_scenarios'], ['alternate_2', 'alternate_3', 'alternate_4',
                                                     'compiled_first', 'reports_first'])
        used = {(v['sides']['US']['candidate_id'], v['sides']['Confederate']['candidate_id'])
                for rs in rows.values() for v in rs}
        self.assertEqual(len(used), 4)
        self.assertEqual(r['emitted_rows'], [])
        self.assertEqual(r['promoted_rows'], 0)
        self.assertEqual(r['coverage']['frame_engagements'], 3)
        self.assertEqual(r['coverage']['decisive_engagements'], 2)
        self.assertEqual(r['coverage']['paired_common_ids'], ['SYN001'])

    def test_declared_scenarios_must_match_generation_rule(self):
        self.s.proposal['scenarios'][0]['assignments']['SYN001'] = {'US': 'rep-us', 'Confederate': 'tab-cs'}
        write_json(self.s.root / 'data/proposal.json', self.s.proposal)
        r = self.s.run()
        self.assertEqual(r['scenario_issues'], [{'code': 'declared_scenarios_differ_from_generation_rule'}])
        self.assertEqual(r['preview_rows_by_scenario'], {})

    def test_engagement_interval_rules(self):
        cases = {('2000-01-03', '2000-01-03'): 'post_engagement_state',
                 ('2000-01-02', '2000-01-02'): 'partial_interval',
                 ('2000-01-02', '2000-01-05'): 'interval_unresolved',
                 (None, None): 'engagement_link_unknown',
                 ('2000-01-01', '2000-01-01'): 'engagement_link_unknown'}
        for period, code in cases.items():
            with self.subTest(period=period):
                self.s.figures[2] = ('rep-us', 'US', 'us-report', 1100, 'reported_engaged', period)
                self.s.write()
                r = self.s.run()
                self.assertIn(code, self.codes(r, 'rep-us'))
                self.assertIn(self.decision(r, 'rep-us')['status'], {'excluded', 'blocked'})

    def test_earlier_state_with_cited_link_is_applicable(self):
        self.s.figures[2] = ('rep-us', 'US', 'us-report', 1100, 'reported_engaged', ('2000-01-01', '2000-01-01'))
        self.s.candidates[2]['citations'] = [{'source_id': 'synthetic-text', 'section': 'us-report',
                                              'locator': 'us-report', 'quote': 'SYNTHETIC US report: 1100 engaged.'}]
        self.s.write()
        self.assertEqual(self.decision(self.s.run(), 'rep-us')['status'], 'eligible_candidate')

    def test_authored_codes_labels_and_severity_order(self):
        self.s.candidates[2]['codes'] = ['adversary_or_hearsay_estimate', 'one_sided_bound']
        self.s.candidates[3]['codes'] = ['derivation_unknown']
        self.s.write()
        r = self.s.run()
        self.assertEqual(self.decision(r, 'rep-us')['status'], 'excluded')
        self.assertEqual(self.codes(r, 'rep-us'), {'adversary_or_hearsay_estimate', 'one_sided_bound'})
        self.assertEqual(self.decision(r, 'rep-cs')['status'], 'eligible_candidate')
        self.assertEqual(self.decision(r, 'rep-cs')['labels'], ['derivation_unknown'])

    def test_unknown_estimation_is_a_label_not_a_block(self):
        self.s.estimation = 'unknown'
        self.s.write()
        r = self.s.run()
        self.assertEqual(self.decision(r, 'tab-us')['status'], 'eligible_candidate')
        self.assertIn('estimation_status_unknown', self.decision(r, 'tab-us')['labels'])
        self.assertEqual(r['coverage']['scenario_row_labels']['compiled_first']['estimation_status_unknown'], 1)

    def test_reinforcements_post_outcome_and_unresolved_role(self):
        self.s.figures[2] = ('rep-us', 'US', 'us-report', 1100, 'reported_reinforcements', ('2000-01-02', '2000-01-03'))
        self.s.candidates[3]['source_role'] = None
        self.s.write()
        r = self.s.run()
        self.assertIn('partial_scope', self.codes(r, 'rep-us'))
        self.assertIn('source_role_unresolved', self.codes(r, 'rep-cs'))
        self.s.phase = 'post_outcome'
        self.s.write()
        r = self.s.run()
        self.assertTrue(all('post_outcome_claim' in self.codes(r, c) for c in ('tab-us', 'tab-cs')))

    def test_mixed_basis_scenarios_and_other_document_class(self):
        self.s.figures[3] = ('rep-cs', 'CS', 'cs-report', 700, 'reported_effective', ('2000-01-02', '2000-01-03'))
        self.s.write()
        r = self.s.run()
        self.assertIn('mixed_basis_1', r['generated_scenarios'])
        mixed = [v for v in r['preview_rows_by_scenario']['mixed_basis_1'] if v['basis_class'] == 'mixed_basis']
        self.assertEqual(len(mixed), 1)
        # reports_first falls back to the only same-basis pair when no own-report pair shares a basis.
        rf = r['preview_rows_by_scenario']['reports_first'][0]['sides']
        self.assertEqual(rf['Confederate']['candidate_id'], 'tab-cs')

    def test_screened_observations_enter_the_ledger_only(self):
        self.s.screened = [{'id': 'enemy-estimate', 'battle_id': 'SYN001', 'side': 'Confederate', 'claim_id': 'strength',
                            'citation_index': 0, 'code': 'adversary_or_hearsay_estimate', 'rationale': 'Synthetic.'}]
        self.s.write()
        r = self.s.run()
        self.assertEqual(r['coverage']['screened_observations'], 1)
        self.assertEqual(r['coverage']['status_counts']['excluded'], 1)
        self.s.screened[0]['code'] = 'derivation_unknown'
        self.s.proposal['screened'] = self.s.screened
        write_json(self.s.root / 'data/proposal.json', self.s.proposal)
        with self.assertRaisesRegex(AdmissionError, 'Screened code'):
            self.s.run()

    def test_inconclusive_records_never_form_rows(self):
        r = self.s.run()
        for rows in r['preview_rows_by_scenario'].values():
            self.assertNotIn('SYN003', {v['battle_id'] for v in rows})

    def test_release_audit_and_production_rejection(self):
        self.s.release()
        a = audit_release(self.s.root, 'data/release.json', allow_test_only=True)
        self.assertEqual(a['release_status'], 'verified')
        self.assertEqual(a['release_admitted_candidates'], 4)
        self.assertEqual(a['promoted_rows'], 0)
        for path in ('data/proposal.json', 'data/release.json'):
            with self.subTest(path=path), self.assertRaisesRegex(AdmissionError, 'Test-only'):
                check(self.s.root, path)

    def test_release_rejects_scope_and_row_mutation(self):
        self.s.release()
        review = __import__('json').loads((self.s.root / 'data/review.json').read_text())
        review['scope'] = sorted(SCOPE - {'basis_pairing'})
        write_json(self.s.root / 'data/review.json', review)
        manifest = __import__('json').loads((self.s.root / 'data/release.json').read_text())
        manifest['review'] = ref(self.s.root, 'data/review.json')
        primary = __import__('json').loads((self.s.root / 'data/primary.json').read_text())
        primary['review_sha256'] = manifest['review']['sha256']
        write_json(self.s.root / 'data/primary.json', primary)
        manifest['reconciliation'] = ref(self.s.root, 'data/primary.json')
        write_json(self.s.root / 'data/release.json', manifest)
        a = audit_release(self.s.root, 'data/release.json', allow_test_only=True)
        self.assertEqual(a['release_status'], 'blocked')
        self.assertEqual(a['release_admitted_candidates'], 0)
        manifest['rows_sha256'] = '0' * 64
        write_json(self.s.root / 'data/release.json', manifest)
        with self.assertRaisesRegex(AdmissionError, 'Released rows mismatch'):
            audit_release(self.s.root, 'data/release.json', allow_test_only=True)

    def test_unsupported_profile_is_invalid(self):
        self.s.proposal['profile']['use'] = 'retrospective_pre_engagement_prediction'
        write_json(self.s.root / 'data/proposal.json', self.s.proposal)
        with self.assertRaisesRegex(AdmissionError, 'Unsupported tier-2 profile'):
            self.s.run()


if __name__ == '__main__':
    unittest.main()
