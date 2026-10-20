"""Offline verification of the bounded Naples objective/result measurement pilot."""

import argparse
from collections import Counter
import hashlib
from pathlib import Path

from . import napoleonic
from .sources import digest, read_json, source_metadata_digest, text_sections, write_json

BASE = 'data/napoleonic/objective-pilot-v1/'
SCOPE, PROTOCOL, OBSERVATIONS = (BASE + name + '.json' for name in ('scope', 'protocol', 'observations'))
SCOPE_SHA = 'a251a54edc75732cd1c0006653c3573cec55d00c2f795b867cbb83966b53bc0b'
PROTOCOL_SHA = 'c452710c4bf6933da2dc4df729b6b1d570c46dba33907308a5ec0afe3c8bc112'
OBSERVATIONS_SHA = 'eed95ce2214a9aaca05c01a3817980da38bcfa6b4a15ae6d3b2e70d7faf8ce72'
CODE = 'generalship/napoleonic_objectives.py'
ARTIFACT = 'artifacts/napoleonic-naples-objective-pilot-v1.json'
REPORT = 'docs/research/napoleonic-naples-objective-pilot-v1.md'
NOTEBOOK = 'docs/research/napoleonic-naples-objective-audit-v1.ipynb'
PRECEDENCE = {'before_relevant_action', 'before_later_phase', 'after_action_commentary', 'unestablished'}
SCOPES = {'local_engagement', 'operational_follow_through', 'broader_campaign', 'author_commentary'}
DETERMINATE = {'reported_action_executed', 'reported_effect_observed', 'reported_effect_not_observed'}
COMPONENT_FIELDS = set(('id battle_id side statement_kind scope_level objective objective_evidence '
                        'reported_precedence precedence_note recording_provenance pre_action_document_evidence '
                        'success_criterion criterion_note criterion_literal normalized_duration_days attainment '
                        'observed_result result_evidence result_window limits related_entries context_evidence').split())


def require(condition, message):
    if not condition:
        raise ValueError('Naples objective pilot: ' + message)


def validate_component(row, passages, entry_ids, protocol):
    require(set(row) == COMPONENT_FIELDS, 'component contract; no added scores or weights')
    require(row['battle_id'] in entry_ids and row['side'] in ('A', 'B'), 'component in frozen entry/side')
    require(row['statement_kind'] in protocol['allowed_statement_kinds'] and row['scope_level'] in SCOPES,
            'separate statement kind and scope')
    require(row['attainment'] in protocol['allowed_attainment'] and row['reported_precedence'] in PRECEDENCE,
            'attainment and temporal vocabulary')
    for field in ('id', 'objective', 'precedence_note', 'criterion_note', 'observed_result', 'result_window'):
        require(isinstance(row[field], str) and row[field].strip(), 'required explanatory field: ' + field)
    require(row['recording_provenance'] == 'retrospective_account'
            and row['pre_action_document_evidence'] == [], 'no invented pre-action document')
    require(row['normalized_duration_days'] is None, 'no invented normalized duration')
    require(row['success_criterion'] is None or isinstance(row['success_criterion'], str)
            and row['success_criterion'].strip(), 'null or explicit success criterion')
    if row['attainment'] in DETERMINATE:
        require(row['success_criterion'] is not None, 'a determinate component needs its explicit criterion')
    if row['attainment'] == 'not_assessable':
        require(row['success_criterion'] is None, 'unassessable criterion remains null')
    if row['statement_kind'] == 'retrospective_commentary':
        require(row['reported_precedence'] == 'after_action_commentary' and row['attainment'] == 'not_assessable',
                'commentary is not a prior mandate')
    if row['statement_kind'] == 'inferred_disposition':
        require(row['reported_precedence'] == 'unestablished' and row['attainment'] == 'not_assessable',
                'resistance does not establish a prior objective')
    used = set()
    for field in ('objective_evidence', 'result_evidence', 'context_evidence'):
        require(isinstance(row[field], list) and len(row[field]) == len(set(row[field]))
                and all(p in passages for p in row[field]), 'valid unique evidence references')
        if field != 'context_evidence':
            require(row[field], 'retain objective and result evidence')
        used.update(row[field])
    literal = row['criterion_literal']
    require(literal is None or isinstance(literal, str) and literal
            and any(literal in passages[p]['quote'] for p in row['objective_evidence']), 'literal criterion evidence')
    require(row['limits'] and all(isinstance(s, str) and s for s in row['limits']), 'visible component limits')
    require(len(row['related_entries']) == len(set(row['related_entries']))
            and set(row['related_entries']) <= set(entry_ids) - {row['battle_id']}, 'bounded cross-entry references')
    return used


