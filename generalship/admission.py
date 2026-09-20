"""Offline, non-promoting feature-admission checks. No model consumes these outputs.

Semantic mappings are authored evidence-use proposals, never inferred truth.
Structural checks cannot prove the sincerity or entailment of a review record.
"""

from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path

from .evidence import citation_text, validate_dossier
from .sources import (digest, safe_path, source_document_date,
                      source_metadata_digest, validate_source_metadata, read_csv)

DEFAULT_PROPOSAL = 'data/admission/shiloh-opening-v1.json'
SIDES = ('US', 'Confederate')
PROFILE = 'opening_available_combatants_v1'
CONTRACT_SHA256 = 'b858b7a27f3617408779c928ea545da814b31229ff2c40caf64927773f320c99'
COHORT_CONTENT_SHA256 = '6bf3a0dd30e5ffde9eb19fac1a495dbf055653a30befeb18ccefd73a7e8db95a'
SCOPE = {'profile', 'boundary', 'temporal', 'population', 'derivation',
         'source_dependence', 'scenarios'}
IMPLEMENTATION = ('generalship/admission.py', 'generalship/evidence.py',
                  'generalship/sources.py')


class AdmissionError(ValueError):
    """Invalid schema or immutable binding; no release may be accepted."""


def require(condition, message):
    if not condition:
        raise AdmissionError(message)


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def implementation_hashes():
    """Bind the executing modules, even when --root points at another checkout."""
    package = Path(__file__).resolve().parent
    return {p: digest(package / Path(p).name) for p in IMPLEMENTATION}


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def load_json(path):
    def constant(value):
        raise AdmissionError(f'Nonfinite JSON value: {value}')
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_pairs,
                      parse_constant=constant)


def shape(value, keys, where):
    require(isinstance(value, dict) and set(value) == set(keys.split()),
            f'{where}: required fields differ')


def text(value, where):
    require(isinstance(value, str) and bool(value.strip()), f'{where}: missing text')


def unique_strings(values, where, nonempty=False):
    require(isinstance(values, list), f'{where}: expected list')
    for value in values:
        text(value, where)
    require(len(set(values)) == len(values) and (not nonempty or values),
            f'{where}: duplicate or empty values')


def indexed(values, where):
    require(isinstance(values, list), f'{where}: expected list')
    result = {}
    for value in values:
        require(isinstance(value, dict), f'{where}: expected object')
        key = value.get('id')
        text(key, where)
        require(key not in result, f'{where}: duplicate ID {key}')
        result[key] = value
    return result


def iso(value, where, nullable=False):
    if value is None and nullable:
        return
    require(isinstance(value, str), f'{where}: expected ISO date')
    require(date.fromisoformat(value).isoformat() == value, f'{where}: invalid date')


def binding(root, ref, json_file=True):
    shape(ref, 'path sha256', 'file binding')
    text(ref['path'], 'binding path')
    path = safe_path(root, ref['path'])
    require(path.is_file() and digest(path) == ref['sha256'],
            f'File binding mismatch: {ref["path"]}')
    return load_json(path) if json_file else path.read_text(encoding='utf-8')


