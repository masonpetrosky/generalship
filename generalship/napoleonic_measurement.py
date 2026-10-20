"""Bounded combined strength/time/authority measurement; never emits model inputs."""

import argparse
import math
from pathlib import Path

from .evidence import citation_text
from .sources import (digest, read_json, safe_path, source_document_date,
                      source_metadata_digest, validate_source_metadata, write_json)

BASE = 'data/napoleonic/peninsula-1812-measurement-v1'
SCOPE = BASE + '/scope.json'
RECORDS = BASE + '/records.json'
SNAPSHOT = BASE + '/source-snapshot.json'
DESIGN = 'docs/napoleonic-peninsula-1812-measurement-v1.md'
REPORT = 'artifacts/napoleonic-peninsula-1812-measurement-v1'
CODE = ('generalship/napoleonic_measurement.py', 'tests/test_napoleonic_measurement.py')
INDEX = 'artifacts/napoleonic-blocker-inventory-v1.json'
FRAME = 'data/napoleonic/frame-v1.json'
COHORT = 'data/napoleonic/cohort-v1.json'
PARTITION = 'data/napoleonic/methods-v1/evaluation.json'
SOURCES = 'data/sources.json'


def require(value, message):
    if not value:
        raise ValueError('Napoleonic combined measurement: ' + message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def indexed(rows):
    require(isinstance(rows, list) and all(isinstance(r, dict) and nonempty(r.get('id')) for r in rows), 'invalid record index')
    require(len({r['id'] for r in rows}) == len(rows), 'duplicate record ID')
    return {r['id']: r for r in rows}


def validate(root, proposal=None):
    root = Path(root)
    scope = read_json(root / SCOPE)
    require(scope['kind'] == 'napoleonic_combined_measurement_scope' and scope['version'] == 1
            and scope['status'] == 'measurement_only', 'scope identity/status')
    inventory = read_json(root / INDEX)
    group = next(g for g in inventory['groups'] if g['campaign'] == inventory['selected_campaign'])
    battles = scope['battle_ids']
    require(scope['selected_campaign'] == group['campaign'] == 'peninsula 1812'
            and battles == group['battle_ids'] and (scope['engagements'], scope['sides']) == (8, 16), 'scope expanded/changed')
    paths = {FRAME, COHORT, PARTITION, SOURCES, INDEX,
             'data/napoleonic/blocker-inventory-v1/scope.json',
             'data/napoleonic/blocker-inventory-v1/verification.json'}
    paths |= {f'data/napoleonic/evidence/{b}.json' for b in battles}
    require(set(scope['bindings']) == paths, 'incomplete scope bindings')
    for path, sha in scope['bindings'].items():
        require(digest(safe_path(root, path)) == sha, 'changed bound input: ' + path)
    partition = read_json(root / PARTITION)
    require(set(battles) <= set(partition['development']) and not set(battles) & set(partition['reserved_final']), 'final reservation entered measurement')
    require(scope['authorization']['owner_message'] == 'Sounds good, go ahead'
            and all(scope['authorization'][k] is False for k in (
                'new_source_fetching', 'feature_admission', 'historical_outcome_fit',
                'calibration_scoring', 'separate_review', 'subagents')), 'authorization exceeded')
    data = read_json(root / RECORDS) if proposal is None else proposal
    require(data['kind'] == 'napoleonic_combined_measurement' and data['version'] == 1
            and data['status'] == 'measurement_only', 'record identity/status')
    require(data['scope_sha256'] == digest(root / SCOPE) and data['design_sha256'] == digest(root / DESIGN)
            and data['source_snapshot_sha256'] == digest(root / SNAPSHOT), 'record input binding')
    require(data['emitted_model_rows'] == [] and data['historical_outcomes_fitted'] is False
            and data['calibration'] == 'prepared_unscored', 'measurement cannot promote or fit')
    registry = {s['id']: s for s in read_json(root / SOURCES)['sources']}
    snapshot = read_json(root / SNAPSHOT)
    require(snapshot['kind'] == 'napoleonic_measurement_source_snapshot' and snapshot['version'] == 1, 'snapshot identity')
    sources = indexed(snapshot['sources'])
    for sid, source in sources.items():
        require(source == registry[sid] and digest(safe_path(root, source['path'])) == source['sha256'], 'changed source metadata/raw: ' + sid)
    validate_source_metadata(root, sources)
    dossiers = {b: read_json(root / f'data/napoleonic/evidence/{b}.json') for b in battles}
    claims = {(b, c['id']): c for b, d in dossiers.items() for c in d['claims']}
    expected = {(b, c['id']) for b, d in dossiers.items() for c in d['claims']
                if c['dimension'] in {'strength', 'responsibility'}}
    passages = indexed(data['passages'])
    images, original_refs, used_sources, texts = set(), set(), set(), {}
    for p in passages.values():
        require(p['battle_ids'] and len(set(p['battle_ids'])) == len(p['battle_ids'])
                and set(p['battle_ids']) <= set(battles), 'passage outside scope')
        cite = p['citation']
        s, im = sources[cite['source_id']], sources[p['image_source_id']]
        require(p['raw_sha256'] == s['sha256'] and p['metadata_sha256'] == source_metadata_digest(s)
                and p['image_sha256'] == im['sha256'] and im['format'] in {'jpg', 'jpeg', 'png'}, 'passage source/image hash')
        require(p['document_date'] == source_document_date(s, cite.get('section')), 'document date is not event time')
        key = s['id'], cite.get('section')
        if key not in texts:
            texts[key] = citation_text(root, sources, cite)
        require(nonempty(cite['quote']) and cite['quote'] in texts[key] and nonempty(cite['locator']), 'quote/locator missing')
        require(p['english_interpretations'] and all(map(nonempty, p['english_interpretations'])), 'missing English interpretation')
        require(p['origins'], 'passage provenance missing')
        for origin in p['origins']:
            if origin['kind'] == 'dossier_citation':
                pair = origin['battle_id'], origin['claim_id']
                require(pair in expected and origin['battle_id'] in p['battle_ids'], 'unindexed claim origin')
                claim = claims[pair]
                require(claim['citations'][origin['citation_index']] == cite, 'original citation altered')
                expected_image = ('bodart-1908-' + cite['section'] + '-image-v1'
                                  if s['id'] == 'bodart-1908-transcription-v1' else s.get('facsimile_source_id'))
                require(expected_image == im['id'], 'dossier passage wrong page')
                original_refs.add((*pair, origin['citation_index']))
            elif origin['kind'] == 'existing_parent_context':
                via = sources[origin['via_source_id']]
                require(via['parent_source_id'] == s['id'] and via['facsimile_source_id'] == im['id']
                        and im['parent_source_id'] == s['id'] and im['parent_sha256'] == s['sha256'], 'context parent/page lineage')
                require(all(type(origin[k]) is int for k in ('start', 'end'))
                        and 0 <= origin['start'] < origin['end'], 'context range')
                raw = (root / s['path']).read_text(encoding='utf-8')
                require(origin['end'] <= len(raw) and raw[origin['start']:origin['end']] == cite['quote'], 'context substring drift')
                require('printed p.' in cite['locator'] and im['id'] in cite['locator'], 'context page locator missing')
                used_sources.add(via['id'])
            else:
                require(False, 'unknown passage origin')
        images.add(im['id']); used_sources.update((s['id'], im['id']))
    require(images == set(scope['inspected_image_ids']) and len(images) == len(scope['inspected_image_ids']) == 28, 'inspected page denominator changed')
    expected_refs = {(b, cid, i) for b, cid in expected for i in range(len(claims[b, cid]['citations']))}
    require(original_refs == expected_refs, 'original strength/authority citation coverage')
    used = set()

    def evidence(ids, battle, allow_empty=False):
        require(isinstance(ids, list) and len(ids) == len(set(ids)) and (ids or allow_empty)
                and all(k in passages and battle in passages[k]['battle_ids'] for k in ids), 'evidence reference/entry mismatch')
        used.update(ids)

    obs = indexed(data['observations'])
    for row in obs.values():
        pair = row['battle_id'], row['claim_id']
        require(pair in expected and row['side'] in {'A', 'B'} and row['kind'] in {'strength', 'authority'}, 'observation scope/type')
        require(all(nonempty(row[k]) for k in ('population_or_scope', 'reported_time', 'source_role', 'note'))
                and row['resolved_person_id'] is None, 'observation interpretation/global identity')
        if row['kind'] == 'strength':
            require(row['unit'] == 'people' and row['actor_label'] is None and row['authority_type'] is None, 'people/authority type confusion')
            if row['value'] is None:
                require(claims[pair]['status'] == 'unknown' and row['precision'] == 'unknown'
                        and row['source_role'] == 'explicit_unknown' and row['evidence'] == [], 'unknown must stay null without invented evidence')
            else:
                require(type(row['value']) in (int, float) and math.isfinite(row['value']) and row['value'] > 0
                        and row['precision'] in {'reported_point', 'approximate'}, 'invalid strength/precision')
        else:
            require(row['value'] is None and row['unit'] is None and row['precision'] is None
                    and nonempty(row['actor_label']) and nonempty(row['authority_type']), 'authority role fields')
        evidence(row['evidence'], row['battle_id'], allow_empty=row['kind'] == 'strength' and row['value'] is None)
        for k in row['evidence']:
            require(any(o.get('battle_id') == pair[0] and o.get('claim_id') == pair[1]
                        for o in passages[k]['origins']), 'observation not tied to original claim')
    actual_claims = []
    for row in data['claim_index']:
        pair = row['battle_id'], row['claim_id']; actual_claims.append(pair)
        require(pair in expected and row['dimension'] == claims[pair]['dimension'] and row['status'] == claims[pair]['status'], 'claim index changed')
        require(row['observation_ids'] and len(set(row['observation_ids'])) == len(row['observation_ids'])
                and set(row['observation_ids']) == {k for k, o in obs.items() if (o['battle_id'], o['claim_id']) == pair}, 'claim observation accounting')
    require(len(actual_claims) == len(set(actual_claims)) and set(actual_claims) == expected, 'claim denominator incomplete')
    for row in indexed(data['co_reports']).values():
        a, b = obs[row['strength_id']], obs[row['authority_id']]
        require(a['kind'] == 'strength' and a['value'] is not None and b['kind'] == 'authority'
                and a['battle_id'] == b['battle_id'] == row['battle_id'] and a['side'] == b['side'], 'co-report force/entry mismatch')
        shared_images = {passages[k]['image_source_id'] for k in a['evidence']} & {passages[k]['image_source_id'] for k in b['evidence']}
        require(shared_images and row['basis'] == 'same_source_local_context'
                and row['status'] == 'co_reported_not_opening_matched' and nonempty(row['note']), 'co-report cannot cross source page or select opening pair')
    for row in indexed(data['arithmetic_checks']).values():
        require(row['terms'] and all(type(v) in (int, float) and math.isfinite(v) for v in row['terms'])
                and type(row['result']) in (int, float) and math.isfinite(row['result']) and row['result'] >= 0
                and sum(row['terms']) == row['result'] and row['unit'] == 'people', 'arithmetic mismatch')
        require(row['kind'] in {'printed_sum', 'diagnostic_residual'} and row['opening_feature'] is None
                and nonempty(row['note']), 'arithmetic cannot become an opening feature')
        evidence(row['evidence'], row['battle_id'])
    frame = {e['id']: e for e in read_json(root / FRAME)['entries']}
    entries = []
    for row in data['entries']:
        b = row['battle_id']; entries.append(b)
        require(b in battles and row['place'] == frame[b]['place'] and row['frozen_interval'] == {
            'start': frame[b]['start_date'], 'end': frame[b]['end_date']}, 'changed frozen entry/interval')
        require(set(row['area']) == {'inside_proposed', 'outside_proposed', 'unresolved'}
                and all(v and all(map(nonempty, v)) for v in row['area'].values()), 'area/unknowns omitted')
        require(row['boundary_candidates'] and row['findings'] and nonempty(row['stopping_reason']), 'entry stopping/boundary record omitted')
        for candidate in indexed(row['boundary_candidates']).values():
            require(candidate['status'] == 'source_relative_only' and nonempty(candidate['label'])
                    and nonempty(candidate['reported_time']), 'unjustified selected/synchronized boundary')
            evidence(candidate['evidence'], b)
        for finding in row['findings']:
            require(nonempty(finding['text']), 'empty finding')
            evidence(finding['evidence'], b)
    require(len(entries) == len(set(entries)) == 8 and set(entries) == set(battles), 'complete campaign accounting')
    pairs = []
    for row in data['side_records']:
        pair = row['battle_id'], row['side']; pairs.append(pair)
        require(pair[0] in battles and pair[1] in {'A', 'B'} and row['status'] == 'blocked', 'side status/scope')
        require(all(row[k] is None for k in ('selected_boundary', 'selected_strength', 'selected_person_id', 'army_id')), 'side cannot select or impute a model input')
        require(set(row['blockers']) == {'joint_boundary_and_area', 'complete_population', 'authority_and_identity', 'army_continuity'}
                and all(map(nonempty, row['blockers'].values())), 'side blockers missing')
        for kind, key in (('strength', 'strength_ids'), ('authority', 'authority_ids')):
            require(row[key] and len(set(row[key])) == len(row[key]) and set(row[key]) == {
                k for k, o in obs.items() if (o['battle_id'], o['side']) == pair and o['kind'] == kind}, 'side observation omission/mismatch')
        evidence(row['evidence'], pair[0])
    require(len(pairs) == len(set(pairs)) == 16 and set(pairs) == {(b, s) for b in battles for s in ('A', 'B')}, 'sixteen-side denominator')
    require(used == passages.keys(), 'orphan adopted passage')
    for b in battles:
        families = {sources[p['citation']['source_id']]['independence_group'] for p in passages.values() if b in p['battle_ids']}
        require(len(families) <= 3, 'per-entry source-family ceiling exceeded')
    # Verify the exact parent/facsimile closure, not a padded witness inventory.
    pending = list(used_sources)
    while pending:
        s = sources[pending.pop()]
        refs = [s.get(k) for k in ('parent_source_id', 'facsimile_source_id', 'document_date_basis_source_id')]
        if isinstance(s.get('supersedes'), dict):
            refs.append(s['supersedes'].get('source_id'))
        for key in refs:
            if key and key not in used_sources:
                used_sources.add(key); pending.append(key)
    require(used_sources == sources.keys(), 'source snapshot closure mismatch')
    return data


def build(root):
    root = Path(root)
    data = validate(root)
    obs = data['observations']
    return {'kind': 'napoleonic_combined_measurement_report', 'version': 1, 'verification': 'primary-verified',
            'bindings': {p: digest(root / p) for p in (SCOPE, RECORDS, SNAPSHOT, DESIGN, *CODE)},
            'counts': {'entries': len(data['entries']), 'sides': len(data['side_records']),
                       'indexed_claims': len(data['claim_index']), 'passages': len(data['passages']),
                       'images': len({p['image_source_id'] for p in data['passages']}),
                       'source_metadata_records': len(read_json(root / SNAPSHOT)['sources']),
                       'strength_observations': sum(o['kind'] == 'strength' for o in obs),
                       'known_strength_observations': sum(o['kind'] == 'strength' and o['value'] is not None for o in obs),
                       'explicit_strength_unknowns': sum(o['kind'] == 'strength' and o['value'] is None for o in obs),
                       'authority_appearances': sum(o['kind'] == 'authority' for o in obs),
                       'source_local_co_reports': len(data['co_reports']),
                       'arithmetic_checks': len(data['arithmetic_checks']),
                       'blocked_sides': sum(r['status'] == 'blocked' for r in data['side_records']),
                       'complete_opening_pairs': 0, 'emitted_model_rows': 0},
            'records': data}


def markdown(report):
    c, d = report['counts'], report['records']
    lines = ['# Peninsula 1812 combined measurement pass v1', '',
             'Primary-verified, existing pinned evidence only. This campaign pass stops here.', '',
             f"**{c['entries']} complete-group entries / {c['sides']} sides**; all {c['indexed_claims']} strength/responsibility claims indexed. {c['passages']} adopted passages on {c['images']} re-inspected full page images, with {c['source_metadata_records']} existing metadata records in the frozen closure.", '',
             f"**Result: {c['source_local_co_reports']} source-local associations between troop totals and named roles; {c['complete_opening_pairs']} complete opening pairs. All {c['blocked_sides']} side mappings remain blocked.** The table preserves {c['known_strength_observations']} numerical strength observations, {c['explicit_strength_unknowns']} explicit strength unknowns and {c['authority_appearances']} authority appearances. Appearances are not distinct people. Selected boundary/strength/person/army remain null; model rows emitted: 0.", '',
             'A co-report associates a source’s people total and actor role locally. It does not establish complete combat-unit personnel at first hostile contact, an effective appointment interval, global person identity or army continuity. Mixed garrisons, infantry bayonets, wider armies, later reinforcements and retrospective reconstructions remain separate.', '',
             '## Complete campaign findings', '',
             '| Entry | Boundary/area inspection | Complete opening mappings |', '| --- | --- | --- |']
    for e in d['entries']:
        lines.append(f"| `{e['battle_id']}` {e['place']} | " + '; '.join(x['label'] + ' — ' + x['reported_time'] for x in e['boundary_candidates']) + ' | A blocked; B blocked |')
    for e in d['entries']:
        lines += ['', '## ' + e['battle_id'] + ' ' + e['place'], '',
                  'Frozen interval: `' + str(e['frozen_interval']['start']) + '` to `' + str(e['frozen_interval']['end']) + '`.', '']
        lines += ['- ' + f['text'] + ' Passage IDs: ' + ', '.join('`' + p + '`' for p in f['evidence']) + '.' for f in e['findings']]
        lines += ['', '**Proposed area:** ' + '; '.join(e['area']['inside_proposed']) + '. Outside: ' + '; '.join(e['area']['outside_proposed']) + '. Unresolved: ' + '; '.join(e['area']['unresolved']) + '.', '',
                  '| Observation | Side | Amount or actor/role | Source population/scope and time | Remaining limit |', '| --- | --- | --- | --- | --- |']
        for o in d['observations']:
            if o['battle_id'] != e['battle_id']:
                continue
            value = ('unknown' if o['value'] is None else str(o['value']) + ' people (' + o['precision'] + ')') if o['kind'] == 'strength' else o['actor_label'] + ' / ' + o['authority_type']
            evidence_text = ', '.join('`' + p + '`' for p in o['evidence']) if o['evidence'] else 'none; explicit unknown'
            lines.append(f"| `{o['id']}` | {o['side']} | {value} | {o['population_or_scope']}; {o['reported_time']} | {o['note']} Evidence: " + evidence_text + ' |')
        lines += ['', '**Side blockers:**', '']
        for side in [s for s in d['side_records'] if s['battle_id'] == e['battle_id']]:
            lines.append('- **' + side['side'] + ':** ' + ' '.join(side['blockers'].values()))
    lines += ['', '## Source-local co-reports', '', '| Case | Strength / authority | What remains unestablished |', '| --- | --- | --- |']
    for r in d['co_reports']:
        lines.append(f"| `{r['id']}` | `{r['strength_id']}` / `{r['authority_id']}` | {r['note']} |")
    lines += ['', '## Arithmetic', '', '| Check | Terms | Result | Disposition |', '| --- | --- | ---: | --- |']
    for a in d['arithmetic_checks']:
        lines.append(f"| `{a['id']}` | " + ' + '.join(str(x) if x >= 0 else '(' + str(x) + ')' for x in a['terms']) + f" | {a['result']} | {a['note']} |")
    lines += ['', '## Passage index', '',
              'The companion JSON retains exact original quotes, marked English interpretations, source metadata, section dates, image hashes, original claim/citation indices and exact raw OCR ranges for additional context. These are inspected AI interpretations, not human adjudication or independent corroboration.', '',
              '| ID | Entry | Source / section / locator | Inspected image |', '| --- | --- | --- | --- |']
    for p in d['passages']:
        cite = p['citation']
        lines.append(f"| `{p['id']}` | " + ', '.join(p['battle_ids']) + f" | `{cite['source_id']}` / {cite.get('section') or 'unsectioned exact OCR substring'} / {cite['locator']} | `{p['image_source_id']}` |")
    lines += ['', '## Stop and remaining limits', '',
              'Stop after these eight entries. No original local return or new order was fetched; mediated originals, full appointment clocks, complete opening populations and cross-entry army identities remain unresolved. Existing dossiers, prepared packet, earlier measurement/inventory records, raw inputs and historical/synthetic results retain their bytes. This pass does not score calibration or admit features.', '',
              'The next useful action is a bounded feasibility checkpoint using the two completed measurement groups (12 entries/24 sides), distinguishing reusable local associations from the specific boundary/population/authority/army evidence needed for the strict opening target. Decide the research or methodological implication before wider extraction; no automatic follow-up series or historical fit is queued.', '']
    return '\n'.join(lines)


def check(root):
    root = Path(root)
    report = build(root)
    require(read_json(root / (REPORT + '.json')) == report, 'stale JSON report; run make reproduce')
    require((root / (REPORT + '.md')).read_text(encoding='utf-8') == markdown(report), 'stale Markdown report; run make reproduce')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    if args.write:
        report = build(root)
        write_json(root / (REPORT + '.json'), report)
        (root / (REPORT + '.md')).write_text(markdown(report), encoding='utf-8')
    else:
        report = check(root)
    print('Peninsula 1812 measurement: ' + str(report['counts']))


if __name__ == '__main__':
    main()
