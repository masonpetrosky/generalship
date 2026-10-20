"""Development-only field/citation inventory; no historical interpretation or model rows."""

import argparse
from collections import Counter, defaultdict
import hashlib
from pathlib import Path

from .evidence import citation_text
from .sources import digest, read_json, safe_path, source_metadata_digest, write_json

BASE = 'data/napoleonic/blocker-inventory-v1'
SCOPE = BASE + '/scope.json'
DESIGN = 'docs/napoleonic-blocker-inventory-v1.md'
REPORT = 'artifacts/napoleonic-blocker-inventory-v1'
CODE = ('generalship/napoleonic_inventory.py', 'tests/test_napoleonic_inventory.py')
PARTITION = 'data/napoleonic/methods-v1/evaluation.json'
FRAME = 'data/napoleonic/frame-v1.json'
COHORT = 'data/napoleonic/cohort-v1.json'
CONVENTIONS = 'data/napoleonic/methods-v1/research-conventions.json'
SOURCES = 'data/sources.json'
LEDGER = 'data/napoleonic/ledger-design-v1/examples.json'
BOUNDARIES = 'data/napoleonic/boundaries-v1/records.json'
AUTHORITY = 'data/napoleonic/authority-v1/mappings.json'
RELEVANT = ('strength', 'responsibility')
SELECTION = {
    'max_entries': 12,
    'exclude_groups': {'third-coalition 1806':
                       'Four-entry measurement pilot stopped; retain its unresolved mappings.'},
    'require_non_frame_strength_and_command_citations_per_entry': True,
    'require_linked_images_for_all_non_frame_relevant_citations': True,
    'order': ['non_frame_image_ids_ascending', 'entries_ascending', 'group_name_ascending'],
    'frame_source_family': 'bodart-kriegs-lexikon-1908',
}


def require(condition, message):
    if not condition:
        raise ValueError('Napoleonic inventory: ' + message)


def groups_for_partition(frame, cohort, partition):
    """Use IDs/year/campaign only, never outcome or commander fields."""
    entries = {r['id']: r for r in frame['entries']}
    ids = cohort['battle_ids']
    dev, final = partition['development'], partition['reserved_final']
    require(len(ids) == len(set(ids)) and len(dev) == len(set(dev))
            and len(final) == len(set(final)), 'duplicate partition/cohort IDs')
    require(not set(dev) & set(final) and set(dev) | set(final) == set(ids), 'partition coverage')
    require(all(entries[b]['start_year'] <= 1813 for b in dev)
            and all(entries[b]['start_year'] >= 1814 for b in final), 'partition year boundary')
    all_groups = defaultdict(list)
    for b in ids:
        all_groups[entries[b]['campaign_group']].append(b)
    require(dict(sorted(all_groups.items())) == partition['frozen_groups'], 'changed complete groups')
    require(all(set(v) <= set(dev) or set(v) <= set(final) for v in all_groups.values()),
            'campaign split between development and final')
    return {k: v for k, v in sorted(all_groups.items()) if set(v) <= set(dev)}


def field_state(record, field):
    return 'absent' if field not in record else 'null' if record[field] is None else 'recorded'


def typed_field(record, field):
    if field not in record:
        return {'state': 'absent', 'records': 0}
    require(isinstance(record[field], list), 'typed field must be an array: ' + field)
    return {'state': 'recorded', 'records': len(record[field])}


def pilot_index(ledger, boundary, authority):
    index = {}
    for force in authority['forces']:
        pair = force['battle_id'], force['side']
        require(pair not in index, 'duplicate indexed pilot side')
        b = [r for r in boundary['sides'] if (r['battle_id'], r['side']) == pair]
        require(len(b) == 1, 'pilot side missing boundary record')
        index[pair] = {
            'record_path': AUTHORITY + '#/forces/' + str(authority['forces'].index(force)),
            'strength_observations': [r['id'] for r in ledger['strength_records']
                                      if (r['battle_id'], r['side']) == pair],
            'command_observations': [r['id'] for r in ledger['command_records']
                                     if (r['battle_id'], r['side']) == pair],
            'boundary_scenario_ids': b[0]['scenario_ids'],
            'blockers': force['blockers'],
            'selections': {k: field_state(force, k) for k in
                           ('selected_boundary', 'selected_strength', 'selected_person_id', 'army_id')},
        }
    return index