def _snapshot(root, ref, allow_test_only):
    snap = binding(root, ref)
    shape(snap, 'schema_version test_only cohort frame registry dossiers source_bindings', 'snapshot')
    require(type(snap['schema_version']) is int and snap['schema_version'] == 1, 'Snapshot version')
    require(type(snap['test_only']) is bool, 'Snapshot test marker')
    require(allow_test_only or not snap['test_only'], 'Test-only snapshot rejected')
    cohort = snap['cohort']
    require(isinstance(cohort, dict), 'Cohort object required')
    unique_strings(cohort['battle_ids'], 'cohort battle IDs', True)
    if not snap['test_only']:
        require(canonical_hash(cohort) == COHORT_CONTENT_SHA256, 'Frozen v1 cohort changed')
    frame = indexed(snap['frame'], 'frame')
    require(set(frame) == set(cohort['battle_ids']), 'Frame must cover every cohort ID exactly once')
    for row in frame.values():
        shape(row, 'id campaign outcome operation baseline_eligible', 'frame row')
        text(row['campaign'], 'campaign')
        require(row['outcome'] in {'Union', 'Confederate', 'Inconclusive'}, 'Unsupported outcome')
        require(type(row['operation']) is bool and type(row['baseline_eligible']) is bool,
                'Frame flags must be boolean')
    registry = snap['registry']
    require(isinstance(registry, dict) and isinstance(registry.get('sources'), list), 'Registry required')
    sources = indexed(registry['sources'], 'sources')
    require(set(snap['source_bindings']) == set(sources), 'Complete source-entry bindings required')
    for sid, source in sources.items():
        b = snap['source_bindings'][sid]
        shape(b, 'metadata_sha256 raw_sha256', 'source binding')
        require(b['metadata_sha256'] == source_metadata_digest(source), f'Source metadata: {sid}')
        require(b['raw_sha256'] == source['sha256'] == digest(safe_path(root, source['path'])),
                f'Raw source: {sid}')
    validate_source_metadata(root, sources)
    if not snap['test_only']:
        # Verify labels and grouping against the bound outcome channel, not an
        # author-editable frame copy or the current working registry.
        battles = {r['battle']: r for r in read_csv(safe_path(root, sources['arnold-cwsac-battles']['path']))}
        forces = {}
        for row in read_csv(safe_path(root, sources['arnold-cwsac-forces']['path'])):
            forces.setdefault(row['battle'], {})[row['belligerent']] = row
        for bid, row in frame.items():
            source = battles[bid]
            require(row['campaign'] == source['campaign'] and row['outcome'] == source['result']
                    and row['operation'] == (source['operation'] == '1'), 'Frame/source mismatch')
            fs = forces.get(bid, {})
            eligible = (set(fs) == set(SIDES) and not row['operation']
                        and row['outcome'] != 'Inconclusive'
                        and all(f['strength_min'] and f['strength_max']
                                and 0 < float(f['strength_min']) <= float(f['strength_max']) for f in fs.values()))
            require(row['baseline_eligible'] == bool(eligible), 'Baseline eligibility/source mismatch')
    dossiers = {}
    for dossier in snap['dossiers']:
        battle = dossier['battle_id']
        require(battle not in dossiers, 'Duplicate dossier')
        validate_dossier(root, dossier, sources, cohort_ids=cohort['battle_ids'])
        dossiers[battle] = dossier
    return snap, frame, sources, dossiers


def _citations(root, sources, values):
    require(isinstance(values, list), 'Citation list required')
    for c in values:
        require(isinstance(c, dict) and isinstance(c.get('quote'), str) and c['quote'].strip(),
                'Citation quote required')
        require(c['quote'] in citation_text(root, sources, c), 'Quote missing from cited passage')


def _mapping(root, sources, node):
    mapping = node['mapping']
    shape(mapping, 'time population derivation members rationale citations source_choices', 'mapping')
    require(mapping['time'] in {'before', 'at_boundary', 'after', 'unknown'}, 'Time relation')
    require(mapping['population'] in {'compatible', 'incompatible', 'unknown'}, 'Population relation')
    require(mapping['derivation'] in {'pre_state', 'post_state', 'participation', 'unknown'}, 'Derivation')
    if mapping['members'] is not None:
        unique_strings(mapping['members'], 'Membership atoms', True)
    text(mapping['rationale'], 'Mapping rationale')
    _citations(root, sources, mapping['citations'])
    require(isinstance(mapping['source_choices'], dict), 'Source choices must be an object')
    for key, value in mapping['source_choices'].items():
        text(key, 'Discrepancy ID'); text(value, 'Source alternative')
    # A resolved semantic claim needs an inspected evidence anchor. Entailment
    # and the membership partition still require separate evidence-use review.
    if (mapping['time'] != 'unknown' or mapping['population'] != 'unknown'
            or mapping['derivation'] != 'unknown' or mapping['members'] is not None):
        require(bool(mapping['citations']), 'Resolved mapping needs citations')
    return mapping


