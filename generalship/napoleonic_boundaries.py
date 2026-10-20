"""Replay a bounded measurement specification; never admit inputs or fit outcomes."""

import argparse
from collections import Counter
import json
from pathlib import Path

from . import napoleonic_ledger_design as prior
from .evidence import citation_text
from .sources import (digest, read_json, safe_path, source_document_date,
                      source_metadata_digest, validate_source_metadata, write_json)

BASE = 'data/napoleonic/boundaries-v1'
SCOPE = BASE + '/scope.json'
RECORDS = BASE + '/records.json'
SNAPSHOT = BASE + '/source-snapshot.json'
VERIFICATION = BASE + '/verification.json'
DESIGN = 'docs/napoleonic-boundaries-v1.md'
REPORT = 'artifacts/napoleonic-boundaries-v1'
CODE = ('generalship/napoleonic_boundaries.py', 'tests/test_napoleonic_boundaries.py')
ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError('Napoleonic boundaries: ' + message)


def shape(value, fields, where):
    require(isinstance(value, dict) and set(value) == set(fields.split()), 'invalid fields: ' + where)


def texts(value):
    return isinstance(value, list) and bool(value) and all(prior.nonempty(x) for x in value)


def reaches(edges, start, end):
    """Strict source-specific partial order, not an inferred historical clock."""
    seen, todo = set(), [start]
    while todo:
        current = todo.pop()
        for row in edges:
            if row['before'] == current:
                if row['after'] == end:
                    return True
                if row['after'] not in seen:
                    seen.add(row['after'])
                    todo.append(row['after'])
    return False


def membership_decision(row):
    """Conditional component membership, never a selected personnel total."""
    if row['assignment'] == 'civilian_population':
        return 'excluded_population'
    if row['area'] == 'outside':
        return 'excluded_area'
    if row['timing'] == 'departure_after_anchor':
        return 'excluded_timing'
    if (row['timing'], row['area'], row['assignment']) == (
            'present_by_anchor', 'inside', 'combat_component'):
        return 'candidate_component'
    return 'unresolved'


def bindings(root):
    scope = read_json(root / SCOPE)
    inputs = {p: digest(safe_path(root, p)) for p in (SCOPE, RECORDS, SNAPSHOT, DESIGN)}
    inputs.update(scope['bindings'])
    return {'inputs': inputs, 'code': {p: digest(ROOT / p) for p in CODE}}


