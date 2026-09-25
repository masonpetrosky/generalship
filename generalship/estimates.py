"""Best-estimate side strength (docs/strength-estimates.md): deterministic rules and checker.

Estimates are a separate layer. Nothing here admits a feature, fits a model or
changes the frozen baseline inputs.
"""

from fractions import Fraction
import re
from pathlib import Path

from .evidence import citation_text
from .sources import digest, read_csv, read_json, safe_path, source_metadata_digest, verify_sources

DEFAULT_LEDGER = 'data/estimates/side-strength-v1.json'
SIDES = ('US', 'Confederate')
BASES = ('reported_engaged', 'reported_effective', 'present_for_duty', 'reported_present', 'unknown')
UNUSABLE = {'other_engagement', 'unreadable_value', 'post_outcome_claim'}
UNRESOLVED = {'scope_unresolved', 'engagement_link_unknown', 'interval_unresolved', 'source_role_unresolved'}
BOUND = {'one_sided_bound', 'partial_scope', 'partial_interval'}
LABEL_CODES = {'derivation_unknown', 'estimation_status_unknown'}
CODES = (UNUSABLE | UNRESOLVED | BOUND | LABEL_CODES
         | {'adversary_or_hearsay_estimate', 'post_engagement_state', 'derived_from_losses'})
LOSS_TIMING = ('none', 'prior_engagements_only', 'not_prior')
ADJUSTMENTS = ('completed_sum', 'prior_loss', 'quoted_ratio')
MARGIN = {'A': Fraction(1, 20), 'B': Fraction(3, 20), 'C': Fraction(3, 10)}
OPPONENT_FACTOR = Fraction(3, 4)
COMPILED_GROUPS = {'nps-cwsac', 'livermore-numbers-losses'}  # scoping memo finding 2
INPUT_ID = re.compile(r'(us|cs)-[a-z0-9-]+')
CONSTANTS = {'margins': {'A': '1/20', 'B': '3/20', 'C': '3/10'}, 'opponent_factor': '3/4',
             'basis_order': list(BASES), 'median': 'lower middle for even counts',
             'rounding': 'nearest 10, halves upward; low floor 10'}


class EstimateError(ValueError):
    """Malformed ledger, broken binding or non-reproducing estimate."""


def require(condition, message):
    if not condition:
        raise EstimateError(message)


# ---------- §3 classification ----------

def conditions(codes, loss_timing, adjustment_kinds, basis):
    """The matching §3 rows for a set of input conditions."""
    codes = set(codes)
    row7 = set()
    if basis == 'unknown':
        row7.add('basis_unknown')
    if loss_timing == 'prior_engagements_only' or 'prior_loss' in adjustment_kinds:
        row7.add('prior_engagements_only')
    row7 |= set(adjustment_kinds) & {'completed_sum', 'quoted_ratio'}
    return {'row1': bool(codes & UNUSABLE), 'row5': bool(codes & BOUND),
            'row2': 'adversary_or_hearsay_estimate' in codes,
            'row3': loss_timing == 'not_prior' or 'post_engagement_state' in codes,
            'row4': bool(codes & UNRESOLVED), 'row7': sorted(row7)}


def class_of(rows):
    """First match in the order row 1, row 5, rows 2-4, 6-8 (S1)."""
    if rows['row1']:
        return 'unusable', 'unusable'
    if rows['row5']:
        return 'bound', None
    if rows['row2']:
        return 'C', 'opponent_or_hearsay'
    if rows['row3']:
        return 'C', 'post_start_information'
    if rows['row4']:
        return 'C', 'applicability_unresolved'
    if len(rows['row7']) >= 2:
        return 'C', 'multiple_adjustments'
    if len(rows['row7']) == 1:
        return 'B', rows['row7'][0]
    return 'A', None


def input_rows(inp):
    return conditions(inp['codes'], inp['loss_timing'], [a['kind'] for a in inp['adjustments']], inp['basis'])


def classify(inp):
    return class_of(input_rows(inp))


# ---------- §4 rules ----------