def _profile(root, profile):
    shape(profile, 'id use target field unit population_rule boundary_rule uncertainty_policy '
          'scenario_policy selection_policy contract evaluation_plan', 'profile')
    binding(root, profile['contract'], json_file=False)
    require(profile['contract']['sha256'] == CONTRACT_SHA256, 'Unsupported contract version')
    for key in ('population_rule', 'boundary_rule'):
        text(profile[key], key)
    require(profile['unit'] == 'people', 'Profile unit')
    require(profile['uncertainty_policy'] == 'preserve_bounds_no_imputation', 'Uncertainty policy')
    require(profile['scenario_policy'] == 'all_applicable_joint_alternatives_no_weights', 'Scenario policy')
    require(profile['selection_policy'] == 'locked_without_outcomes_or_scores', 'Selection policy')
    plan = profile['evaluation_plan']
    shape(plan, 'research_cutoff grouping comparison fitting source_selection', 'evaluation plan')
    iso(plan['research_cutoff'], 'research cutoff')
    require(plan['grouping'] == 'whole_campaign_holdout'
            and plan['comparison'] == 'paired_common_rows_and_separate_expanded_coverage'
            and plan['fitting'] == 'not_performed'
            and plan['source_selection'] == 'no_outcome_or_score_selection', 'Evaluation policy')
    return (profile['id'] == PROFILE and profile['use'] == 'retrospective_pre_engagement_prediction'
            and profile['target'] == 'recorded_decisive_union_outcome'
            and profile['field'] == 'opening_available_combatants')


def _boundary(root, b, sources, frame, profile):
    shape(b, 'id battle_id profile_id date contact_definition area availability_rule '
          'members_by_side citations rationale', 'boundary')
    require(b['battle_id'] in frame and b['profile_id'] == profile['id'], 'Boundary scope')
    iso(b['date'], 'Boundary date', nullable=True)
    for key in ('contact_definition', 'area', 'availability_rule'):
        if b[key] is not None:
            text(b[key], key)
    require(set(b['members_by_side']) == set(SIDES), 'Boundary requires both sides')
    for members in b['members_by_side'].values():
        if members is not None:
            unique_strings(members, 'Target membership atoms', True)
    _citations(root, sources, b['citations'])
    text(b['rationale'], 'Boundary rationale')


def _reason(reasons, gate, severity, code, node=None):
    item = {'gate': gate, 'severity': severity, 'code': code, 'node_id': node}
    if item not in reasons:
        reasons.append(item)


def _status(reasons):
    for severity in ('invalid', 'excluded', 'blocked'):
        if any(r['severity'] == severity for r in reasons):
            return severity
    return 'eligible_candidate'


