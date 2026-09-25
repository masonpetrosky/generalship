"""Offline, non-promoting checks for the tier-2 `reported_side_strength_v1` profile.

Implements docs/feature-admission-reported-strength.md beside, not inside, the
opening-profile validator. No model consumes these outputs; `emitted_rows` is
always empty and `promoted_rows` is always zero.
"""

from collections import Counter
from datetime import date
from pathlib import Path

from .admission import (AdmissionError, SIDES, _citations, _snapshot, _status, binding,
                        canonical_hash, indexed, iso, load_json, require, shape, text,
                        unique_strings)
from .evidence import citation_text
from .sources import digest, read_csv, safe_path, source_metadata_digest

PROFILE = 'reported_side_strength_v1'
USE = 'retrospective_whole_engagement_strength_diagnostic'
CONTRACT_SHA256 = 'b858b7a27f3617408779c928ea545da814b31229ff2c40caf64927773f320c99'
OUTPUT_NAME = 'diagnostic_union_score'
BASES = {'reported_engaged', 'reported_effective', 'reported_present', 'present_for_duty'}
ROLES = {'own_report', 'compiled_total'}
# Design §3 and §8: every authored code has one fixed severity.
CODES = {
    'partial_scope': 'excluded', 'other_engagement': 'excluded',
    'post_engagement_state': 'excluded', 'partial_interval': 'excluded',
    'adversary_or_hearsay_estimate': 'excluded', 'derived_from_losses': 'excluded',
    'post_outcome_claim': 'excluded',
    'scope_unresolved': 'blocked', 'engagement_link_unknown': 'blocked',
    'interval_unresolved': 'blocked', 'source_role_unresolved': 'blocked',
    'basis_unknown': 'blocked', 'unreadable_value': 'blocked', 'one_sided_bound': 'blocked',
    'derivation_unknown': 'label',
}
LABELS = {'derivation_unknown', 'estimation_status_unknown'}
SCOPE = {'scope', 'engagement_match', 'source_role', 'printed_value', 'derivation',
         'source_dependence', 'basis_pairing', 'scenarios'}
IMPLEMENTATION = ('generalship/strength_admission.py', 'generalship/admission.py',
                  'generalship/evidence.py', 'generalship/sources.py')
DEFAULT_PROPOSAL = 'data/admission/reported-strength-v1.json'


def implementation_hashes():
    package = Path(__file__).resolve().parent
    return {p: digest(package / Path(p).name) for p in IMPLEMENTATION}


def _profile(root, profile):
    shape(profile, 'id use target field unit population_rule interval_rule uncertainty_policy '
          'scenario_policy selection_policy contract design evaluation_plan', 'profile')
    binding(root, profile['contract'], json_file=False)
    binding(root, profile['design'], json_file=False)
    require(profile['contract']['sha256'] == CONTRACT_SHA256, 'Unsupported contract version')
    require(profile['id'] == PROFILE and profile['use'] == USE
            and profile['target'] == 'recorded_decisive_union_outcome'
            and profile['field'] == 'reported_side_strength' and profile['unit'] == 'people',
            'Unsupported tier-2 profile')
    for key in ('population_rule', 'interval_rule'):
        text(profile[key], key)
    require(profile['uncertainty_policy'] == 'preserve_bounds_no_imputation', 'Uncertainty policy')
    require(profile['scenario_policy'] == 'generated_pair_ranking_v1', 'Scenario policy')
    require(profile['selection_policy'] == 'locked_without_outcomes_or_scores', 'Selection policy')
    plan = profile['evaluation_plan']
    shape(plan, 'research_cutoff grouping comparison fitting source_selection output_name', 'evaluation plan')
    iso(plan['research_cutoff'], 'research cutoff')
    require(plan['grouping'] == 'whole_campaign_holdout'
            and plan['comparison'] == 'common_new_and_all_rows_per_scenario'
            and plan['fitting'] == 'not_performed'
            and plan['source_selection'] == 'no_outcome_or_score_selection'
            and plan['output_name'] == OUTPUT_NAME, 'Evaluation policy')


