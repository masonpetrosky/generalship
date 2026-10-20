"""Bounded, source-specific ledger design examples. Never admit rows or fit outcomes."""

from collections import Counter, defaultdict
import math
from pathlib import Path

from .evidence import citation_text
from .sources import (digest, read_json, safe_path, source_document_date,
                      source_metadata_digest, validate_source_metadata, write_json)

BASE = 'data/napoleonic/ledger-design-v1'
SCOPE = BASE + '/scope.json'
EXAMPLES = BASE + '/examples.json'
SNAPSHOT = BASE + '/source-snapshot.json'
VERIFICATION = BASE + '/verification.json'
DESIGN = 'docs/napoleonic-ledgers-v1.md'
REPORT = 'artifacts/napoleonic-ledger-design-v1'
FRAME = 'data/napoleonic/frame-v1.json'
COHORT = 'data/napoleonic/cohort-v1.json'
EVALUATION = 'data/napoleonic/methods-v1/evaluation.json'
CODE = ('generalship/napoleonic_ledger_design.py', 'generalship/cli.py',
        'generalship/sources.py', 'generalship/evidence.py',
        'tests/test_napoleonic_ledger_design.py', 'tests/test_workflow.py')
CODE_ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError('Napoleonic ledger design: ' + message)


def shape(value, keys, where):
    require(isinstance(value, dict) and set(value) == set(keys.split()), 'invalid fields: ' + where)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def indexed(rows, key='id'):
    require(isinstance(rows, list) and all(isinstance(r, dict) and nonempty(r.get(key)) for r in rows),
            'expected records with nonempty IDs')
    result = {r[key]: r for r in rows}
    require(len(result) == len(rows), 'duplicate record ID')
    return result


def selected_group(entries, development_ids):
    """Selection reads only membership, group and start year, never outcomes or strengths."""
    groups = defaultdict(list)
    for entry in entries:
        if entry['id'] in development_ids:
            groups[entry['campaign_group']].append(entry)
    require(bool(groups), 'empty development partition')
    key = min(groups, key=lambda k: (len(groups[k]), min(e['start_year'] for e in groups[k]), k))
    return key, sorted(e['id'] for e in groups[key])


def validate_amount(amount):
    shape(amount, 'kind lower upper lower_inclusive upper_inclusive', 'amount')
    kind, lo, hi = amount['kind'], amount['lower'], amount['upper']
    require(kind in {'point', 'approximate', 'range', 'lower_bound', 'upper_bound', 'unknown'}, 'amount kind')
    for endpoint, flag in [('lower', 'lower_inclusive'), ('upper', 'upper_inclusive')]:
        value = amount[endpoint]
        require(value is None or (type(value) in (int, float) and math.isfinite(value) and value >= 0),
                'nonnegative finite quantity required')
        require((value is None and amount[flag] is None) or (value is not None and type(amount[flag]) is bool),
                'endpoint inclusion must match its bound')
    require({'point': lo is not None and hi == lo,
             'approximate': lo is not None and hi == lo,
             'range': lo is not None and hi is not None and lo < hi,
             'lower_bound': lo is not None and hi is None,
             'upper_bound': lo is None and hi is not None,
             'unknown': lo is None and hi is None}[kind], 'bounds do not match amount kind')
    if kind in {'point', 'approximate', 'range'}:
        require(amount['lower_inclusive'] is True and amount['upper_inclusive'] is True,
                'closed printed point/range required; no invented precision')


def decision(excluded, blocked):
    return {'status': 'excluded' if excluded else 'blocked' if blocked else 'eligible_candidate',
            'excluded_reasons': sorted(set(excluded)), 'blocked_reasons': sorted(set(blocked))}


