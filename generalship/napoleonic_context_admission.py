"""Offline, non-promoting audit of the complete 1805 context-code group."""

import argparse
from collections import Counter
from pathlib import Path

from .sources import (digest, read_json, source_document_date,
                      source_metadata_digest, text_sections, write_json)

BASE = 'data/napoleonic/context-admission-v1/'
SCOPE, PROTOCOL, SNAPSHOT, OBSERVATIONS = (BASE + name + '.json' for name in
                                         ('scope', 'protocol', 'snapshot', 'observations'))
FROZEN = {
    SCOPE: '2fd62ae480f57925d67d6988bc00e20a9642e3f38bc8080ffd71901b5af7ec21',
    PROTOCOL: 'ce232355d2026d0710b40f59f079113cb79f4fdd22a37bd59d397ff5d7bfd71e',
    SNAPSHOT: '357bdb2e33124cd76246db4c43ed5baafc87af7ff8c0b361843644085bfa75e9',
    OBSERVATIONS: '2928317f09ca70da2c82d775f761d86a0a47b443d3acdb5b6c92a17c9a39a1db',
}
CODE = 'generalship/napoleonic_context_admission.py'
ARTIFACT = 'artifacts/napoleonic-1805-context-admission-v1.json'
REPORT = 'docs/research/napoleonic-1805-context-admission-v1.md'
NOTEBOOK = 'docs/research/napoleonic-1805-context-admission-audit-v1.ipynb'
STATUSES = ('eligible_candidate', 'blocked', 'excluded')
DIMENSIONS = ('posture', 'fortification')


def require(condition, message):
    if not condition:
        raise ValueError('1805 context audit: ' + message)


def field_rows(claims, entries):
    """Aggregate alternatives without treating citations as votes or extra rows."""
    fields = []
    for bid in entries:
        for dim in DIMENSIONS:
            alternatives = [c for c in claims if c['battle_id'] == bid and c['dimension'] == dim]
            require(alternatives, 'complete engagement-field coverage')
            states = {c['audit_status'] for c in alternatives}
            usable = {c['original_code'] for c in alternatives if c['audit_status'] == 'eligible_candidate'}
            if states == {'excluded'}:
                status = 'excluded'
            elif 'blocked' in states or len(usable) != 1:
                status = 'blocked'
            else:
                status = 'eligible_candidate'
            fields.append({'battle_id': bid, 'dimension': dim, 'audit_status': status,
                           'candidate_code': next(iter(usable)) if status == 'eligible_candidate' else None,
                           'claim_ids': [c['claim_id'] for c in alternatives],
                           'alternative_codes': list(dict.fromkeys(c['original_code'] for c in alternatives)),
                           'physical_absence': {'A': None, 'B': None}})
    return fields


def profile(data, snapshot):
    claims = data['claims']; fields = field_rows(claims, data['entry_ids'])
    statuses = lambda rows: {s: sum(c['audit_status'] == s for c in rows) for s in STATUSES}
    all_citations = [c for d in snapshot['dossiers'] for claim in d['claims'] for c in claim['citations']]
    prior_sources = {c['source_id'] for c in all_citations}
    images = {p['registered_facsimile_source_id'] for p in data['passages'].values()
              if p['registered_facsimile_source_id']}
    complete = [bid for bid in data['entry_ids'] if all(f['audit_status'] == 'eligible_candidate'
                                                    for f in fields if f['battle_id'] == bid)]
    return {'entries': len(data['entry_ids']), 'engagement_fields': len(fields), 'source_claims': len(claims),
            'field_status_counts': statuses(fields), 'claim_status_counts': statuses(claims),
            'by_dimension': {dim: statuses([f for f in fields if f['dimension'] == dim]) for dim in DIMENSIONS},
            'complete_joint_entry_ids': complete,
            'fortification_candidate_entry_ids': [f['battle_id'] for f in fields if f['dimension'] == 'fortification'
                                                 and f['audit_status'] == 'eligible_candidate'],
            'prior_citation_occurrences': len(all_citations),
            'unique_prior_passages': len({tuple(sorted(c.items())) for c in all_citations}),
            'extra_context_passages': len(data['passages']) - len({tuple(sorted(c.items())) for c in all_citations}),
            'text_sources': len(prior_sources), 'registered_facsimiles': len(images),
            'images_reinspected': len(data['inspection']['images_reinspected']),
            'source_family_groups': sorted({snapshot['sources'][sid]['record']['independence_group']
                                            for sid in prior_sources}),
            'facsimile_reinspected_passages': sum(p['facsimile_reinspected'] for p in data['passages'].values()),
            'passages_without_registered_facsimile': sum(not p['registered_facsimile_source_id']
                                                        for p in data['passages'].values()),
            'historical_fits': 0, 'model_rows_emitted': 0, 'features_admitted': 0, 'reserved_final_entries_used': 0,
            'fields': fields}