def _candidate(root, c, profile, supported, boundary, sources, dossiers, reasons):
    shape(c, 'id battle_id side entity_id boundary_id root_node nodes', 'candidate')
    require(c['side'] in SIDES, 'Candidate side')
    dossier = dossiers[c['battle_id']]
    entities = {e['id']: e for e in dossier['entities']}
    require(c['entity_id'] in entities and entities[c['entity_id']]['kind'] == 'formation', 'Candidate entity')
    side = {'US': 'US', 'CS': 'Confederate'}[entities[c['entity_id']]['side']]
    require(side == c['side'], 'Candidate side/entity mismatch')
    require(boundary['battle_id'] == c['battle_id'], 'Candidate boundary mismatch')
    nodes = indexed(c['nodes'], 'nodes')
    require(c['root_node'] in nodes, 'Missing root node')
    observations, visited, active, values = [], set(), set(), {}
    if not supported:
        _reason(reasons, 'profile', 'excluded', 'unsupported_profile')
    if (any(boundary[k] is None for k in ('date', 'contact_definition', 'area', 'availability_rule'))
            or boundary['members_by_side'][c['side']] is None or not boundary['citations']):
        _reason(reasons, 'temporal_population', 'blocked', 'boundary_unresolved')
    quantities = {q['id']: q for q in dossier.get('quantities', [])}
    claims = {q['id']: q for q in dossier['claims']}
    source_choices = {}

    def visit(nid):
        require(nid in nodes and nid not in active, 'Missing dependency or cycle')
        if nid in visited:
            return values[nid]
        n = nodes[nid]
        shape(n, 'id kind reference inputs mapping', 'node')
        require(n['kind'] in {'quantity', 'claim', 'identity', 'sum', 'subtract'}, 'Transform kind')
        unique_strings(n['inputs'], 'Dependency IDs')
        m = _mapping(root, sources, n)
        active.add(nid)
        children = [visit(i) for i in n['inputs']]
        value, members = None, m['members']
        if m['time'] == 'after' or m['derivation'] in {'post_state', 'participation'}:
            _reason(reasons, 'temporal', 'excluded', 'post_boundary_dependency', nid)
        if m['population'] == 'incompatible':
            _reason(reasons, 'population', 'excluded', 'population_mismatch', nid)
        for key in ('time', 'population', 'derivation'):
            if m[key] == 'unknown':
                _reason(reasons, key, 'blocked', f'{key}_unknown', nid)
        if members is None:
            _reason(reasons, 'overlap', 'blocked', 'membership_unknown', nid)
        for key, choice in m['source_choices'].items():
            if key in source_choices and source_choices[key] != choice:
                _reason(reasons, 'derivation', 'excluded', 'incompatible_source_choices', nid)
            source_choices[key] = choice
        if n['kind'] in {'quantity', 'claim'}:
            require(not children and isinstance(n['reference'], str), 'Observation node shape')
            if n['kind'] == 'claim':
                claim = claims[n['reference']]
                require(claim['value'] is None or claim['dimension'] == 'outcome',
                        'Only null or outcome claims may be non-quantity leaves')
                if claim['dimension'] == 'outcome':
                    _reason(reasons, 'temporal', 'excluded', 'target_leakage', nid)
                else:
                    _reason(reasons, 'derivation', 'blocked', 'missing_observation', nid)
                observations.append({'node_id': nid, 'claim': claim, 'quantity': None})
            else:
                q = quantities[n['reference']]
                qside = {'US': 'US', 'CS': 'Confederate'}[entities[q['entity_id']]['side']]
                require(qside == c['side'], 'Cross-side quantity')
                claim = claims[q['claim_id']]
                citations = claim['citations'] + q['estimation_citations']
                document_dates = [{'citation': ct, 'document_date': source_document_date(
                    sources[ct['source_id']], ct.get('section')),
                    'publication_date': sources[ct['source_id']].get('publication_date'),
                    'retrieved_at': sources[ct['source_id']].get('retrieved_at')}
                    for ct in citations]
                representations = {}
                for ct in citations + m['citations']:
                    source = sources[ct['source_id']]
                    image = sources.get(source.get('facsimile_source_id'))
                    representations[source['id']] = {
                        'metadata_sha256': source_metadata_digest(source), 'raw_sha256': source['sha256'],
                        'same_document_key': image['sha256'] if image else source['sha256'],
                        'independence_group': source['independence_group'],
                        'independence_established': False}
                observations.append({'node_id': nid, 'claim': claim, 'quantity': q,
                                     'document_dates': document_dates,
                                     'source_representations': representations,
                                     'historical_knowledge_at': None})
                value = [q['lower'], q['upper']]
                if (q['basis'] in {'reported_engaged', 'reported_reinforcements'}
                        or claim['phase'] == 'post_outcome'):
                    _reason(reasons, 'temporal', 'excluded', 'participation_or_post_outcome_observation', nid)
                # Calendar inequalities are conservative: a same-day date does
                # not establish order relative to contact; a later day is later.
                if (q['period']['start'] and boundary['date']
                        and q['period']['start'] > boundary['date']):
                    _reason(reasons, 'temporal', 'excluded', 'observed_state_after_boundary', nid)
                elif (q['period']['end'] and boundary['date']
                      and q['period']['end'] > boundary['date']):
                    _reason(reasons, 'temporal', 'blocked', 'state_interval_crosses_boundary', nid)
                if q['period']['start'] is None and not m['citations']:
                    _reason(reasons, 'temporal', 'blocked', 'state_time_unestablished', nid)
                if q['estimation_status'] == 'unknown':
                    _reason(reasons, 'uncertainty', 'blocked', 'estimation_provenance_unknown', nid)
        else:
            require(n['reference'] is None, 'Transform cannot override an observation')
            require((n['kind'] == 'identity' and len(children) == 1)
                    or (n['kind'] == 'sum' and len(children) >= 2)
                    or (n['kind'] == 'subtract' and len(children) == 2), 'Transform arity')
            if any(ch[1] is None for ch in children):
                _reason(reasons, 'overlap', 'blocked', 'dependency_membership_unknown', nid)
            else:
                sets = [set(ch[1]) for ch in children]
                if n['kind'] == 'sum':
                    if sum(map(len, sets)) != len(set.union(*sets)):
                        _reason(reasons, 'overlap', 'excluded', 'overlapping_sum', nid)
                    expected = set.union(*sets)
                elif n['kind'] == 'subtract':
                    if not sets[1] <= sets[0]:
                        _reason(reasons, 'overlap', 'excluded', 'subtraction_not_nested', nid)
                    expected = sets[0] - sets[1]
                else:
                    expected = sets[0]
                if members is not None and set(members) != expected:
                    _reason(reasons, 'overlap', 'invalid', 'transform_membership_mismatch', nid)
            if all(ch[0] is not None for ch in children):
                bounds = [ch[0] for ch in children]
                if n['kind'] == 'sum':
                    value = [sum(b[k] for b in bounds) for k in (0, 1)]
                elif n['kind'] == 'subtract':
                    value = [bounds[0][0] - bounds[1][1], bounds[0][1] - bounds[1][0]]
                else:
                    value = bounds[0]
                if value[0] < 0:
                    _reason(reasons, 'derivation', 'blocked', 'subtraction_bounds_negative', nid)
        active.remove(nid); visited.add(nid)
        values[nid] = (value, members)
        return values[nid]

    value, members = visit(c['root_node'])
    require(visited == set(nodes), 'Unreachable nodes are not allowed')
    target = boundary['members_by_side'][c['side']]
    if target is not None and members is not None and set(target) != set(members):
        _reason(reasons, 'population', 'blocked', 'incomplete_target_population')
    if value is None:
        _reason(reasons, 'derivation', 'blocked', 'missing_value')
    elif value[0] <= 0:
        _reason(reasons, 'derivation', 'blocked', 'nonpositive_strength')
    status = _status(reasons)
    return {'candidate_id': c['id'], 'candidate_sha256': canonical_hash(c),
            'battle_id': c['battle_id'], 'side': c['side'], 'boundary_id': c['boundary_id'],
            'status': status, 'reasons': reasons,
            'gates': {'binding_schema': 'pass', 'applicability': status,
                      'evidence_use_review': 'not_supplied', 'release': 'not_requested'},
            'preview_bounds': value if status == 'eligible_candidate' else None,
            'observations': observations, 'source_choices': source_choices}