def _intervals(root, sources, frame):
    """Engagement intervals come from the bound CWSAC battle table, never from authored text."""
    require('arnold-cwsac-battles' in sources, 'Bound battle table required for intervals')
    rows = {r['battle']: r for r in read_csv(safe_path(root, sources['arnold-cwsac-battles']['path']))}
    result = {}
    for bid in frame:
        require(bid in rows, f'No bound interval for {bid}')
        start, end = rows[bid]['start_date'], rows[bid]['end_date'] or rows[bid]['start_date']
        iso(start, 'interval start'); iso(end, 'interval end')
        result[bid] = (date.fromisoformat(start), date.fromisoformat(end))
    return result


def _document_key(sources, source_id):
    source = sources[source_id]
    image = sources.get(source.get('facsimile_source_id'))
    return image['sha256'] if image else source['sha256']


def _reason(reasons, gate, code, severity=None):
    item = {'gate': gate, 'severity': severity or CODES[code], 'code': code}
    if item not in reasons:
        reasons.append(item)


def _candidate(root, c, sources, dossiers, frame, intervals):
    shape(c, 'id battle_id side entity_id quantity_id source_role codes rationale citations', 'candidate')
    require(c['side'] in SIDES and c['battle_id'] in frame, 'Candidate scope')
    dossier = dossiers.get(c['battle_id'])
    require(dossier is not None and dossier['schema_version'] == 3, 'Candidate needs a schema v3 dossier')
    entities = {e['id']: e for e in dossier['entities']}
    require(c['entity_id'] in entities and entities[c['entity_id']]['kind'] == 'formation', 'Candidate entity')
    require({'US': 'US', 'CS': 'Confederate'}[entities[c['entity_id']]['side']] == c['side'],
            'Candidate side/entity mismatch')
    quantities = {q['id']: q for q in dossier['quantities']}
    require(c['quantity_id'] in quantities, 'Unknown quantity')
    q = quantities[c['quantity_id']]
    require(q['entity_id'] == c['entity_id'], 'Quantity/entity mismatch')
    claim = next(x for x in dossier['claims'] if x['id'] == q['claim_id'])
    cited = claim['citations'][q['citation_index']]
    text(c['rationale'], 'Candidate rationale')
    _citations(root, sources, c['citations'])
    unique_strings(c['codes'], 'Candidate codes')
    reasons = []
    if c['source_role'] not in ROLES:
        require(c['source_role'] is None, 'Source role vocabulary')
        _reason(reasons, 'source_role', 'source_role_unresolved')
    for code in c['codes']:
        require(code in CODES, f'Unknown code: {code}')
        _reason(reasons, 'authored', code)
    if claim['phase'] == 'post_outcome':
        _reason(reasons, 'temporal', 'post_outcome_claim')
    if q['basis'] == 'reported_reinforcements':
        _reason(reasons, 'scope', 'partial_scope')
    else:
        require(q['basis'] in BASES, 'Quantity basis')
    # Design §8: engagement-interval rules replace the opening contact checks.
    start, end = intervals[c['battle_id']]
    ps, pe = q['period']['start'], q['period']['end']
    if ps is None:
        _reason(reasons, 'temporal', 'engagement_link_unknown')
    else:
        ps, pe = date.fromisoformat(ps), date.fromisoformat(pe)
        if ps > start:
            _reason(reasons, 'temporal', 'post_engagement_state')
        elif ps < start:
            # An earlier state date needs a cited source link to this engagement.
            if not c['citations']:
                _reason(reasons, 'temporal', 'engagement_link_unknown')
        elif pe != end:
            _reason(reasons, 'temporal', 'partial_interval' if pe < end else 'interval_unresolved')
    if q['lower'] <= 0:
        _reason(reasons, 'derivation', 'unreadable_value')
    labels = sorted({r['code'] for r in reasons if r['severity'] == 'label'}
                    | ({'estimation_status_unknown'} if q['estimation_status'] == 'unknown' else set()))
    reasons = [r for r in reasons if r['severity'] != 'label']
    status = _status(reasons)
    return {'candidate_id': c['id'], 'candidate_sha256': canonical_hash(c),
            'battle_id': c['battle_id'], 'side': c['side'], 'status': status,
            'reasons': reasons, 'labels': labels,
            'gates': {'binding_schema': 'pass', 'applicability': status,
                      'evidence_use_review': 'not_supplied', 'release': 'not_requested'},
            'source_id': cited['source_id'], 'document_key': _document_key(sources, cited['source_id']),
            'source_role': c['source_role'], 'basis': q['basis'], 'quantity_id': q['id'],
            'preview_bounds': [q['lower'], q['upper']] if status == 'eligible_candidate' else None,
            'observation': {'quantity': q, 'claim_id': claim['id'], 'claim_phase': claim['phase'],
                            'citation': cited, 'source_metadata_sha256': source_metadata_digest(sources[cited['source_id']]),
                            'raw_sha256': sources[cited['source_id']]['sha256'],
                            'independence_established': False}}


