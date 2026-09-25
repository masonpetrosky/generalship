"""Modelled side strength, grade E (docs/strength-imputation.md §2).

A typical-size model of log strength from command echelon, side, period and theater, fitted on the
sides the reviewed v2 strength ledger grades A–C, calibrated by leave-one-out and truncated to each
grade D side's applicable bounds. It uses no outcome, casualty figure or source outside the reviewed
ledgers and the frozen CWSAC tables. Nothing here fits a rating.
"""

from collections import Counter, defaultdict
from fractions import Fraction
import math
from statistics import NormalDist

from .command import check as check_command
from .estimates import BOUND, class_of, conditions, printed_value, round10
from .estimates_v2 import check as check_strength
from .sources import digest, read_csv, read_json, safe_path

STRENGTH = 'data/estimates/side-strength-v2.json'
COMMAND = 'data/command/responsibility-v2.json'
CAMPAIGNS = 'data/raw/cwsac_campaigns.csv'
BATTLES = 'data/raw/cwsac_battles.csv'
DESIGN = 'docs/strength-imputation.md'
SIDES = ('US', 'Confederate')
ECHELONS = ('army', 'corps_or_wing', 'division', 'brigade', 'regiment', 'detachment_or_post', 'flotilla', 'unknown')
PERIODS = ('1861-1862', '1863', '1864-1865')
THEATERS = ('Eastern', 'Western', 'Trans-Mississippi', 'Lower Seaboard', 'Pacific Coast')
REFERENCE = {'echelon': 'unknown', 'side': 'US', 'period': '1863', 'theater': 'Eastern'}
RIDGE = 1.0
MIN_ROWS = 5
Z90 = NormalDist().inv_cdf(0.9)
TAIL = 1e-12


class ImputationError(ValueError):
    """Malformed inputs or a non-reproducing imputation."""


def period(start_date):
    y = int(start_date[:4])
    return '1861-1862' if y <= 1862 else '1863' if y == 1863 else '1864-1865'


def solve(a, b):
    """Gaussian elimination with partial pivoting (small dense systems)."""
    n = len(b)
    m = [row[:] + [bv] for row, bv in zip(a, b)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[piv] = m[piv], m[i]
        for r in range(i + 1, n):
            f = m[r][i] / m[i][i]
            if f:
                for c in range(i, n + 1):
                    m[r][c] -= f * m[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][c] * x[c] for c in range(i + 1, n))) / m[i][i]
    return x


class Model:
    """Ridge least squares on indicator columns; intercept unpenalized (§2 Fit)."""

    def __init__(self, rows, levels):
        self.levels = levels  # predictor -> non-reference levels (column order)
        self.columns = ['intercept'] + [f'{k}={v}' for k, vs in levels.items() for v in vs]
        p = len(self.columns)
        xtx = [[0.0] * p for _ in range(p)]
        xty = [0.0] * p
        xs = [self.vector(r) for r in rows]
        for x, r in zip(xs, rows):
            for i in range(p):
                if x[i]:
                    xty[i] += x[i] * r['y']
                    for j in range(p):
                        xtx[i][j] += x[i] * x[j]
        for i in range(1, p):
            xtx[i][i] += RIDGE
        self.beta = solve(xtx, xty)
        n = len(rows)
        rss = sum((r['y'] - self.mean_x(x)) ** 2 for x, r in zip(xs, rows))
        self.n, self.p = n, p
        self.sigma = math.sqrt(rss / n) * math.sqrt(n / (n - p))

    def vector(self, r):
        return [1.0] + [1.0 if r[k] == v else 0.0 for k, vs in self.levels.items() for v in vs]

    def mean_x(self, x):
        return sum(b * xi for b, xi in zip(self.beta, x))

    def mean(self, r):
        return self.mean_x(self.vector(r))


