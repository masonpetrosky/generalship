"""The v3 side-strength ledger: grade D sides filled from upstream tabulations (docs/ledgers-v3.md).

v3 copies the v2 ledger and adds inputs only to sides v2 grades D. The new inputs are cells from
tables of the already-pinned upstream package: the CWSAC Report Updates and CWSS force tables,
plus Bodart (1908) and Clodfelter (2008) through one-to-one 'eq' concordances. Coding is
mechanical (`upstream_inputs`) apart from the documented OVERRIDES. Estimates come from the
unchanged v1 engine in estimates.py. Nothing here admits a feature, fits a model or changes the
frozen baseline inputs.
"""

from collections import defaultdict
import copy
from pathlib import Path

from .estimates import (BASES, CODES, CONSTANTS, LOSS_TIMING, SIDES, _document_key, _passage, _printed_in_quote,
                        classify, estimate_row, estimate_side, nested_sets, require)
from .sources import digest, read_csv, read_json, safe_path, source_metadata_digest, verify_sources

DEFAULT_LEDGER = 'data/estimates/side-strength-v3.json'
PREDECESSOR = 'data/estimates/side-strength-v2.json'
ADDENDUM = 'docs/ledgers-v3.md'
OWNER_DECISION = 'data/estimates/owner-decision-v3-sources-2026-10-06.json'
COMPILED = {'nps-cwsac', 'livermore-numbers-losses'}
REVISION_NOTE = 'v3: filled from upstream tables (docs/ledgers-v3.md)'
# (table, source of the forces rows, key column, value column, concordance source or None)
TABLES = (
    ('cws2', 'arnold-cws2-forces', 'battle', 'strength', None),
    ('cwss', 'arnold-cwss-forces', 'BattlefieldCode', 'TroopsEngaged', None),
    ('bodart-engaged', 'arnold-bodart1908-forces', 'battle_id', 'strength_engaged', 'arnold-bodart1908-to-cwsac'),
    ('bodart-total', 'arnold-bodart1908-forces', 'battle_id', 'strength', 'arnold-bodart1908-to-cwsac'),
    ('clodfelter', 'arnold-clodfelter-forces', 'battle_id', 'strength', 'arnold-clodfelter-to-cwsac'),
)
# Population basis and tier-2 codes per table, from the upstream schema (docs/ledgers-v3.md §3).
CODING = {
    'cws2': ('reported_engaged', ['derivation_unknown']),
    'cwss': ('reported_engaged', ['derivation_unknown']),
    'bodart-engaged': ('reported_engaged', ['derivation_unknown']),
    'bodart-total': ('unknown', ['derivation_unknown', 'scope_unresolved']),
    'clodfelter': ('unknown', ['derivation_unknown']),
}
# Cells whose own description shows they count only part of the side (docs/ledgers-v3.md §3).
OVERRIDES = {
    ('NC001', 'US', 'cws2'): {'codes': ['derivation_unknown', 'partial_scope'], 'bound': 'lower',
                              'reason': 'the description sums the landing units (220 + 500 + 60 + 100 + 55 = 935) '
                                        'and names the Atlantic Blockading Squadron without a count'},
    ('VA076', 'Confederate', 'cws2'): {'codes': ['derivation_unknown', 'partial_scope'], 'bound': 'lower',
                                       'reason': "the description names only the 'Confederate Home Guard'"},
}
PREFIX = {'US': 'us', 'Confederate': 'cs'}


def _forces(root, sources, sid, key):
    return {(r[key], r['belligerent']): r for r in read_csv(safe_path(root, sources[sid]['path']))}


def concordance(root, sources, sid):
    """{cwsac id: [(from id, relation, targets)]} from one of Arnold's concordance files."""
    out = defaultdict(list)
    for r in read_json(safe_path(root, sources[sid]['path'])):
        for t in r['battles_to']:
            for f in r['battles_from']:
                out[t].append((str(f), r['relation'], list(r['battles_to'])))
    return out


def link_status(links, battle):
    """('ok', from id) for one unambiguous one-to-one eq link; otherwise (reason, None) per candidate."""
    found = links.get(battle, [])
    eq = [(f, rel, to) for f, rel, to in found if rel == 'eq']
    result = []
    for f, rel, to in found:
        if rel != 'eq':
            result.append((f, f'concordance relation {rel!r}, not eq'))
        elif len(to) != 1:
            result.append((f, f'eq link covers {len(to)} records ({", ".join(to)})'))
        elif len(eq) != 1:
            result.append((f, 'more than one eq link reaches this record'))
        else:
            result.append((f, 'ok'))
    return result


def _value(cell):
    try:
        v = int(cell)
    except (TypeError, ValueError):
        return None
    return v if v > 0 else None


