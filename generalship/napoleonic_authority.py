"""Bounded source-local authority mapping; no person/army admission or historical fit."""

import argparse
from collections import Counter
from itertools import combinations
import json
from pathlib import Path

from . import napoleonic_boundaries as boundary
from . import napoleonic_ledger_design as ledger
from .evidence import citation_text
from .sources import (digest, read_json, safe_path, source_document_date,
                      source_metadata_digest, validate_source_metadata, write_json)

BASE = 'data/napoleonic/authority-v1'
SCOPE = BASE + '/scope.json'
MAPPINGS = BASE + '/mappings.json'
SUPPLEMENT = BASE + '/source-supplement.json'
VERIFICATION = BASE + '/verification.json'
DESIGN = 'docs/napoleonic-authority-v1.md'
REPORT = 'artifacts/napoleonic-authority-v1'
CODE = ('generalship/napoleonic_authority.py', 'tests/test_napoleonic_authority.py')
ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError('Napoleonic authority: ' + message)


def shape(value, fields, where):
    require(isinstance(value, dict) and set(value) == set(fields.split()), 'invalid fields: ' + where)


def bindings(root):
    paths = set(read_json(root / SCOPE)['bindings']) | {SCOPE, MAPPINGS, SUPPLEMENT, DESIGN}
    return {'inputs': {p: digest(safe_path(root, p)) for p in sorted(paths)},
            'code': {p: digest(ROOT / p) for p in CODE}}