def _screened(root, s, sources, dossiers, frame):
    """A figure recorded in the ledger with a face-value exclusion or block; never a pair."""
    shape(s, 'id battle_id side claim_id citation_index code rationale', 'screened observation')
    require(s['side'] in SIDES and s['battle_id'] in frame, 'Screened scope')
    require(s['code'] in CODES and CODES[s['code']] in {'excluded', 'blocked'}, 'Screened code')
    text(s['rationale'], 'Screened rationale')
    dossier = dossiers.get(s['battle_id'])
    require(dossier is not None, 'Screened observation needs a dossier')
    claim = next((x for x in dossier['claims'] if x['id'] == s['claim_id']), None)
    require(claim is not None and claim['dimension'] == 'strength' and claim['status'] != 'unknown',
            'Screened claim must be an evidenced strength claim')
    i = s['citation_index']
    require(type(i) is int and 0 <= i < len(claim['citations']), 'Screened citation index')
    ct = claim['citations'][i]
    require(ct['quote'] in citation_text(root, sources, ct), 'Screened quote missing')
    return {'screened_id': s['id'], 'battle_id': s['battle_id'], 'side': s['side'],
            'status': CODES[s['code']], 'code': s['code'], 'source_id': ct['source_id'], 'quote': ct['quote']}


def _pairs(battle, decisions):
    eligible = [d for d in decisions.values() if d['battle_id'] == battle and d['status'] == 'eligible_candidate']
    us = [d for d in eligible if d['side'] == 'US']
    cs = [d for d in eligible if d['side'] == 'Confederate']
    same, mixed = [], []
    for u in us:
        for c in cs:
            if u['source_role'] == c['source_role'] == 'compiled_total' and u['document_key'] == c['document_key']:
                klass = 'a'
            elif u['source_role'] == c['source_role'] == 'own_report':
                klass = 'b'
            else:
                klass = 'c'
            key = (u['source_id'], c['source_id'], u['quantity_id'], c['quantity_id'])
            (same if u['basis'] == c['basis'] else mixed).append((klass, key, u, c))
    order_a = lambda p: ('abc'.index(p[0]), p[1])
    order_b = lambda p: ('bac'.index(p[0]), p[1])
    return sorted(same, key=order_a), sorted(same, key=order_b), sorted(mixed, key=order_a)


def generate_scenarios(frame, decisions):
    """Design §4's complete, pre-extraction generation rule."""
    battles = [b for b, r in sorted(frame.items()) if not r['operation'] and r['outcome'] != 'Inconclusive']
    pairs = {b: _pairs(b, decisions) for b in battles}
    pick = lambda p: {'US': p[2]['candidate_id'], 'Confederate': p[3]['candidate_id']}
    empty = {'US': None, 'Confederate': None}

    def build(chooser):
        return {b: (chooser(b) if b in pairs else empty) for b in sorted(frame)}
    first = lambda b: pick(pairs[b][0][0]) if pairs[b][0] else empty
    scenarios = {'compiled_first': build(first),
                 'reports_first': build(lambda b: pick(pairs[b][1][0]) if pairs[b][1] else empty)}
    max_same = max((len(p[0]) for p in pairs.values()), default=0)
    for k in range(2, max_same + 1):
        scenarios[f'alternate_{k}'] = build(lambda b, k=k: pick(pairs[b][0][k - 1]) if len(pairs[b][0]) >= k else first(b))
    max_mixed = max((len(p[2]) for p in pairs.values()), default=0)
    for k in range(1, max_mixed + 1):
        scenarios[f'mixed_basis_{k}'] = build(
            lambda b, k=k: (pick(pairs[b][2][min(k, len(pairs[b][2])) - 1]) if pairs[b][2] else first(b)))
    return scenarios