def validate(root, bundle=None):
    old_report = prior.check(root)  # replay the unchanged prior contract, not just its hash
    old_scope = read_json(root / prior.SCOPE)
    scope = read_json(root / SCOPE)
    require(scope.get('kind') == 'napoleonic_boundary_scope' and scope.get('version') == 1
            and scope.get('status') == 'design_only', 'scope identity/status')
    required = set(old_scope['bindings']) | {prior.SCOPE, prior.EXAMPLES, prior.SNAPSHOT,
                                           prior.VERIFICATION, prior.DESIGN}
    require(set(scope['bindings']) == required, 'incomplete frozen-input bindings')
    for path, sha in scope['bindings'].items():
        require(digest(safe_path(root, path)) == sha, 'changed bound input: ' + path)
    require(scope['battle_ids'] == old_scope['battle_ids'] and scope['selected_group'] == old_scope['selected_group']
            and scope['engagement_denominator'] == 4 and scope['side_denominator'] == 8,
            'scope must retain the same four entries/eight sides')
    require(scope['historical_blinding'] is False and scope['authorization'] == {
        'owner_message': 'Sounds good, go ahead',
        'accepted_recommendation': 'Specify contact, area, availability and relative ordering for the same four entries/eight sides using existing pinned evidence, retaining unresolved mappings.',
        'new_source_fetching': False, 'feature_admission': False, 'historical_outcome_fit': False,
        'synthetic_job': False, 'calibration_scoring': False, 'separate_review': False,
        'subagents': False}, 'authorization exceeded')
    bundle = read_json(root / RECORDS) if bundle is None else bundle
    shape(bundle, 'kind version status scope_sha256 design_sha256 source_snapshot passages events orderings scenarios membership_cases sides emitted_model_rows historical_outcomes_fitted calibration', 'records')
    require(bundle['kind'] == 'napoleonic_boundary_records' and bundle['version'] == 1
            and bundle['status'] == 'design_only', 'records identity/status')
    require(bundle['scope_sha256'] == digest(root / SCOPE) and bundle['design_sha256'] == digest(root / DESIGN)
            and bundle['source_snapshot'] == {'path': SNAPSHOT, 'sha256': digest(root / SNAPSHOT)}, 'records binding')
    require(bundle['emitted_model_rows'] == [] and bundle['historical_outcomes_fitted'] is False
            and bundle['calibration'] == 'prepared_unscored', 'design cannot promote, fit or score')
    snapshot = read_json(root / SNAPSHOT)
    require(snapshot['kind'] == 'napoleonic_boundary_source_snapshot' and snapshot['version'] == 1, 'snapshot identity')
    sources = prior.indexed(snapshot['sources'])
    for source in sources.values():
        require(digest(safe_path(root, source['path'])) == source['sha256'], 'source raw checksum')
    validate_source_metadata(root, sources)
    passages = prior.indexed(bundle['passages'])
    images, passage_families = set(), {}
    battles = set(scope['battle_ids'])
    for row in passages.values():
        shape(row, 'id battle_id citation raw_sha256 metadata_sha256 document_date facsimile_source_id facsimile_sha256 interpretation_en', 'passage')
        require(row['battle_id'] in battles and prior.nonempty(row['interpretation_en']), 'passage scope/interpretation')
        citation = row['citation']
        source = sources.get(citation.get('source_id'))
        require(source is not None and row['raw_sha256'] == source['sha256']
                and row['metadata_sha256'] == source_metadata_digest(source), 'passage source binding')
        require(prior.nonempty(citation.get('quote'))
                and citation['quote'] in citation_text(root, sources, citation), 'quote absent from cited section')
        require(row['document_date'] == source_document_date(source, citation.get('section')), 'section document date')
        facsimile = sources.get(row['facsimile_source_id'])
        require(facsimile is not None and facsimile['format'] in {'jpg', 'jpeg', 'png'}
                and row['facsimile_sha256'] == facsimile['sha256']
                and facsimile['parent_source_id'] == source.get('parent_source_id')
                and facsimile['independence_group'] == source['independence_group'], 'facsimile binding')
        if source.get('facsimile_source_id'):
            require(facsimile['id'] == source['facsimile_source_id'], 'transcript image differs')
        images.add(facsimile['id'])
        passage_families[row['id']] = source['independence_group']

    used = set()

    def refs(row):
        ids = row['evidence']
        require(texts(ids) and len(set(ids)) == len(ids)
                and all(k in passages and passages[k]['battle_id'] == row['battle_id'] for k in ids), 'evidence reference/scope')
        used.update(ids)
        return {passage_families[k] for k in ids}

    events = prior.indexed(bundle['events'])
    event_families = {}
    for row in events.values():
        shape(row, 'id battle_id kind date_label time_label assertion_en evidence', 'event')
        require(row['battle_id'] in battles and row['kind'] in {'hostile_contact', 'movement', 'investment', 'works', 'later_presence', 'assault'}, 'event scope/type')
        require(prior.nonempty(row['date_label']) and prior.nonempty(row['assertion_en'])
                and (row['time_label'] is None or prior.nonempty(row['time_label'])), 'event labels; no synthesized clock')
        event_families[row['id']] = refs(row)
    edges = list(prior.indexed(bundle['orderings']).values())
    for edge in edges:
        shape(edge, 'id battle_id before after basis note evidence', 'ordering')
        require(edge['before'] in events and edge['after'] in events and edge['before'] != edge['after']
                and all(events[edge[k]]['battle_id'] == edge['battle_id'] for k in ('before', 'after')), 'ordering reference/scope')
        families = refs(edge)
        require(len(families) == 1 and families <= event_families[edge['before']]
                and families <= event_families[edge['after']], 'ordering mixes source clocks')
        require(edge['basis'] in {'stated_sequence', 'narrative_sequence'} and prior.nonempty(edge['note']), 'ordering basis')
    require(not any(reaches(edges, event, event) for event in events), 'ordering cycle')
    scenarios = prior.indexed(bundle['scenarios'])
    for row in scenarios.values():
        shape(row, 'id battle_id label anchor_event_id contact_status area unknowns evidence', 'scenario')
        anchor = events.get(row['anchor_event_id'])
        require(anchor is not None and anchor['battle_id'] == row['battle_id'] and prior.nonempty(row['label']), 'scenario anchor')
        require(row['contact_status'] in {'source_relative_candidate', 'later_phase', 'noncontact_marker', 'unresolved_operation_link'}, 'contact status')
        if row['contact_status'] == 'source_relative_candidate':
            require(anchor['kind'] == 'hostile_contact', 'noncontact cannot become first contact')
        if row['contact_status'] == 'noncontact_marker':
            require(anchor['kind'] in {'movement', 'investment', 'works'}, 'noncontact marker type')
        shape(row['area'], 'inside outside unresolved', 'area')
        require(all(texts(v) for v in row['area'].values()) and texts(row['unknowns']), 'area limits/unknowns')
        refs(row)
    cases = prior.indexed(bundle['membership_cases'])
    decisions = {}
    for row in cases.values():
        shape(row, 'id battle_id side scenario_id label timing time_event_id area assignment decision note evidence', 'membership')
        scenario = scenarios.get(row['scenario_id'])
        event = events.get(row['time_event_id'])
        require(row['side'] in {'A', 'B'} and scenario is not None and event is not None
                and row['battle_id'] == scenario['battle_id'] == event['battle_id'], 'membership reference/scope')
        require(row['timing'] in {'present_by_anchor', 'departure_after_anchor', 'later_presence_only', 'unestablished'}
                and row['area'] in {'inside', 'outside', 'mixed', 'unestablished'}
                and row['assignment'] in {'combat_component', 'civilian_population', 'unestablished'}, 'membership codes')
        require(prior.nonempty(row['label']) and prior.nonempty(row['note']), 'membership rationale')
        anchor = scenario['anchor_event_id']
        families = refs(row)
        require(families & event_families[event['id']], 'membership event lacks a cited source family')
        common_families = families & event_families[anchor] & event_families[event['id']]
        paths = [[edge for edge in edges if passage_families[edge['evidence'][0]] == family]
                 for family in common_families]
        if row['timing'] == 'present_by_anchor':
            require(event['id'] == anchor, 'prior presence alone cannot establish availability at the anchor')
        if row['timing'] in {'departure_after_anchor', 'later_presence_only'}:
            require(any(reaches(path, anchor, event['id']) for path in paths), 'unsupported later ordering')
        if row['timing'] == 'departure_after_anchor':
            require(event['kind'] == 'movement', 'later observation is not proof of later departure/arrival')
        decisions[row['id']] = membership_decision(row)
        require(row['decision'] == decisions[row['id']], 'incorrect conditional membership decision')
    sides = {(r['battle_id'], r['side']): r for r in bundle['sides']}
    pairs = {(battle, side) for battle in battles for side in ('A', 'B')}
    require(len(sides) == len(bundle['sides']) and sides.keys() == pairs, 'side coverage omitted/duplicated')
    old_strengths = read_json(root / prior.EXAMPLES)['strength_records']
    for pair, row in sides.items():
        shape(row, 'battle_id side scenario_ids membership_ids prior_strength_ids selected_boundary selected_strength army_id responsible_person_id unknowns', 'side')
        require(all(row[k] is None for k in ('selected_boundary', 'selected_strength', 'army_id', 'responsible_person_id')), 'design cannot select model inputs')
        for field, expected in [
                ('scenario_ids', {k for k, v in scenarios.items() if v['battle_id'] == pair[0]}),
                ('membership_ids', {k for k, v in cases.items() if (v['battle_id'], v['side']) == pair}),
                ('prior_strength_ids', {v['id'] for v in old_strengths if (v['battle_id'], v['side']) == pair})]:
            require(texts(row[field]) and len(set(row[field])) == len(row[field]) and set(row[field]) == expected, 'side accounting: ' + field)
        require(texts(row['unknowns']), 'side unknowns required')
    require(used == passages.keys(), 'unused or unaccounted passage')
    families_by_entry = {battle: sorted({passage_families[k] for k, row in passages.items() if row['battle_id'] == battle}
                                      | set(old_report['source_families_by_entry'][battle])) for battle in sorted(battles)}
    require(all(len(v) <= 3 for v in families_by_entry.values()), 'source-family ceiling exceeded')
    return {'kind': 'napoleonic_boundary_check', 'version': 1, 'status': 'valid_specification',
            'engagements': len(battles), 'sides': len(sides), 'prior_strength_observations_indexed': len(old_strengths),
            'events': len(events), 'orderings': len(edges), 'scenarios': len(scenarios),
            'passages': len(passages), 'source_snapshot_entries': len(sources), 'inspected_image_ids': sorted(images),
            'source_families_by_entry': families_by_entry, 'membership_cases': len(cases),
            'membership_counts': dict(sorted(Counter(decisions.values()).items())), 'membership_decisions': decisions,
            'scenario_status_counts': dict(sorted(Counter(r['contact_status'] for r in scenarios.values()).items())),
            'side_coverage': [{'battle_id': b, 'side': s, 'membership_cases': len(sides[b, s]['membership_ids']),
                               'selected_boundary': None, 'selected_strength': None, 'army_id': None,
                               'responsible_person_id': None} for b, s in sorted(sides)],
            'unresolved_joint_opening_sides': len(sides), 'complete_candidate_engagements': 0,
            'emitted_model_rows': [], 'historical_outcomes_fitted': False, 'calibration': 'prepared_unscored',
            'development_engagements': old_report['development_engagements'],
            'reserved_final_engagements': old_report['reserved_final_engagements']}


