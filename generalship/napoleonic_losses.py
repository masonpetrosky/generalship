"""Verify the bounded 1805 source-loss pilot and regenerate its measurement report."""

import argparse
from collections import Counter
from decimal import Decimal
from fractions import Fraction
import json
import math
from pathlib import Path
import re

from . import napoleonic
from .sources import digest, read_json, source_metadata_digest, text_sections, write_json

BASE = 'data/napoleonic/loss-pilot-v1/'
SCOPE, PROTOCOL, OBSERVATIONS = (BASE + p + '.json' for p in ('scope', 'protocol', 'observations'))
SCOPE_SHA = 'f76e09e714ac7b4d75eda1cac153a5983bd6b951b8e245b0947c9e8ea71eacc5'
PROTOCOL_SHA = '05158992955cea30b2e429e968ea256ca7a048bfce9c3be5ad83223b8d427f17'
OBSERVATIONS_SHA = '6aab931bff48695c71e4d2a9ef4e52d56e5e081a97494afaadd15f2b5cc776b8'
ARTIFACT = 'artifacts/napoleonic-1805-loss-pilot-v1.json'
REPORT = 'docs/research/napoleonic-1805-loss-feasibility-v1.md'
CODE = 'generalship/napoleonic_losses.py'
NOTEBOOK = 'docs/research/napoleonic-1805-loss-audit-v1.ipynb'
SOURCE = 'bodart-1908-transcription-v1'
ALL_RANKS = ('killed', 'wounded', 'killed_and_wounded', 'captured', 'missing', 'reported_personnel_total')
MATERIAL = {'guns': {'guns'}, 'flags': {'flags', 'eagles'},
            'other_material': {'ammunition_wagons', 'horses'}}


def require(condition, message):
    if not condition:
        raise ValueError('Napoleonic loss pilot: ' + message)


def literal_value(literal, percent=False):
    tokens = re.findall(r'\d+(?:[. ]\d{3})*(?:·\d+)?', literal)
    require(len(tokens) == 1, 'one numeric literal per quantity')
    clean = tokens[0].replace(' ', '').replace('.', '').replace('·', '.')
    result = Decimal(clean)
    require(percent or result == result.to_integral_value(), 'integer personnel/material count')
    return result


def whole_value(side, category):
    """Never coalesce subsets, equipment, combined categories, or unstated zeroes."""
    values = [q for q in side['quantities'] if q['category'] == category
              and q['population'] == 'whole_side' and q['unit'] == 'people']
    require(len(values) <= 1, 'duplicate whole-side category')
    return values[0]['value'] if values else None


def declared_sum_profile(side):
    """Source-declared composition; agreement is not proof of unique historical people."""
    indexed = {q['id']: q for q in side['quantities']}
    profiles = []
    for rule in side['source_arithmetic']:
        total = indexed[rule['total']]
        parts = [indexed[k] for k in rule['parts']]
        if total['category'] == 'reported_personnel_total' and total['population'] == 'whole_side':
            profiles.append(tuple(sorted(q['category'] for q in parts)))
    require(len(profiles) <= 1, 'multiple total-composition profiles')
    return profiles[0] if profiles else None


def validate_quantity(quantity, passages, allowed):
    q = quantity
    require(q['category'] in allowed and isinstance(q['literal'], str) and q['literal'], 'quantity category/literal')
    require(type(q['value']) in (int, float) and math.isfinite(q['value']) and q['value'] >= 0, 'nonnegative finite quantity')
    require(q['evidence'] and all(k in passages for k in q['evidence']), 'quantity evidence links')
    require(any(q['literal'] in passages[k]['quote'] for k in q['evidence']), 'literal in cited passage')
    require(literal_value(q['literal'], q['category'] == 'personnel_percent') == Decimal(str(q['value'])), 'literal/value mismatch')
    require(q['qualifier'] in ('reported_point', 'approximate'), 'source qualifier')
    require(('ca.' in q['literal']) == (q['qualifier'] == 'approximate'), 'retain literal approximation')
    if q['category'] in MATERIAL:
        require(q['unit'] in MATERIAL[q['category']] and q['population'] == 'side_material', 'material is not personnel')
    elif q['category'] == 'personnel_percent':
        require(q['unit'] == 'percent' and q['value'] <= 100, 'percentage unit/range')
    elif q['category'] == 'officer_subset':
        require(q['unit'] == 'people' and q['population'] == 'officer_subset', 'officers are a subset')
    else:
        require(q['unit'] == 'people' and q['population'] in ('whole_side', 'austrian_subset_of_side_B'), 'personnel population/unit')
    if q['category'] != 'personnel_percent':
        require(type(q['value']) is int, 'integer count')
    require(q['basis'] in ('printed_loss', 'narrative_explicit_captivity'), 'quantity basis')
    if q['basis'] == 'narrative_explicit_captivity':
        require(q['category'] == 'captured' and any(re.search(r'Kriegsgefangenschaft|kriegsgefangen', passages[k]['quote'])
                                                  for k in q['evidence']), 'captivity needs an explicit source statement')