def build(root):
    for path, sha in FROZEN.items():
        require(digest(root / path) == sha, 'changed frozen record: ' + path)
    scope, protocol, snapshot, data = (read_json(root / p) for p in FROZEN)
    for path, sha in scope['bindings'].items():
        require(digest(root / path) == sha, 'changed bound input: ' + path)
    partition = read_json(root / 'data/napoleonic/methods-v1/evaluation.json')
    ids = scope['entry_ids']
    require(scope['campaign_group'] == 'third-coalition 1805' and len(ids) == len(set(ids)) == 22
            and ids == partition['frozen_groups'][scope['campaign_group']]
            and set(ids) <= set(partition['development']) and not set(ids) & set(partition['reserved_final']),
            'whole frozen development group')
    require(scope['dimensions'] == list(DIMENSIONS) and scope['verification'] == 'primary'
            and scope['source_fetching'] is scope['historical_fits_authorized'] is scope['reserved_final_numerical_use'] is False
            and scope['features_admitted'] == 0, 'bounded primary non-promoting scope')
    require(data['entry_ids'] == snapshot['entry_ids'] == ids
            and data['scope_sha256'] == FROZEN[SCOPE] and data['protocol_sha256'] == FROZEN[PROTOCOL]
            and data['snapshot_sha256'] == FROZEN[SNAPSHOT], 'record bindings')
    require(protocol['posture_target'].startswith('Audit the existing realized-offensive-role code')
            and 'never unfortified or two zero indicators' in protocol['fortification_target'], 'frozen variable meanings')
    require(data['verification'] == 'primary' and data['historical_fits'] == data['features_admitted']
            == data['model_rows_emitted'] == data['reserved_final_entries_used'] == 0
            and data['commander_credit'] is data['selection_weights'] is None, 'no model, release, weights or causal credit')
    registry = {s['id']: s for s in read_json(root / 'data/sources.json')['sources']}
    for sid, binding in snapshot['sources'].items():
        s = binding['record']
        require(registry[sid] == s and source_metadata_digest(s) == binding['metadata_sha256'], 'source metadata binding')
        require(digest(root / s['path']) == s['sha256'], 'source raw hash: ' + sid)
    entries = {e['battle_id']: e for e in data['entries']}
    require(list(entries) == ids and len(data['entries']) == len(ids), 'unique complete entry observations')
    passages = data['passages']; sections = {}; prior_keys = set(); used = set()
    reinspected = data['inspection']['images_reinspected']
    require(len(reinspected) == len(set(reinspected)) and all(s in snapshot['sources'] and
            snapshot['sources'][s]['record']['format'] in ('jpg', 'png') for s in reinspected), 'listed image inspections')
    for pid, p in passages.items():
        s = snapshot['sources'][p['source_id']]['record']
        if s['id'] not in sections:
            sections[s['id']] = text_sections((root / s['path']).read_text(encoding='utf-8'))
        bounds = p['character_range']; text = sections[s['id']][p['section']]
        require(len(bounds) == 2 and all(type(x) is int for x in bounds)
                and 0 <= bounds[0] < bounds[1] <= len(text) and text[bounds[0]:bounds[1]] == p['quote'],
                'section-anchored quotation: ' + pid)
        require(p['raw_sha256'] == s['sha256'] and p['metadata_sha256'] == source_metadata_digest(s)
                and p['family'] == s['independence_group'], 'passage metadata binding')
        require(p['document_date'] == source_document_date(s, p['section'])
                and p['publication_year'] == s.get('publication_year'), 'document date is not event or receipt date')
        fac = s.get('facsimile_source_id')
        require(p['registered_facsimile_source_id'] == fac
                and p['facsimile_raw_sha256'] == (snapshot['sources'][fac]['record']['sha256'] if fac else None)
                and p['facsimile_reinspected'] is (fac in reinspected), 'honest facsimile coverage')
        require(p['locator'] and p['inspection'] == 'primary_inspected_quoted_passage', 'primary passage inspection')
    originals = {}
    require([d['battle_id'] for d in snapshot['dossiers']] == ids, 'snapshot covers whole group')
    for d in snapshot['dossiers']:
        require(digest(root / d['path']) == d['sha256'], 'original dossier is immutable')
        selected = [c for c in read_json(root / d['path'])['claims'] if c['dimension'] in DIMENSIONS]
        require(selected == d['claims'], 'snapshot preserves original claims')
        for c in d['claims']:
            originals[d['battle_id'], c['id']] = c
    keys = [(c['battle_id'], c['claim_id']) for c in data['claims']]
    require(len(keys) == len(set(keys)) and set(keys) == set(originals), 'unique complete source-claim coverage')
    for c in data['claims']:
        original = originals[c['battle_id'], c['claim_id']]; entry = entries[c['battle_id']]
        require(c['dimension'] == original['dimension'] and c['original_code'] == original['code']
                and c['original_phase'] == original['phase'] and c['original_status'] == original['status'], 'unchanged prior claim')
        require(c['audit_status'] in STATUSES and c['reason_codes'] and c['reason'], 'status with explicit reason')
        require(c['physical_absence'] == {'A': None, 'B': None} and c['historical_information_set'] is None,
                'no invented physical absence or command knowledge')
        if c['dimension'] == 'posture':
            require(c['audit_status'] == 'excluded' and c['reason_codes'] == ['realized_action_not_precontact_state'],
                    'realized posture cannot become prior intent')
        elif c['audit_status'] == 'eligible_candidate':
            require(entry['fortification_basis'] == 'source_relative_precontact'
                    and 'source_relative_precontact' in c['reason_codes'] and 'reporting_category_only' in c['reason_codes'],
                    'eligible works require sourced pre-contact scope')
            if c['original_code'] == 'none_named':
                require(entry['position_coverage'] == 'both_side_descriptions', 'none_named needs both position descriptions')
            else:
                require(entry['position_coverage'] == 'named_positive_side', 'named-positive works basis')
        require(len(c['citations']) == len(original['citations'])
                and [r['index'] for r in c['citations']] == list(range(len(original['citations']))),
                'all prior citation occurrences accounted for')
        for old, ref in zip(original['citations'], c['citations']):
            require(ref['passage_id'] in passages and ref['disposition'] == 'inspected_prior_passage', 'prior citation disposition')
            p = passages[ref['passage_id']]
            require(all(p[k] == v for k, v in old.items()), 'literal prior citation identity')
            prior_keys.add(ref['passage_id']); used.add(ref['passage_id'])
    for entry in entries.values():
        require(entry['anchor'] and entry['area'] and entry['fortification_note'] and entry['focus_passages']
                and len(entry['focus_passages']) == len(set(entry['focus_passages']))
                and all(p in passages for p in entry['focus_passages']), 'entry boundary/scope/evidence')
        require(entry['boundary_timestamp'] is entry['knowledge_or_receipt_time'] is entry['causal_credit'] is None
                and entry['physical_absence'] == {'A': None, 'B': None}, 'visible opening/knowledge/absence nulls')
        used.update(entry['focus_passages'])
    require(used == set(passages), 'no orphan passages')
    p = profile(data, snapshot); inspection = data['inspection']
    require(inspection['prior_citation_occurrences_inspected'] == p['prior_citation_occurrences']
            and inspection['unique_prior_passages_inspected'] == len(prior_keys) == p['unique_prior_passages']
            and inspection['new_context_passages_inspected'] == p['extra_context_passages']
            and inspection['text_source_ids'] == sorted(sections), 'exact inspection denominators')
    decision = data['decision']
    require(not p['complete_joint_entry_ids'] and decision['joint_posture_plus_fortification'] ==
            'no_go_for_preparing_unchanged_joint_experiment' and decision['fortification_only'] ==
            'candidate_definitions_retained_not_experiment_authorization', 'decision matches coverage and bounded authority')
    return {'kind': 'napoleonic_context_admission_audit', 'version': 1, 'verification': 'primary',
            'input_sha256': {path: digest(root / path) for path in (*FROZEN, CODE)},
            'source_bindings': {sid: {'path': v['record']['path'], 'sha256': v['record']['sha256'],
                                      'metadata_sha256': v['metadata_sha256']}
                                for sid, v in snapshot['sources'].items()},
            'profile': p, 'decision': decision, 'observations': data}