def _scenarios(scenarios, frame, decisions):
    by_id = indexed(scenarios, 'scenarios')
    require(bool(by_id), 'At least one explicit scenario is required')
    rows, issues, selected = {}, [], set()
    for sid, scenario in sorted(by_id.items()):
        shape(scenario, 'id assignments rationale', 'scenario')
        text(scenario['rationale'], 'Scenario rationale')
        require(isinstance(scenario['assignments'], dict)
                and set(scenario['assignments']) == set(frame), 'Scenario must retain the whole frame')
        result, choices = [], {}
        for battle, assignment in sorted(scenario['assignments'].items()):
            require(isinstance(assignment, dict) and set(assignment) == set(SIDES), 'Scenario sides')
            pair = {}
            for side in SIDES:
                cid = assignment[side]
                if cid is None:
                    continue
                require(isinstance(cid, str) and cid in decisions, 'Unknown scenario candidate')
                d = decisions[cid]
                require(d['battle_id'] == battle and d['side'] == side, 'Scenario candidate scope')
                selected.add(cid)
                if d['status'] != 'eligible_candidate':
                    issues.append({'scenario_id': sid, 'candidate_id': cid, 'code': 'inapplicable_candidate'})
                    continue
                pair[side] = d
                for key, value in d['source_choices'].items():
                    if key in choices and choices[key] != value:
                        issues.append({'scenario_id': sid, 'candidate_id': cid, 'code': 'incompatible_joint_choices'})
                    choices[key] = value
            if len(pair) == 2:
                if pair['US']['boundary_id'] != pair['Confederate']['boundary_id']:
                    issues.append({'scenario_id': sid, 'candidate_id': None, 'code': 'unequal_side_boundaries'})
                elif not frame[battle]['operation'] and frame[battle]['outcome'] != 'Inconclusive':
                    result.append({'battle_id': battle, 'campaign': frame[battle]['campaign'],
                                   'profile_id': PROFILE, 'boundary_id': pair['US']['boundary_id'],
                                   'strength_bounds': {s: pair[s]['preview_bounds'] for s in SIDES}})
        rows[sid] = result
    applicable = {k for k, d in decisions.items() if d['status'] == 'eligible_candidate'}
    for cid in sorted(applicable - selected):
        issues.append({'scenario_id': None, 'candidate_id': cid, 'code': 'applicable_alternative_not_represented'})
    # A compromised scenario emits no preview row, even for its unaffected battles.
    invalid_scenarios = {i['scenario_id'] for i in issues if i['scenario_id'] is not None}
    for sid in invalid_scenarios:
        rows[sid] = []
    return rows, issues, selected


