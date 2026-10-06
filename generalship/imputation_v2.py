"""Grade E modelled side strength for any war profile, with the pre-start view (docs/commander-ratings-v4.md §2).

The model, calibration, bounds and truncation are those of imputation.py (docs/strength-imputation.md
§2), whose functions are reused unchanged. A profile supplies what imputation.py hardcodes: the sides,
echelon levels, periods, theaters, reference levels and files.

New in v2 is the pre-start view. Each side whose ledger estimate carries `post_start_information` is
re-estimated by the frozen engine (estimates.estimate_side) without every dependence group that matches
strength-estimates §3 row 3. A side left with a class A-C candidate keeps that pre-start estimate; a side
left with none is modelled as grade E. No post-start figure then reaches a force ratio. With
prestart=False and the v2 ledger, impute() equals imputation.impute exactly (tests/test_imputation_v2.py).
"""

from collections import Counter, defaultdict
from fractions import Fraction
import math

from .estimates import SIDES as ENGINE_SIDES, _groups, estimate_row, estimate_side, printed_value, round10
from .frame import battles as frame_battles, period as frame_period, period_labels, theaters as frame_theaters
from .imputation import MIN_ROWS, TAIL, Z90, Model, calibrate, eligible_bound, quantile, truncated
from .sources import digest, read_json, safe_path

DESIGN = 'docs/commander-ratings-v4.md'
OUTPUT = 'artifacts/strength-imputation-v2.json'
CODE = ('generalship/imputation_v2.py', 'generalship/imputation.py', 'generalship/frame.py', 'generalship/estimates.py')


# ---------- the pre-start view ----------

def prestart_inputs(inputs):
    """The inputs left after removing every member of a dependence group that matches §3 row 3."""
    by_id = {i['id']: i for i in inputs}
    drop = {m for g in _groups(inputs, by_id) if g['rows']['row3'] for m in g['members']}
    kept = [i for i in inputs if i['id'] not in drop]
    for i in kept:
        for a in i['adjustments']:
            if set(a['operands']) & drop:
                raise ValueError(f"{i['id']}: an adjustment operand is a removed post-start input")
    return kept, sorted(drop)


def prestart_view(ledger):
    """{(battle_id, side): re-estimate} for every side whose ledger estimate carries post_start_information.

    The engine re-estimates the whole row (estimate_row), so a side's row-level labels follow from both
    sides' pre-start estimates; only the post-start sides take the new estimate."""
    out = {}
    for e in ledger['engagements']:
        post = [s for s in ENGINE_SIDES if 'post_start_information' in e['sides'][s]['estimate']['labels']]
        if not post:
            continue
        kept = {s: prestart_inputs(e['sides'][s]['inputs']) if s in post else (e['sides'][s]['inputs'], [])
                for s in ENGINE_SIDES}
        row = estimate_row({s: estimate_side(kept[s][0]) for s in ENGINE_SIDES})
        for s in post:
            if 'post_start_information' in row[s]['labels']:
                raise ValueError(f"{e['battle_id']} {s}: the pre-start estimate still uses post-start information")
            out[(e['battle_id'], s)] = {'ledger_estimate': e['sides'][s]['estimate'], 'estimate': row[s],
                                        'removed_inputs': kept[s][1], 'inputs': kept[s][0]}
    return out


# ---------- the side frame and the model ----------

def side_frame(root, profile, strength, command, prestart=True):
    led = read_json(safe_path(root, strength))
    cmd = {e['battle_id']: e for e in read_json(safe_path(root, command))['engagements']}
    battles = frame_battles(root, profile)
    theater = frame_theaters(root, profile)
    view = prestart_view(led) if prestart else {}
    out = []
    for e in led['engagements']:
        b = e['battle_id']
        for s in profile['sides']:
            c = cmd[b]['sides'][s]
            joint = 'joint_command' in c['labels']
            v = view.get((b, s))
            out.append({'battle_id': b, 'side': s,
                        'estimate': v['estimate'] if v else e['sides'][s]['estimate'],
                        'inputs': v['inputs'] if v else e['sides'][s]['inputs'],
                        'post_start_ledger': v is not None,
                        'ledger_echelon': c['echelon'], 'joint_command': joint,
                        'echelon_raw': 'unknown' if joint else c['echelon'],
                        'period': frame_period(profile, battles[b]['start_date']),
                        'theater': theater[battles[b]['campaign']], 'result': battles[b]['result']})
    return out, view