def report(bundle):
    p = bundle['profile']; data = bundle['observations']; passages = data['passages']
    text = ['# 1805 posture and fortification admission audit v1', '',
            '**Primary-verified proposed-use audit, begun 2026-10-20. No features admitted or historical model fitted.**', '',
            '## Decision', '',
            '**No-go for preparing the unchanged joint posture-plus-fortification prediction experiment.** '
            'The realized-offensive-role variable describes action during the engagement. It cannot be an unchanged '
            'pre-contact condition. This is a variable/use mismatch, not a finding that prior intentions cannot be researched. '
            'A planned-role variable would need its own definition and evidence audit.', '',
            f'All {p["entries"]} frozen entries are retained: {p["engagement_fields"]} engagement-field candidates from '
            f'{p["source_claims"]} source-specific claims. There are **{len(p["complete_joint_entry_ids"])} complete joint rows**. '
            'Source alternatives and repeated citations never add engagements.', '',
            '| Unit | Eligible candidate | Blocked | Excluded | Total |', '| --- | ---: | ---: | ---: | ---: |']
    for dim in DIMENSIONS:
        counts = p['by_dimension'][dim]
        text.append(f'| {dim} fields | ' + ' | '.join(str(counts[s]) for s in STATUSES) + ' | 22 |')
    text += ['| All source claims | ' + ' | '.join(str(p['claim_status_counts'][s]) for s in STATUSES) + ' | 51 |', '',
             'The six fortification candidates are Neresheim (`none_named`), Verona (`both_fortified`), '
             'Caldiero (`B_fortified`), Scharnitz (`B_fortified`), Austerlitz (`A_fortified`) and Steken (`none_named`). '
             'These are source-qualified named-work categories. Neither a positive category nor `none_named` '
             'establishes physical absence for an unmentioned side. No two zero indicators are emitted.', '',
             'The six candidates do not establish a viable modelling sample, a causal fortification effect or a corpus-wide coverage rate. '
             'Any fortification-only design must define reporting/missingness, source and coding sensitivities, coextensive '
             'force/target rows and grouped evaluation before a separately authorized experiment. The compiler-strength '
             'benchmark totals are not silently promoted to opening strengths. **Stop this complete-group audit here.**', '',
             '## Fixed use, scope and evidence', '',
             '- The [scope](../../' + SCOPE + '), [protocol](../../' + PROTOCOL + ') and '
             '[snapshot](../../' + SNAPSHOT + ') were fixed before semantic assessment, at base commit '
             '`e8612ffbefa123d18a22d924fcbeeae8bab81f40`. The sample is the complete earliest development group, '
             '`third-coalition 1805`, not a representative draw from the 273 development entries.',
             '- Proposed use: retrospective pre-engagement prediction of the frozen recorded A-side result. '
             'The boundary is immediately before the first hostile contact belonging to the frozen entry, including outposts. '
             'An exact clock is not required when source-relative ordering is adequate. A null old replacement timestamp '
             'alone does not exclude a claim; a later publication alone does not exclude a reconstruction.',
             '- Relevant works may be beyond the first outpost hit if they were already held within the reported engagement '
             'dispositions. Austerlitz and Caldiero pass on this basis. Permanent construction alone cannot establish '
             'occupation or settle an ambiguous capitulation/operation window.',
             '- Original brief-v3 codes describe realized offensive role and works fought from. This audit separately tests '
             'their proposed pre-contact application, preserving source codes, phase tags and alternatives. A supported '
             'source claim is not an admitted predictor. The existing Civil War admission validator does not implement this profile.',
             '- All 52 reserved-final entries remain unused. No source was fetched, dossier changed, release emitted, '
             'historical fit run, prior experiment replaced or commander credit assigned.', '',
             f'The primary agent read all **{p["prior_citation_occurrences"]} prior citation occurrences / '
             f'{p["unique_prior_passages"]} distinct citation objects**, plus {p["extra_context_passages"]} existing-source context excerpts. '
             f'The {p["text_sources"]} text sources have {p["registered_facsimiles"]} registered facsimile sources; '
             f'**{p["images_reinspected"]} images were visually re-inspected** here. All text and registered image bytes and '
             'complete source metadata were checked against the frozen snapshot. Other images were not newly visually checked. '
             'Quoted-text inspection is not full-volume or new facsimile verification.', '',
             f'There are {len(p["source_family_groups"])} registered author/family groups across the whole campaign, '
             'not that many independent witnesses per entry. Dependency notes remain in the snapshot (including Alombert/Krauss, '
             'Schönhals-derived accounts and the Dürnstein Kotzebue/relation lineage). No source vote or reliability weight is used. '
             'A date of publication/document is distinct from event ordering or historical receipt; command knowledge remains unknown.', '',
             '## All 22 engagement fields', '',
             '| Entry | Original posture alternatives | Posture | Original fortification alternatives | Fortification |',
             '| --- | --- | --- | --- | --- |']
    fields = {(f['battle_id'], f['dimension']): f for f in p['fields']}
    for e in data['entries']:
        a, b = (fields[e['battle_id'], dim] for dim in DIMENSIONS)
        text.append(f'| [{e["battle_id"]} {e["place"]}](#{e["battle_id"].lower()}) | '
                    + ', '.join('`'+v+'`' for v in a['alternative_codes']) + ' | excluded | '
                    + ', '.join('`'+v+'`' for v in b['alternative_codes']) + f' | {b["audit_status"]} |')
    text += ['', 'Excluded means a known incompatible variable or later state. Blocked means an unresolved mapping. '
             'At the field level, an excluded alternative does not override a remaining unknown: Mariazell’s later castle '
             'occupation is excluded, while its whole fortification field remains blocked. The claim counts include '
             '24 excluded realized-posture claims and that one known later-state claim.', '',
             '## Boundary and source-use findings', '']
    for e in data['entries']:
        text += [f'<a id="{e["battle_id"].lower()}"></a>', '', f'### {e["battle_id"]} — {e["place"]}', '',
                 '**Candidate opening:** ' + e['anchor'], '', '**Area:** ' + e['area'], '', e['fortification_note'], '']
        for pid in e['focus_passages']:
            passage = passages[pid]; path = bundle['source_bindings'][passage['source_id']]['path']
            text += [f'- `{pid}` / [{passage["source_id"]}](../../{path}), {passage["locator"]}:',
                     '  > ' + ' '.join(passage['quote'].split()), '']
    text += ['## All 51 source-claim dispositions', '',
             '| Entry / original claim | Original code | Proposed-use status | Reason |', '| --- | --- | --- | --- |']
    for c in data['claims']:
        text.append(f'| {c["battle_id"]} / `{c["claim_id"]}` | `{c["original_code"]}` | '
                    f'{c["audit_status"]} | ' + ', '.join(c['reason_codes']) + ' |')
    text += ['', 'Every original citation occurrence has an indexed inspection disposition in the '
             '[observations](../../' + OBSERVATIONS + '). That record retains every exact quote, section/locator, '
             'character range, raw and metadata SHA-256, document-date null and registered image binding. '
             'The snapshot retains the full original claim and source dependency record. These are primary findings, '
             'not separate or independent review records.', '', '## Source bindings for quoted findings', '',
             'The table below covers every source quoted in the entry findings above. The complete 91-source text '
             'catalogue and 77 image bindings remain in the snapshot; hashes are not independence certificates.', '',
             '| Source / pinned text | Raw SHA-256 | Metadata SHA-256 | Facsimile re-inspected here |',
             '| --- | --- | --- | --- |']
    selected = {pid for e in data['entries'] for pid in e['focus_passages']}
    sources = {}
    for pid in sorted(selected):
        passage = passages[pid]; sources[passage['source_id']] = passage
    for sid in sorted(sources):
        passage = sources[sid]
        path = bundle['source_bindings'][sid]['path']
        text.append(f'| [{sid}](../../{path}) | `{passage["raw_sha256"]}` | `{passage["metadata_sha256"]}` | '
                    + ('yes' if passage['facsimile_reinspected'] else 'no') + ' |')
    text += ['', '### Images actually re-inspected', '',
             '| Image | Raw SHA-256 | Metadata SHA-256 |', '| --- | --- | --- |']
    for sid in data['inspection']['images_reinspected']:
        binding = bundle['source_bindings'][sid]
        text.append(f'| [{sid}](../../{binding["path"]}) | `{binding["sha256"]}` | `{binding["metadata_sha256"]}` |')
    text += ['', '## Reproduction and limits', '',
             '- `python3 -m generalship.napoleonic_context_admission --write` regenerates this report and the JSON artifact '
             'offline. Without `--write` it also checks their saved equality.',
             '- The [executed audit notebook](napoleonic-1805-context-admission-audit-v1.ipynb) independently recounts '
             'the 22/44/51 denominators, alternatives, source references and material cases. Four saved code cells execute '
             'top to bottom using only the Python standard library; tests compare their saved outputs.',
             '- `make check` covers frozen-byte, source/citation, scope, missingness, alternative and non-promotion contracts. '
             '`make reproduce` regenerates the repository without invoking historical or synthetic fitting jobs.', '',
             'Automated checks establish integrity and accounting; primary passage inspection supports this encoding. '
             'Neither guarantees historical truth or unbiased reporting. Fortification reporting can reflect compiler detail, '
             'battle scale, side, publication lineage and outcome; this purposive one-group audit cannot quantify that selection. '
             'Earlier command-created preparation can be a mediator. Prediction, tactical effects and campaign contribution '
             'remain distinct, with no battle/campaign double counting.', '']
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
        require((root / REPORT).read_text(encoding='utf-8') == rendered, 'saved report differs')
    print('1805 context audit: 22 entries / 44 fields / 51 claims; 6 candidate, 16 blocked fortification fields; joint no-go.')


if __name__ == '__main__':
    main()