def lower_median(values):
    values = sorted(values)
    return values[(len(values) - 1) // 2]


def upper_median(values):
    values = sorted(values)
    return values[len(values) // 2]


def round10(x):
    """Nearest 10, halves upward, on exact rationals."""
    return int((Fraction(x) / 10 + Fraction(1, 2)).__floor__()) * 10


def printed_value(inp):
    return (Fraction(inp['printed']['lower']) + Fraction(inp['printed']['upper'])) / 2


def value_of(inp, by_id):
    """Rule 1: starting value, then prior_loss, then quoted_ratio (S3)."""
    kinds = {a['kind']: a for a in inp['adjustments']}
    if 'completed_sum' in kinds:
        value = sum((value_of(by_id[o], by_id) for o in kinds['completed_sum']['operands']), Fraction(0))
    else:
        value = printed_value(inp)
    if 'prior_loss' in kinds:
        value -= sum((printed_value(by_id[o]) for o in kinds['prior_loss']['operands']), Fraction(0))
    if 'quoted_ratio' in kinds:
        value *= printed_value(by_id[kinds['quoted_ratio']['operands'][0]]) / 100
    return value


def _groups(inputs, by_id):
    """Rule 2 dependence groups (S4): union-find over the listed links."""
    parent = {i['id']: i['id'] for i in inputs}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)
    operands = {o for i in inputs for a in i['adjustments'] for o in a['operands']}
    pool = [i for i in inputs if i['id'] not in operands]
    for i, a in enumerate(pool):
        for b in pool[i + 1:]:
            va, vb = printed_value(a), printed_value(b)
            if a['document_key'] and a['document_key'] == b['document_key'] and va == vb and a['basis'] == b['basis']:
                union(a['id'], b['id'])
            if (a.get('reproduction_of') == b['id'] or b.get('reproduction_of') == a['id']) and va == vb:
                union(a['id'], b['id'])
            if {a['independence_group'], b['independence_group']} == COMPILED_GROUPS and va == vb:
                union(a['id'], b['id'])
    members = {}
    for i in pool:
        members.setdefault(find(i['id']), []).append(i)
    groups = []
    for ms in members.values():
        ms = sorted(ms, key=lambda i: (i['source_id'] or '', i['id']))
        codes = set().union(*(set(m['codes']) for m in ms))
        timing = max((m['loss_timing'] for m in ms), key=LOSS_TIMING.index)
        kinds = sorted({a['kind'] for m in ms for a in m['adjustments']})
        bases = {m['basis'] for m in ms}
        basis = bases.pop() if len(bases) == 1 else 'unknown'
        rows = conditions(codes, timing, kinds, basis)
        klass, tag = class_of(rows)
        groups.append({'id': ms[0]['id'], 'members': [m['id'] for m in ms], 'klass': klass, 'tag': tag,
                       'rows': rows, 'basis': basis, 'value': value_of(ms[0], by_id), 'codes': codes,
                       'kinds': kinds, 'compiled': any(m['independence_group'] in COMPILED_GROUPS for m in ms)})
    return sorted(groups, key=lambda g: g['id'])


def estimate_side(inputs, *, factor=OPPONENT_FACTOR, basis_order=BASES, median=lower_median):
    by_id = {i['id']: i for i in inputs}
    groups = _groups(inputs, by_id)
    cands = [g for g in groups if g['klass'] in {'A', 'B', 'C'}]
    labels = {'whole_engagement_leakage'}
    if not cands:
        return {'grade': 'D', 'point': None, 'low': None, 'high': None, 'exact': None, 'point_basis': None,
                'method': 'grade_D_no_candidate', 'labels': sorted(labels), 'point_groups': [], 'range_groups': []}
    best = next(k for k in 'ABC' if any(c['klass'] == k for c in cands))
    pool = [c for c in cands if c['klass'] == best]
    if best == 'C' and any(c['tag'] != 'opponent_or_hearsay' for c in pool):
        pool = [c for c in pool if c['tag'] != 'opponent_or_hearsay']
    point_basis = next(b for b in basis_order if any(c['basis'] == b for c in pool))
    used = [c for c in pool if c['basis'] == point_basis]
    if all(c['tag'] == 'opponent_or_hearsay' for c in pool):
        opp = [c for c in cands if c['tag'] == 'opponent_or_hearsay' and c['basis'] in {point_basis, 'unknown'}]
        vals = [c['value'] for c in opp]
        point, low, high = factor * median([c['value'] for c in used]), min(vals) / 2, max(vals)
        rng, method = opp, 'rule4_opponent_only'
        labels.add('opponent_estimate_point')
    else:
        point = median([c['value'] for c in used])
        post_used = any(c['rows']['row3'] for c in used)
        rng = [c for c in cands if c['tag'] != 'opponent_or_hearsay' and c['basis'] in {point_basis, 'unknown'}
               and (not c['rows']['row3'] or post_used)]
        m = MARGIN[best]
        low = min(c['value'] for c in rng) * (1 - m)
        high = max(c['value'] for c in rng) * (1 + m)
        raised = None  # an opponent candidate that sets high is used for the range (engine review R1)
        for c in cands:
            if c['tag'] == 'opponent_or_hearsay' and c['basis'] in {point_basis, 'unknown'} and c['value'] > high:
                high, raised = c['value'], c
        if raised is not None:
            rng = rng + [raised]
        method = 'rule3_median'
    for inp in inputs:  # rule 7 bounds
        rows = input_rows(inp)
        if not rows['row5'] or inp['basis'] != point_basis or inp.get('bound') not in {'upper', 'lower'}:
            continue
        residual = conditions([c for c in inp['codes'] if c not in BOUND], inp['loss_timing'],
                              [a['kind'] for a in inp['adjustments']], inp['basis'])
        if class_of(residual)[0] not in {'A', 'B'}:
            continue
        b = printed_value(inp)
        if inp['bound'] == 'upper':
            if b < point:
                labels.add('bound_conflict')
            elif b < high:
                high = b
        elif b > point:
            labels.add('bound_conflict')
        elif b > low:
            low = b
    touched = {c['id']: c for c in used + rng}
    for c in touched.values():
        if c['rows']['row3']:
            labels.add('post_start_information')
        if c['rows']['row4']:
            labels.add('applicability_unresolved')
        if 'derivation_unknown' in c['codes']:
            labels.add('derivation_unknown')
    for c in used:
        if 'completed_sum' in c['kinds']:
            labels.add('partial_completed')
        if 'estimation_status_unknown' in c['codes']:
            labels.add('estimation_status_unknown')
        if c['compiled']:
            labels.add('compiled_dependence')
    if len(touched) == 1:
        labels.add('single_input')
    rp, rl, rh = round10(point), round10(low), round10(high)
    if rl < 10:
        rl = 10
        labels.add('floor_applied')
    return {'grade': best, 'point': rp, 'low': rl, 'high': rh,
            'exact': {'point': str(point), 'low': str(low), 'high': str(high)},
            'point_basis': point_basis, 'method': method, 'labels': sorted(labels),
            'point_groups': sorted(c['id'] for c in used), 'range_groups': sorted(c['id'] for c in rng)}


def estimate_row(sides):
    out = {s: dict(e) for s, e in sides.items()}
    if all(out[s]['point'] is not None for s in SIDES):
        pb = (out['US']['point_basis'], out['Confederate']['point_basis'])
        if pb[0] != pb[1] or 'unknown' in pb:
            for s in SIDES:
                out[s]['labels'] = sorted(set(out[s]['labels']) | {'basis_mixed'})
    return out


def nested_sets(estimate):
    grades = {estimate[s]['grade'] for s in SIDES}
    leak = any('post_start_information' in estimate[s]['labels'] for s in SIDES)
    sets = [k for k, allowed in (('set1_A', {'A'}), ('set2_AB', {'A', 'B'}), ('set3_ABC', {'A', 'B', 'C'}))
            if grades <= allowed]
    return {'sets': sets, 'excluded_post_start_information': leak}


# ---------- Checker ----------

def _passage(root, sources, dossier, inp):
    ref = inp['ref']
    if 'dossier' in ref:
        claim = next(c for c in dossier['claims'] if c['id'] == ref['dossier']['claim_id'])
        ct = claim['citations'][ref['dossier']['citation_index']]
    else:
        ct = ref['citation']
    return ct['source_id'], ct['quote'], citation_text(root, sources, ct)


def _printed_in_quote(value, quote):
    return any(f in quote for f in {str(value), f'{value:,}'})


def _document_key(sources, source_id):
    source = sources[source_id]
    image = sources.get(source.get('facsimile_source_id'))
    return image['sha256'] if image else source['sha256']


def check(root, path=DEFAULT_LEDGER, ledger=None):
    """Replay the ledger at path, or an in-memory ledger (used by the tamper tests)."""
    root = Path(root)
    if ledger is None:
        ledger = read_json(safe_path(root, str(path)))
    require(ledger.get('kind') == 'side_strength_estimate_ledger' and ledger.get('schema_version') == 1, 'Ledger kind')
    for key in ('design', 'script', 'cohort'):
        b = ledger['bindings'][key]
        require(digest(safe_path(root, b['path'])) == b['sha256'], f'Binding mismatch: {key}')
    sources = verify_sources(root)
    # Bind the cited source entries, not the whole registry, so unrelated additions do not break replay.
    cited = ledger['bindings']['cited_sources']
    for sid, b in cited.items():
        require(sid in sources and source_metadata_digest(sources[sid]) == b['metadata_sha256']
                and sources[sid]['sha256'] == b['raw_sha256'], f'Cited source binding mismatch: {sid}')
    cohort = read_json(root / 'data/pilot/cohort.json')['battle_ids']
    battles = {r['battle']: r for r in read_csv(safe_path(root, sources['arnold-cwsac-battles']['path']))}
    forces = {(r['battle'], r['belligerent']): r for r in read_csv(safe_path(root, sources['arnold-cwsac-forces']['path']))}
    in_scope = sorted(b for b in cohort if battles[b]['result'] != 'Inconclusive' and battles[b]['operation'] != '1')
    out_scope = sorted(set(cohort) - set(in_scope))
    engagements = {e['battle_id']: e for e in ledger['engagements']}
    require(sorted(engagements) == in_scope, 'Coverage: in-scope engagements differ')
    require(sorted(o['battle_id'] for o in ledger['out_of_scope']) == out_scope, 'Coverage: out-of-scope records differ')
    require(all(o.get('reason') for o in ledger['out_of_scope']), 'Out-of-scope records need a reason')
    require(set(ledger['bindings']['dossiers']) == set(in_scope), 'Every in-scope dossier must be bound')
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