def _rows(frame, decisions, assignments):
    rows = []
    for battle, a in sorted(assignments.items()):
        if a['US'] is None or a['Confederate'] is None:
            continue
        sides = {s: decisions[a[s]] for s in SIDES}
        rows.append({'battle_id': battle, 'campaign': frame[battle]['campaign'], 'profile_id': PROFILE,
                     'basis_class': 'same_basis' if sides['US']['basis'] == sides['Confederate']['basis'] else 'mixed_basis',
                     'sides': {s: {'candidate_id': d['candidate_id'], 'source_id': d['source_id'],
                                   'source_role': d['source_role'], 'basis': d['basis'], 'labels': d['labels'],
                                   'strength_bounds': d['preview_bounds']} for s, d in sides.items()}})
    return rows


def _coverage(frame, dossiers, decisions, screened, rows):
    ledger = []
    for battle, record in sorted(frame.items()):
        sides = {}
        for side in SIDES:
            ds = [d for d in decisions.values() if d['battle_id'] == battle and d['side'] == side]
            ss = [s for s in screened.values() if s['battle_id'] == battle and s['side'] == side]
            sides[side] = {'candidate_ids': [d['candidate_id'] for d in ds],
                           'screened_ids': [s['screened_id'] for s in ss],
                           'status_counts': dict(sorted(Counter([d['status'] for d in ds] + [s['status'] for s in ss]).items())),
                           'reasons': sorted({r['code'] for d in ds for r in d['reasons']} | {s['code'] for s in ss}),
                           'labels': sorted({l for d in ds for l in d['labels']})}
        ledger.append({'battle_id': battle, 'campaign': record['campaign'], 'dossier_available': battle in dossiers,
                       'baseline_eligible': record['baseline_eligible'],
                       'outcome_eligible': record['outcome'] != 'Inconclusive',
                       'engagement_grain': not record['operation'], 'sides': sides,
                       'complete_in_scenarios': sorted(s for s, rs in rows.items() if any(v['battle_id'] == battle for v in rs))})
    complete = {v['battle_id'] for rs in rows.values() for v in rs}
    baseline = {b for b, r in frame.items() if r['baseline_eligible']}
    decisive = {b for b, r in frame.items() if not r['operation'] and r['outcome'] != 'Inconclusive'}
    return {'frame_engagements': len(frame), 'frame_campaigns': len({r['campaign'] for r in frame.values()}),
            'decisive_engagements': len(decisive), 'dossiers_available': len(dossiers),
            'candidate_observations': len(decisions), 'screened_observations': len(screened),
            'status_counts': dict(sorted(Counter([d['status'] for d in decisions.values()]
                                                 + [s['status'] for s in screened.values()]).items())),
            'complete_engagements_any_scenario': len(complete),
            'baseline_eligible_engagements': len(baseline),
            'paired_common_ids': sorted(complete & baseline), 'newly_covered_ids': sorted(complete - baseline),
            'scenario_rows': {s: len(rs) for s, rs in rows.items()},
            'scenario_row_labels': {s: {'derivation_unknown': sum(any('derivation_unknown' in v['sides'][x]['labels'] for x in SIDES) for v in rs),
                                        'estimation_status_unknown': sum(any('estimation_status_unknown' in v['sides'][x]['labels'] for x in SIDES) for v in rs),
                                        'mixed_basis': sum(v['basis_class'] == 'mixed_basis' for v in rs),
                                        'own_report': sum(any(v['sides'][x]['source_role'] == 'own_report' for x in SIDES) for v in rs)}
                                    for s, rs in rows.items()},
            'ledger': ledger}


