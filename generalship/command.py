"""Command-responsibility ledger checker (docs/commander-ratings.md §2).

The ledger names one responsible commander per side of each decisive, non-aggregate
engagement, as a graded best estimate. Nothing here fits a model or rates anyone.
"""

from pathlib import Path

from .evidence import citation_text
from .sources import digest, read_csv, read_json, safe_path, source_metadata_digest, verify_sources

DEFAULT_LEDGER = 'data/command/responsibility-v1.json'
DEFAULT_REGISTRY = 'data/command/commanders-v1.json'
SIDES = ('US', 'Confederate')
SIDE_PREFIX = {'US': 'us', 'Confederate': 'cs'}
LABELS = {'responsibility_unresolved', 'command_changed', 'joint_command', 'superior_directing'}
ECHELONS = {'army', 'corps_or_wing', 'division', 'brigade', 'regiment', 'detachment_or_post', 'flotilla', 'unknown'}
NESTING = {'nested', 'not_nested', 'nesting_unresolved'}
RANK_ORDER = {'army': ['General', 'Lieutenant General', 'Major General', 'Brigadier General', 'Colonel',
                       'Lieutenant Colonel', 'Lieutenant'],
              'navy': ['Rear Admiral', 'Flag Officer', 'Captain', 'Commander']}
# Grades each recorded rule can give (design §2 grade table).
RULE_GRADES = {'2': {'A', 'B', 'C'}, '3a': {'A', 'C'}, '3b': {'C'}, '3c': {'D'}, '5': {'A', 'C', 'D'}, '6': {'D'}}


class CommandError(ValueError):
    """Malformed ledger, broken binding or unverifiable citation."""


def require(condition, message):
    if not condition:
        raise CommandError(message)


def rank_level(rank, navy):
    """Position in the declared order; 'Brevet' and 'Acting' rank as the named rank."""
    base = rank.replace('Brevet ', '').replace('Acting ', '')
    order = RANK_ORDER['navy' if navy == '1' else 'army']
    require(base in order, f'Undeclared rank: {rank}')
    return order.index(base)


def resolve(root, sources, dossiers, citation):
    """Return (source_id, passage) for a ledger citation."""
    if 'dossier' in citation:
        ref = citation['dossier']
        dossier = dossiers[citation['battle_id']]
        claim = next((c for c in dossier['claims'] if c['id'] == ref['claim_id']), None)
        require(claim is not None, f"Unknown dossier claim {ref['claim_id']}")
        ct = claim['citations'][ref['citation_index']]
        require(ct['source_id'] == citation['source_id'], 'Dossier citation source differs')
        return ct['source_id'], citation_text(root, sources, ct)
    return citation['source_id'], citation_text(root, sources, citation)


def contained_pairs(battles, ids):
    """Same-campaign pairs among ids whose frozen interval lies inside the other's (design §2 rule 7)."""
    pairs = []
    for a in ids:
        for b in ids:
            ra, rb = battles[a], battles[b]
            if a != b and ra['campaign'] == rb['campaign'] and ra['start_date'] <= rb['start_date'] \
                    and rb['end_date'] <= ra['end_date'] and (ra['start_date'], ra['end_date']) != (rb['start_date'], rb['end_date']):
                pairs.append((a, b))
    return sorted(pairs)