def validate(root, proposal=None):
    previous = boundary.check(root)
    prior_scope = read_json(root / boundary.SCOPE)
    scope = read_json(root / SCOPE)
    require(scope.get('kind') == 'napoleonic_authority_scope' and scope.get('version') == 1
            and scope.get('status') == 'design_only', 'scope identity/status')
    expected = set(prior_scope['bindings']) | {boundary.SCOPE, boundary.RECORDS, boundary.SNAPSHOT,
                                              boundary.VERIFICATION, boundary.DESIGN}
    require(set(scope['bindings']) == expected, 'parent/input bindings incomplete')
    for path, sha in scope['bindings'].items():
        require(digest(safe_path(root, path)) == sha, 'changed bound input: ' + path)
    battles = scope['battle_ids']
    require(battles == prior_scope['battle_ids'] and scope['selected_group'] == prior_scope['selected_group']
            and (scope['engagement_denominator'], scope['side_denominator']) == (4, 8), 'scope expanded or denominator changed')
    require(scope['historical_blinding'] is False and scope['authorization'] == {
        'owner_message': 'Sounds good, go ahead',
        'accepted_recommendation': 'Map commander authority and army continuity for the same four engagements before expanding extraction, using pinned evidence and preserving unsupported links.',
        **{k: False for k in ('new_source_fetching', 'feature_admission', 'historical_outcome_fit',
                             'synthetic_job', 'calibration_scoring', 'separate_review', 'subagents')}}, 'authorization exceeded')
    data = read_json(root / MAPPINGS) if proposal is None else proposal
    shape(data, 'kind version status scope_sha256 design_sha256 supplement_sha256 passages roles identity_links reconciliations organization_context forces continuity_pairs emitted_model_rows historical_outcomes_fitted calibration', 'mappings')
    require(data['kind'] == 'napoleonic_authority_mappings' and data['version'] == 1
            and data['status'] == 'design_only', 'mapping identity/status')
    require(data['scope_sha256'] == digest(root / SCOPE) and data['design_sha256'] == digest(root / DESIGN)
            and data['supplement_sha256'] == digest(root / SUPPLEMENT), 'mapping hash binding')
    require(data['emitted_model_rows'] == [] and data['historical_outcomes_fitted'] is False
            and data['calibration'] == 'prepared_unscored', 'mapping cannot promote, fit or score')
    sources = {}
    for path in (ledger.SNAPSHOT, boundary.SNAPSHOT):
        for source in read_json(root / path)['sources']:
            require(source['id'] not in sources or sources[source['id']] == source, 'conflicting parent metadata')
            sources[source['id']] = source
    supplement = read_json(root / SUPPLEMENT)
    require(supplement['kind'] == 'napoleonic_authority_source_supplement' and supplement['version'] == 1,
            'source supplement identity')
    for key, source in ledger.indexed(supplement['sources']).items():
        require(key not in sources and digest(safe_path(root, source['path'])) == source['sha256'], 'supplement overwrites metadata or raw checksum differs')
        sources[key] = source
    validate_source_metadata(root, sources)
    passages = ledger.indexed(data['passages'])
    families, images = {}, set()
    for row in passages.values():
        shape(row, 'id battle_ids citation raw_sha256 metadata_sha256 document_date facsimile_source_id facsimile_sha256 interpretation_en', 'passage')
        require(boundary.texts(row['battle_ids']) and len(set(row['battle_ids'])) == len(row['battle_ids'])
                and set(row['battle_ids']) <= set(battles) and ledger.nonempty(row['interpretation_en']), 'passage scope/interpretation')
        cite = row['citation']
        source = sources.get(cite.get('source_id'))
        require(source is not None and row['raw_sha256'] == source['sha256']
                and row['metadata_sha256'] == source_metadata_digest(source), 'passage source binding')
        require(ledger.nonempty(cite.get('quote')) and cite['quote'] in citation_text(root, sources, cite), 'quote absent from section')
        require(row['document_date'] == source_document_date(source, cite.get('section')), 'section document date')
        image = sources.get(row['facsimile_source_id'])
        require(image is not None and image['format'] in {'jpg', 'jpeg', 'png'}
                and row['facsimile_sha256'] == image['sha256'], 'facsimile binding')
        expected_image = source.get('facsimile_source_id')
        if source['id'] == 'bodart-1908-transcription-v1':
            expected_image = 'bodart-1908-' + cite['section'] + '-image-v1'
        require(image['id'] == expected_image, 'wrong page image')
        images.add(image['id'])
        families[row['id']] = source['independence_group']
    used = set()

    def refs(row, allowed_battles):
        ids = row['evidence']
        require(boundary.texts(ids) and len(set(ids)) == len(ids) and all(
            key in passages and set(passages[key]['battle_ids']) & set(allowed_battles) for key in ids), 'evidence scope/reference')
        used.update(ids)
        return {families[key] for key in ids}

    old_roles = ledger.indexed(read_json(root / ledger.EXAMPLES)['command_records'])
    scenarios = ledger.indexed(read_json(root / boundary.RECORDS)['scenarios'])
    roles = ledger.indexed(data['roles'])
    linked = []
    authority_types = {'compiler_label', 'operational_task', 'formation_command', 'field_direction',
                       'expedition_decision', 'negotiation', 'troop_appointment', 'superior_or_visit',
                       'siege_direction', 'garrison_office', 'acting_governor', 'investment_direction',
                       'column_direction', 'assault_direction', 'garrison_command', 'delegated_negotiation'}
    for row in roles.values():
        shape(row, 'id original_observation_id battle_id side actor_label authority_type force_scope reported_time appointment_start appointment_end effective_transfer_at resolved_person_id scenario_ids note evidence', 'role')
        require(row['battle_id'] in battles and row['side'] in {'A', 'B'} and row['authority_type'] in authority_types, 'role scope/type')
        require(all(ledger.nonempty(row[k]) for k in ('actor_label', 'force_scope', 'reported_time', 'note')), 'role labels/rationale')
        require(all(row[k] is None for k in ('appointment_start', 'appointment_end', 'effective_transfer_at', 'resolved_person_id')), 'invented appointment/transfer or person selection')
        require(boundary.texts(row['scenario_ids']) and len(set(row['scenario_ids'])) == len(row['scenario_ids'])
                and all(key in scenarios and scenarios[key]['battle_id'] == row['battle_id'] for key in row['scenario_ids']), 'role scenario reference')
        require(len(refs(row, [row['battle_id']])) == 1, 'role mixes source assertions')
        original = row['original_observation_id']
        if original is not None:
            require(original in old_roles and row['id'] == original, 'unknown original role')
            prior = old_roles[original]
            require(all(row[k] == prior[k] for k in ('battle_id', 'side', 'actor_label'))
                    and row['force_scope'] == prior['force_scope'] and row['reported_time'] == prior['state_description'], 'original role altered')
            citations = [passages[k]['citation'] for k in row['evidence']]
            require(all(ref['citation'] in citations for ref in prior['evidence']), 'original role evidence omitted')
            linked.append(original)
    require(len(linked) == len(old_roles) and set(linked) == old_roles.keys(), 'original command accounting')
    require({k for k, v in roles.items() if v['original_observation_id'] is None} == {
        'B371a-A-capitulation-massena', 'B371a-A-capitulation-franceschi'}, 'additional role scope changed')
    identities = ledger.indexed(data['identity_links'])
    require(set(identities) == set(('damas-within-koch stuart-within-bunbury massena-capitulation '
        'hotz-capitulation stuart-stewart hesse-variants hotz-storz mirabelli-cross-source '
        'reynier-cross-entry implicit-marshal-titles franceschi-role-identity verdier-cross-entry-source').split()),
        'identity question coverage')
    for row in identities.values():
        shape(row, 'id mentions status basis resolved_person_id note', 'identity link')
        require(row['status'] in {'source_local_coreference', 'unresolved'} and row['resolved_person_id'] is None
                and ledger.nonempty(row['note']) and len(row['mentions']) >= 2, 'identity status/person/rationale')
        ids = []
        for mention in row['mentions']:
            shape(mention, 'passage_id label', 'identity mention')
            key = mention['passage_id']
            require(key in passages and ledger.nonempty(mention['label'])
                    and mention['label'] in passages[key]['citation']['quote'], 'identity label absent from passage')
            ids.append(key)
            used.add(key)
        require(len({(m['passage_id'], m['label']) for m in row['mentions']}) == len(row['mentions']), 'duplicate identity mention')
        if row['status'] == 'source_local_coreference':
            require(row['basis'] in {'continuous_episode', 'same_document'} and len({families[k] for k in ids}) == 1
                    and bool(set.intersection(*(set(passages[k]['battle_ids']) for k in ids))), 'source-local identity crosses family/entry')
            if row['basis'] == 'same_document':
                require(len({(passages[k]['citation']['source_id'], passages[k]['citation'].get('section')) for k in ids}) == 1,
                        'same-document identity crosses document')
        else:
            require(row['basis'] in {'cross_source', 'cross_entry', 'title_referent', 'role_identity'}, 'unresolved identity basis')
    reconciliations = ledger.indexed(data['reconciliations'])
    require(set(reconciliations) == set(('campo-policy-and-local-direction maida-expedition-and-field '
        'gaeta-command-and-delegation gaeta-governor-succession amantea-broader-and-local').split()), 'reconciliation coverage')
    for row in reconciliations.values():
        shape(row, 'id battle_id role_ids finding effective_transfer_at note evidence', 'reconciliation')
        require(row['battle_id'] in battles and boundary.texts(row['role_ids'])
                and all(k in roles and roles[k]['battle_id'] == row['battle_id'] for k in row['role_ids'])
                and len(set(row['role_ids'])) == len(row['role_ids']), 'reconciliation role reference')
        require(row['finding'] in {'different_scopes_or_phases', 'unresolved_identity_or_transfer'}
                and row['effective_transfer_at'] is None and ledger.nonempty(row['note']), 'unfounded handover or reconciliation')
        refs(row, [row['battle_id']])
    forces = ledger.indexed(data['forces'])
    expected_sides = {(battle, side) for battle in battles for side in ('A', 'B')}
    actual_sides = []
    for row in forces.values():
        shape(row, 'id battle_id side reported_scopes role_ids selected_boundary selected_strength selected_person_id army_id blockers note evidence', 'force')
        pair = row['battle_id'], row['side']
        require(pair in expected_sides and row['id'] == '-'.join(pair), 'force scope/handle')
        require(all(row[k] is None for k in ('selected_boundary', 'selected_strength', 'selected_person_id', 'army_id')), 'force mapping cannot select inputs')
        require(set(row['blockers']) == {'joint_boundary', 'complete_population', 'person_authority_mapping', 'army_definition_and_continuity'}
                and len(row['blockers']) == 4 and boundary.texts(row['reported_scopes']) and ledger.nonempty(row['note']), 'force blockers/scopes')
        expected_roles = {k for k, v in roles.items() if (v['battle_id'], v['side']) == pair}
        require(boundary.texts(row['role_ids']) and len(set(row['role_ids'])) == len(row['role_ids'])
                and set(row['role_ids']) == expected_roles, 'force role accounting')
        refs(row, [row['battle_id']])
        actual_sides.append(pair)
    require(len(actual_sides) == len(set(actual_sides)) and set(actual_sides) == expected_sides, 'force side coverage')
    organizations = ledger.indexed(data['organization_context'])
    require(set(organizations) == {'three-corps-and-detachments', 'occupation-and-blockade', 'capitulation-staff-office'},
            'organization context coverage')
    for row in organizations.values():
        shape(row, 'id force_ids assertion_en army_id note evidence', 'organization context')
        require(boundary.texts(row['force_ids']) and all(k in forces for k in row['force_ids'])
                and row['army_id'] is None and ledger.nonempty(row['assertion_en']) and ledger.nonempty(row['note']), 'organization context cannot establish army identity')
        refs(row, [forces[k]['battle_id'] for k in row['force_ids']])
    pairs = ledger.indexed(data['continuity_pairs'])
    wanted_pairs = {tuple(sorted((a + '-' + side, b + '-' + side))) for a, b in combinations(battles, 2) for side in ('A', 'B')}
    observed_pairs = []
    for row in pairs.values():
        shape(row, 'id force_ids status army_id missing_evidence note evidence', 'continuity')
        keys = row['force_ids']
        require(isinstance(keys, list) and len(keys) == 2 and tuple(sorted(keys)) in wanted_pairs, 'continuity pair scope')
        require(row['status'] == 'not_established' and row['army_id'] is None and boundary.texts(row['missing_evidence'])
                and ledger.nonempty(row['note']), 'continuity cannot merge by label or commander')
        refs(row, [forces[k]['battle_id'] for k in keys])
        observed_pairs.append(tuple(sorted(keys)))
    require(len(observed_pairs) == len(set(observed_pairs)) and set(observed_pairs) == wanted_pairs, 'continuity pair coverage')
    require(used == passages.keys(), 'unused passage')
    effort = {b: sorted(set(previous['source_families_by_entry'][b]) | {families[k] for k, row in passages.items() if b in row['battle_ids']}) for b in battles}
    require(all(len(fs) <= 3 for fs in effort.values()), 'source-family ceiling')
    return {'kind': 'napoleonic_authority_check', 'version': 1, 'status': 'valid_mapping',
            'engagements': len(battles), 'sides': len(forces), 'original_roles_indexed': len(linked),
            'additional_roles': len(roles) - len(linked), 'role_appearances': len(roles),
            'authority_types': dict(sorted(Counter(r['authority_type'] for r in roles.values()).items())),
            'passages': len(passages), 'inspected_image_ids': sorted(images), 'source_pool_entries': len(sources),
            'supplement_entries': len(supplement['sources']), 'source_families_by_entry': effort,
            'identity_links': len(identities), 'identity_status_counts': dict(sorted(Counter(r['status'] for r in identities.values()).items())),
            'reconciliations': len(data['reconciliations']), 'organization_contexts': len(data['organization_context']),
            'continuity_pairs': len(pairs), 'established_continuity_pairs': 0, 'unresolved_opening_sides': len(forces),
            'side_coverage': [{'battle_id': b, 'side': s, 'role_appearances': len(forces[b+'-'+s]['role_ids']),
                               'blockers': forces[b+'-'+s]['blockers']} for b, s in sorted(expected_sides)],
            'complete_candidate_engagements': 0, 'emitted_model_rows': [], 'historical_outcomes_fitted': False,
            'calibration': 'prepared_unscored', 'development_engagements': previous['development_engagements'],
            'reserved_final_engagements': previous['reserved_final_engagements']}