def check(root):
    report = validate(root)
    record = read_json(root / VERIFICATION)
    require(record.get('kind') == 'napoleonic_boundary_primary_verification' and record.get('version') == 1
            and record.get('verification') == 'primary-verified' and record.get('independent_review') is False
            and record.get('authorizes_feature_admission') is False and record.get('historical_outcomes_fitted') is False,
            'primary verification identity/scope')
    require(record['bindings'] == bindings(root), 'stale primary verification bindings')
    require(record['inspected_image_ids'] == report['inspected_image_ids'], 'primary image inventory')
    report['status'] = 'primary-verified specification'
    return report


def report_text(report):
    lines = ['# Naples boundary/membership specification v1', '',
             'Primary-verified, using existing pinned evidence. Four engagements / eight sides; no force, commander or army selected and no model row emitted.', '',
             f"**{report['passages']} adopted passages on {len(report['inspected_image_ids'])} re-inspected images**, {report['events']} source-qualified events, {report['orderings']} before/after relations, {report['scenarios']} scenarios and {report['membership_cases']} membership cases.",
             f"All {report['prior_strength_observations_indexed']} prior strength observations remain indexed; their immutable v1 dispositions are unchanged.", '',
             '| Entry | What the passages distinguish | Remaining opening gap |', '| --- | --- | --- |',
             '| Campo Tenese | Reconnaissance displacement, outposts and main attack; Damas’s reported 2 pm is not the earlier contact clock. | Exact component positions and availability at the earliest local contact. |',
             '| Maida | Artillery fire precedes skirmish and main clash; tower guards, the 20th light company and Ross’s body are separate. | 4/5 July source conflict, rear columns, all-arms personnel basis and first-contact membership. |',
             '| Gaëta | Initial rifle fire, March battery construction, garrison fire and July battery opening are separate phases. | Initial contact/date/area link; July figures cannot become initial-force totals. |',
             '| Amantea | Earlier attempt, 18 December investment, later departures and formal siege phases remain distinct. | Investment is not proof of first fire; later-phase concurrency and garrison membership unresolved. |', '',
             '## Coverage', '', '| Entry | Side | Worked membership cases | Joint opening/force mapping |', '| --- | --- | ---: | --- |']
    for row in report['side_coverage']:
        lines.append(f"| {row['battle_id']} | {row['side']} | {row['membership_cases']} | unresolved |")
    lines += ['', f"**{report['unresolved_joint_opening_sides']}/8 joint opening mappings remain unresolved; zero complete candidate engagements.** All selected boundaries, strengths, people and army IDs remain null.",
              'Source-relative event anchors and a proposed spatial rule do not resolve a complete historical opening population.', '',
              '## Conditional membership', '', '| Decision | Cases |', '| --- | ---: |']
    for key, count in report['membership_counts'].items():
        lines.append(f"| {key} | {count} |")
    lines += ['', 'These are component/scenario decisions, not independent observations, force totals or a full-cohort yield estimate. Candidate components include troops at a narrated contact and Huard at the investment marker; the latter does not establish hostile contact.',
              'Nonparticipation never proves absence. Later presence alone never proves an arrival after first contact. The 20th light company and Ross’s later reported body are kept distinct.',
              'The Amantea 4,700 sum fails an 18 December investment scenario because two columns depart later; its applicability at a later formal attack remains unresolved.', '',
              '## Limits and stopping rule', '',
              'The checker verifies provenance, references, source-specific acyclic ordering, shared scenarios, coverage and declared membership rules. Historical entailment is primary-verified, not independently reviewed or adjudicated. Unknown ordering and spatial limits remain explicit.',
              f"Development/final reservation: **{report['development_engagements']}/{report['reserved_final_engagements']}**. Calibration remains prepared/unscored. Prior dossiers, source registry, raw inputs and numerical results are unchanged.",
              'Stop this boundary step here. Next: a bounded person/authority and army-continuity mapping for the same four entries before wider ledger extraction.', '',
              '[Design and worked interpretation](../docs/napoleonic-boundaries-v1.md), [source-bound records](../data/napoleonic/boundaries-v1/records.json), [source metadata snapshot](../data/napoleonic/boundaries-v1/source-snapshot.json), [primary verification](../data/napoleonic/boundaries-v1/verification.json).', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='Regenerate only the specification report')
    args = parser.parse_args()
    report = check(ROOT)
    if args.write:
        write_json(ROOT / (REPORT + '.json'), report)
        (ROOT / (REPORT + '.md')).write_text(report_text(report), encoding='utf-8')
    else:
        require(read_json(ROOT / (REPORT + '.json')) == report
                and (ROOT / (REPORT + '.md')).read_text(encoding='utf-8') == report_text(report), 'generated report is stale')
    print(json.dumps({k: v for k, v in report.items() if k not in {
        'membership_decisions', 'side_coverage', 'inspected_image_ids', 'source_families_by_entry'}}, indent=2))


if __name__ == '__main__':
    main()
