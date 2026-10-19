"""Small, standard-library logistic recovery experiments; never imports historical outcomes.

This is a diagnostic solver, not a replacement for the frozen rating engines. Coordinates use
the same normal-prior MAP objective. Tests compare its solution with run 4 on constructed data.
"""

import math
import random
from collections import defaultdict

from .baseline import sigmoid


def features(row, commanders=True, armies=False):
    out = {'intercept': 1.0, 'force': row['x']}
    for prefix, enabled, fields in (('commander', commanders, ('a', 'b')),
                                    ('army', armies, ('army_a', 'army_b'))):
        if enabled:
            for field, sign in zip(fields, (1.0, -1.0)):
                if row.get(field) is not None:
                    key = f'{prefix}:{row[field]}'
                    out[key] = out.get(key, 0.0) + sign
    return {k: v for k, v in out.items() if v != 0.0}


def softplus(z):
    return max(z, 0.0) + math.log1p(math.exp(-abs(z)))


def fit(rows, *, tau=0.6, army_sd=0.8, commanders=True, armies=False, tolerance=1e-7):
    """Sparse coordinate Newton MAP, with a checked final gradient and per-step backtracking."""
    if not rows or tau <= 0 or army_sd <= 0:
        raise ValueError('Nonempty rows and positive prior SDs are required')
    xs = [features(r, commanders, armies) for r in rows]
    ys = [r['y'] for r in rows]
    if any(y not in (0, 1) for y in ys) or any(not math.isfinite(v) for x in xs for v in x.values()):
        raise ValueError('Synthetic response or covariate is invalid')
    adjacency = defaultdict(list)
    for i, x in enumerate(xs):
        for k, v in x.items():
            adjacency[k].append((i, v))
    keys = sorted(adjacency)
    precision = {k: 1.0 / (tau if k.startswith('commander:') else
                           army_sd if k.startswith('army:') else 1.0) ** 2 for k in keys}
    coef, eta = dict.fromkeys(keys, 0.0), [0.0] * len(rows)

    def gradient(k):
        return precision[k] * coef[k] + math.fsum(v * (sigmoid(eta[i]) - ys[i])
                                                  for i, v in adjacency[k])

    for _ in range(2000):
        for k in keys:
            pairs, value, prec = adjacency[k], coef[k], precision[k]
            probabilities = [(i, v, sigmoid(eta[i])) for i, v in pairs]
            g = prec * value + math.fsum(v * (p - ys[i]) for i, v, p in probabilities)
            h = prec + math.fsum(v * v * p * (1.0 - p) for _, v, p in probabilities)
            delta = -g / h
            if abs(delta) < 1e-13:
                continue
            current = prec * value * value / 2.0 + math.fsum(softplus(eta[i]) - ys[i] * eta[i]
                                                            for i, _ in pairs)
            scale = 1.0
            while True:
                change = scale * delta
                trial = prec * (value + change) ** 2 / 2.0 + math.fsum(
                    softplus(eta[i] + v * change) - ys[i] * (eta[i] + v * change) for i, v in pairs)
                if trial <= current + 1e-4 * change * g + 1e-13:
                    break
                scale /= 2.0
                if scale < 1e-12:
                    raise ValueError('Synthetic coordinate line search did not converge')
            coef[k] += change
            for i, v in pairs:
                eta[i] += v * change
        maximum = max(abs(gradient(k)) for k in keys)
        if maximum < tolerance:
            return {'coef': coef, 'max_gradient': maximum}
    raise ValueError('Synthetic coordinate fit did not converge')


def predict(model, row, *, commanders=True, armies=False):
    return sigmoid(math.fsum(model['coef'].get(k, 0.0) * v for k, v in
                             features(row, commanders, armies).items()))


def loss(p, y):
    p = min(1.0 - 1e-15, max(1e-15, p))
    return -y * math.log(p) - (1 - y) * math.log1p(-p)


def mean(values):
    values = list(values)
    return math.fsum(values) / len(values) if values else None


def summarize(values):
    """Descriptive repetition distribution, not an interval for a historical parameter."""
    values = sorted(v for v in values if v is not None)
    if not values:
        return {'n': 0, 'mean': None, 'q025': None, 'q975': None}
    n = len(values)
    return {'n': n, 'mean': mean(values), 'q025': values[int((n - 1) * 0.025)],
            'q975': values[int((n - 1) * 0.975)]}


def centered(values):
    centre = mean(values.values())
    return {k: v - centre for k, v in values.items()}


def recovery(model, truth):
    true = centered(truth)
    estimated = centered({k: model['coef'].get(f'commander:{k}', 0.0) for k in truth})
    vt = math.fsum(v * v for v in true.values())
    ve = math.fsum(v * v for v in estimated.values())
    cross = math.fsum(v * estimated[k] for k, v in true.items())
    return {'rmse': math.sqrt(mean((estimated[k] - true[k]) ** 2 for k in true)),
            'estimated_sd': math.sqrt(ve / len(true)),
            'slope': cross / vt if vt > 1e-14 else None,
            'correlation': cross / math.sqrt(vt * ve) if vt * ve > 1e-14 else None}