def levels_for(train, profile):
    """Non-reference levels per predictor after merging levels with fewer than MIN_ROWS training rows."""
    order = {'echelon': profile['echelons'], 'side': profile['sides'], 'period': period_labels(profile),
             'theater': profile['theaters']}
    ref = profile['reference']
    merges, mapping = {}, {}
    counts = {k: Counter(r[k] for r in train) for k in ('echelon', 'side', 'period', 'theater')}
    for k in counts:
        m = {}
        for v in order[k]:
            if v == ref[k] or counts[k][v] >= MIN_ROWS:
                m[v] = v
            elif k == 'echelon':
                m[v] = 'unknown'
            else:  # the adjacent level in the declared order
                seq = [x for x in order[k] if counts[k][x] >= MIN_ROWS or x == ref[k]]
                i = order[k].index(v)
                m[v] = min(seq, key=lambda x: abs(order[k].index(x) - i))
            if m[v] != v and counts[k][v]:
                merges[f'{k}={v}'] = {'into': m[v], 'training_rows': counts[k][v]}
        mapping[k] = m
    levels = {k: [v for v in order[k] if mapping[k][v] == v and v != ref[k] and counts[k][v] >= MIN_ROWS] for k in counts}
    return mapping, levels, merges


def apply_mapping(r, mapping):
    return {**r, 'echelon': mapping['echelon'].get(r['echelon_raw'], 'unknown'), 'side': r['side'],
            'period': mapping['period'][r['period']], 'theater': mapping['theater'][r['theater']]}