def strength_decision(row, boundary):
    """Technical design applicability only; no historical approval or emitted value."""
    validate_amount(row['amount'])
    excluded, blocked = [], []
    if boundary is None:
        blocked.append('opening_boundary_unestablished')
    if row['boundary_relation'] in {'after', 'crosses'}:
        excluded.append('post_boundary_state')
    elif row['boundary_relation'] == 'unestablished':
        blocked.append('state_relation_unestablished')
    if row['unit'] != 'people':
        excluded.append('not_personnel')
    if row['basis'] in {'inhabitants', 'prisoners', 'reported_engaged'}:
        excluded.append('wrong_population_basis')
    elif row['basis'] in {'infantry', 'cavalry', 'rank_and_file'}:
        excluded.append('partial_personnel_basis')
    elif row['basis'] == 'unspecified_personnel':
        blocked.append('personnel_basis_unestablished')
    if row['population'] in {'component', 'wider_formation', 'outside_entry', 'town_population'}:
        excluded.append('wrong_target_scope')
    elif row['population'] == 'unresolved':
        blocked.append('target_membership_unestablished')
    if row['derivation'] in {'illustrative', 'post_state'}:
        excluded.append('illustrative_or_post_state_derivation')
    elif row['derivation'] == 'unknown':
        blocked.append('derivation_unestablished')
    if row['amount']['kind'] in {'lower_bound', 'upper_bound'}:
        blocked.append('one_sided_bound')
    elif row['amount']['kind'] == 'unknown':
        blocked.append('quantity_unknown')
    elif row['amount']['lower'] == row['amount']['upper'] == 0:
        excluded.append('nonpositive_personnel')
    return decision(excluded, blocked)


def command_decision(row, boundary):
    excluded, blocked = [], []
    if boundary is None:
        blocked.append('opening_boundary_unestablished')
    if row['boundary_relation'] in {'after', 'crosses'}:
        excluded.append('post_boundary_role')
    elif row['boundary_relation'] == 'unestablished':
        blocked.append('role_time_unestablished')
    if row['population'] == 'outside_entry':
        excluded.append('outside_entry_role')
    if row['resolved_person_id'] is None:
        blocked.append('person_identity_unresolved')
    if row['authority_at_boundary'] != 'established':
        blocked.append('target_authority_unestablished')
    return decision(excluded, blocked)


def sum_decision(proposal, records, boundary):
    """Direct sum probes only. Components need not individually be whole-target totals."""
    require(len(proposal['input_ids']) >= 2 and len(set(proposal['input_ids'])) == len(proposal['input_ids']),
            'sum needs distinct direct observation inputs')
    require(all(key in records for key in proposal['input_ids']), 'sum input is not a strength observation')
    inputs = [records[key] for key in proposal['input_ids']]
    require(all((r['battle_id'], r['side']) == (proposal['battle_id'], proposal['side']) for r in inputs),
            'sum crosses engagement or side')
    for row in inputs:
        validate_amount(row['amount'])
    exact = all(r['amount']['kind'] == 'point' for r in inputs)
    result = sum(r['amount']['lower'] for r in inputs) if exact else None
    require((result is None and proposal['arithmetic_sum'] is None)
            or (type(proposal['arithmetic_sum']) in (int, float) and proposal['arithmetic_sum'] == result),
            'incorrect or invented arithmetic sum')
    excluded, blocked = [], []
    if boundary is None:
        blocked.append('opening_boundary_unestablished')
    if any(r['unit'] != 'people' or r['basis'] in {'inhabitants', 'prisoners', 'reported_engaged'} for r in inputs):
        excluded.append('incompatible_input_population')
    if any(r['population'] in {'outside_entry', 'wider_formation', 'town_population'} for r in inputs):
        excluded.append('incompatible_input_scope')
    if any(r['basis'] == 'rank_and_file' for r in inputs):
        excluded.append('partial_input_basis')
    if any(r['boundary_relation'] in {'after', 'crosses'} or r['derivation'] in {'post_state', 'illustrative'} for r in inputs):
        excluded.append('incompatible_input_state_or_derivation')
    if any(r['boundary_relation'] == 'unestablished' for r in inputs):
        blocked.append('input_state_relation_unestablished')
    if any(r['derivation'] == 'unknown' for r in inputs):
        blocked.append('input_derivation_unestablished')
    if not exact:
        blocked.append('nonpoint_inputs')
    if proposal['disjoint_membership'] == 'overlap':
        excluded.append('overlapping_inputs')
    elif proposal['disjoint_membership'] != 'established':
        blocked.append('disjoint_membership_unestablished')
    if proposal['same_state_time'] == 'incompatible':
        excluded.append('incompatible_state_times')
    elif proposal['same_state_time'] != 'established':
        blocked.append('common_state_time_unestablished')
    if proposal['complete_target'] == 'incomplete':
        excluded.append('incomplete_target_population')
    elif proposal['complete_target'] != 'complete':
        blocked.append('complete_target_unestablished')
    return {'arithmetic_sum': result, **decision(excluded, blocked)}