def profile(data, entry_ids):
    rows = data['components']
    keys = [(battle, side) for battle in entry_ids for side in ('A', 'B')]
    by_side = {key: [r for r in rows if (r['battle_id'], r['side']) == key] for key in keys}
    prior = lambda r: r['statement_kind'] not in ('inferred_disposition', 'retrospective_commentary')
    side_rows = []
    for (battle, side), components in by_side.items():
        side_rows.append({'battle_id': battle, 'side': side, 'component_ids': [r['id'] for r in components],
                          'reported_before_relevant_action': any(prior(r) and r['reported_precedence'] == 'before_relevant_action'
                                                                for r in components),
                          'reported_before_later_phase': any(prior(r) and r['reported_precedence'] == 'before_later_phase'
                                                            for r in components),
                          'inferred_only': all(r['statement_kind'] == 'inferred_disposition' for r in components),
                          'pre_action_document': any(r['pre_action_document_evidence'] for r in components),
                          'common_grade': None})
    passages = data['passages']
    return {'entries': len(entry_ids), 'sides': len(keys), 'duplicate_side_keys': len(side_rows) - len(by_side),
            'components': len(rows), 'passages': len(passages),
            'images_inspected': len(data['inspection']['images_inspected']),
            'adopted_source_families': sorted({p['family'] for p in passages.values()}),
            'image_checked_passages': sum(bool(p['images']) for p in passages.values()),
            'ocr_only_passage_ids': [pid for pid, p in passages.items() if not p['images']],
            'prior_objective_claims': len(data['prior_objective_claims']),
            'prior_citation_dispositions': dict(sorted(Counter(c['disposition'] for r in data['prior_objective_claims']
                                                             for c in r['citations']).items())),
            'reported_before_action_sides': sum(r['reported_before_relevant_action'] for r in side_rows),
            'reported_before_later_phase_only_sides': sum(r['reported_before_later_phase']
                                                       and not r['reported_before_relevant_action'] for r in side_rows),
            'inferred_only_sides': sum(r['inferred_only'] for r in side_rows),
            'pre_action_document_sides': sum(r['pre_action_document'] for r in side_rows),
            'missing_success_criteria': [r['id'] for r in rows if r['success_criterion'] is None],
            'statement_kind_counts': dict(sorted(Counter(r['statement_kind'] for r in rows).items())),
            'attainment_counts': dict(sorted(Counter(r['attainment'] for r in rows).items())),
            'cross_entry_components': [r['id'] for r in rows if r['related_entries']],
            'side_coverage': side_rows, 'historical_fits': 0, 'reserved_final_entries_used': 0}


