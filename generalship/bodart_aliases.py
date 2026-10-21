"""Scoped, passage-backed compiler-name migration; no fetching or model fitting."""

from collections import Counter
from pathlib import Path

from . import bodart_ratings as v1
from .bodart_bulk import source_registry_with_bulk
from .sources import digest, read_json, safe_path, text_sections, validate_source_metadata

SOURCES = 'data/bodart/aliases-v1/sources.json'
ALIASES = 'data/bodart/aliases-v1/aliases.json'
COHORT = 'data/bodart/ratings-v2/cohort.json'
DESIGN = 'docs/bodart-ratings-v2.md'
CODE = 'generalship/bodart_aliases.py'


def require(ok, message):
    if not ok:
        raise ValueError('Bodart aliases: ' + message)


def source_registry_with_aliases(root):
    registry = source_registry_with_bulk(root)
    path = Path(root) / SOURCES
    if path.is_file():
        sources = read_json(path)['sources']
        require(len({s['id'] for s in sources}) == len(sources), 'duplicate source ID')
        require(not set(registry) & {s['id'] for s in sources}, 'source replaces a frozen entry')
        registry.update({s['id']: s for s in sources})
    return registry


def load(root, parent):
    registry = source_registry_with_aliases(root)
    sources = read_json(root / SOURCES)['sources']
    for s in sources:
        require(digest(safe_path(root, s['path'])) == s['sha256'], 'changed source: ' + s['id'])
        require(registry[s['parent_source_id']]['sha256'] == s['parent_sha256'], 'changed source parent')
    validate_source_metadata(root, registry)
    manifest = read_json(root / ALIASES)
    require(manifest['parent_cohort_sha256'] == digest(root / v1.COHORT), 'changed parent cohort')
    require(manifest['sources_sha256'] == digest(root / SOURCES), 'changed source registry')
    require(1 <= len(manifest['groups']) <= 8, 'bounded group ceiling exceeded')
    require(len({g['id'] for g in manifest['groups']}) == len(manifest['groups']), 'duplicate group')
    seen = set()
    for g in manifest['groups']:
        members = g['members']
        require(len(members) >= 2 and len(members) == len(set(members)), 'invalid group members')
        require(g['canonical_unit'] in members and not seen.intersection(members), 'overlapping/chained alias group')
        seen.update(members)
        actual = [{'battle_id': r['id'], 'side': s, 'original_unit': r[s], 'raw_label': r[s + '_raw'],
                   'year': r['year'], 'source_id': r['source_id'], 'source_sha256': r['source_sha256'],
                   'locator': r['locator']}
                  for r in parent['rows'] for s in ('a', 'b') if r[s] in members]
        require(actual == g['scoped_occurrences'], 'occurrence scope changed: ' + g['id'])
        require(set(members) == {o['original_unit'] for o in actual}, 'unobserved alias member')
        pages = g['index_page_references']
        missing = None if pages is None else sorted({o['battle_id'] for o in actual
                                                     if int(o['battle_id'][1:4]) not in pages})
        require(missing == g['index_unlisted_battle_ids'], 'hidden index omission')
        require(g['status'] == 'primary_verified_compiler_identity_mapping' and g['citations'], 'unadmitted group')
        for c in g['citations']:
            source, image = registry[c['source_id']], registry[c['image_source_id']]
            require(c['source_sha256'] == source['sha256'], 'citation hash')
            sections = text_sections(safe_path(root, source['path']).read_text(encoding='utf-8'))
            require(c['quote'] in sections[c['section']] and c['locator'], 'citation passage/locator')
            require(source['facsimile_source_id'] == image['id'] and image['format'] == 'jpg', 'citation image')
    return manifest, {s['path']: s['sha256'] for s in sources}


def migrate(rows, groups):
    """Apply only explicit source labels, then preserve symmetric orientation."""
    mapping = {u: g['canonical_unit'] for g in groups for u in g['members']}
    migrated = []
    for original in rows:
        r = dict(original)
        a, b = mapping.get(r['a'], r['a']), mapping.get(r['b'], r['b'])
        require(a != b, 'same canonical identity on both sides: ' + r['id'])
        r['original_units'] = {'a': original['a'], 'b': original['b']}
        r['orientation_flipped'] = a > b
        if a > b:
            a, b = b, a
            r['a_raw'], r['b_raw'] = r['b_raw'], r['a_raw']
            r['personnel_a'], r['personnel_b'] = r['personnel_b'], r['personnel_a']
            r['x'], r['y'] = -r['x'], 1 - r['y']
        r['a'], r['b'] = a, b
        migrated.append(r)
    return migrated


def coverage(rows):
    counts = Counter(r[s] for r in rows for s in ('a', 'b'))
    cc = v1.components(rows)
    groups = Counter(cc.values())
    return {'engagements': len(rows), 'labels': len(counts), 'ordered_labels': sum(n >= 3 for n in counts.values()),
            'components': len(groups), 'largest_component_labels': max(groups.values(), default=0),
            'personnel_checked': sum(r['personnel_checked'] for r in rows)}


def prepare(root):
    require(read_json(root / v1.COHORT) == v1.prepare(root), 'original cohort no longer reproduces')
    parent = read_json(root / v1.COHORT)
    manifest, source_bindings = load(root, parent)
    rows = migrate(parent['rows'], manifest['groups'])
    mapping = {u: g['canonical_unit'] for g in manifest['groups'] for u in g['members']}
    paths = (v1.COHORT, v1.RUN, v1.TABLE, v1.RESERVATION, v1.CODE, SOURCES, ALIASES, DESIGN,
             CODE, 'generalship/bodart_ratings_v2.py', 'tests/test_bodart_aliases.py')
    return {'kind': 'bodart-ratings-v2-cohort', 'parent_entries': parent['parent_entries'],
            'reserved_final': parent['reserved_final'], 'rows': rows, 'ledger': parent['ledger'],
            'input_sha256': {**v1.bindings(root, paths), **source_bindings},
            'before': coverage(parent['rows']), 'after': coverage(rows),
            'changed_occurrences': sum(mapping.get(r[s], r[s]) != r[s] for r in parent['rows'] for s in ('a', 'b')),
            'alias_occurrences': sum(len(g['scoped_occurrences']) for g in manifest['groups']),
            'orientation_flips': sum(r['orientation_flipped'] for r in rows),
            'groups': [{'id': g['id'], 'name': g['display_name'], 'canonical_unit': g['canonical_unit'],
                        'original_labels': len(g['members']), 'appearances': len(g['scoped_occurrences'])}
                       for g in manifest['groups']]}