def upstream_inputs(root, sources, battle, side, existing, tables=None):
    """New inputs and the inventory of every upstream row for one grade D side (mechanical)."""
    tables = tables or _load(root, sources)
    p = PREFIX[side]
    inputs, inventory = [], []
    pool = list(existing)
    for name, sid, key, column, link_sid in TABLES:
        rows = []
        if link_sid is None:
            rows.append((battle, None))
        else:
            for f, status in link_status(tables[link_sid], battle):
                rows.append((f, status))
        for row_id, status in rows:
            row = tables[sid].get((row_id, side))
            entry = {'table': name, 'source_id': sid, 'row_key': {key: row_id, 'belligerent': side}, 'column': column}
            if row is None:
                continue
            cell = row[column]
            entry['cell'] = cell
            value = _value(cell)
            if status not in (None, 'ok'):
                entry['use'] = status if cell else f'{status}; empty cell'
                inventory.append(entry)
                continue
            if value is None:
                entry['use'] = 'empty cell' if not cell.strip() else 'zero or non-numeric cell: not a count'
                inventory.append(entry)
                continue
            basis, codes = CODING[name]
            ov = OVERRIDES.get((battle, side, name), {})
            inp = {'id': f'{p}-{name}', 'source_id': sid,
                   'ref': {'citation': {'source_id': sid, 'row_key': entry['row_key'], 'column': column, 'quote': cell}},
                   'printed': {'lower': value, 'upper': value}, 'basis': basis,
                   'codes': sorted(ov.get('codes', codes)), 'loss_timing': 'none', 'adjustments': [],
                   'bound': ov.get('bound'), 'document_key': _document_key(sources, sid),
                   'independence_group': sources[sid]['independence_group']}
            if link_sid:
                inp['link'] = {'source_id': link_sid, 'from': row_id, 'to': battle, 'relation': 'eq'}
            if name == 'cws2' and row.get('description'):
                inp['note'] = f"CWS2 description: {row['description']}"
            if ov:
                inp['note'] = (inp.get('note', '') + f"; coded partial: {ov['reason']}").lstrip('; ')
            require(inp['id'] not in {o['id'] for o in pool}, f'{battle} {side}: input ID {inp["id"]} already used')
            same = [o for o in pool if o.get('independence_group') in COMPILED and o.get('source_id')
                    and o['printed']['lower'] == o['printed']['upper'] == value]
            if same:  # rule 2 extended: an exact NPS/CWSAC or Livermore figure repeated is one figure
                inp['reproduction_of'] = sorted(same, key=lambda o: o['id'])[0]['id']
            inp['class'] = classify(inp)[0]
            inputs.append(inp)
            pool.append(inp)
            entry['use'] = inp['id']
            inventory.append(entry)
    return inputs, inventory


def _load(root, sources):
    tables = {}
    for name, sid, key, column, link_sid in TABLES:
        tables[sid] = _forces(root, sources, sid, key)
        if link_sid:
            tables[link_sid] = concordance(root, sources, link_sid)
    return tables


def build(root):
    """The v3 ledger, from the v2 ledger and the pinned upstream tables."""
    root = Path(root)
    sources = verify_sources(root)
    v2 = read_json(safe_path(root, PREDECESSOR))
    tables = _load(root, sources)
    led = copy.deepcopy(v2)
    led['version'] = 3
    led['status'] = 'primary_verified_not_fitted'
    used = set()
    for e in led['engagements']:
        changed = False
        for s in SIDES:
            side = e['sides'][s]
            if side['estimate']['grade'] != 'D':
                continue
            new, inv = upstream_inputs(root, sources, e['battle_id'], s, side['inputs'], tables)
            e['inventory'].setdefault('upstream', {})[s] = inv
            if new:
                side['inputs'] = side['inputs'] + new
                used |= {i['source_id'] for i in new} | {i['link']['source_id'] for i in new if 'link' in i}
                changed = True
        est = estimate_row({s: estimate_side(e['sides'][s]['inputs']) for s in SIDES})
        for s in SIDES:
            side = e['sides'][s]
            side['estimate'] = est[s]
            if est[s]['grade'] == 'D':
                if 'upstream' in e['inventory'] and e['inventory']['upstream'].get(s):
                    side['null_reason'] = side['null_reason'] + ' v3: the upstream tables give no usable candidate (see inventory).'
            else:
                side.pop('null_reason', None)
        if changed:
            e['rationale'] = (e.get('rationale', '') + f' {REVISION_NOTE}.').strip()
        e['nested'] = nested_sets(est)
    cited = dict(v2['bindings']['cited_sources'])
    for sid in sorted(used):
        cited[sid] = {'metadata_sha256': source_metadata_digest(sources[sid]), 'raw_sha256': sources[sid]['sha256']}
    led['bindings'] = {**{k: v for k, v in v2['bindings'].items() if k not in ('addendum', 'script', 'owner_decision', 'cited_sources')},
                       'addendum': {'path': ADDENDUM, 'sha256': digest(safe_path(root, ADDENDUM))},
                       'script': {'path': 'generalship/estimates_v3.py', 'sha256': digest(safe_path(root, 'generalship/estimates_v3.py'))},
                       'owner_decision': {'path': OWNER_DECISION, 'sha256': digest(safe_path(root, OWNER_DECISION))},
                       'predecessor': {'path': PREDECESSOR, 'sha256': digest(safe_path(root, PREDECESSOR))},
                       'cited_sources': dict(sorted(cited.items()))}
    led['extractor_policies'] = v2['extractor_policies'] + [
        'v3 adds inputs only to sides the v2 ledger grades D; every other side keeps its v2 inputs (docs/ledgers-v3.md).',
        'Upstream cells are coded by table: CWS2 and CWSS counts as reported_engaged, Bodart strength_engaged as '
        'reported_engaged, Bodart strength (total personnel) as basis unknown with scope_unresolved, and Clodfelter '
        'strength as basis unknown; every upstream cell carries derivation_unknown.',
        'Bodart and Clodfelter rows are used only through a one-to-one eq concordance link; zero cells are not counts.',
        'An upstream figure equal to an NPS/CWSAC or Livermore figure on the same side is recorded as its reproduction.',
        'Two CWS2 cells whose descriptions name only part of the side are coded partial_scope lower bounds (OVERRIDES).']
    return led


