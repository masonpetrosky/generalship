"""Future development-only diagnostic. Exact owner authorization is mandatory."""

import argparse
from collections import defaultdict
import math
from pathlib import Path
import platform
import random

from .baseline import advantage, fit_logistic
from . import napoleonic_benchmark as prep
from .sources import digest, read_json, write_json

OUTPUT = 'artifacts/napoleonic-benchmark-run-v1.json'
MODELS = ('force', 'equal_odds', 'training_prior')


def authorize(root, authorization):
    prep.require(authorization is not None and Path(authorization).is_file(), 'exact owner run authorization required')
    proposal = prep.validate_proposal(root)
    auth = read_json(Path(authorization))
    prep.require(auth.get('kind') == 'napoleonic_benchmark_owner_run_authorization' and auth.get('approved') is True
                 and auth.get('proposal_sha256') == digest(root / prep.PROPOSAL)
                 and auth.get('command') == proposal['command'] and auth.get('scope') == proposal['scope']
                 and isinstance(auth.get('owner_request'), str) and bool(auth['owner_request'].strip()),
                 'missing, false or mismatched exact owner run authorization')
    return auth


def load_outcomes(root, ids):
    frame = {r['id']: r for r in read_json(root / 'data/napoleonic/frame-v1.json')['entries']}
    return {b: frame[b]['outcome_side_a'] for b in ids}


def folds(rows, scope, evaluation):
    if evaluation == 'forward_1813':
        return [('1813', [r for r in rows if r['start_year'] <= 1812], [r for r in rows if r['start_year'] == 1813])]
    field = 'campaign_group' if evaluation == 'leave_campaign_out' else 'war'
    groups = sorted(scope['development_groups']) if field == 'campaign_group' else sorted(
        {g.rsplit(' ', 1)[0] for g in scope['development_groups']})
    return [(g, [r for r in rows if r[field] != g], [r for r in rows if r[field] == g]) for g in groups]


def losses(p, y):
    clipped = min(1 - 1e-15, max(1e-15, p))
    return (p - y) ** 2, -y * math.log(clipped) - (1 - y) * math.log1p(-clipped)


def weights(predictions, grouping):
    if not predictions:
        return []
    if grouping == 'battle':
        return [1 / len(predictions)] * len(predictions)
    sizes = defaultdict(int)
    for p in predictions:
        sizes[p['held_out_group']] += 1
    return [1 / (len(sizes) * sizes[p['held_out_group']]) for p in predictions]


def metrics(predictions, key, grouping):
    if not predictions:
        return None
    ws = weights(predictions, grouping)
    ls = [losses(p[key], p['y']) for p in predictions]
    return {'brier': sum(w * l[0] for w, l in zip(ws, ls)),
            'log_loss': sum(w * l[1] for w, l in zip(ws, ls))}


def calibration(predictions, key, grouping, edges):
    ws, result = weights(predictions, grouping), []
    for i, (low, high) in enumerate(zip(edges, edges[1:])):
        selected = [(p, w) for p, w in zip(predictions, ws) if low <= p[key]
                    and (p[key] < high or (i == len(edges) - 2 and p[key] == high))]
        total = sum(w for p, w in selected)
        result.append({'lower': low, 'upper': high, 'n': len(selected),
                       'mean_probability': sum(w * p[key] for p, w in selected) / total if total else None,
                       'recorded_a_win_share': sum(w * p['y'] for p, w in selected) / total if total else None})
    return result


def percentile(xs, p):
    ordered = sorted(xs); pos = (len(ordered) - 1) * p
    low, high = math.floor(pos), math.ceil(pos)
    return ordered[low] + (ordered[high] - ordered[low]) * (pos - low)


def bootstrap(predictions, comparator, design):
    groups = defaultdict(list)
    for p in predictions:
        groups[p['held_out_group']].append(losses(p['force'], p['y'])[1] - losses(p[comparator], p['y'])[1])
    if len(groups) < 2:
        return {'status': 'not_estimable', 'groups': len(groups)}
    stats = [(len(v), sum(v)) for g, v in sorted(groups.items())]
    rng = random.Random(design['seed']); samples = {'battle': [], 'equal_group': []}
    for _ in range(design['draws']):
        draw = [stats[rng.randrange(len(stats))] for i in stats]
        samples['battle'].append(sum(v for n, v in draw) / sum(n for n, v in draw))
        samples['equal_group'].append(sum(v / n for n, v in draw) / len(draw))
    return {'status': 'descriptive_cluster_bootstrap', 'groups': len(groups), 'draws': design['draws'],
            'seed': design['seed'], 'force_minus_comparator_log_loss': {
                weighting: [percentile(values, p) for p in design['interval']] for weighting, values in samples.items()}}