def generate(schedule, scenario, repetition, protocol):
    """All effects, force values, army assignments and responses below are invented simulations."""
    rng = random.Random(protocol['seed'] + 100000 * protocol['scenarios'].index(scenario) + repetition)
    labels = sorted({r[s] for r in schedule for s in ('a', 'b')})
    groups = sorted({r['campaign'] for r in schedule})
    label_index, group_index = {c: i for i, c in enumerate(labels)}, {c: i for i, c in enumerate(groups)}
    commander_sd = protocol['commander_sd'] if scenario in ('commander', 'switching_armies') else 0.0
    army_sd = protocol['army_sd'] if scenario in ('stable_army_alias', 'switching_armies') else 0.0
    truth = {c: rng.gauss(0.0, commander_sd) for c in labels}
    bias = {c: rng.gauss(0.0, protocol['source_bias_sd']) for c in labels}
    group_effect = {g: rng.gauss(0.0, protocol['group_sd']) if scenario != 'null' else 0.0 for g in groups}
    army_effect = {}
    out = []
    for r in schedule:
        army = {}
        for slot in ('a', 'b'):
            key = ('permanent:' + r[slot]) if scenario != 'switching_armies' else (
                f'{slot}:pool:{(label_index[r[slot]] + group_index[r["campaign"]]) % protocol["army_pools_per_side"]}')
            army[slot] = key
            if key not in army_effect:
                army_effect[key] = rng.gauss(0.0, army_sd)
        true_x = rng.uniform(-0.5, 0.5)
        observed_x = true_x
        if scenario == 'source_bias':
            observed_x = max(-0.95, min(0.95, true_x + bias[r['a']] - bias[r['b']]))
        eta = (true_x + truth[r['a']] - truth[r['b']] + army_effect[army['a']]
               - army_effect[army['b']] + group_effect[r['campaign']])
        kept = {k: r[k] for k in ('battle_id', 'campaign', 'war', 'year', 'a', 'b')}
        out.append({**kept, 'army_a': army['a'], 'army_b': army['b'], 'x': observed_x,
                    'y': int(rng.random() < sigmoid(eta))})
    return out, truth


def folds(rows, strategy):
    if strategy == 'forward_time':
        train, test = [r for r in rows if r['year'] <= 1812], [r for r in rows if r['year'] >= 1813]
        return [(train, test)] if train and test else []
    field = 'campaign' if strategy == 'war_year' else 'war'
    return [([r for r in rows if r[field] != g], [r for r in rows if r[field] == g])
            for g in sorted({r[field] for r in rows})]


def validate(rows, strategy, protocol):
    predictions = []
    for train, test in folds(rows, strategy):
        commander = fit(train, tau=protocol['fit_tau'])
        force = fit(train, tau=protocol['fit_tau'], commanders=False)
        prior = (sum(r['y'] for r in train) + 1.0) / (len(train) + 2.0)
        for r in test:
            p = predict(commander, r)
            predictions.append({'campaign': r['campaign'],
                                'force': loss(p, r['y']) - loss(predict(force, r, commanders=False), r['y']),
                                'prior': loss(p, r['y']) - loss(prior, r['y'])})
    groups = sorted({r['campaign'] for r in predictions})
    result = {'rows': len(predictions), 'groups': len(groups)}
    for comparator in ('force', 'prior'):
        result[comparator + '_battle'] = mean(r[comparator] for r in predictions)
        result[comparator + '_group'] = mean(mean(r[comparator] for r in predictions if r['campaign'] == g)
                                             for g in groups)
    return result


def experiment(schedule, protocol, progress=None):
    outputs = {}
    for scenario in protocol['scenarios']:
        recoveries, army_recoveries, validation = [], [], defaultdict(list)
        for rep in range(protocol['repetitions']):
            rows, truth = generate(schedule, scenario, rep, protocol)
            recoveries.append(recovery(fit(rows, tau=protocol['fit_tau']), truth))
            if scenario in ('stable_army_alias', 'switching_armies'):
                army_recoveries.append(recovery(fit(rows, tau=protocol['fit_tau'],
                                                   army_sd=protocol['army_sd'], armies=True), truth))
            if rep < protocol['validation_repetitions']:
                for strategy in protocol['validation_strategies']:
                    validation[strategy].append(validate(rows, strategy, protocol))
        item = {'repetitions': len(recoveries),
                'recovery': {k: summarize(r[k] for r in recoveries) for k in recoveries[0]},
                'validation': {s: {'repetitions': len(v), 'rows': v[0]['rows'], 'groups': v[0]['groups'],
                                   **{k: summarize(r[k] for r in v) for k in v[0] if k not in ('rows', 'groups')}}
                               for s, v in validation.items()}}
        if army_recoveries:
            item['with_observed_synthetic_armies'] = {k: summarize(r[k] for r in army_recoveries)
                                                     for k in army_recoveries[0]}
        outputs[scenario] = item
        if progress:
            progress(scenario)
    return outputs