def _coverage(frame, dossiers, decisions, rows):
    ledger = []
    for battle, record in sorted(frame.items()):
        sides = {}
        for side in SIDES:
            ds = [d for d in decisions.values() if d['battle_id'] == battle and d['side'] == side]
            sides[side] = {'candidate_ids': [d['candidate_id'] for d in ds],
                           'status_counts': dict(sorted(Counter(d['status'] for d in ds).items())),
                           'reasons': sorted({r['code'] for d in ds for r in d['reasons']}),
                           'evidence_use_reviewed': sum(d['status'] == 'admitted' for d in ds)}
        ledger.append({'battle_id': battle, 'campaign': record['campaign'],
                       'dossier_available': battle in dossiers,
                       'baseline_eligible': record['baseline_eligible'],
                       'outcome_eligible': record['outcome'] != 'Inconclusive',
                       'engagement_grain': not record['operation'], 'sides': sides,
                       'complete_in_scenarios': [s for s, rs in rows.items()
                                                 if any(v['battle_id'] == battle for v in rs)]})
    complete = {v['battle_id'] for rs in rows.values() for v in rs}
    baseline = {b for b, r in frame.items() if r['baseline_eligible']}
    return {'frame_engagements': len(frame), 'frame_campaigns': len({r['campaign'] for r in frame.values()}),
            'dossiers_available': len(dossiers),
            'engagements_with_candidates': len({d['battle_id'] for d in decisions.values()}),
            'candidate_observations': len(decisions),
            'status_counts': dict(sorted(Counter(d['status'] for d in decisions.values()).items())),
            'complete_candidate_engagements': len(complete),
            'baseline_eligible_engagements': len(baseline),
            'paired_common_ids': sorted(complete & baseline),
            'newly_covered_ids': sorted(complete - baseline),
            'scenario_rows': {s: len(rs) for s, rs in rows.items()}, 'ledger': ledger}