def build(root):
    for path, sha in ((SCOPE, SCOPE_SHA), (PROTOCOL, PROTOCOL_SHA), (OBSERVATIONS, OBSERVATIONS_SHA)):
        require(digest(root / path) == sha, 'changed frozen pilot record: ' + path)
    scope, protocol, data = (read_json(root / p) for p in (SCOPE, PROTOCOL, OBSERVATIONS))
    for path, sha in scope['bindings'].items():
        require(digest(root / path) == sha, 'changed bound input: ' + path)
    require(scope['verification'] == 'primary' and scope['source_fetching'] is False
            and scope['historical_fits_authorized'] is False and scope['reserved_final_numerical_use'] is False,
            'bounded primary source audit')
    partition = read_json(root / 'data/napoleonic/methods-v1/evaluation.json')
    ids = scope['entry_ids']
    require(scope['campaign_group'] == 'third-coalition 1806'
            and ids == partition['frozen_groups'][scope['campaign_group']]
            and len(ids) == len(set(ids)) == 4 and set(ids) <= set(partition['development'])
            and not set(ids) & set(partition['reserved_final']), 'whole frozen development group')
    require(protocol['scope_sha256'] == SCOPE_SHA and data['scope_sha256'] == SCOPE_SHA
            and data['protocol_sha256'] == PROTOCOL_SHA and data['entry_ids'] == ids, 'record bindings and complete entries')
    require(data['verification'] == 'primary' and data['historical_fits'] == data['features_admitted']
            == data['reserved_final_entries_used'] == 0 and data['common_grade'] is None
            and data['commander_credit'] is None, 'no grade, promotion, attribution or model run')
    registry = {s['id']: s for s in read_json(root / 'data/sources.json')['sources']}
    passages = data['passages']; sections = {}; checked_files = set(); images = set()
    for pid, p in passages.items():
        s = registry[p['source_id']]
        if s['id'] not in sections:
            require(digest(root / s['path']) == s['sha256'], 'source raw hash')
            sections[s['id']] = text_sections((root / s['path']).read_text())
        require(p['raw_sha256'] == s['sha256'] and p['metadata_sha256'] == source_metadata_digest(s)
                and p['family'] == s['independence_group'], 'source metadata binding')
        section = sections[s['id']][p['section']]; bounds = p['character_range']
        require(len(bounds) == 2 and all(type(x) is int for x in bounds)
                and 0 <= bounds[0] < bounds[1] <= len(section)
                and section[bounds[0]:bounds[1]] == p['quote'], 'section-anchored quotation: ' + pid)
        require(p['locator'] and p['english_rendering'] and p['verification'] == 'primary_inspected_section_and_listed_images',
                'locator, rendering and primary inspection')
        require(p['registered_facsimile_source_id'] == s.get('facsimile_source_id'), 'registered facsimile link')
        image_ids = [i['source_id'] for i in p['images']]
        require(len(image_ids) == len(set(image_ids)), 'unique passage images')
        if s.get('facsimile_source_id'):
            require(s['facsimile_source_id'] in image_ids, 'inspect registered facsimile')
        for image in p['images']:
            meta = registry[image['source_id']]
            require(meta['source_kind'] == 'page_image_of_registered_ocr_text' and meta['format'] in ('jpg', 'png')
                    and meta['independence_group'] == p['family']
                    and image['path'] == meta['path'] and image['sha256'] == meta['sha256']
                    and image['metadata_sha256'] == source_metadata_digest(meta), 'bound image and source family')
            if image['path'] not in checked_files:
                require(digest(root / image['path']) == image['sha256'], 'image raw hash')
                checked_files.add(image['path'])
            images.add(image['source_id'])
    inspection = data['inspection']
    require(inspection['images_inspected'] == sorted(images) and inspection['source_fetches'] == inspection['new_sources'] == 0
            and inspection['separate_review'] is False, 'actual source/inspection scope')
    rows = data['components']
    require(len(rows) == len({r['id'] for r in rows}), 'unique component IDs')
    require({(r['battle_id'], r['side']) for r in rows} == {(b, s) for b in ids for s in ('A', 'B')},
            'complete eight-side coverage')
    used = set()
    for row in rows:
        used.update(validate_component(row, passages, ids, protocol))
    require(used == set(passages), 'all adopted passages linked, no orphan evidence')
    for battle in ids:
        families = {passages[pid]['family'] for r in rows if r['battle_id'] == battle
                    for field in ('objective_evidence', 'result_evidence', 'context_evidence') for pid in r[field]}
        require(len(families) <= 2, 'at most two narrative families plus frozen Bodart frame per entry')
    expected = []
    for battle in ids:
        d = read_json(root / f'data/napoleonic/evidence/{battle}.json')
        for c in d['claims']:
            if c['dimension'] == 'objectives':
                expected.append((battle, c))
    prior = data['prior_objective_claims']
    require([(r['battle_id'], r['claim_id']) for r in prior] == [(b, c['id']) for b, c in expected],
            'all prior objective claims indexed')
    for row, (battle, claim) in zip(prior, expected):
        require(row['dossier_sha256'] == digest(root / f'data/napoleonic/evidence/{battle}.json')
                and row['status'] == claim['status'], 'unchanged prior dossier/status')
        require([r['citation_index'] for r in row['citations']] == list(range(len(claim['citations']))),
                'all prior citations accounted for')
        for r, c in zip(row['citations'], claim['citations']):
            expected_refs = [pid for pid, p in passages.items() if p['source_id'] == c['source_id']
                             and p['section'] == c['section'] and (c['quote'] in p['quote'] or p['quote'] in c['quote'])]
            require(r['source_id'] == c['source_id'] and r['section'] == c['section']
                    and r['prior_quote_sha256'] == hashlib.sha256(c['quote'].encode()).hexdigest()
                    and r['adopted_passages'] == expected_refs, 'honest prior citation disposition')
            require(r['disposition'] == ('used_for_bounded_pilot' if expected_refs else 'prior_reference_only')
                    and r['note'], 'prior pointer is not new verification')
    return {'kind': 'napoleonic_objective_feasibility_pilot', 'version': 1, 'verification': 'primary',
            'input_sha256': {p: digest(root / p) for p in (SCOPE, PROTOCOL, OBSERVATIONS, CODE)},
            'scope': scope, 'observations': data, 'profile': profile(data, ids),
            'decision': {'descriptive_components': 'retain_with_source_scope_and_gaps',
                         'common_numerical_grade': 'not_supported_by_this_pilot',
                         'reason': 'Reported intentions, prescribed actions, expected consequences and inferred dispositions '
                                   'have different criteria and windows; several results or criteria are unestablished. '
                                   'No common value scale or aggregation is defended.',
                         'historical_fits': 0, 'features_admitted': 0, 'reserved_final_entries_used': 0,
                         'stopping_disposition': data['stopping_disposition']}}