def check(root, path=DEFAULT_LEDGER, ledger=None):
    """Replay the v3 ledger: v2 sides carried forward, upstream inputs re-derived and verified, estimates reproduced."""
    root = Path(root)
    if ledger is None:
        ledger = read_json(safe_path(root, str(path)))
    require(ledger.get('kind') == 'side_strength_estimate_ledger' and ledger.get('schema_version') == 1, 'Ledger kind')
    require(ledger.get('version') == 3, 'Ledger version')
    for key in ('design', 'addendum', 'script', 'engine', 'cohort', 'owner_decision', 'predecessor'):
        b = ledger['bindings'][key]
        require(digest(safe_path(root, b['path'])) == b['sha256'], f'Binding mismatch: {key}')
    require(ledger['constants'] == CONSTANTS, 'Ledger constants differ from the code')
    sources = verify_sources(root)
    for sid, b in ledger['bindings']['cited_sources'].items():
        require(sid in sources and source_metadata_digest(sources[sid]) == b['metadata_sha256']
                and sources[sid]['sha256'] == b['raw_sha256'], f'Cited source binding mismatch: {sid}')
    v2 = read_json(safe_path(root, ledger['bindings']['predecessor']['path']))
    require(ledger['bindings']['dossiers'] == v2['bindings']['dossiers'], 'v3 binds the dossier versions v2 binds')
    require(ledger['out_of_scope'] == v2['out_of_scope'], 'Out-of-scope records differ from v2')
    require([e['battle_id'] for e in ledger['engagements']] == [e['battle_id'] for e in v2['engagements']], 'Coverage differs from v2')
    tables = _load(root, sources)
    cited = ledger['bindings']['cited_sources']
    v2_by = {e['battle_id']: e for e in v2['engagements']}
    results = {}
    for e in ledger['engagements']:
        bid = e['battle_id']
        old = v2_by[bid]
        for s in SIDES:
            side, prev = e['sides'][s], old['sides'][s]
            n = len(prev['inputs'])
            require(side['inputs'][:n] == prev['inputs'], f'{bid} {s}: v2 inputs must be carried forward unchanged')
            new = side['inputs'][n:]
            if prev['estimate']['grade'] != 'D':
                require(not new, f'{bid} {s}: inputs added to a side v2 grades A-C')
                continue
            expected, inv = upstream_inputs(root, sources, bid, s, prev['inputs'], tables)
            require(new == expected, f'{bid} {s}: upstream inputs do not re-derive')
            require(e['inventory'].get('upstream', {}).get(s, []) == inv, f'{bid} {s}: upstream inventory incomplete')
            for inp in new:
                where = f'{bid} {s} {inp["id"]}'
                require(set(inp['codes']) <= CODES and inp['basis'] in BASES and inp['loss_timing'] in LOSS_TIMING, f'{where}: codes')
                sid, quote, passage = _passage(root, sources, None, inp)
                require(sid == inp['source_id'] and sid in cited, f'{where}: source ID or unbound source')
                require(quote == passage, f'{where}: quote is not the whole cell')
                require(inp['document_key'] == _document_key(sources, sid), f'{where}: document key')
                require(inp['independence_group'] == sources[sid]['independence_group'], f'{where}: independence group')
                for v in {inp['printed']['lower'], inp['printed']['upper']}:
                    require(_printed_in_quote(v, quote), f'{where}: printed value {v} not in quote')
                require(inp['class'] == classify(inp)[0], f'{where}: class')
                if 'link' in inp:
                    require(inp['link']['source_id'] in cited, f'{where}: unbound concordance')
                    require(dict(link_status(tables[inp['link']['source_id']], bid)).get(inp['link']['from']) == 'ok',
                            f'{where}: no one-to-one eq concordance link')
        est = estimate_row({s: estimate_side(e['sides'][s]['inputs']) for s in SIDES})
        for s in SIDES:
            require(e['sides'][s]['estimate'] == est[s], f'{bid} {s}: estimate does not reproduce')
            if est[s]['point'] is None:
                require(bool(e['sides'][s].get('null_reason')), f'{bid} {s}: grade D needs a reason')
            else:
                require(0 < est[s]['low'] <= est[s]['point'] <= est[s]['high'], f'{bid} {s}: range order')
        require(nested_sets(est) == e['nested'], f'{bid}: nested-set membership does not reproduce')
        results[bid] = est
    sets = {b: nested_sets(results[b]) for b in results}
    v2_grades = {(e['battle_id'], s): e['sides'][s]['estimate']['grade'] for e in v2['engagements'] for s in SIDES}
    return {'kind': 'side_strength_estimate_check', 'version': 3, 'in_scope': len(results), 'out_of_scope': len(ledger['out_of_scope']),
            'side_grades': {g: sum(results[b][s]['grade'] == g for b in results for s in SIDES) for g in 'ABCD'},
            'filled_from_d': {g: sum(results[b][s]['grade'] == g and v2_grades[(b, s)] == 'D' for b in results for s in SIDES) for g in 'ABC'},
            'rows_by_set_fit_eligible': {k: sum(k in sets[b]['sets'] and not sets[b]['excluded_post_start_information']
                                                for b in results) for k in ('set1_A', 'set2_AB', 'set3_ABC')},
            'rows_excluded_post_start_information': sum(sets[b]['excluded_post_start_information'] for b in results),
            'fitted': False, 'promoted_rows': 0}