def validate(root, bundle=None):
    """Validate a new design proposal without claiming verification of altered content."""
    scope = read_json(root / SCOPE)
    require(scope.get('kind') == 'napoleonic_ledger_design_scope' and scope.get('version') == 1
            and scope.get('status') == 'design_only', 'scope identity/status')
    required = {FRAME, COHORT, EVALUATION} | {f'data/napoleonic/evidence/{b}.json' for b in scope['battle_ids']}
    require(set(scope['bindings']) == required, 'scope bindings must cover frame, cohort, partition and dossiers')
    for path, sha in scope['bindings'].items():
        require(digest(safe_path(root, path)) == sha, 'changed bound input: ' + path)
    frame, cohort, partition = (read_json(root / p) for p in (FRAME, COHORT, EVALUATION))
    development, final = set(partition['development']), set(partition['reserved_final'])
    require(not development.intersection(final) and development | final == set(cohort['battle_ids']),
            'evaluation partition does not cover unchanged cohort')
    group, battles = selected_group(frame['entries'], development)
    require((scope['selected_group'], scope['battle_ids']) == (group, battles), 'selection rule changed')
    require((len(battles), 2 * len(battles), len(development), len(final)) ==
            (scope['engagement_denominator'], scope['side_denominator'], scope['development_engagements'], scope['reserved_final_engagements']),
            'incorrect scope denominators')
    require(set(scope['authorization']) == {'owner_message', 'accepted_recommendation', 'new_source_fetching',
            'historical_outcome_fit', 'synthetic_job', 'feature_admission', 'calibration_scoring', 'separate_review'}
            and all(scope['authorization'][k] is False for k in scope['authorization']
                    if k not in {'owner_message', 'accepted_recommendation'}), 'design authorization exceeded')
    require(scope['historical_blinding'] is False, 'historical blinding must not be claimed')
    bundle = read_json(root / EXAMPLES) if bundle is None else bundle
    shape(bundle, 'kind version status scope_sha256 design_sha256 source_snapshot strength_records command_records side_records claim_index discrepancies sum_proposals emitted_rows historical_outcomes_fitted calibration', 'bundle')
    require(bundle['kind'] == 'napoleonic_ledger_design_examples' and bundle['version'] == 1
            and bundle['status'] == 'design_only', 'bundle identity/status')
    require(bundle['emitted_rows'] == [] and bundle['historical_outcomes_fitted'] is False
            and bundle['calibration'] == 'prepared_unscored', 'design cannot promote, fit or score calibration')
    require(bundle['scope_sha256'] == digest(root / SCOPE) and bundle['design_sha256'] == digest(root / DESIGN),
            'scope/design hash mismatch')
    require(bundle['source_snapshot'] == {'path': SNAPSHOT, 'sha256': digest(root / SNAPSHOT)}, 'source snapshot binding')
    snapshot = read_json(root / SNAPSHOT)
    require(snapshot['kind'] == 'napoleonic_ledger_design_source_snapshot' and snapshot['version'] == 1, 'snapshot identity')
    sources = indexed(snapshot['sources'])
    for source in sources.values():
        require(digest(safe_path(root, source['path'])) == source['sha256'], 'source raw checksum: ' + source['id'])
        if source.get('parent_source_id'):
            require(source['parent_source_id'] in sources, 'source parent absent')
            if 'parent_sha256' in source:
                require(source['parent_sha256'] == sources[source['parent_source_id']]['sha256'], 'source parent checksum')
    validate_source_metadata(root, sources)
    entries = {e['id']: e for e in frame['entries']}
    dossiers = {b: read_json(root / f'data/napoleonic/evidence/{b}.json') for b in battles}
    claims = {(b, c['id']): c for b, d in dossiers.items() for c in d['claims']
              if c['dimension'] in {'strength', 'responsibility'}}
    strengths, commands = indexed(bundle['strength_records']), indexed(bundle['command_records'])
    require(not strengths.keys() & commands.keys(), 'observation IDs overlap')
    records = strengths | commands
    allowed_pairs = {(b, side) for b in battles for side in ('A', 'B')}
    claim_uses, images, passages, families = defaultdict(set), set(), set(), defaultdict(set)
    for key, row in records.items():
        require((row['battle_id'], row['side']) in allowed_pairs, 'observation outside selected sides')
        common = 'id battle_id side population state_description boundary_relation receipt_at note evidence'
        shape(row, common + (' amount printed_value unit basis source_role derivation' if key in strengths else
                            ' actor_label resolved_person_id role force_scope authority_at_boundary'), key)
        require(row['population'] in {'unresolved', 'whole_side', 'component', 'wider_formation', 'outside_entry', 'town_population'}, 'population code')
        require(row['boundary_relation'] in {'unestablished', 'before', 'at_boundary', 'after', 'crosses'}, 'boundary relation code')
        require(nonempty(row['state_description']) and row['receipt_at'] is None and isinstance(row['note'], str), 'state/receipt/note')
        require(isinstance(row['evidence'], list) and bool(row['evidence']), 'observation needs evidence')
        row_families = set()
        for ref in row['evidence']:
            shape(ref, 'claim_id citation_index citation metadata_sha256 raw_sha256 document_date facsimile_source_id', 'evidence')
            claim = claims.get((row['battle_id'], ref['claim_id']))
            index = ref['citation_index']
            require(claim is not None and type(index) is int and 0 <= index < len(claim['citations']), 'claim/citation reference')
            citation = ref['citation']
            require(citation == claim['citations'][index], 'citation differs from bound dossier')
            source = sources.get(citation['source_id'])
            require(source is not None and ref['metadata_sha256'] == source_metadata_digest(source)
                    and ref['raw_sha256'] == source['sha256'], 'source metadata/raw binding')
            require(nonempty(citation['quote']) and citation['quote'] in citation_text(root, sources, citation), 'quote not in cited section')
            require(ref['document_date'] == source_document_date(source, citation.get('section')), 'section document date changed')
            image_id = source.get('facsimile_source_id')
            if source['id'] == 'bodart-1908-transcription-v1':
                image_id = f"bodart-1908-{citation['section']}-image-v1"
            require(ref['facsimile_source_id'] == image_id and image_id in sources
                    and sources[image_id]['format'] in {'jpg', 'jpeg', 'png'}, 'facsimile binding')
            images.add(image_id)
            passages.add((source['id'], citation.get('section'), citation['quote']))
            row_families.add(source['independence_group'])
            claim_uses[row['battle_id'], ref['claim_id']].add(key)
        require(len(row_families) == 1, 'observation mixes source families')
        families[row['battle_id']].update(row_families)
        if key in strengths:
            validate_amount(row['amount'])
            require(row['unit'] in {'people', 'guns', 'horses', 'units'}, 'quantity unit')
            require(row['basis'] in {'all_arms', 'unspecified_personnel', 'infantry', 'cavalry', 'rank_and_file',
                    'reported_engaged', 'prisoners', 'inhabitants', 'guns'}, 'quantity basis')
            require(row['unit'] == ('guns' if row['basis'] == 'guns' else 'people'), 'unit/basis mismatch')
            require(row['source_role'] in {'compiled_total', 'own_retrospective', 'retrospective_history',
                    'opponent_estimate', 'hearsay_estimate'}, 'source role')
            require(row['derivation'] in {'direct_reported', 'unknown', 'illustrative', 'post_state'}, 'derivation code')
            quotes = ' '.join(' '.join(ref['citation']['quote'].split()) for ref in row['evidence'])
            require((row['amount']['kind'] == 'unknown' and row['printed_value'] is None)
                    or (nonempty(row['printed_value']) and row['printed_value'] in quotes), 'printed value absent from cited passage')
        else:
            require(row['resolved_person_id'] is None and row['authority_at_boundary'] == 'unestablished',
                    'worked design does not resolve identities/authority')
            require(all(nonempty(row[field]) for field in ('actor_label', 'role', 'force_scope')), 'command role fields')
            require(row['role'] in {'printed_commander', 'operational_order_recipient', 'superior_directive',
                    'formation_command', 'local_direction', 'expedition_decision', 'local_negotiation',
                    'siege_troop_command', 'superior_visit', 'siege_direction', 'superior_deployment',
                    'garrison_governor', 'acting_governor', 'investment_direction', 'column_leader',
                    'assault_direction', 'garrison_command'}, 'command role code')
    require(all(len(fs) <= 3 for fs in families.values()), 'worked entry exceeds source-family ceiling')
    indexed_claims = {(c['battle_id'], c['claim_id']): c for c in bundle['claim_index']}
    require(len(indexed_claims) == len(bundle['claim_index']) and indexed_claims.keys() == claims.keys(), 'claim index omits or duplicates a relevant claim')
    for pair, row in indexed_claims.items():
        shape(row, 'battle_id claim_id dimension sha256 observation_ids disposition remaining_scope', 'claim index')
        require(row['sha256'] == source_metadata_digest(claims[pair]) and row['dimension'] == claims[pair]['dimension'], 'claim binding')
        require(len(set(row['observation_ids'])) == len(row['observation_ids']) and set(row['observation_ids']) == claim_uses[pair], 'claim/observation accounting')
        require(row['disposition'] == ('worked_excerpts' if row['observation_ids'] else 'retained_in_dossier')
                and nonempty(row['remaining_scope']), 'unextracted claim scope missing')
    sides = {(r['battle_id'], r['side']): r for r in bundle['side_records']}
    require(len(sides) == len(bundle['side_records']) and sides.keys() == allowed_pairs, 'side coverage omitted or duplicated')
    side_report = []
    for (battle, side), row in sorted(sides.items()):
        shape(row, 'battle_id side frozen_start_date frozen_end_date opening_boundary army_id responsible_person_id selected_strength_id strength_ids command_ids unknowns', 'side record')
        require((row['frozen_start_date'], row['frozen_end_date']) == (entries[battle]['start_date'], entries[battle]['end_date']), 'frozen interval changed')
        require(all(row[k] is None for k in ('opening_boundary', 'army_id', 'responsible_person_id', 'selected_strength_id')), 'design side cannot select a boundary, identity or force')
        for field, pool in [('strength_ids', strengths), ('command_ids', commands)]:
            expected = {key for key, r in pool.items() if (r['battle_id'], r['side']) == (battle, side)}
            require(bool(expected) and len(set(row[field])) == len(row[field]) and set(row[field]) == expected, 'side observation accounting')
        require(isinstance(row['unknowns'], list) and bool(row['unknowns']) and all(nonempty(x) for x in row['unknowns']), 'explicit side unknowns required')
        side_report.append({'battle_id': battle, 'place': entries[battle]['place'], 'side': side,
                            'strength_observations': len(row['strength_ids']), 'command_observations': len(row['command_ids']),
                            'opening_strength': 'blocked', 'opening_responsibility': 'blocked',
                            'army_id': None, 'responsible_person_id': None})
    discrepancies = indexed(bundle['discrepancies'])
    covered = set()
    for row in discrepancies.values():
        shape(row, 'id battle_id side kind observation_ids resolution note', 'discrepancy')
        pair = row['battle_id'], row['side']
        require(pair in sides and row['resolution'] is None and nonempty(row['note']), 'unresolved discrepancy fields')
        require(len(row['observation_ids']) >= 2 and len(set(row['observation_ids'])) == len(row['observation_ids'])
                and all(key in records and (records[key]['battle_id'], records[key]['side']) == pair for key in row['observation_ids']), 'discrepancy references')
        require(row['kind'] in {'population_phase_or_value', 'authority_phase_or_identity'}, 'discrepancy kind')
        if row['kind'] == 'population_phase_or_value':
            require(pair not in covered and set(row['observation_ids']) == set(sides[pair]['strength_ids']), 'strength alternatives omitted/duplicated')
            covered.add(pair)
    require(covered == allowed_pairs, 'strength alternatives need a disposition for every side')
    strength_results = {key: strength_decision(row, sides[row['battle_id'], row['side']]['opening_boundary']) for key, row in strengths.items()}
    command_results = {key: command_decision(row, sides[row['battle_id'], row['side']]['opening_boundary']) for key, row in commands.items()}
    probes = {}
    for key, row in indexed(bundle['sum_proposals']).items():
        shape(row, 'id battle_id side input_ids arithmetic_sum disjoint_membership same_state_time complete_target note', 'sum proposal')
        require((row['battle_id'], row['side']) in sides and nonempty(row['note']), 'sum side/note')
        require(row['disjoint_membership'] in {'established', 'unestablished', 'overlap'}
                and row['same_state_time'] in {'established', 'unestablished', 'incompatible'}
                and row['complete_target'] in {'complete', 'unestablished', 'incomplete'}, 'sum mapping codes')
        probes[key] = sum_decision(row, strengths, sides[row['battle_id'], row['side']]['opening_boundary'])
    return {'kind': 'napoleonic_ledger_design_check', 'version': 1, 'status': 'valid_design_examples',
            'scope_group': group, 'engagements': len(battles), 'sides': len(sides), 'indexed_claims': len(claims),
            'strength_observations': len(strengths), 'command_observations': len(commands),
            'source_snapshot_entries': len(sources), 'distinct_cited_passages': len(passages), 'inspected_image_ids': sorted(images),
            'source_families_by_entry': {b: sorted(fs) for b, fs in sorted(families.items())},
            'strength_status_counts': dict(sorted(Counter(v['status'] for v in strength_results.values()).items())),
            'command_status_counts': dict(sorted(Counter(v['status'] for v in command_results.values()).items())),
            'side_coverage': side_report, 'strength_decisions': strength_results, 'command_decisions': command_results,
            'sum_proposals': probes, 'unknown_army_ids': len(sides), 'unresolved_opening_boundaries': len(sides),
            'complete_candidate_engagements': 0, 'emitted_model_rows': [], 'historical_outcomes_fitted': False,
            'calibration': 'prepared_unscored', 'development_engagements': len(development), 'reserved_final_engagements': len(final)}