def report(bundle):
    data = bundle['observations']; p = bundle['profile']
    names = {'B370c': 'Campo Tenese', 'B370d': 'Maida', 'B371a': 'Gaëta', 'B379c': 'Amantea'}
    relations = {'reported_action_executed': 'Reported action carried out',
                 'reported_effect_observed': 'Reported effect observed',
                 'reported_effect_not_observed': 'Stated effect not observed in checked window',
                 'reported_incomplete_or_mixed': 'Partial or qualified correspondence',
                 'not_established': 'Achievement unestablished', 'not_assessable': 'Criterion unestablished'}
    text = ['# Naples objective-and-result pilot v1', '',
            'Primary-verified source encoding; no separate review.', '',
            '**Retain descriptive objective/result components. A common numerical outcome grade is not supported by this pilot.** '
            'The existing sources can distinguish local accomplishment from broader expectations, with explicit gaps. '
            'Their heterogeneous tasks, criteria and windows do not supply an interchangeable measure of victory quality.', '',
            '## Scope and coverage', '',
            f'The complete frozen `third-coalition 1806` group is **{p["entries"]} entries / {p["sides"]} sides**: '
            'Campo Tenese, Maida, Gaëta and Amantea. The group is a research/evaluation grouping, not one command appointment. '
            'Amantea retains its December 1806–February 1807 interval. The owner accepted this group before the pilot; '
            'it is not a representative sample of all 273 development entries.', '',
            f'The [scope](../../{SCOPE}) and [protocol](../../{PROTOCOL}) preceded the completed encoding. '
            f'The [observation record](../../{OBSERVATIONS}) retains **{p["components"]} propositions**, '
            f'**{p["passages"]} adopted passages**, **{p["images_inspected"]} inspected pinned images** and '
            f'**{len(p["adopted_source_families"])} existing author families**. There are no duplicate entry-side coverage keys. '
            'No new source or fetch was required. Reprints, the translated capitulation and multiple pages of a work are not independent witnesses.', '',
            f'The {p["prior_objective_claims"]} prior objective claims and all 49 citation indices remain accounted for: '
            '22 cite an adopted excerpt or containing context; 27 are unchanged prior-reference-only pointers, not newly verified propositions. '
            'The bound dossiers, prepared packet, raw files and prior measurement/model records remain unchanged.', '',
            f'For **{p["reported_before_action_sides"]}/8 sides**, a source reports an intention before the relevant action; '
            f'**{p["inferred_only_sides"]}/8** retains only an inferred disposition. '
            'Gaëta B also has a separate late-siege council intention before further resistance. Its early refusal, '
            'general royal/regency command and later council are not collapsed into one timeless mandate. '
            '**0/8** has an adopted objective supported by a supplied, contemporaneously dated pre-action document. '
            'This concerns the inspected passages, not the survival of all possible archival evidence. '
            'Retrospective reporting may support descriptive history; it does not establish when an intention was recorded or known.', '',
            f'Explicit success criteria remain null for **{len(p["missing_success_criteria"])}/{p["components"]} propositions**. '
            f'**{p["image_checked_passages"]}/{p["passages"]}** adopted passages were checked on pinned images; '
            f'the other **{len(p["ocr_only_passage_ids"])}/{p["passages"]}** are explicitly OCR-only. '
            'Two full-OCR quotations about Damas’s partial junction were checked on the existing p. 396 image; '
            'that paragraph is absent from the old partial figure transcription, which stays unchanged.', '',
            '## Source-linked objective/result table', '',
            'A is France and its allies; B is the opposing side. Each row is one proposition, not an extra engagement or command weight. '
            'The attainment labels describe the relationship between the quoted purpose and reported result. They are neither an ordered rating '
            'nor a count of successes. Unknown is not failure. A prescribed action is different from its military benefit.', '',
            '| Entry / side | Proposition and scope | Reported timing / recording | Reported result and relation | Criterion / material limit | Evidence |',
            '| --- | --- | --- | --- | --- | --- |']
    for row in data['components']:
        refs = list(dict.fromkeys(row['objective_evidence'] + row['result_evidence'] + row['context_evidence']))
        cells = [f'{row["battle_id"]} {names[row["battle_id"]]} / {row["side"]}',
                 f'**{row["id"]}**: {row["objective"]} '
                 f'({row["statement_kind"].replace("_", " ")}; {row["scope_level"].replace("_", " ")})',
                 row['precedence_note'] + ' Later account; no supplied dated pre-action objective document.',
                 row['observed_result'] + ' **' + relations[row['attainment']] + '**',
                 ('Unknown criterion. ' if row['success_criterion'] is None else row['success_criterion'] + ' ') + row['criterion_note'],
                 ', '.join(f'[{pid}](#{pid})' for pid in refs)]
        text.append('| ' + ' | '.join(c.replace('|', '\\|').replace('\n', ' ') for c in cells) + ' |')
    text += ['', '## Interpretation and feasible use', '',
             '**Local results can be recorded without a universal score.** Koch’s reported directive to attack the left corps at Campo Tenese '
             'can be compared with his account of an attack. At Gaëta and Amantea, a reported purpose to take the named place can be linked '
             'to surrender/occupation. These are different kinds of accomplishment, not equally valuable successes or estimates of command contribution.', '',
             '**Partial results and prior-objective uncertainty matter.** Damas describes retirement from Campo Tenese and some joining at the Crati, '
             'with the advanced guard not joining. The planned delay is not measured. His later “inch by inch” judgment is commentary, not a prior mandate. '
             'At Amantea, fidelity language and resistance do not supply the garrison’s prior operational objective or deadline; its side remains in the table.', '',
             '**Maida’s battlefield result does not fulfill the whole expected chain.** Bunbury’s anticipated retreat toward Catanzaro has a qualified '
             'directional match in the reported retreat; arrival timing and causation are unestablished. The general-insurrection criterion remains undefined. '
             'The anticipated relief of Gaëta through abandonment is not observed by the later capitulation/entry. This linked evidence is not another '
             'Maida win or an extra Gaëta outcome weight. Movement from the original French position also prevents treating victory as proof of the planned '
             'camp attack/flank geometry.', '',
             '**A siege’s eventual surrender does not answer every mission.** The late Gaëta council favors holding longer, but the OCR duration '
             '`dix4iait jours*` has no pinned p. 243 facsimile in the allowed set. Its numeric duration stays null; no deadline or mission-failure label '
             'is invented. Colletta’s early higher-command refusal and Koch’s speculative origin account remain distinct. Hotz/Storz and superior/delegated '
             'roles are not reconciled into one exclusive commander.', '',
             '**Capture, speed, redeployment and pacification stay separate.** A surrender does not establish how much a siege was accelerated or that '
             'the entire reported besieging body was used elsewhere. Amantea’s reduction does not prove wider pacification: the source presents a necessary '
             'condition involving more than one town, not sufficiency. Conditional embarkation/non-service terms do not establish permanent force destruction '
             'or later compliance. Koch’s 33 siege days and Colletta’s 40 excluding the first assault keep their different clocks; no efficiency ratio is calculated.', '',
             'These are material measurement limits for a common grade, rather than reasons to discard useful descriptive passages. '
             'No common utility scale, defensible aggregation, complete appointment window, replacement pool or causal identification is supplied here. '
             'Source agreement is not historical adjudication; the translated outcome instrument remains a printed version in Koch’s family. '
             'The OCR-only passages remain listed below, with no correction or claim of unseen facsimile inspection.', '',
             '## Decision and stop', '',
             '**Go for retaining these source-qualified descriptive components; no-go for deriving one common numerical grade from them.** '
             'No scalar, ordinal rank, commander credit, model input or historical fit is produced. All 52 final entries remain unused numerically. '
             'The strict-opening, identity and 1805 appointment/window branches keep their existing stopped/paused dispositions. '
             'This pilot ends with the table and decision; no wider extraction, new source search or run follows automatically.', '',
             '## Exact adopted passages and provenance', '',
             'English renderings below are the primary agent’s translations/paraphrases. Original quotations retain their source wording and OCR defects. '
             'Every raw and metadata hash is SHA-256. A manually linked context image is distinguished from a registered transcription/facsimile link.', '']
    for pid, passage in data['passages'].items():
        text += [f'### {pid}', '',
                 f'`{passage["source_id"]}`; section `{passage["section"]}`; {passage["locator"]}. '
                 f'Characters `{passage["character_range"][0]}:{passage["character_range"][1]}` of the pinned section.', '',
                 '> ' + passage['quote'], '', 'Primary English rendering: ' + passage['english_rendering'], '',
                 f'Raw SHA-256: `{passage["raw_sha256"]}`. Metadata SHA-256: `{passage["metadata_sha256"]}`. '
                 f'Family: `{passage["family"]}`.']
        if passage['images']:
            for image in passage['images']:
                basis = 'registered facsimile' if image['source_id'] == passage['registered_facsimile_source_id'] else 'manually linked existing context image'
                text += [f'Inspected [{image["source_id"]}](../../{image["path"]}) ({basis}); '
                         f'image SHA-256 `{image["sha256"]}`; metadata SHA-256 `{image["metadata_sha256"]}`.']
        else:
            text += ['**OCR-only adopted passage; no pinned page image inspected for this passage.**']
        if passage['note']:
            text += [passage['note']]
        text += ['']
    text += ['## Reproduction and limits of verification', '',
             f'- `python3 -m generalship.napoleonic_objectives` checks the fixed scope/protocol/observations, source/metadata/image hashes, '
             'section ranges, four entries/eight sides, all prior objective references, explicit nulls and non-promotion.',
             '- `python3 -m generalship.napoleonic_objectives --write` regenerates this report and the JSON artifact offline.',
             f'- The [audit notebook](napoleonic-naples-objective-audit-v1.ipynb) independently recounts keys, temporal provenance, null criteria '
             'and relation categories, and checks the material partial/unknown cases. Its code cells execute top to bottom with the Python standard library; '
             'saved outputs are checked by tests. Optional notebook packages are not required.',
             '- `make reproduce` regenerates the repository; `make check` tests the contracts and saved artifacts. Neither runs historical fitting jobs.',
             '', 'The automated checks establish byte identity, linkage and accounting. Primary source inspection supports this encoding; '
             'neither establishes historical truth, independent corroboration, sincere prior intent or causal attribution.', '']
    return '\n'.join(text)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    bundle = build(root); rendered = report(bundle)
    if args.write:
        write_json(root / ARTIFACT, bundle)
        (root / REPORT).write_text(rendered, encoding='utf-8')
    else:
        require(read_json(root / ARTIFACT) == bundle, 'saved artifact differs')
        require((root / REPORT).read_text() == rendered, 'saved report differs')
    print('Naples objective pilot: 4 entries / 8 sides; descriptive components retained; no common numerical grade.')


if __name__ == '__main__':
    main()