def truncated(mu, sd, lo=None, hi=None):
    """Standardized truncation limits and their normal mass."""
    nd = NormalDist()
    a = -math.inf if lo is None else (math.log(lo) - mu) / sd
    b = math.inf if hi is None else (math.log(hi) - mu) / sd
    fa = 0.0 if a == -math.inf else nd.cdf(a)
    fb = 1.0 if b == math.inf else nd.cdf(b)
    return a, b, fa, fb


def quantile(mu, sd, q, lo=None, hi=None):
    _, _, fa, fb = truncated(mu, sd, lo, hi)
    u = min(max(fa + q * (fb - fa), 1e-300), 1 - 1e-16)
    return math.exp(mu + sd * NormalDist().inv_cdf(u))


def draw(mu, sd, u, lo=None, hi=None):
    """Inverse-CDF draw from the truncated normal on the log scale (§5)."""
    return quantile(mu, sd, u, lo, hi)


def eligible_bound(inp):
    """§2 Bounds: a directional bound that is class A or B apart from its bound codes (rule 7 test)."""
    if inp.get('bound') not in {'lower', 'upper'}:
        return False, 'no bound direction'
    residual = conditions([c for c in inp['codes'] if c not in BOUND], inp['loss_timing'],
                          [a['kind'] for a in inp['adjustments']], inp['basis'])
    k, tag = class_of(residual)
    if k in {'A', 'B'}:
        return True, None
    return False, f'fails the rule 7 test (class {k}{", " + tag if tag else ""})'


def side_frame(root):
    """Every in-scope side with its predictors, ledger estimate and inputs."""
    strength = read_json(safe_path(root, STRENGTH))
    command = {e['battle_id']: e for e in read_json(safe_path(root, COMMAND))['engagements']}
    battles = {r['battle']: r for r in read_csv(safe_path(root, BATTLES))}
    theater = {r['campaign']: r['theater'] for r in read_csv(safe_path(root, CAMPAIGNS))}
    out = []
    for e in strength['engagements']:
        b = e['battle_id']
        for s in SIDES:
            c = command[b]['sides'][s]
            joint = 'joint_command' in c['labels']
            out.append({'battle_id': b, 'side': s, 'estimate': e['sides'][s]['estimate'],
                        'inputs': e['sides'][s]['inputs'], 'ledger_echelon': c['echelon'],
                        'joint_command': joint,
                        'echelon_raw': 'unknown' if joint else c['echelon'],
                        'period': period(battles[b]['start_date']),
                        'theater': theater[battles[b]['campaign']],
                        'result': battles[b]['result']})
    return out


def levels_for(train):
    """Non-reference levels per predictor after merging levels with fewer than MIN_ROWS rows (§2)."""
    merges = {}
    counts = {k: Counter(r[k] for r in train) for k in ('echelon', 'side', 'period', 'theater')}
    order = {'echelon': ECHELONS, 'side': SIDES, 'period': PERIODS, 'theater': THEATERS}
    mapping = {}
    for k in counts:
        m = {}
        for v in order[k]:
            if v == REFERENCE[k] or counts[k][v] >= MIN_ROWS:
                m[v] = v
            elif k == 'echelon':
                m[v] = 'unknown'
            else:  # adjacent level in the declared order (none merges on the v2 ledgers)
                seq = [x for x in order[k] if counts[k][x] >= MIN_ROWS or x == REFERENCE[k]]
                i = order[k].index(v)
                m[v] = min(seq, key=lambda x: abs(order[k].index(x) - i))
            if m[v] != v and counts[k][v]:
                merges[f'{k}={v}'] = {'into': m[v], 'training_rows': counts[k][v]}
        mapping[k] = m
    levels = {k: [v for v in order[k] if mapping[k][v] == v and v != REFERENCE[k] and counts[k][v] >= MIN_ROWS]
              for k in counts}
    return mapping, levels, merges


def apply_mapping(r, mapping):
    return {**r, 'echelon': mapping['echelon'].get(r['echelon_raw'], 'unknown'),
            'side': r['side'], 'period': mapping['period'][r['period']],
            'theater': mapping['theater'][r['theater']]}