def build(root):
    for path, sha in ((SCOPE, SCOPE_SHA), (PROTOCOL, PROTOCOL_SHA), (OBSERVATIONS, OBSERVATIONS_SHA)):
        require(digest(root / path) == sha, 'changed frozen pilot record: ' + path)
    scope, protocol, data = (read_json(root / path) for path in (SCOPE, PROTOCOL, OBSERVATIONS))
    for path, sha in scope['bindings'].items():
        require(digest(root / path) == sha, 'changed bound source/input: ' + path)
    require(scope['historical_fits_authorized'] is False and scope['reserved_final_numerical_use'] is False
            and scope['source_fetching'] is False and scope['verification'] == 'primary', 'bounded source audit only')
    partition = read_json(root / 'data/napoleonic/methods-v1/evaluation.json')
    require(scope['campaign_group'] == 'third-coalition 1805'
            and scope['entry_ids'] == partition['frozen_groups'][scope['campaign_group']]
            and len(scope['entry_ids']) == len(set(scope['entry_ids'])) == 22
            and set(scope['entry_ids']) <= set(partition['development'])
            and not set(scope['entry_ids']) & set(partition['reserved_final']), 'whole frozen development group')
    require(data['scope_sha256'] == SCOPE_SHA and data['protocol_sha256'] == PROTOCOL_SHA
            and data['historical_models_fitted'] == data['features_admitted'] == data['reserved_final_entries_used'] == 0,
            'observation scope/no modeling')
    require([e['battle_id'] for e in data['entries']] == scope['entry_ids'], 'complete entry order/grain')
    frame = {r['id']: r for r in read_json(root / napoleonic.FRAME)['entries']}
    raw = {r['id']: r for r in napoleonic.entries((root / napoleonic.TRANSCRIPTION).read_text())}
    registry = {r['id']: r for r in read_json(root / 'data/sources.json')['sources']}
    source = registry[SOURCE]; sections = text_sections((root / source['path']).read_text())
    require(scope['source_family'] == source['independence_group'], 'one controlling compiler family')
    passages = data['passages']; expected_passages = {}
    for battle in scope['entry_ids']:
        entry = raw[battle]
        for i, line in enumerate(entry['text'], 1):
            if line != '[Offiziersverlust table not transcribed]':
                expected_passages[f'{battle}:L{i}'] = (battle, line)
        if battle == 'B369c':
            for i, line in enumerate(entry['page_notes'], 1):
                expected_passages[f'{battle}:N{i}'] = (battle, line)
    require(passages.keys() == expected_passages.keys(), 'complete anchored entry passages/notes')
    for key, (battle, line) in expected_passages.items():
        cite = passages[key]; page = frame[battle]['page']; image = registry[f'bodart-1908-p{page:03d}-image-v1']
        require(cite['source_id'] == SOURCE and cite['section'] == f'p{page:03d}'
                and cite['quote'] == line and line in sections[cite['section']], 'entry-anchored quotation: ' + key)
        require(cite['raw_sha256'] == source['sha256'] and cite['metadata_sha256'] == source_metadata_digest(source)
                and cite['image_source_id'] == image['id'] and cite['image_sha256'] == image['sha256'], 'passage hashes')
        require(cite['verification'] == 'primary_inspected_transcription_and_page_image', 'primary inspection record')
    require([c['id'] for c in data['conventions']] == ['selection', 'columns', 'winner-rule', 'available-strength',
                                                     'unengaged-strength', 'rounding', 'percentage-denominator'], 'all inspected conventions')
    for item in data['conventions']:
        cite = item['citation']; image = registry[item['image_source_id']]
        require(cite['source_id'] == SOURCE and cite['quote'] in sections[cite['section']]
                and item['raw_sha256'] == source['sha256'] and item['image_sha256'] == image['sha256'], 'convention evidence')
    require(data['inspection']['entry_pages'] == scope['entry_pages']
            and data['inspection']['convention_pages'] == [45, 46, 47]
            and data['inspection']['separate_review'] is False and data['inspection']['new_sources'] == 0
            and data['inspection']['extracted_source_families'] == 1 and data['inspection']['officer_tables_extracted'] is False,
            'actual inspection scope')
    strengths = {r['battle_id']: r for r in read_json(root / 'artifacts/napoleonic-benchmark-v1.json')['entries']}
    side_keys = []; quantity_ids = []; arithmetic = []; percentages = []; disputes = []
    for entry in data['entries']:
        battle = entry['battle_id']; f = frame[battle]
        require(entry['place'] == f['place'] and entry['type_printed'] == f['type_printed']
                and entry['frame_pages'] == f['pages'], 'unchanged frame metadata')
        require(entry['source_passages'] == [k for k in passages if k.startswith(battle + ':')]
                and tuple(entry['sides']) == ('A', 'B'), 'entry source/side grain')
        pointer = entry['existing_dossier']; path = 'data/napoleonic/evidence/' + battle + '.json'
        require(pointer['path'] == path and pointer['sha256'] == digest(root / path)
                and pointer['status'] == 'linked_existing_record_not_reinspected_for_this_pilot', 'dossier pointer binding/status')
        draft = read_json(root / path)
        expected = [{'claim_id': c['id'], 'status': c['status']} for c in draft['claims'] if c['dimension'] == 'outcome']
        require(pointer['outcome_claims'] == expected, 'retain existing outcome claims/disputes')
        disputes += [{'battle_id': battle, **c, 'path': path, 'sha256': pointer['sha256']}
                     for c in expected if c['status'] == 'disputed']
        for side, record in entry['sides'].items():
            side_keys.append((battle, side))
            column = f['french_side'] if side == 'A' else 'loser' if f['french_side'] == 'winner' else 'winner'
            require(record['source_column'] == column, 'frozen side orientation')
            indexed = {q['id']: q for q in record['quantities']}
            require(len(indexed) == len(record['quantities']), 'unique side quantity keys')
            for q in record['quantities']:
                require(q['id'].startswith(battle + ':' + side + ':')
                        and all(k.startswith(battle + ':') for k in q['evidence']), 'quantity entry/side anchor')
                validate_quantity(q, passages, protocol['categories']); quantity_ids.append(q['id'])
            known = [c for c in ALL_RANKS if whole_value(record, c) is not None]
            require(record['unstated_all_ranks_categories'] == [c for c in ALL_RANKS if c not in known], 'missing stays null')
            for rule in record['source_arithmetic']:
                require(rule['kind'] == 'printed_sum' and len(rule['parts']) == len(set(rule['parts']))
                        and rule['total'] not in rule['parts']
                        and all(k in indexed for k in rule['parts'] + [rule['total']]), 'source-sum references')
                quantities = [indexed[k] for k in rule['parts'] + [rule['total']]]
                require(all(q['unit'] == 'people' and q['population'] == 'whole_side' for q in quantities), 'same-population personnel sum')
                difference = sum(indexed[k]['value'] for k in rule['parts']) - indexed[rule['total']]['value']
                arithmetic.append({'battle_id': battle, 'side': side, 'parts': rule['parts'], 'total': rule['total'],
                                   'difference_people': difference, 'historical_disjointness_established': False})
            for q in record['quantities']:
                if q['category'] != 'personnel_percent':
                    continue
                numerator = indexed[q['applies_to']]
                require(numerator['unit'] == 'people' and numerator['population'] == q['population'], 'percent population/measure')
                denominator = strengths[battle]['sides'][side]['primary_value']
                basis = 'unchanged_prepared_compiler_personnel_total'
                require(not ('explicit_subset_denominator' in q and 'direct_source_denominator' in q), 'one explicit denominator')
                if 'explicit_subset_denominator' in q or 'direct_source_denominator' in q:
                    subset = q.get('explicit_subset_denominator', q.get('direct_source_denominator'))
                    require(subset['population'] == numerator['population']
                            and Decimal(str(subset['value'])) == literal_value(subset['literal'])
                            and any(subset['literal'] in passages[k]['quote'] for k in subset['evidence']), 'explicit subset denominator')
                    denominator = subset['value']
                    basis = 'source_explicit_national_subset' if 'explicit_subset_denominator' in q else 'direct_printed_strength_table_for_loss_arithmetic_only'
                    if 'direct_source_denominator' in q:
                        cells = passages[subset['evidence'][0]]['quote'].split('|')
                        source_cell = cells[0] if column == 'winner' else cells[-1]
                        require(len(cells) == 3 and subset['literal'] in source_cell, 'direct denominator source column')
                implied = Fraction(100 * numerator['value'], denominator) if denominator else None
                difference = Fraction(str(q['value'])) - implied if implied is not None else None
                percentages.append({'battle_id': battle, 'side': side, 'quantity_id': q['id'],
                                    'category': numerator['category'], 'population': numerator['population'],
                                    'numerator_people': numerator['value'], 'denominator_people': denominator,
                                    'denominator_basis': basis, 'printed_percent': q['value'],
                                    'implied_percent': round(float(implied), 6) if implied is not None else None,
                                    'printed_minus_implied_pp': round(float(difference), 6) if difference is not None else None,
                                    'interpretation': 'Arithmetic diagnostic only; retain both printed figures without source repair.'})
    require(len(side_keys) == len(set(side_keys)) == 44 and len(quantity_ids) == len(set(quantity_ids)), 'unique complete row/quantity grain')
    coverage = {}
    for category in ALL_RANKS:
        sides = [(e['battle_id'], s) for e in data['entries'] for s, r in e['sides'].items() if whole_value(r, category) is not None]
        pairs = [e['battle_id'] for e in data['entries'] if all(whole_value(r, category) is not None for r in e['sides'].values())]
        coverage[category] = {'sides': len(sides), 'side_denominator': 44, 'pairs': len(pairs), 'entry_denominator': 22,
                              'pair_ids': pairs, 'missing_side_keys': [[b, s] for b, s in side_keys if (b, s) not in sides]}
    has_number = lambda r: any(whole_value(r, c) is not None for c in ALL_RANKS)
    any_pairs = [e['battle_id'] for e in data['entries'] if all(has_number(r) for r in e['sides'].values())]
    matching_total_pairs = [e['battle_id'] for e in data['entries']
                            if declared_sum_profile(e['sides']['A']) == declared_sum_profile(e['sides']['B'])
                            == ('captured', 'killed_and_wounded')]
    by_type = {}
    for kind in sorted({e['type_printed'] for e in data['entries']}):
        entries = [e for e in data['entries'] if e['type_printed'] == kind]
        by_type[kind] = {'entries': len(entries), 'any_numeric_pair': sum(e['battle_id'] in any_pairs for e in entries),
                         'killed_wounded_pairs': sum(e['battle_id'] in coverage['killed_and_wounded']['pair_ids'] for e in entries),
                         'captured_pairs': sum(e['battle_id'] in coverage['captured']['pair_ids'] for e in entries)}
    universal = [c for c in ('killed', 'wounded', 'killed_and_wounded', 'captured', 'missing') if coverage[c]['pairs'] == 22]
    if len(matching_total_pairs) == 22:
        universal.append('source_declared_killed_wounded_plus_captured_total')
    profile = {'entries': 22, 'sides': 44, 'duplicate_side_keys': 0, 'quantities': len(quantity_ids),
               'entry_passages': len(passages), 'convention_passages': len(data['conventions']), 'images_inspected': 11,
               'source_families': 1, 'numeric_personnel_sides': sum(has_number(r) for e in data['entries'] for r in e['sides'].values()),
               'numeric_sides_by_side': {s: sum(has_number(e['sides'][s]) for e in data['entries']) for s in ('A', 'B')},
               'quantity_counts_by_category': dict(Counter(q['category'] for e in data['entries'] for r in e['sides'].values() for q in r['quantities'])),
               'any_numeric_pairs': len(any_pairs), 'any_numeric_pair_ids': any_pairs,
               'no_numeric_side_keys': [[e['battle_id'], s] for e in data['entries'] for s, r in e['sides'].items() if not has_number(r)],
               'explicit_zero_all_ranks_observations': sum(q['value'] == 0 for e in data['entries'] for r in e['sides'].values()
                    for q in r['quantities'] if q['population'] == 'whole_side' and q['category'] in ALL_RANKS),
               'category_coverage': coverage, 'declared_composition_total_pairs': matching_total_pairs, 'by_type': by_type,
               'source_sum_checks': arithmetic, 'percent_checks': percentages, 'existing_disputed_outcome_pointers': disputes}
    return {'kind': 'napoleonic_1805_loss_measurement_pilot', 'version': 1, 'verification': 'primary_verified',
            'input_sha256': {p: digest(root / p) for p in (SCOPE, PROTOCOL, OBSERVATIONS, CODE)},
            'scope': scope, 'observations': data, 'profile': profile,
            'decision': {'status': 'source_component_candidate_only' if universal else 'no_go_for_one_whole_group_loss_grade',
                         'full_coverage_defined_categories': universal, 'source_component_table_supported': True,
                         'strategic_value_measured': False, 'commander_effect_estimated': False,
                         'new_model_inputs': False, 'historical_fits': 0, 'reserved_final_entries_used': 0,
                         'stopping_rule': 'Stop this pilot; preserve narrower component coverage and all unknowns. '
                                          'No model run, broader extraction or new source search follows automatically.'}}