def evaluate(rows, labels, scope, protocol, evaluation):
    """Pure evaluation; tests supply only small constructed records and labels."""
    predictions, fold_records = [], []
    for group, train, test in folds(rows, scope, evaluation):
        record = {'held_out_group': group, 'train_ids': [r['battle_id'] for r in train],
                  'test_ids': [r['battle_id'] for r in test]}
        prep.require(not set(record['train_ids']) & set(record['test_ids']), 'train/test overlap')
        if not test or len(train) < protocol['minimum_training_rows']:
            record['status'] = 'empty_test' if not test else 'insufficient_training'
            fold_records.append(record)
            continue
        feature = lambda r: advantage(r['sides']['A']['primary_value'], r['sides']['B']['primary_value'])
        ys = [labels[r['battle_id']] for r in train]
        model = fit_logistic([feature(r) for r in train], ys, protocol['ridge'])
        prior = (sum(ys) + 1) / (len(ys) + 2)
        record.update(status='scored', intercept=model.intercept, slope=model.slope, training_prior=prior)
        fold_records.append(record)
        for r in test:
            predictions.append({'battle_id': r['battle_id'], 'campaign_group': r['campaign_group'],
                                'held_out_group': group, 'y': labels[r['battle_id']],
                                'force': model.predict(feature(r)), 'equal_odds': 0.5, 'training_prior': prior})
    predictions.sort(key=lambda p: p['battle_id'])
    result = {'evaluation': evaluation, 'eligible_entries': len(rows), 'scored_entries': len(predictions),
              'unscored_ids': sorted({r['battle_id'] for r in rows} - {p['battle_id'] for p in predictions}),
              'groups_in_design': len(fold_records), 'groups_scored': len({p['held_out_group'] for p in predictions}),
              'folds': fold_records, 'predictions': predictions,
              'metrics': {weighting: {key: metrics(predictions, key, weighting) for key in MODELS}
                          for weighting in ('battle', 'equal_group')},
              'calibration': {weighting: {key: calibration(predictions, key, weighting, protocol['calibration_edges'])
                                         for key in MODELS} for weighting in ('battle', 'equal_group')},
              'per_group': {group: {key: metrics([p for p in predictions if p['held_out_group'] == group], key, 'battle')
                                    for key in MODELS} for group, _, _ in folds(rows, scope, evaluation)},
              'force_minus_prior_by_engagement': sorted([
                  {'battle_id': p['battle_id'], 'held_out_group': p['held_out_group'],
                   'log_loss_difference': losses(p['force'], p['y'])[1] - losses(p['training_prior'], p['y'])[1]}
                  for p in predictions], key=lambda r: (-abs(r['log_loss_difference']), r['battle_id']))}
    if evaluation == 'leave_campaign_out':
        result['bootstrap'] = {c: bootstrap(predictions, c, protocol['bootstrap']) for c in MODELS if c != 'force'}
    return result


def run(root, authorization, output):
    auth = authorize(root, authorization)  # Before outcome access and every fit.
    prep.require(output == OUTPUT and not (root / output).exists(), 'output must be the proposed new result path')
    prep.check(root)
    data, scope, protocol = (read_json(root / p) for p in (prep.ARTIFACT + '.json', prep.SCOPE, prep.PROTOCOL))
    labels = load_outcomes(root, scope['development_ids'])
    result = {'kind': 'napoleonic_compiler_benchmark_run', 'version': 1, 'status': 'descriptive_not_command_effect',
              'proposal_sha256': digest(root / prep.PROPOSAL), 'authorization_sha256': digest(Path(authorization)),
              'environment': {'python': platform.python_version(), 'implementation': platform.python_implementation()},
              'executed_bindings': prep.proposal(root)['bindings'],
              'owner_request': auth['owner_request'], 'reserved_final_used': False,
              'populations': {population: {evaluation: evaluate(prep.population_rows(data, population), labels, scope,
                                                               protocol, evaluation) for evaluation in protocol['evaluations']}
                              for population in protocol['populations']}}
    write_json(root / output, result)
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--authorization', type=Path, required=True)
    p.add_argument('--out', required=True)
    args = p.parse_args()
    run(args.root, args.authorization, args.out)


if __name__ == '__main__':
    main()