def calibrate(train, levels):
    """Leave-one-out coverage c and the widening factor k (§2 Calibration)."""
    loo = []
    for i in range(len(train)):
        m = Model(train[:i] + train[i + 1:], levels)
        loo.append((train[i], m.mean(train[i]), m.sigma))
    inside = lambda k: sum(abs(r['y'] - mu) <= Z90 * k * sd for r, mu, sd in loo) / len(loo)
    c = inside(1.0)
    k = 1.0
    while inside(k) < 0.80:
        k = round(k + 0.01, 2)
    by_echelon = defaultdict(list)
    for r, mu, _ in loo:
        by_echelon[r['echelon']].append(abs(r['y'] - mu))
    med = lambda xs: sorted(xs)[len(xs) // 2] if len(xs) % 2 else sum(sorted(xs)[len(xs) // 2 - 1:len(xs) // 2 + 1]) / 2
    return c, k, {'median_abs_log_error': med([abs(r['y'] - mu) for r, mu, _ in loo]),
                  'median_abs_log_error_by_echelon': {e: med(v) for e, v in sorted(by_echelon.items())}}


def impute(root, *, train_grades='ABC', joint_ledger_echelon=False, all_bounds=False, verify=True):
    """Fit the grade E model and return it with every grade D side's grade E distribution."""
    if verify:
        check_strength(root, STRENGTH)
        check_command(root, COMMAND)
    frame = side_frame(root)
    for r in frame:
        if joint_ledger_echelon:
            r['echelon_raw'] = r['ledger_echelon']
    train_raw = [r for r in frame if r['estimate']['grade'] in train_grades and r['estimate']['point']
                 and 'post_start_information' not in r['estimate']['labels']]
    for r in train_raw:
        r['y'] = math.log(r['estimate']['point'])
    pre = [{**r, 'echelon': r['echelon_raw']} for r in train_raw]
    mapping, levels, merges = levels_for(pre)
    train = [apply_mapping(r, mapping) for r in train_raw]
    model = Model(train, levels)
    c, k, loo = calibrate(train, levels)
    sd = k * model.sigma
    # descriptive leave-one-campaign-out coverage at k
    by_camp = defaultdict(list)
    battles = {r['battle']: r for r in read_csv(safe_path(root, BATTLES))}
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
                 'grade_D': dict(Counter((r['echelon_raw'] if k2 == 'echelon' else r[k2]) for r in frame
                                         if r['estimate']['grade'] == 'D'))}
            for k2 in ('echelon', 'period', 'theater', 'side')}
    sel = Counter()
    for r in frame:
        won = (r['result'] == 'Union') == (r['side'] == 'US')
        sel[('grade_D' if r['estimate']['grade'] == 'D' else 'graded', 'won' if won else 'lost')] += 1
    return {'kind': 'strength_imputation', 'version': 1,
            'model': {'columns': model.columns, 'coefficients': model.beta, 'sigma': model.sigma, 'k': k,
                      'predictive_sd': sd, 'n': model.n, 'p': model.p, 'ridge': RIDGE, 'reference': REFERENCE,
                      'merges': merges, 'loo_coverage_80': c, **loo, 'loco_coverage_80_at_k': loco_cov,
                      'train_grades': train_grades},
            'composition': comp,
            'selection_descriptive': {f'{a}_{b}': n for (a, b), n in sorted(sel.items())},
            'sides': sorted(sides, key=lambda s: (s['battle_id'], SIDES.index(s['side'])))}


def build(root, verify=True):
    """The committed output (§7): bindings plus the primary imputation."""
    result = impute(root, verify=verify)
    result['bindings'] = {p: digest(safe_path(root, p)) for p in (DESIGN, STRENGTH, COMMAND, CAMPAIGNS, BATTLES,
                                                                  'generalship/imputation.py')}
    return result