def summarize_group(name, rows, selection):
    citations = [c for r in rows for c in r['relevant_citations'] if not c['frame_family']]
    image_entries, family_entries = defaultdict(set), defaultdict(set)
    for r in rows:
        for c in r['relevant_citations']:
            if not c['frame_family']:
                family_entries[c['family']].add(r['battle_id'])
                if c['image']:
                    image_entries[c['image']['source_id']].add(r['battle_id'])
    images = {c['image']['source_id']: c['image']['sha256'] for c in citations if c['image']}
    by_hash = defaultdict(list)
    for key, sha in images.items():
        by_hash[sha].append(key)
    missing = sum(c['image'] is None for c in citations)
    both = sum(all(any(c['dimension'] == dim and not c['frame_family']
                       for c in r['relevant_citations']) for dim in RELEVANT) for r in rows)
    exclusions = []
    if name in selection['exclude_groups']:
        exclusions.append('stopped_pilot')
    if len(rows) > selection['max_entries']:
        exclusions.append('above_12_entry_batch_bound')
    if both != len(rows):
        exclusions.append('non_frame_dimension_citations_missing')
    if missing:
        exclusions.append('non_frame_image_links_missing')
    return {
        'campaign': name, 'battle_ids': [r['battle_id'] for r in rows],
        'entries': len(rows), 'sides': 2 * len(rows),
        'claims': sum(r['claims'] for r in rows),
        'unknown_claims': sum(r['statuses'].get('unknown', 0) for r in rows),
        'disputed_claims': sum(r['statuses'].get('disputed', 0) for r in rows),
        'brief_v3_records': sum(r['completion_brief_version'] == 3 for r in rows),
        'tactical_boundaries_recorded': sum(r['boundaries']['tactical_replacement_at'] == 'recorded' for r in rows),
        'campaign_boundaries_recorded': sum(r['boundaries']['campaign_replacement_at'] == 'recorded' for r in rows),
        'dossiers_with_typed_quantities': sum(r['typed']['quantities']['records'] > 0 for r in rows),
        'indexed_pilot_sides': sum(s['pilot_mapping'] is not None for r in rows for s in r['sides']),
        'entries_with_non_frame_citations_in_both_dimensions': both,
        'non_frame_citation_references': len(citations),
        'non_frame_missing_image_references': missing,
        'non_frame_image_ids': len(images), 'non_frame_distinct_image_hashes': len(by_hash),
        'duplicate_image_hash_ids': [sorted(v) for _, v in sorted(by_hash.items()) if len(v) > 1],
        'non_frame_images_shared_across_entries': sum(len(v) > 1 for v in image_entries.values()),
        'non_frame_family_entry_counts': {k: len(v) for k, v in sorted(family_entries.items())},
        'eligible_next_batch': not exclusions, 'selection_exclusions': exclusions,
    }


def select_campaign(groups):
    eligible = [g for g in groups if g['eligible_next_batch']]
    return min(eligible, key=lambda g: (g['non_frame_image_ids'], g['entries'], g['campaign']))['campaign'] if eligible else None