def check(root):
    report = validate(root)
    verification = read_json(root / VERIFICATION)
    require(verification.get('kind') == 'napoleonic_authority_primary_verification' and verification.get('version') == 1
            and verification.get('verification') == 'primary-verified' and verification.get('independent_review') is False
            and verification.get('authorizes_feature_admission') is False and verification.get('historical_outcomes_fitted') is False,
            'primary verification scope')
    require(verification['bindings'] == bindings(root), 'stale verification bindings')
    require(verification['inspected_image_ids'] == report['inspected_image_ids'], 'verification image inventory')
    report['status'] = 'primary-verified mapping'
    return report


def report_text(report):
    lines = ['# Naples authority and army-continuity mapping v1', '',
             'Primary-verified; source-local mapping only. No feature admitted, responsible person or army selected, historical outcome fitted or model row emitted.', '',
             f"**{report['engagements']} engagements / {report['sides']} sides**; all **{report['original_roles_indexed']} prior command-role observations** indexed plus **{report['additional_roles']} capitulation-role examples**.",
             f"**{report['passages']} adopted passages on {len(report['inspected_image_ids'])} re-inspected pinned images**. Reused immutable source metadata plus {report['supplement_entries']} additional existing records; no fetching, source registration or dossier change.", '',
             '## Findings', '',
             '- Campo Tenese: council policy, Reynier’s local direction and Damas’s formation command remain separate scopes.',
             '- Maida: Bunbury’s expedition/reconnaissance roles and Koch’s field dispositions retain their source dates and name forms.',
             '- Gaëta: troop command, a superior’s visit/direction, acting government and delegated capitulation powers cannot become one exclusive handover. The dated capitulation names Masséna as siege-corps commander and Franceschi as his delegate; it does not establish opening appointments.',
             '- Amantea: the marshal’s wider directives, Reynier’s broader/siege command and Huard’s investment leadership do not supply an exclusive local transfer clock.', '',
             f"Identity links: **{report['identity_status_counts'].get('source_local_coreference', 0)} source-local co-references / {report['identity_status_counts'].get('unresolved', 0)} unresolved hypotheses**. Source-local links are not global person IDs. Hotz/Storz, Hesse variants, Stuart/Stewart, recurring Reynier/Verdier labels, Mirabelli, implicit marshal titles and the two Franceschi roles keep their stated limits.", '',
             f"Army continuity: **{report['established_continuity_pairs']}/{report['continuity_pairs']} same-side inter-engagement pairs established**. Reported 1st/2nd-corps, detachment and staff-office relationships remain organizational context, not a persistent army registry.", '',
             '## Complete side mappings', '', '| Entry | Side | Role appearances | Opening force/person/army mapping |', '| --- | --- | ---: | --- |']
    for row in report['side_coverage']:
        lines.append(f"| {row['battle_id']} | {row['side']} | {row['role_appearances']} | unresolved |")
    lines += ['', f"**{report['unresolved_opening_sides']}/8 complete opening mappings remain blocked; zero complete candidate engagements.** Missing joint boundary, complete population, boundary-matched person/authority and army definition/continuity stay explicit. Role appearances are not unique people or extra battle weights.", '',
              '## Stopping decision', '',
              'Stop this four-entry measurement pilot here. A source-local identity or phase-specific authority claim does not overcome the remaining force/boundary gaps. No further historical deep dive follows merely from an unknown.',
              'Next recommended action: a mechanical blocker inventory across the 273 development entries, grouped by complete campaign, to choose the next bounded measurement batch by reusable evidence. Inventory presence is not semantic reconciliation.',
              f"The **{report['development_engagements']}/{report['reserved_final_engagements']}** development/final reservation, 47 prepared/unscored calibration tasks and all earlier numerical results are unchanged. No subagent or separate reviewer ran.", '',
              '[Design and source findings](../docs/napoleonic-authority-v1.md), [mappings and exact passages](../data/napoleonic/authority-v1/mappings.json), [primary verification](../data/napoleonic/authority-v1/verification.json).', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    report = check(ROOT)
    if args.write:
        write_json(ROOT / (REPORT + '.json'), report)
        (ROOT / (REPORT + '.md')).write_text(report_text(report), encoding='utf-8')
    else:
        require(read_json(ROOT / (REPORT + '.json')) == report
                and (ROOT / (REPORT + '.md')).read_text(encoding='utf-8') == report_text(report), 'generated report is stale')
    print(json.dumps({k: v for k, v in report.items() if k not in {'side_coverage', 'source_families_by_entry', 'inspected_image_ids', 'authority_types'}}, indent=2))


if __name__ == '__main__':
    main()