def impute(root, profile, strength=None, command=None, *, train_grades='ABC', joint_ledger_echelon=False,
           all_bounds=False, prestart=True):
    """Fit the grade E model; return it with the distribution of every side graded D in the (pre-start) view."""
    strength = strength or profile['strength_ledger']
    command = command or profile['command_ledger']
    frame, view = side_frame(root, profile, strength, command, prestart)
    for r in frame:
        if joint_ledger_echelon:
            r['echelon_raw'] = r['ledger_echelon']
    train_raw = [r for r in frame if r['estimate']['grade'] in train_grades and r['estimate']['point']
                 and 'post_start_information' not in r['estimate']['labels']]
    for r in train_raw:
        r['y'] = math.log(r['estimate']['point'])
    pre = [{**r, 'echelon': r['echelon_raw']} for r in train_raw]
    mapping, levels, merges = levels_for(pre, profile)
    train = [apply_mapping(r, mapping) for r in train_raw]
    model = Model(train, levels)
    c, k, loo = calibrate(train, levels)
    sd = k * model.sigma
    battles = frame_battles(root, profile)
    by_camp = defaultdict(list)
    for r in train:
        by_camp[battles[r['battle_id']]['campaign']].append(r)
    hit = 0
    for camp, rows in by_camp.items():
        m = Model([r for r in train if battles[r['battle_id']]['campaign'] != camp], levels)
        hit += sum(abs(r['y'] - m.mean(r)) <= Z90 * k * m.sigma for r in rows)
    loco_cov = hit / len(train)
    sides = []
    for r in frame:
        if r['estimate']['grade'] != 'D':
            continue
        x = apply_mapping(r, mapping)
        mu = model.mean(x)
        lows, highs, set_aside = [], [], []
        for inp in r['inputs']:
            if inp.get('bound') in {'lower', 'upper'} and all_bounds:
                ok, why = True, None
            else:
                ok, why = eligible_bound(inp)
            if ok:
                (lows if inp['bound'] == 'lower' else highs).append((printed_value(inp), inp['id']))
            else:
                set_aside.append({'input': inp['id'], 'bound': inp.get('bound'), 'reason': why})
        labels = {'modelled_estimate', 'echelon_basis'}
        if r['post_start_ledger']:
            labels.add('post_start_modelled')
        if r['joint_command'] and not joint_ledger_echelon:
            labels.add('joint_command_echelon_unknown')
        if r['ledger_echelon'] == 'flotilla':
            labels.add('naval_side')
        if any(s['bound'] in {'lower', 'upper'} for s in set_aside):
            labels.add('bound_not_applied')
        L = max(lows)[0] if lows else None
        U = min(highs)[0] if highs else None
        if all_bounds and any(('post_engagement_state' in i['codes'] or i['loss_timing'] == 'not_prior')
                              for i in r['inputs'] if i.get('bound') in {'lower', 'upper'}):
            labels.add('post_start_information')
        if L is not None and U is not None and L > U:
            labels.add('bound_conflict')
            L = U = None
        lo = float(L) if L is not None else None
        hi = float(U) if U is not None else None
        if lo is not None:
            labels.add('bounded_lower')
        if hi is not None:
            labels.add('bounded_upper')
        _, _, fa, fb = truncated(mu, sd, lo, hi)
        fixed = None
        if fb - fa < TAIL:
            labels.add('bound_dominates')
            fixed = hi if (hi is not None and math.log(hi) < mu) else lo
        q = (lambda p: fixed) if fixed is not None else (lambda p: quantile(mu, sd, p, lo, hi))
        rounded = lambda v: max(10, round10(Fraction(v).limit_denominator(1000)))
        sides.append({'battle_id': r['battle_id'], 'side': r['side'], 'grade': 'E',
                      'predictors': {'echelon': x['echelon'], 'ledger_echelon': r['ledger_echelon'], 'side': r['side'],
                                     'period': x['period'], 'theater': x['theater']},
                      'mu_log': mu, 'sd_log': sd, 'lower_bound': lo, 'upper_bound': hi, 'fixed': fixed,
                      'applied_bounds': {'lower': [i for _, i in lows], 'upper': [i for _, i in highs]},
                      'set_aside_inputs': set_aside,
                      'point': rounded(q(0.5)), 'low': rounded(q(0.1)), 'high': rounded(q(0.9)),
                      'labels': sorted(labels)})
    comp = {k2: {'training': dict(Counter(r[k2] for r in train_raw if k2 != 'echelon') if k2 != 'echelon'
                                  else Counter(r['echelon_raw'] for r in train_raw)),
                 'modelled': dict(Counter((r['echelon_raw'] if k2 == 'echelon' else r[k2]) for r in frame
                                          if r['estimate']['grade'] == 'D'))}
            for k2 in ('echelon', 'period', 'theater', 'side')}
    a_won = next(o for o, v in profile['outcomes'].items() if v == 1)
    sel = Counter()
    for r in frame:
        won = (r['result'] == a_won) == (r['side'] == profile['sides'][0])
        sel[('modelled' if r['estimate']['grade'] == 'D' else 'graded', 'won' if won else 'lost')] += 1
    order = {s: i for i, s in enumerate(profile['sides'])}
    pre_start = [{'battle_id': b, 'side': s, 'removed_inputs': v['removed_inputs'],
                  'ledger': {k2: v['ledger_estimate'][k2] for k2 in ('grade', 'point', 'low', 'high')},
                  'pre_start': {k2: v['estimate'][k2] for k2 in ('grade', 'point', 'low', 'high', 'point_basis', 'method', 'labels')}}
                 for (b, s), v in sorted(view.items(), key=lambda kv: (kv[0][0], order[kv[0][1]]))]
    return {'kind': 'strength_imputation', 'version': 2, 'profile': profile['name'],
            'options': {'train_grades': train_grades, 'joint_ledger_echelon': joint_ledger_echelon,
                        'all_bounds': all_bounds, 'prestart': prestart},
            'model': {'columns': model.columns, 'coefficients': model.beta, 'sigma': model.sigma, 'k': k,
                      'predictive_sd': sd, 'n': model.n, 'p': model.p, 'ridge': 1.0, 'reference': profile['reference'],
                      'merges': merges, 'loo_coverage_80': c, **loo, 'loco_coverage_80_at_k': loco_cov,
                      'train_grades': train_grades},
            'composition': comp,
            'selection_descriptive': {f'{a}_{b}': n for (a, b), n in sorted(sel.items())},
            'pre_start_view': pre_start,
            'sides': sorted(sides, key=lambda s: (s['battle_id'], order[s['side']]))}


def build(root, profile):
    """The committed grade E output of run 4: bindings plus the primary imputation."""
    result = impute(root, profile)
    bound = (DESIGN, profile['strength_ledger'], profile['command_ledger'], profile['campaigns'], profile['battles']) + CODE
    result['bindings'] = {p: digest(safe_path(root, p)) for p in bound}
    return result