def verification_bindings(root):
    inputs = {p: digest(root / p) for p in (SCOPE, EXAMPLES, SNAPSHOT, DESIGN)}
    inputs.update(read_json(root / SCOPE)['bindings'])
    return {'inputs': inputs, 'code': {p: digest(CODE_ROOT / p) for p in CODE}}


def check(root):
    report = validate(root)
    record = read_json(root / VERIFICATION)
    require(record.get('kind') == 'napoleonic_ledger_design_primary_verification' and record.get('version') == 1
            and record.get('verification') == 'primary-verified' and record.get('independent_review') is False
            and record.get('authorizes_feature_admission') is False and record.get('historical_outcomes_fitted') is False,
            'primary verification identity/scope')
    require(record['bindings'] == verification_bindings(root), 'primary verification has stale input/code bindings')
    require(record['inspected_image_ids'] == report['inspected_image_ids'], 'primary image inventory differs')
    return report


def report_text(report):
    strength_counts = ', '.join(f'{n} {status}' for status, n in report['strength_status_counts'].items())
    command_counts = ', '.join(f'{n} {status}' for status, n in report['command_status_counts'].items())
    lines = ['# Napoleonic ledger design v1: worked result', '',
             'Primary-verified design examples only. No Napoleonic historical outcome fitted; no feature admitted or model row emitted.', '',
             f"The deterministic scope is **{report['scope_group']}**: **{report['engagements']} engagements / {report['sides']} sides**.",
             f"The bundle indexes all **{report['indexed_claims']} strength/responsibility claims**, with **{report['strength_observations']} strength observations** and **{report['command_observations']} command-role observations**.",
             f"It binds {report['source_snapshot_entries']} source metadata entries, {report['distinct_cited_passages']} distinct cited passages and {len(report['inspected_image_ids'])} re-inspected page images.",
             'These are worked excerpts, not exhaustive atomic extraction, an independent review, an error-rate sample or a forecast of full-cohort admission yield.', '',
             '## Side coverage', '', '| Entry | Place | Side | Strength observations | Role observations | Opening strength | Opening responsibility |',
             '| --- | --- | --- | ---: | ---: | --- | --- |']
    for row in report['side_coverage']:
        lines.append(f"| {row['battle_id']} | {row['place']} | {row['side']} | {row['strength_observations']} | {row['command_observations']} | {row['opening_strength']} | {row['opening_responsibility']} |")
    lines += ['', f"**{report['unresolved_opening_boundaries']}/{report['sides']} opening boundaries remain unresolved; {report['unknown_army_ids']}/{report['sides']} army IDs remain null.** Responsible-person and strength selections are also null.",
              'The frozen intervals are preserved, including Amantea into 1807. No start date is substituted for a contact or appointment boundary.', '',
              '## Observation applicability', '',
              f'Strength observations: **{strength_counts}**. Command-role observations: **{command_counts}**.',
              'Reasons overlap. An excluded component can still be retained as evidence; components require their own compatible transformation before they can contribute to a whole target.',
              'All side-level opening mappings remain blocked. Technical applicability is not historical adjudication or a release approval.', '',
              '## Arithmetic probes', '', '| Probe | Arithmetic only | Opening applicability | Remaining evidence |', '| --- | ---: | --- | --- |']
    explanations = {
        'amantea-columns': 'Common state, disjoint membership, target coverage and derivation remain unestablished.',
        'gaeta-local-and-posts': 'Area/membership, target coverage and derivation remain unestablished.',
        'maida-missing-artillery-personnel': 'Artillery people are missing; the all-arms target is incomplete.'}
    for name, row in report['sum_proposals'].items():
        lines.append(f"| {name.replace('-', ' ')} | {row['arithmetic_sum']:,} | {row['status']} | {explanations.get(name, 'See the JSON report for all applicability reasons.')} |")
    lines += ['', 'These sums do not select any force. All lack an approved opening boundary. The [JSON report](napoleonic-ledger-design-v1.json) retains every gate reason.',
              'One-sided bounds remain one-sided, illustrative assumptions remain illustrative, and rank-and-file, actual participation, prisoners, inhabitants and guns keep their own bases.', '',
              '## Remaining gates', '',
              'Define contact, area, availability and relative ordering for the same four entries; retain unresolved mappings if the existing passages do not establish them. Then resolve person/authority and army-continuity mappings under a versioned contract.',
              f"The numerical reservation stays **{report['development_engagements']} development / {report['reserved_final_engagements']} final entries**. Calibration remains prepared and unscored. A historical fit still needs a complete design and exact owner run authorization.", '',
              '[Design](../docs/napoleonic-ledgers-v1.md), [worked observations and discrepancies](../data/napoleonic/ledger-design-v1/examples.json), [frozen metadata snapshot](../data/napoleonic/ledger-design-v1/source-snapshot.json), [primary verification](../data/napoleonic/ledger-design-v1/verification.json).', '']
    return '\n'.join(lines)


def write_artifacts(root, report=None):
    report = check(root) if report is None else report
    write_json(root / (REPORT + '.json'), report)
    (root / (REPORT + '.md')).write_text(report_text(report), encoding='utf-8')
    return [REPORT + '.json', REPORT + '.md']


def check_artifacts(root, report):
    require(read_json(root / (REPORT + '.json')) == report
            and (root / (REPORT + '.md')).read_text(encoding='utf-8') == report_text(report), 'generated report is stale')