def validate_proposal(root, path=DEFAULT_PROPOSAL, *, allow_test_only=False):
    """Return complete coverage and diagnostic previews; never write model inputs."""
    root = Path(root)
    ppath = safe_path(root, str(path))
    proposal = load_json(ppath)
    shape(proposal, 'schema_version kind test_only profile snapshot boundaries candidates scenarios', 'proposal')
    require(type(proposal['schema_version']) is int and proposal['schema_version'] == 1
            and proposal['kind'] == 'admission_proposal', 'Proposal kind/version')
    require(type(proposal['test_only']) is bool, 'Proposal test marker')
    require(allow_test_only or not proposal['test_only'], 'Test-only proposal rejected')
    snapshot, frame, sources, dossiers = _snapshot(root, proposal['snapshot'], allow_test_only)
    require(snapshot['test_only'] == proposal['test_only'], 'Test marker mismatch')
    supported = _profile(root, proposal['profile'])
    for source in sources.values():
        retrieved = source.get('retrieved_at')
        if retrieved is not None:
            iso(retrieved, 'Source retrieval date')
            require(retrieved <= proposal['profile']['evaluation_plan']['research_cutoff'],
                    'Source snapshot exceeds research cutoff')
    boundaries = indexed(proposal['boundaries'], 'boundaries')
    for b in boundaries.values():
        _boundary(root, b, sources, frame, proposal['profile'])
    candidates = indexed(proposal['candidates'], 'candidates')
    decisions = {}
    for cid, candidate in sorted(candidates.items()):
        # Frame/side identity is required to place even invalid candidates in the
        # ledger. An unplaceable object invalidates the whole proposal.
        require(candidate.get('battle_id') in frame and candidate.get('side') in SIDES,
                'Unplaceable candidate')
        evaluated_reasons = []
        try:
            decisions[cid] = _candidate(root, candidate, proposal['profile'], supported,
                                       boundaries[candidate['boundary_id']], sources, dossiers, evaluated_reasons)
        except (ValueError, KeyError, TypeError, OSError) as exc:
            _reason(evaluated_reasons, 'binding_schema', 'invalid', str(exc))
            decisions[cid] = {'candidate_id': cid, 'candidate_sha256': canonical_hash(candidate),
                'battle_id': candidate['battle_id'], 'side': candidate['side'],
                'boundary_id': candidate.get('boundary_id'), 'status': 'invalid',
                'reasons': evaluated_reasons,
                'gates': {'binding_schema': 'fail', 'applicability': 'incomplete',
                          'evidence_use_review': 'not_supplied', 'release': 'not_requested'},
                'preview_bounds': None, 'observations': [], 'source_choices': {}}
    rows, issues, selected = _scenarios(proposal['scenarios'], frame, decisions)
    return {'schema_version': 1, 'kind': 'admission_proposal_check', 'test_only': proposal['test_only'],
            'validator_sha256': implementation_hashes(),
            'proposal_sha256': digest(ppath), 'snapshot_sha256': proposal['snapshot']['sha256'],
            'profile_sha256': canonical_hash(proposal['profile']),
            'boundaries_sha256': canonical_hash(proposal['boundaries']),
            'candidate_hashes': {c: d['candidate_sha256'] for c, d in decisions.items()},
            'status': 'invalid' if any(d['status'] == 'invalid' for d in decisions.values()) else 'checked',
            'decisions': list(decisions.values()), 'scenario_issues': issues,
            'selected_candidate_ids': sorted(selected), 'preview_rows_by_scenario': rows,
            'coverage': _coverage(frame, dossiers, decisions, rows),
            'target_channel': {b: r['outcome'] for b, r in sorted(frame.items())},
            'emitted_rows': [], 'promoted_rows': 0,
            'limits': ['Semantic mappings require evidence-use review; matching a quote does not establish entailment.',
                       'Preview rows are not released model inputs; no fitting or promotion occurs.']}