def build(root):
    root = Path(root)
    scope = read_json(root / SCOPE)
    require(scope['kind'] == 'napoleonic_blocker_inventory_scope' and scope['version'] == 1
            and scope['status'] == 'mechanical_inventory_only' and scope['selection'] == SELECTION,
            'scope or fixed selection rule changed')
    require(scope['authorization']['owner_message'] == 'Sounds good, go ahead'
            and all(scope['authorization'][k] is False for k in (
                'new_source_fetching', 'feature_admission', 'historical_outcome_fit',
                'calibration_scoring', 'separate_review', 'subagents')), 'authorization exceeded')
    partition = read_json(root / PARTITION)
    frame, cohort = read_json(root / FRAME), read_json(root / COHORT)
    require(partition['frame_sha256'] == digest(root / FRAME)
            and partition['cohort_sha256'] == digest(root / COHORT)
            and cohort['frame_sha256'] == digest(root / FRAME), 'partition/frame/cohort binding')
    groups = groups_for_partition(frame, cohort, partition)
    require((len(partition['development']), len(partition['reserved_final']), len(groups)) == (273, 52, 13)
            and scope['development_entries'] == 273 and scope['reserved_final_entries'] == 52,
            'frozen denominators changed')
    paths = {PARTITION, FRAME, COHORT, CONVENTIONS, SOURCES, LEDGER, BOUNDARIES, AUTHORITY}
    paths |= {f'data/napoleonic/evidence/{b}.json' for b in partition['development']}
    require(set(scope['bindings']) == paths, 'scope must bind exactly development inputs, no final dossiers')
    for path, sha in scope['bindings'].items():
        require(digest(safe_path(root, path)) == sha, 'changed bound input: ' + path)
    sources = {r['id']: r for r in read_json(root / SOURCES)['sources']}
    aliases = read_json(root / CONVENTIONS)['family_aliases']
    index = pilot_index(read_json(root / LEDGER), read_json(root / BOUNDARIES), read_json(root / AUTHORITY))
    frame_rows = {r['id']: r for r in frame['entries']}
    texts, checked_bytes = {}, set()

    def checked(source):
        if source['id'] not in checked_bytes:
            require(digest(safe_path(root, source['path'])) == source['sha256'], 'raw hash mismatch: ' + source['id'])
            checked_bytes.add(source['id'])

    def reference(claim, i, cite):
        source = sources[cite['source_id']]
        checked(source)
        key = source['id'], cite.get('section')
        if key not in texts:
            texts[key] = citation_text(root, sources, cite)
        require(cite['quote'] and cite['quote'] in texts[key], 'quote absent: ' + source['id'])
        image_id = source.get('facsimile_source_id')
        if source['id'] == 'bodart-1908-transcription-v1':
            image_id = 'bodart-1908-' + cite['section'] + '-image-v1'
        image = sources.get(image_id)
        if image_id:
            require(image is not None and image['format'] in {'jpg', 'jpeg', 'png'}, 'invalid image link')
            checked(image)
        family = aliases.get(source['independence_group'], source['independence_group'])
        return {
            'claim_id': claim['id'], 'dimension': claim['dimension'], 'citation_index': i,
            'source_id': source['id'], 'section': cite.get('section'), 'locator': cite['locator'],
            'quote_sha256': hashlib.sha256(cite['quote'].encode('utf-8')).hexdigest(),
            'raw_sha256': source['sha256'], 'metadata_sha256': source_metadata_digest(source),
            'family': family, 'frame_family': family == SELECTION['frame_source_family'],
            'image': {'source_id': image['id'], 'path': image['path'], 'sha256': image['sha256']} if image else None,
        }

    rows = []
    for battle in partition['development']:
        path = f'data/napoleonic/evidence/{battle}.json'
        d = read_json(root / path)
        require(d['battle_id'] == battle, 'dossier ID/path mismatch')
        record = d.get('research_completion')
        claims = d['claims']
        by_dimension = {dim: dict(sorted(Counter(c['status'] for c in claims if c['dimension'] == dim).items()))
                        for dim in sorted({c['dimension'] for c in claims})}
        sides = []
        for side in ('A', 'B'):
            local = record['sides'][side] if record else None
            mapping = index.get((battle, side))
            sides.append({'side': side,
                          'completion_claim_refs': {k: local[k] for k in ('strength_claim_ids', 'command_claim_ids')} if local else None,
                          'pilot_mapping': mapping,
                          'inspection_need': 'indexed_pilot_mapping_blocked' if mapping else 'side_mapping_absent_from_indexed_packages'})
        rows.append({
            'battle_id': battle, 'place': frame_rows[battle]['place'], 'campaign': frame_rows[battle]['campaign_group'],
            'dossier_path': path, 'dossier_sha256': scope['bindings'][path],
            'status': d['status'], 'schema_version': d['schema_version'],
            'boundaries': {k: field_state(d, k) for k in ('tactical_replacement_at', 'campaign_replacement_at')},
            'typed': {k: typed_field(d, k) for k in ('entities', 'events', 'quantities')},
            'completion_brief_version': record['brief_version'] if record else None,
            'claims': len(claims), 'statuses': dict(sorted(Counter(c['status'] for c in claims).items())),
            'dimensions': by_dimension,
            'relevant_claim_ids': {dim: [c['id'] for c in claims if c['dimension'] == dim] for dim in RELEVANT},
            'relevant_citations': [reference(c, i, cite) for c in claims if c['dimension'] in RELEVANT
                                   for i, cite in enumerate(c['citations'])],
            'sides': sides,
        })
    summaries = [summarize_group(name, [r for r in rows if r['battle_id'] in ids], SELECTION)
                 for name, ids in groups.items()]
    all_sides = [s for r in rows for s in r['sides']]
    indexed = [s['pilot_mapping'] for s in all_sides if s['pilot_mapping'] is not None]
    return {
        'kind': 'napoleonic_blocker_inventory', 'version': 1, 'status': 'mechanical_inventory_only',
        'provenance': {p: digest(root / p) for p in (SCOPE, DESIGN, *CODE)},
        'denominators': {'development_entries': len(rows), 'development_sides': len(all_sides),
                         'development_groups': len(groups), 'reserved_final_entries': len(partition['reserved_final']),
                         'reserved_final_groups': len(partition['frozen_groups']) - len(groups), 'final_dossiers_opened': 0},
        'totals': {
            'claims': sum(r['claims'] for r in rows),
            'unknown_claims': sum(r['statuses'].get('unknown', 0) for r in rows),
            'disputed_claims': sum(r['statuses'].get('disputed', 0) for r in rows),
            'brief_v3_records': sum(r['completion_brief_version'] == 3 for r in rows),
            'boundary_states': {k: dict(sorted(Counter(r['boundaries'][k] for r in rows).items()))
                                for k in ('tactical_replacement_at', 'campaign_replacement_at')},
            'typed_quantity_states': dict(sorted(Counter(r['typed']['quantities']['state'] for r in rows).items())),
            'indexed_pilot_sides': len(indexed), 'sides_without_indexed_mapping': len(all_sides) - len(indexed),
            'recorded_pilot_selections': {k: sum(s['selections'][k] == 'recorded' for s in indexed)
                                          for k in ('selected_boundary', 'selected_strength', 'selected_person_id', 'army_id')},
            'relevant_citation_references': sum(len(r['relevant_citations']) for r in rows),
            'raw_sources_hash_checked': len(checked_bytes),
            'raw_files_hash_checked': len({sources[s]['path'] for s in checked_bytes}),
        },
        'selection_rule': SELECTION, 'selected_campaign': select_campaign(summaries),
        'groups': summaries, 'dossiers': rows,
        'limits': ['Presence and byte/quote checks only; no new historical entailment inspection.',
                   'Absent structured records do not mean absent historical evidence.',
                   'Fewer pages can mean thinner coverage; selected campaign is not representative.',
                   'No side inferred from claim text; source families do not prove independence.',
                   'Final dossiers excluded from this inventory; the reservation is not historical blinding.'],
        'emitted_model_rows': [], 'historical_outcomes_fitted': False, 'calibration': 'prepared_unscored',
    }


