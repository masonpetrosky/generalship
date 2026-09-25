"""Checker for the v2 (cohort v2) side-strength ledger (docs/ledgers-v2.md).

The estimation rules are the unchanged v1 engine in estimates.py, whose bytes the v1 ledger
binds; this module only replays a successor ledger against the cohort its bindings name.
Nothing here admits a feature, fits a model or changes the frozen baseline inputs.
"""

from pathlib import Path

from .estimates import (ADJUSTMENTS, BASES, CODES, CONSTANTS, INPUT_ID, LOSS_TIMING, SIDES, EstimateError,
                        _document_key, _passage, _printed_in_quote, classify, estimate_row, estimate_side,
                        nested_sets, printed_value, require, value_of)
from .sources import digest, read_csv, read_json, safe_path, source_metadata_digest, verify_sources

DEFAULT_LEDGER = 'data/estimates/side-strength-v2.json'


def check(root, path=DEFAULT_LEDGER, ledger=None, only=None):
    """Replay a v2 ledger at path, or an in-memory ledger (used by the tamper tests).
    `only` checks a subset of engagements during extraction and skips the coverage checks."""
    root = Path(root)
    if ledger is None:
        ledger = read_json(safe_path(root, str(path)))
    require(ledger.get('kind') == 'side_strength_estimate_ledger' and ledger.get('schema_version') == 1, 'Ledger kind')
    require(ledger.get('version') == 2, 'Ledger version')
    for key in ('design', 'addendum', 'script', 'engine', 'cohort', 'owner_decision'):
        b = ledger['bindings'][key]
        require(digest(safe_path(root, b['path'])) == b['sha256'], f'Binding mismatch: {key}')
    sources = verify_sources(root)
    # Bind the cited source entries, not the whole registry, so unrelated additions do not break replay.
    cited = ledger['bindings']['cited_sources']
    for sid, b in cited.items():
        require(sid in sources and source_metadata_digest(sources[sid]) == b['metadata_sha256']
                and sources[sid]['sha256'] == b['raw_sha256'], f'Cited source binding mismatch: {sid}')
    cohort = read_json(safe_path(root, ledger['bindings']['cohort']['path']))['battle_ids']
    battles = {r['battle']: r for r in read_csv(safe_path(root, sources['arnold-cwsac-battles']['path']))}
    forces = {(r['battle'], r['belligerent']): r for r in read_csv(safe_path(root, sources['arnold-cwsac-forces']['path']))}
    in_scope = sorted(b for b in cohort if battles[b]['result'] != 'Inconclusive' and battles[b]['operation'] != '1')
    # Two-sided rule (docs/ledgers-v2.md): a record with any other listed belligerent is out of scope.
    others = {b for (b, side) in forces if side not in SIDES}
    others |= {r['battle'] for r in read_csv(safe_path(root, sources['arnold-cwsac-commanders']['path'])) if r['belligerent'] not in SIDES}
    in_scope = [b for b in in_scope if b not in others]
    out_scope = sorted(set(cohort) - set(in_scope))
    engagements = {e['battle_id']: e for e in ledger['engagements']}
    if only is None:
        require(sorted(engagements) == in_scope, 'Coverage: in-scope engagements differ')
        require(sorted(o['battle_id'] for o in ledger['out_of_scope']) == out_scope, 'Coverage: out-of-scope records differ')
        require(all(o.get('reason') for o in ledger['out_of_scope']), 'Out-of-scope records need a reason')
        require(set(ledger['bindings']['dossiers']) == set(in_scope), 'Every in-scope dossier must be bound')
    else:
        require(set(only) <= set(in_scope), 'Subset check: engagement outside the in-scope cohort')
        in_scope = sorted(only)
    require(ledger['constants'] == CONSTANTS, 'Ledger constants differ from the code')
    results = {}
    for bid in in_scope:
        b = ledger['bindings']['dossiers'][bid]
        require(digest(safe_path(root, b['path'])) == b['sha256'], f'Dossier binding: {bid}')
        dossier = read_json(safe_path(root, b['path']))
        e = engagements[bid]
        require(set(e['sides']) == set(SIDES), f'{bid}: both sides required')
        require(e['interval'] == [battles[bid]['start_date'], battles[bid]['end_date'] or battles[bid]['start_date']],
                f'{bid}: interval differs from the frozen record')
        estimates = {}
        for side in SIDES:
            s = e['sides'][side]
            ids = [i['id'] for i in s['inputs']]
            require(len(set(ids)) == len(ids), f'{bid} {side}: duplicate input IDs')
            for inp in s['inputs']:
                where = f'{bid} {side} {inp["id"]}'
                require(inp['printed']['lower'] <= inp['printed']['upper'], f'{where}: printed bounds reversed')
                require(inp.get('bound') in {'upper', 'lower', None}, f'{where}: bound direction')
                require('derived_from_losses' not in inp['codes'] or inp['loss_timing'] != 'none', f'{where}: loss timing')
                require(inp.get('reproduction_of') in (None, *ids), f'{where}: unresolved reproduction link')
                require(inp['source_id'] not in {'livermore-ocr-v1'} and not str(inp['source_id']).endswith('-image-v1'),
                        f'{where}: Livermore figures are cited from the transcription')
                require(set(inp['codes']) <= CODES and inp['basis'] in BASES and inp['loss_timing'] in LOSS_TIMING, f'{where}: codes')
                require(all(a['kind'] in ADJUSTMENTS and all(o in ids for o in a['operands']) for a in inp['adjustments']),
                        f'{where}: adjustments')
                if any(a['kind'] == 'completed_sum' for a in inp['adjustments']):
                    require(inp['source_id'] is None and inp['ref'] is None, f'{where}: a sum has no quote of its own')
                    by_id = {i['id']: i for i in s['inputs']}
                    require(value_of(inp, by_id) == printed_value(inp), f'{where}: sum printed value differs from its operands')
                    require(all(by_id[o]['basis'] == inp['basis'] for a in inp['adjustments'] for o in a['operands']),
                            f'{where}: a sum takes its operands\' basis')
                else:
                    sid, quote, passage = _passage(root, sources, dossier, inp)
                    require(sid == inp['source_id'] and sid in cited, f'{where}: source ID or unbound source')
                    require(quote in passage, f'{where}: quote not in passage')
                    require(inp['document_key'] == _document_key(sources, sid), f'{where}: document key')
                    require(inp['independence_group'] == sources[sid]['independence_group'], f'{where}: independence group')
                    if inp.get('printed_text'):
                        require(inp['printed_text'] in quote, f'{where}: printed text not in quote')
                    else:
                        for v in {inp['printed']['lower'], inp['printed']['upper']}:
                            require(_printed_in_quote(v, quote), f'{where}: printed value {v} not in quote')
                require(inp['class'] == classify(inp)[0], f'{where}: class {inp["class"]} != {classify(inp)[0]}')
            estimates[side] = estimate_side(s['inputs'])
        estimates = estimate_row(estimates)
        for side in SIDES:
            require(e['sides'][side]['estimate'] == estimates[side], f'{bid} {side}: estimate does not reproduce')
            est = estimates[side]
            if est['point'] is not None:
                require(0 < est['low'] <= est['point'] <= est['high'], f'{bid} {side}: range order')
            else:
                require(bool(e['sides'][side].get('null_reason')), f'{bid} {side}: grade D needs a reason')
        inv = e['inventory']
        all_ids = {i['id'] for side in SIDES for i in e['sides'][side]['inputs']}
        named = [u for x in inv['dossier_claims'] + inv['dossier_quantities'] if isinstance(x['use'], list) for u in x['use']]
        named += list(inv['cwsac_forces'].values()) + list((inv.get('livermore') or {}).get('inputs', []))
        unresolved = [u for u in named if INPUT_ID.fullmatch(u) and u not in all_ids]
        require(not unresolved, f'{bid}: inventory names unknown inputs {unresolved}')
        claims = {c['id'] for c in dossier['claims'] if c['dimension'] == 'strength'}
        require(claims <= {x['claim_id'] for x in inv['dossier_claims']}, f'{bid}: dossier claim inventory incomplete')
        quantities = {q['id'] for q in dossier.get('quantities', [])}
        require(quantities <= {x['quantity_id'] for x in inv['dossier_quantities']}, f'{bid}: quantity inventory incomplete')
        for side in SIDES:
            if forces.get((bid, side), {}).get('strength_min'):
                require(side in inv['cwsac_forces'], f'{bid}: CWSAC forces figure not inventoried')
        require(nested_sets(estimates) == e['nested'], f'{bid}: nested-set membership does not reproduce')
        results[bid] = estimates
    sets = {b: nested_sets(results[b]) for b in results}
    return {'kind': 'side_strength_estimate_check', 'in_scope': len(in_scope), 'out_of_scope': len(out_scope),
            'side_grades': {g: sum(results[b][s]['grade'] == g for b in results for s in SIDES) for g in 'ABCD'},
            'rows_by_set_fit_eligible': {k: sum(k in sets[b]['sets'] and not sets[b]['excluded_post_start_information']
                                                for b in results) for k in ('set1_A', 'set2_AB', 'set3_ABC')},
            'rows_excluded_post_start_information': sum(sets[b]['excluded_post_start_information'] for b in results),
            'fitted': False, 'promoted_rows': 0}