def agreement(root):
    """Descriptive: how each upstream table compares with sides v2 already grades A-C, and whether
    Arnold's machine-readable Livermore table matches the project's Livermore transcription inputs."""
    import math
    import statistics
    root = Path(root)
    sources = verify_sources(root)
    tables = _load(root, sources)
    v2 = read_json(safe_path(root, PREDECESSOR))
    out = {}
    for name, sid, key, column, link_sid in TABLES:
        ratios = []
        for e in v2['engagements']:
            for s in SIDES:
                est = e['sides'][s]['estimate']
                if est['grade'] == 'D':
                    continue
                if link_sid:
                    ok = [f for f, st in link_status(tables[link_sid], e['battle_id']) if st == 'ok']
                    row = tables[sid].get((ok[0], s)) if ok else None
                else:
                    row = tables[sid].get((e['battle_id'], s))
                v = _value(row[column]) if row else None
                if v:
                    ratios.append(v / est['point'])
        logs = [math.log(r) for r in ratios]
        out[name] = {'graded_sides_compared': len(ratios),
                     'median_ratio_table_to_ledger_point': math.exp(statistics.median(logs)) if logs else None,
                     'within_25_percent': sum(abs(x) <= math.log(1.25) for x in logs),
                     'beyond_factor_2': sum(abs(x) > math.log(2) for x in logs)}
    lf = _forces(root, sources, 'arnold-livermore-forces', 'battle_id')
    links = concordance(root, sources, 'arnold-livermore-to-cwsac')
    checked, mismatched = 0, []
    for e in v2['engagements']:
        ok = [f for f, st in link_status(links, e['battle_id']) if st == 'ok']
        if not ok:
            continue
        for s in SIDES:
            row = lf.get((ok[0], 'Union' if s == 'US' else s))
            v = _value(row['str']) if row else None
            if not v:
                continue
            ours = {i['printed']['lower'] for i in e['sides'][s]['inputs']
                    if i.get('independence_group') == 'livermore-numbers-losses' and i['printed']['lower'] == i['printed']['upper']}
            if not ours:
                continue
            checked += 1
            if v not in ours:
                mismatched.append({'battle_id': e['battle_id'], 'side': s, 'arnold': v, 'transcription': sorted(ours)})
    return {'kind': 'strength_compilation_agreement', 'version': 1, 'status': 'descriptive_not_a_model_input',
            'tables_vs_graded_v2_sides': out,
            'livermore_transcription_check': {'sides_compared': checked, 'mismatches': mismatched},
            'note': 'Agreement is not corroboration: these compilations share sources. Ratios compare a table figure with the '
                    'v2 point of a side graded A-C; the bases may differ.'}