def report(data):
    profile = data['profile']; source = data['observations']; coverage = profile['category_coverage']
    out = ['# 1805 loss-measurement feasibility pilot v1', '',
           'Primary-verified source encoding. One existing compiler family; no separate review.', '',
           '**No-go for one common loss-based grade across the complete 22-entry group.** '
           'The source supports a component table with explicit gaps. It does not support replacing '
           'win/loss with one comparable severity or victory-quality number for every entry.', '',
           f'Of **22 entries / 44 sides**, {profile["numeric_personnel_sides"]}/44 sides have some numerical '
           f'personnel-loss observation; {profile["any_numeric_pairs"]}/22 entries have observations on both sides. '
           'Numerical presence is not a common definition. Killed-and-wounded figures are paired in '
           f'**{coverage["killed_and_wounded"]["pairs"]}/22 entries**, prisoner figures in '
           f'**{coverage["captured"]["pairs"]}/22**, and an explicit source-declared killed/wounded-plus-prisoner '
           f'composition on both sides in **{len(profile["declared_composition_total_pairs"])}/22**. '
           'No single defined all-ranks component covers the full group.', '',
           '## Scope and decision', '',
           'The owner accepted this bounded audit of the earliest frozen development group, '
           '`third-coalition 1805`, selected before assessing its loss availability. The exact '
           '[scope](../../' + SCOPE + ') and [protocol](../../' + PROTOCOL + ') retain all 22 land-cohort IDs, '
           'including entries without figures. The source’s broader war/year heading also contains naval '
           'entries; those were already outside the frozen land group and are not silently added. '
           'This source group spans multiple theaters and is not treated as one command appointment.', '',
           'The intended check is measurement feasibility: a whole-group measure needs the same explicit '
           'personnel definition and compatible population/time interpretation on both sides of every entry, '
           'without filling unknowns with zero, adding overlapping subsets or mixing people and equipment. '
           'This is a coverage/definition rule, not a statistical sample-size threshold. Narrower coverage '
           'is published even when the whole-group rule fails.', '',
           'The pilot ends here. The component evidence is useful, but there is no outcome score, utility '
           'weight, model fit, new admitted input, commander effect or campaign contribution estimate. '
           'The 52 final-evaluation entries remain unused numerically. The uncorrected benchmark, failed '
           'probability-correction branch, stopped appointment branch and paused opening research are unchanged.', '',
           '## Grain, completeness and comparability', '',
           'One row is one frozen entry side. A is France and its allies; B is the opposing side. '
           'Printed winner/loser columns are retained as provenance, never inferred from casualties. '
           'There are zero duplicate side keys. Empty cells mean unknown; no explicit all-ranks zero is '
           'printed in the encoded observations. A dash remains null.', '',
           '| All-ranks category | Sides with a figure / 44 | Paired entries / 22 | Interpretation |',
           '| --- | ---: | ---: | --- |']
    descriptions = {'killed': 'No separate all-ranks count; combined figures are not split.',
                    'wounded': 'No separate all-ranks count; officer-only tables do not supply it.',
                    'killed_and_wounded': 'Explicit combined category; retains approximate qualifiers.',
                    'captured': 'Explicit numerical prisoner/captivity claim; mostly prisoners is not a count.',
                    'missing': 'No separately quantified all-ranks category.',
                    'reported_personnel_total': 'Printed aggregate or unclassified headline loss; compositions differ.'}
    for category in ALL_RANKS:
        c = coverage[category]
        out.append(f'| {category} | {c["sides"]} | {c["pairs"]} | {descriptions[category]} |')
    out += ['', 'The separate killed and wounded unknowns concern **all ranks**. Detailed officer tables are '
            'visible on the images but omitted from the old raw transcription; this pilot preserves headline '
            'officer subsets and does not promote their breakdowns into all-ranks counts.', '',
            'Missing numerical loss observations occur on **8/22 A sides and 1/22 B sides**. This is source '
            'coverage asymmetry, not evidence of zero losses. All nine missing side keys remain in the JSON. '
            'The ten co-reported personnel-total pairs have heterogeneous definitions; they are not ten '
            'validated common attrition labels.', '',
            '| Printed engagement type | Entries | Any numerical pair | Killed/wounded pair | Prisoner pair |',
            '| --- | ---: | ---: | ---: | ---: |']
    for kind, values in profile['by_type'].items():
        out.append(f'| {kind} | {values["entries"]} | {values["any_numeric_pair"]} | '
                   f'{values["killed_wounded_pairs"]} | {values["captured_pairs"]} |')
    out += ['', 'The paired killed/wounded IDs are `' + '`, `'.join(coverage['killed_and_wounded']['pair_ids']) + '`. '
            'Verona (`B365c`) is the only entry with both numerical prisoner counts and both printed '
            'killed/wounded-plus-prisoner totals. This describes source-local components, not a validated '
            'historical attrition model or a representative sample of the whole cohort.', '',
            '## Every side and retained gap', '',
            'All figures are people. `ca.` is retained as approximate. A reported total can subsume earlier '
            'components; never add all columns. Composition, material, officer/national subsets, qualifiers '
            'and exact evidence IDs are retained in the [140-quantity source record](../../' + OBSERVATIONS + '). '
            'The source-page link opens the inspected facsimile. Complete quotations follow below.', '',
            '| Entry / place | Side (printed column) | Killed + wounded | Captured | Reported total / unsplit loss | Source / scope note |',
            '| --- | --- | ---: | ---: | ---: | --- |']
    def display(record, category):
        matches = [q for q in record['quantities'] if q['category'] == category
                   and q['population'] == 'whole_side' and q['unit'] == 'people']
        if not matches:
            return 'unknown'
        q = matches[0]
        return ('ca. ' if q['qualifier'] == 'approximate' else '') + f'{q["value"]:,}'
    for entry in source['entries']:
        for side, record in entry['sides'].items():
            page = entry['frame_pages'][0]
            note_parts = list(record['notes'])
            if record['surrender_condition']:
                conditions = {'captivity': 'Explicit captivity statement',
                              'captivity_with_conditional_officer_return': 'Captivity with conditional officer return',
                              'conditional_free_withdrawal_no_capture_count': 'Conditional free withdrawal; no prisoner count',
                              'battle_and_capitulation': 'Fighting plus capitulation'}
                note_parts.insert(0, conditions[record['surrender_condition']['kind']])
            if record['time_scope'] == 'explicit_blockade_and_bombardment_12_to_17_October':
                note_parts.insert(0, 'Explicit blockade/bombardment losses, 12–17 October')
            notes = '; '.join(note_parts)
            notes = notes.replace('|', '\\|')
            out.append(f'| {entry["battle_id"]} {entry["place"]} | {side} ({record["source_column"]}) | '
                       + ' | '.join(display(record, c) for c in ('killed_and_wounded', 'captured', 'reported_personnel_total'))
                       + f' | [p. {page}](../../data/raw/bodart-1908-v1/p{page:03d}.jpg)'
                       + ('; ' + notes if notes else '') + ' |')
    out += ['', '## Findings and impact on use', '',
            '**High: incomplete and unequal category coverage.** The source has numerical observations '
            'for 35/44 sides, while a common killed/wounded pair exists for 6/22 entries. Using only those '
            'six changes the evaluated population; filling missing counts with zero invents outcomes. '
            'Keep component-specific denominators and exclusions. Confidence is high for this inspected '
            'source encoding; historical accuracy remains unadjudicated.', '',
            '**High: capture, release and loss periods differ.** Memmingen and Trochtelfingen explicitly '
            'put the named forces into captivity. Ulm describes captivity with conditional officer return '
            'and reports French losses for the blockade/bombardment of 12–17 October. Dornbirn allows '
            'conditional free withdrawal to Bohemia for the named Austrian force; its 4,000 strength is '
            'not a quantified prisoner loss. Castelfranco combines fighting and capitulation. These facts '
            'remain separate statements rather than one interchangeable measure of permanent force destruction. '
            'The corresponding quoted entries and page images are retained below.', '',
            '**High: nested figures and unspecified composition.** Hollabrunn’s 1,800 prisoners are within '
            'an approximately 3,000 personnel-loss total; no killed/wounded remainder is inferred by subtraction. '
            'Austerlitz’s 6,000 Austrian losses are within the 36,000 coalition total. Officer subsets, '
            'guns, flags/eagles, ammunition wagons and horses remain separate. Ten printed personnel sums '
            'reconcile arithmetically; that alone does not establish unique people or interchangeable historical '
            'loss definitions.', '',
            '**Medium for source arithmetic, high for an unqualified loss-rate grade: printed percentages '
            'and denominators can disagree.** Haslach prints 1,500 losses, 6,000 strength and 32%; the '
            'ratio of the printed counts is 25%. Dürnstein prints 6,600 French losses, 8,000 strength and '
            '88%; the count ratio is 82.5%. Caldiero prints 8,000 French total losses, 46,000 strength and '
            '18.4%; the count ratio is 17.391304%. The discrepancies are visible in the original images. '
            'We retain the counts and percentages without selecting a corrected historical value or assuming '
            'that every small residual is an error. Rounded figures and an unreported alternative denominator '
            'remain possible explanations, not established repairs.', '',
            '## All printed-percentage arithmetic checks', '',
            'Counts divided by printed compiler strengths, not opening exposure or effective combatants. '
            'The older benchmark did not select the Dürnstein strength row; this pilot reads its explicit '
            '25,000 / 8,000 row directly for arithmetic only. This new observation does not revise the '
            'old frame, prepared benchmark or model inputs. The Austerlitz national subset uses its '
            'explicit 16,000 Austrian denominator. No missing casualty number is reconstructed from a percentage. '
            'Percentage-point differences are diagnostics, not corrections or precision estimates.', '',
            '| Entry | Side / population | Measure | Printed loss / strength | Printed % | Count ratio % | Difference pp |',
            '| --- | --- | --- | ---: | ---: | ---: | ---: |']
    for row in profile['percent_checks']:
        ratio = 'unknown' if row['implied_percent'] is None else f'{row["implied_percent"]:.6f}'
        difference = 'unknown' if row['printed_minus_implied_pp'] is None else f'{row["printed_minus_implied_pp"]:+.6f}'
        out.append(f'| {row["battle_id"]} | {row["side"]} / {row["population"]} | {row["category"]} | '
                   f'{row["numerator_people"]:,} / {row["denominator_people"] if row["denominator_people"] is not None else "unknown"} | '
                   f'{row["printed_percent"]:g} | {ratio} | {difference} |')
    out += ['', '## Existing alternatives and interpretation limits', '',
            'The pilot links all 22 existing dossiers by hash and retains their outcome-claim IDs/statuses. '
            'The following existing disputed outcome claims remain visible as pointers. Their underlying '
            'non-Bodart passages were **not re-inspected in this pilot** and are not promoted into new '
            'numerical alternatives or resolved by the arithmetic above.', '',
            '| Entry | Existing disputed claim | Existing dossier |', '| --- | --- | --- |']
    for pointer in profile['existing_disputed_outcome_pointers']:
        out.append(f'| {pointer["battle_id"]} | `{pointer["claim_id"]}` | '
                   f'[unchanged draft](../../{pointer["path"]}) |')
    out += ['', 'Bodart’s selection rule, rounded totals, available rather than necessarily engaged strengths '
            'and potentially strength-dependent winner coding remain limits. A casualty figure is a source '
            'claim, and one compiler family is not independent corroboration. Attrition cannot supply the '
            'strategic value of an objective, pursuit, territory, readiness or later campaign contribution '
            'without their own evidence and definitions. No scalar utility or commander credit is invented. '
            'There is no historical model or uncertainty interval in this pilot.', '',
            'There is no modern freshness/trend question for this fixed 1908 archive: raw and metadata '
            'hashes are checked instead. The assessment does not estimate feasibility across all 273 '
            'development entries from this single complete source group. Wider extraction and historical '
            'adjudication do not follow automatically from the remaining gaps.', '',
            '## Inspected source conventions', '',
            'The convention passages below were re-inspected on printed pp. 45–47. Entry passages were '
            'inspected on pp. 363–370: **11 pinned images, 72 entry/footnote passages and seven convention '
            'passages**, all from the same family. The transcription omits the detailed officer tables; '
            'the audit’s all-ranks scope and separate headline officer subsets preserve that limitation.', '']
    for item in source['conventions']:
        c = item['citation']
        out += [f'### {item["id"]}', '', item['interpretation_en'], '',
                '> ' + c['quote'].replace('\n', ' '), '',
                f'`{c["source_id"]}`, `{c["section"]}`; {c["locator"]}. '
                f'Image `{item["image_source_id"]}` SHA-256 `{item["image_sha256"]}`.', '']
    out += ['## Entry passages and facsimile locators', '',
            'All entry citations use `bodart-1908-transcription-v1`, raw SHA-256 '
            '`bf12437b6d19226ce127ce5d81e59d20358a5b1999ffe00f5ac6a8f8c20ef986`. '
            'Every citation in the observation JSON retains its own source metadata hash and image hash. '
            'Generic table headers are anchored to their exact entry and line; matching words on another '
            'entry are insufficient.', '']
    for entry in source['entries']:
        page = entry['frame_pages'][0]
        first = source['passages'][entry['source_passages'][0]]
        out += [f'### {entry["battle_id"]}: {entry["place"]}', '',
                f'[Inspected p. {page}](../../data/raw/bodart-1908-v1/p{page:03d}.jpg), '
                f'image `{first["image_source_id"]}`; SHA-256 `{first["image_sha256"]}`.', '']
        for key in entry['source_passages']:
            out += [f'`{key}` — {source["passages"][key]["locator"]}', '',
                    '> ' + source['passages'][key]['quote'].replace('\n', ' '), '']
    out += ['## Reproduction and primary checks', '',
            '- [Measurement JSON](../../' + ARTIFACT + '), [source observations](../../' + OBSERVATIONS + '), '
            '[audit module](../../' + CODE + ') and [executed companion notebook](napoleonic-1805-loss-audit-v1.ipynb). '
            'The notebook recomputes the principal coverage counts from the saved side records.',
            f'- Scope SHA-256 `{SCOPE_SHA}`; protocol SHA-256 `{PROTOCOL_SHA}`; '
            f'observation SHA-256 `{OBSERVATIONS_SHA}`. The generated JSON also binds the exact audit code.',
            '- `python3 -m generalship.napoleonic_losses` checks all fixed input hashes, 22 entry IDs / '
            '44 side keys, 140 quantities/literals/units, exact entry-anchored quotes and image bindings, '
            'all subsets, all missing-category lists, ten printed sums, 19 percentage diagnostics and '
            'all 22 dossier pointers/statuses. Source interpretation is primary verification, not a '
            'separate historical review.',
            '- `--write` regenerates only this report and its measurement JSON from the immutable '
            'source record. `make check` and `make reproduce` include this offline path. '
            'It makes no network request, model call or historical fit and does not modify a dossier, '
            'packet, frozen benchmark or previous result.', '']
    return '\n'.join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = build(args.root)
    text = report(data)
    if args.write:
        write_json(args.root / ARTIFACT, data)
        (args.root / REPORT).write_text(text, encoding='utf-8')
    require(read_json(args.root / ARTIFACT) == data, 'stale audit JSON')
    require((args.root / REPORT).read_text(encoding='utf-8') == text, 'stale audit report')
    print(json.dumps({'status': data['decision']['status'], **{k: data['profile'][k] for k in
          ('entries', 'sides', 'quantities', 'entry_passages', 'convention_passages', 'images_inspected', 'source_families',
           'numeric_personnel_sides', 'any_numeric_pairs')}, 'historical_fits': 0, 'reserved_final_entries_used': 0}, indent=2))


if __name__ == '__main__':
    main()