def validate_proposal(root, path=DEFAULT_PROPOSAL, *, allow_test_only=False):
    root = Path(root)
    ppath = safe_path(root, str(path))
    proposal = load_json(ppath)
    shape(proposal, 'schema_version kind test_only profile snapshot candidates screened scenarios', 'proposal')
    require(type(proposal['schema_version']) is int and proposal['schema_version'] == 2
            and proposal['kind'] == 'admission_proposal', 'Proposal kind/version')
    require(type(proposal['test_only']) is bool and (allow_test_only or not proposal['test_only']),
            'Test-only proposal rejected')
    snapshot, frame, sources, dossiers = _snapshot(root, proposal['snapshot'], allow_test_only)
    require(snapshot['test_only'] == proposal['test_only'], 'Test marker mismatch')
    _profile(root, proposal['profile'])
    cutoff = proposal['profile']['evaluation_plan']['research_cutoff']
    for source in sources.values():
        if source.get('retrieved_at') is not None:
            require(source['retrieved_at'] <= cutoff, 'Source snapshot exceeds research cutoff')
    intervals = _intervals(root, sources, frame)
    decisions = {}
    for cid, c in sorted(indexed(proposal['candidates'], 'candidates').items()):
        require(c.get('battle_id') in frame and c.get('side') in SIDES, 'Unplaceable candidate')
        try:
            decisions[cid] = _candidate(root, c, sources, dossiers, frame, intervals)
        except (ValueError, KeyError, TypeError, IndexError, StopIteration, OSError) as exc:
            decisions[cid] = {'candidate_id': cid, 'candidate_sha256': canonical_hash(c), 'battle_id': c['battle_id'],
                              'side': c['side'], 'status': 'invalid',
                              'reasons': [{'gate': 'binding_schema', 'severity': 'invalid', 'code': str(exc)}],
                              'labels': [], 'gates': {'binding_schema': 'fail', 'applicability': 'incomplete',
                                                      'evidence_use_review': 'not_supplied', 'release': 'not_requested'},
                              'source_id': None, 'document_key': None, 'source_role': None, 'basis': None,
                              'quantity_id': None, 'preview_bounds': None, 'observation': None}
    screened = {sid: _screened(root, s, sources, dossiers, frame)
                for sid, s in sorted(indexed(proposal['screened'], 'screened').items())}
    require(not set(screened) & set(decisions), 'Screened and candidate IDs must differ')
    generated = generate_scenarios(frame, decisions)
    declared = indexed(proposal['scenarios'], 'scenarios')
    issues = []
    for sid, s in declared.items():
        shape(s, 'id assignments rationale', 'scenario')
        text(s['rationale'], 'Scenario rationale')
    if set(declared) != set(generated) or any(declared[s]['assignments'] != generated[s] for s in generated if s in declared):
        issues.append({'code': 'declared_scenarios_differ_from_generation_rule'})
    rows = {sid: _rows(frame, decisions, a) for sid, a in generated.items()} if not issues else {}
    return {'schema_version': 2, 'kind': 'strength_admission_proposal_check', 'profile_id': PROFILE,
            'test_only': proposal['test_only'], 'validator_sha256': implementation_hashes(),
            'proposal_sha256': digest(ppath), 'snapshot_sha256': proposal['snapshot']['sha256'],
            'profile_sha256': canonical_hash(proposal['profile']),
            'candidate_hashes': {c: d['candidate_sha256'] for c, d in decisions.items()},
            'status': 'invalid' if any(d['status'] == 'invalid' for d in decisions.values()) else 'checked',
            'decisions': list(decisions.values()), 'screened': list(screened.values()),
            'scenario_issues': issues, 'generated_scenarios': sorted(generated),
            'preview_rows_by_scenario': rows,
            'coverage': _coverage(frame, dossiers, decisions, screened, rows),
            'target_channel': {b: r['outcome'] for b, r in sorted(frame.items())},
            'labels_required': ['partial_outcome_leakage', 'conditional_on_source_availability'],
            'emitted_rows': [], 'promoted_rows': 0,
            'limits': ['Tier-2 diagnostic rows; never opening strength, win probability or command effect.',
                       'Semantic codes are authored evidence-use proposals and require separate review.',
                       'Preview rows are not released model inputs; no fitting or promotion occurs.']}


def review_bindings(report):
    return {k: report[k] for k in ('proposal_sha256', 'snapshot_sha256', 'profile_sha256', 'candidate_hashes')}