def check(root, path=DEFAULT_LEDGER, ledger=None, only=None):
    """Replay the ledger. `only` checks a subset of engagements during extraction and skips coverage."""
    root = Path(root)
    if ledger is None:
        ledger = read_json(safe_path(root, str(path)))
    require(ledger.get('kind') == 'command_responsibility_ledger' and ledger.get('schema_version') == 1, 'Ledger kind')
    for key in ('design', 'cohort', 'registry'):
        b = ledger['bindings'][key]
        require(digest(safe_path(root, b['path'])) == b['sha256'], f'Binding mismatch: {key}')
    sources = verify_sources(root)
    for sid, b in ledger['bindings']['cited_sources'].items():
        require(sid in sources and source_metadata_digest(sources[sid]) == b['metadata_sha256']
                and sources[sid]['sha256'] == b['raw_sha256'], f'Cited source binding mismatch: {sid}')
    require(ledger['rank_order'] == RANK_ORDER, 'Rank order differs from the code')
    registry = {c['id']: c for c in read_json(safe_path(root, ledger['bindings']['registry']['path']))['commanders']}
    names = {(n, c['side']): c['id'] for c in registry.values() for n in c['cwsac_names']}
    for c in registry.values():
        require(c['id'].startswith(SIDE_PREFIX[c['side']] + '-'), f"Registry ID prefix: {c['id']}")
        require(bool(c['cwsac_names']) or bool(c.get('passage_citation')), f"Registry entry without a source: {c['id']}")
    cohort = read_json(root / 'data/pilot/cohort.json')['battle_ids']
    battles = {r['battle']: r for r in read_csv(safe_path(root, sources['arnold-cwsac-battles']['path']))}
    listings = {}
    for r in read_csv(safe_path(root, sources['arnold-cwsac-commanders']['path'])):
        listings.setdefault((r['battle'], r['belligerent']), []).append(r)
    in_scope = sorted(b for b in cohort if battles[b]['result'] != 'Inconclusive' and battles[b]['operation'] != '1')
    engagements = {e['battle_id']: e for e in ledger['engagements']}
    if only is None:
        require(sorted(engagements) == in_scope, 'Coverage: in-scope engagements differ')
        require(set(ledger['bindings']['dossiers']) == set(in_scope), 'Every in-scope dossier must be bound')
    else:
        in_scope = sorted(only)
    dossiers = {}
    for bid in in_scope:
        b = ledger['bindings']['dossiers'][bid]
        require(digest(safe_path(root, b['path'])) == b['sha256'], f'Dossier binding: {bid}')
        dossiers[bid] = read_json(safe_path(root, b['path']))
    for c in registry.values():
        if c.get('passage_citation'):
            ct = c['passage_citation']
            sid, passage = resolve(root, sources, dossiers, ct)
            require(ct['quote'] in passage, f"Registry passage citation: {c['id']}")
    grades = {g: 0 for g in 'ABCD'}
    for bid in in_scope:
        e = engagements[bid]
        require(set(e['sides']) == set(SIDES), f'{bid}: both sides required')
        for side in SIDES:
            s = e['sides'][side]
            where = f'{bid} {side}'
            require(s['grade'] in RULE_GRADES.get(s['rule'], set()), f"{where}: grade {s['grade']} under rule {s['rule']}")
            require((s['grade'] == 'D') == (s['commander_id'] is None), f'{where}: grade D if and only if no commander')
            require(set(s['labels']) <= LABELS and s['echelon'] in ECHELONS, f'{where}: labels or echelon')
            require(('superior_directing' in s['labels']) == (s.get('superior') is not None), f'{where}: superior_directing names a superior')
            for i in [s['commander_id'], s['successor'], s.get('superior'), *s['candidates']]:
                require(i is None or (i in registry and registry[i]['side'] == side), f'{where}: unknown or wrong-side commander {i}')
            require(s['commander_id'] not in s['candidates'], f'{where}: the choice is not its own candidate')
            require(('command_changed' in s['labels']) or s['successor'] is None, f'{where}: successor without command_changed')
            if s['rule'] in {'2', '3a'} and s['grade'] == 'C':
                require('responsibility_unresolved' in s['labels'], f'{where}: contradicted listing must be labelled')
            if s['rule'] in {'3b', '3c'}:
                require('responsibility_unresolved' in s['labels'], f'{where}: rank fallback must be labelled')
            listed = listings.get((bid, side), [])
            accounted = {s['commander_id'], *s['candidates']}
            for r in listed:
                require(names.get((r['fullname'], side)) in accounted, f"{where}: listing {r['fullname']} not accounted for")
            navies = {r['navy'] for r in listed}
            if len(navies) > 1:
                require(s['rule'] == '5', f'{where}: mixed services require rule 5')
            elif len(listed) > 1:
                require(s['rule'] in {'3a', '3b', '3c'}, f'{where}: several listings in one service require rule 3')
                top = min(rank_level(r['rank'], r['navy']) for r in listed)
                tied = sum(rank_level(r['rank'], r['navy']) == top for r in listed) > 1
                if s['rule'] == '3b':
                    require(not tied and names[next(r['fullname'] for r in listed if rank_level(r['rank'], r['navy']) == top), side]
                            == s['commander_id'], f'{where}: rule 3(b) must choose the senior listed officer')
                if s['rule'] == '3c':
                    require(tied, f'{where}: rule 3(c) needs a tie')
            elif len(listed) == 1:
                require(s['rule'] in {'2', '6'}, f'{where}: a single listing uses rule 2')
            if s['grade'] == 'B':
                require(s['rule'] == '2' and all(c['source_id'] == 'arnold-cwsac-commanders' for c in s['citations']),
                        f'{where}: grade B cites only the listing')
            if s['grade'] == 'A':
                require(any(c['source_id'] != 'arnold-cwsac-commanders' for c in s['citations']), f'{where}: grade A needs a stating passage')
            require(bool(s['rationale']), f'{where}: rationale')
            require(bool(s['superior_citations']) <= ('superior_directing' in s['labels']), f'{where}: superior citations without the label')
            for ct in s['citations'] + s['superior_citations']:
                require(ct['battle_id'] == bid, f'{where}: citation battle')
                sid, passage = resolve(root, sources, dossiers, ct)
                require(sid in ledger['bindings']['cited_sources'], f'{where}: unbound source {sid}')
                if ct.get('column') == 'rank':
                    require(ct['quote'] == passage, f'{where}: listing rank differs')
                else:
                    require(ct['quote'] in passage, f"{where}: quote not in passage: {ct['quote'][:60]}")
            grades[s['grade']] += 1
    pairs = contained_pairs(battles, in_scope) if only is None else sorted((n['containing'], n['contained']) for n in ledger['nesting'])
    recorded = {(n['containing'], n['contained']): n for n in ledger['nesting']}
    require(sorted(recorded) == pairs, 'Nesting: every contained-interval pair needs exactly one outcome')
    for n in ledger['nesting']:
        require(n['outcome'] in NESTING and n['reason'], f"Nesting outcome for {n['containing']}/{n['contained']}")
        for ct in n.get('citations', []):
            sid, passage = resolve(root, sources, dossiers, ct)
            require(ct['quote'] in passage, f"Nesting quote not in passage: {ct['quote'][:60]}")
    return {'kind': 'command_responsibility_check', 'engagements': len(in_scope), 'sides': 2 * len(in_scope),
            'side_grades': grades, 'registry_commanders': len(registry),
            'nesting': {o: sum(n['outcome'] == o for n in ledger['nesting']) for o in sorted(NESTING)},
            'rated': False}