def review_bindings(report):
    return {k: report[k] for k in ('proposal_sha256', 'snapshot_sha256', 'profile_sha256',
                                  'boundaries_sha256', 'candidate_hashes')}


def audit_release(root, path, *, allow_test_only=False):
    """Verify a separately reviewed manifest without installing or fitting it.

    Test-only stubs are reachable through an explicit Python test harness only;
    normal CLI/build calls never enable them. Artifacts are not signatures.
    """
    root = Path(root)
    manifest = load_json(safe_path(root, str(path)))
    shape(manifest, 'schema_version kind test_only proposal implementation_sha256 review reconciliation '
          'rows_sha256 coverage_sha256', 'release manifest')
    require(type(manifest['schema_version']) is int and manifest['schema_version'] == 1
            and manifest['kind'] == 'admission_release_audit', 'Release kind/version')
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
    require(reconciliation['proposal_sha256'] == report['proposal_sha256']
            and reconciliation['review_sha256'] == manifest['review']['sha256'], 'Reconciliation binding')
    require(reconciliation['kind'] == 'primary_evidence_use_reconciliation', 'Reconciliation kind')
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
    require(review['verdict'] in {'accept', 'corrections_needed'}, 'Review verdict')
    require(reconciliation['decision'] in {'accept', 'corrections_needed'}, 'Primary decision')
    require(isinstance(review['findings'], list) and isinstance(reconciliation['unresolved_findings'], list),
            'Review findings required')
    accepted = (review['kind'] == 'separate_evidence_use_review' and set(review['scope']) == SCOPE
                and review['verdict'] == reconciliation['decision'] == 'accept'
                and not review['findings'] and not reconciliation['unresolved_findings'])
    require(report['status'] != 'invalid', 'Invalid proposal cannot be released')
    require(not report['scenario_issues'], 'Unresolved scenario coverage or compatibility')
    require(canonical_hash(report['preview_rows_by_scenario']) == manifest['rows_sha256'], 'Released rows mismatch')
    require(canonical_hash(report['coverage']) == manifest['coverage_sha256'], 'Coverage ledger mismatch')
    # The manifest binds the complete proposal-stage ledger and preview rows.
    # Review disposition is separately bound; release status does not rewrite it.
    for d in report['decisions']:
        if d['status'] == 'eligible_candidate':
            d['gates']['evidence_use_review'] = 'pass' if accepted else 'fail'
            d['gates']['release'] = 'verified' if accepted else 'blocked'
            d['status'] = 'admitted' if accepted and d['candidate_id'] in report['selected_candidate_ids'] else 'blocked'
            if not accepted:
                _reason(d['reasons'], 'review', 'blocked', 'evidence_use_review_not_accepted')
    report.update(kind='admission_release_check', release_status='verified' if accepted else 'blocked',
                  audited_rows_by_scenario=report['preview_rows_by_scenario'] if accepted else {},
                  review_sha256=manifest['review']['sha256'],
                  release_sha256=digest(safe_path(root, str(path))))
    # Coverage retains its explicitly named proposal-stage status counts.
    report['coverage_stage'] = 'proposal_before_review'
    report['release_admitted_candidates'] = sum(d['status'] == 'admitted' for d in report['decisions'])
    return report


def check(root, path=DEFAULT_PROPOSAL):
    """CLI entry: test-only artifacts are always rejected."""
    document = load_json(safe_path(root, str(path)))
    require(isinstance(document, dict), 'Admission document must be an object')
    kind = document.get('kind')
    if kind == 'admission_release_audit':
        return audit_release(root, path)
    return validate_proposal(root, path)