def markdown(data):
    d, t = data['denominators'], data['totals']
    lines = ['# Napoleonic development blocker inventory v1', '',
             'Mechanical inventory; primary verification covers fields, hashes, counts and selection, not historical entailment.', '',
             f"**Next bounded campaign: `{data['selected_campaign']}`.** Selection uses existing citation/image metadata under the fixed 12-entry cap. Inspect its existing pages before adopting a mapping.", '',
             f"Scope: **{d['development_entries']} entries / {d['development_sides']} sides / {d['development_groups']} complete development groups**. The {d['reserved_final_entries']} reserved entries in {d['reserved_final_groups']} groups are counted from the partition; their dossiers were not opened by this inventory.", '',
             f"The development dossiers contain {t['claims']:,} claims, {t['unknown_claims']:,} explicit unknowns and {t['disputed_claims']:,} disputed claims. Brief-v3 records: {t['brief_v3_records']}/{d['development_entries']}; earlier drafts retain their original brief.", '',
             f"Dossier boundary states: tactical `{t['boundary_states']['tactical_replacement_at']}`; campaign `{t['boundary_states']['campaign_replacement_at']}`. Typed quantity field states: `{t['typed_quantity_states']}`.", '',
             f"The indexed measurement packages cover {t['indexed_pilot_sides']}/{d['development_sides']} sides (the stopped Naples pilot); {t['sides_without_indexed_mapping']} sides have no mapping in those packages. Recorded non-null selections among the indexed sides: `{t['recorded_pilot_selections']}`. These are record-presence counts, not admission decisions.", '',
             '## Complete campaign comparison', '',
             'Pages = distinct registered non-Bodart image IDs directly linked from strength/responsibility citations. Shared = pages cited by more than one entry. Missing links are citation references without this direct metadata link, not a count of unavailable or uninspected pages. Unknown/disputed = claims, not missing sides. No outcome values enter selection.', '',
             '| Campaign | Entries | Unknown / disputed claims | Both dimensions cite non-frame sources | Pages / shared | Missing direct links | Selection |',
             '| --- | ---: | ---: | ---: | ---: | ---: | --- |']
    for g in data['groups']:
        status = 'selected' if g['campaign'] == data['selected_campaign'] else 'eligible' if g['eligible_next_batch'] else ', '.join(g['selection_exclusions'])
        lines.append(f"| `{g['campaign']}` | {g['entries']} | {g['unknown_claims']} / {g['disputed_claims']} | {g['entries_with_non_frame_citations_in_both_dimensions']}/{g['entries']} | {g['non_frame_image_ids']} / {g['non_frame_images_shared_across_entries']} | {g['non_frame_missing_image_references']} | {status} |")
    selected = next((g for g in data['groups'] if g['campaign'] == data['selected_campaign']), None)
    if selected:
        lines += ['', '## Next inspection scope', '',
                  f"Keep all **{selected['entries']} entries / {selected['sides']} sides**, using **{selected['non_frame_image_ids']} non-Bodart pages** already cited in the two dimensions, plus the existing Bodart references. IDs: " + ', '.join('`' + b + '`' for b in selected['battle_ids']) + '.', '',
                  f"Family navigation counts (entries): `{selected['non_frame_family_entry_counts']}`. Identical image hashes under multiple IDs: `{selected['duplicate_image_hash_ids']}`.", '',
                  'Prepare one combined, source-specific population/time/authority table from these existing passages and full pinned pages. Test whether a common opening boundary can support a complete force/person pair for either side. Keep each unresolved side explicit and stop after this complete campaign; no automatic deep-dive queue.', '',
                  '| Entry | Strength / responsibility claim IDs to inspect |', '| --- | --- |']
        for r in data['dossiers']:
            if r['campaign'] == selected['campaign']:
                lines.append(f"| `{r['battle_id']}` {r['place']} | " + '; '.join(dim + ': ' + ', '.join('`' + c + '`' for c in ids) for dim, ids in r['relevant_claim_ids'].items()) + ' |')
    lines += ['', '## Provenance and limits', '',
              f"{t['relevant_citation_references']:,} strength/responsibility citation references retain dossier/claim IDs, citation indices, sections, locators, quote hashes and source/metadata/image hashes in the companion JSON. {t['raw_sources_hash_checked']:,} registered source IDs covering {t['raw_files_hash_checked']:,} distinct raw paths were hash-checked. The scope binds every development dossier, source registry and pilot package; see `data/napoleonic/blocker-inventory-v1/scope.json`.", '',
              *['- ' + s for s in data['limits']], '',
              'No new historical claim, source fetch, feature admission, calibration score, separate review, synthetic job or historical fit. Model rows emitted: 0.', '']
    return '\n'.join(lines)


def check(root):
    root = Path(root)
    data = build(root)
    require(read_json(root / (REPORT + '.json')) == data, 'stale JSON report; run make reproduce')
    require((root / (REPORT + '.md')).read_text(encoding='utf-8') == markdown(data), 'stale Markdown report; run make reproduce')
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    if args.write:
        data = build(root)
        write_json(root / (REPORT + '.json'), data)
        (root / (REPORT + '.md')).write_text(markdown(data), encoding='utf-8')
    else:
        data = check(root)
    print(f"Development inventory: {len(data['dossiers'])} entries; next campaign: {data['selected_campaign']}; 0 model rows.")


if __name__ == '__main__':
    main()