def audit_release(root, path, *, allow_test_only=False):
    """Verify a separately reviewed tier-2 manifest without installing or fitting it."""
    root = Path(root)
    manifest = load_json(safe_path(root, str(path)))
    shape(manifest, 'schema_version kind test_only proposal implementation_sha256 review reconciliation '
          'rows_sha256 coverage_sha256', 'release manifest')
    require(manifest['schema_version'] == 2 and manifest['kind'] == 'strength_admission_release_audit',
            'Release kind/version')
    require(type(manifest['test_only']) is bool and (allow_test_only or not manifest['test_only']),
            'Test-only release rejected')
    binding(root, manifest['proposal'])
    report = validate_proposal(root, manifest['proposal']['path'], allow_test_only=allow_test_only)
    require(report['test_only'] == manifest['test_only'], 'Release test marker mismatch')
    require(manifest['implementation_sha256'] == implementation_hashes(), 'Implementation hash mismatch')
    review = binding(root, manifest['review'])
    reconciliation = binding(root, manifest['reconciliation'])
    shape(review, 'kind test_only bindings scope reviewer date verdict findings response', 'review')
    shape(reconciliation, 'kind test_only proposal_sha256 review_sha256 actor date decision '
          'unresolved_findings rationale', 'reconciliation')
    require(review['test_only'] is manifest['test_only'] and reconciliation['test_only'] is manifest['test_only'],
            'Review test marker mismatch')
    require(review['bindings'] == review_bindings(report), 'Review does not bind exact proposal inputs')
    require(reconciliation['kind'] == 'primary_evidence_use_reconciliation'
            and reconciliation['proposal_sha256'] == report['proposal_sha256']
            and reconciliation['review_sha256'] == manifest['review']['sha256'], 'Reconciliation binding')
    iso(review['date'], 'Review date'); iso(reconciliation['date'], 'Reconciliation date')
    shape(review['reviewer'], 'identity kind model effort', 'reviewer')
    text(review['reviewer']['identity'], 'Reviewer identity')
    require(review['reviewer']['kind'] in {'ai', 'human', 'test_stub'}, 'Reviewer kind')
    if review['reviewer']['kind'] == 'test_stub':
        require(manifest['test_only'] and allow_test_only, 'Test reviewer rejected')
    elif review['reviewer']['kind'] == 'ai':
        text(review['reviewer']['model'], 'Reviewer model'); text(review['reviewer']['effort'], 'Reviewer effort')
    text(reconciliation['actor'], 'Primary actor'); text(reconciliation['rationale'], 'Primary rationale')
    require(reconciliation['actor'] != review['reviewer']['identity'], 'Separate review requires different actors')
    text(binding(root, review['response'], json_file=False), 'Actual review response')
    unique_strings(review['scope'], 'Review scope')
    require(review['verdict'] in {'accept', 'corrections_needed'}
            and reconciliation['decision'] in {'accept', 'corrections_needed'}, 'Verdicts')
    require(isinstance(review['findings'], list) and isinstance(reconciliation['unresolved_findings'], list),
            'Review findings required')
    accepted = (review['kind'] == 'separate_evidence_use_review' and set(review['scope']) == SCOPE
                and review['verdict'] == reconciliation['decision'] == 'accept'
                and not review['findings'] and not reconciliation['unresolved_findings'])
    require(report['status'] != 'invalid', 'Invalid proposal cannot be released')
    require(not report['scenario_issues'], 'Unresolved scenario generation')
    require(canonical_hash(report['preview_rows_by_scenario']) == manifest['rows_sha256'], 'Released rows mismatch')
    require(canonical_hash(report['coverage']) == manifest['coverage_sha256'], 'Coverage ledger mismatch')
    selected = {v['sides'][side]['candidate_id'] for rows in report['preview_rows_by_scenario'].values()
                for v in rows for side in SIDES}
    for d in report['decisions']:
        if d['status'] == 'eligible_candidate':
            d['gates']['evidence_use_review'] = 'pass' if accepted else 'fail'
            d['gates']['release'] = 'verified' if accepted else 'blocked'
            d['status'] = 'admitted' if accepted and d['candidate_id'] in selected else 'blocked'
            if not accepted:
                d['reasons'].append({'gate': 'review', 'severity': 'blocked', 'code': 'evidence_use_review_not_accepted'})
    report.update(kind='strength_admission_release_check', release_status='verified' if accepted else 'blocked',
                  audited_rows_by_scenario=report['preview_rows_by_scenario'] if accepted else {},
                  review_sha256=manifest['review']['sha256'], release_sha256=digest(safe_path(root, str(path))),
                  coverage_stage='proposal_before_review',
                  release_admitted_candidates=sum(d['status'] == 'admitted' for d in report['decisions']))
    return report


def check(root, path=DEFAULT_PROPOSAL):
    document = load_json(safe_path(root, str(path)))
    require(isinstance(document, dict), 'Admission document must be an object')
    if document.get('kind') == 'strength_admission_release_audit':
        return audit_release(root, path)
    return validate_proposal(root, path)
