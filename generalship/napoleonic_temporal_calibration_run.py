"""Explicit future temporal calibration job. Never invoked by checks or reproduction."""

import argparse
import math
from pathlib import Path
import platform

from .baseline import advantage, fit_logistic, sigmoid
from . import napoleonic_benchmark_run as scoring
from . import napoleonic_temporal_calibration as prep
from .sources import digest, read_json, write_json


def fit_offset(logits, labels, ridge=1.0):
    """Unique minimizer of sum(log loss(sigmoid(z+delta), y)) + ridge*delta²/2."""
    prep.require(logits and len(logits) == len(labels) and math.isfinite(ridge) and ridge > 0
                 and all(math.isfinite(z) for z in logits) and all(y in (0, 1) for y in labels), 'offset inputs')
    # The derivative is strictly increasing, with Hessian at least ridge.
    # [-n/ridge, n/ridge] brackets its unique zero for binary labels.
    low, high = -len(labels) / ridge, len(labels) / ridge
    for iteration in range(1, 201):
        delta = (low + high) / 2
        gradient = ridge * delta + math.fsum(sigmoid(z + delta) - y for z, y in zip(logits, labels))
        if abs(gradient) <= 1e-9:
            return {'offset': delta, 'score_equation': gradient, 'iterations': iteration}
        if gradient > 0:
            high = delta
        else:
            low = delta
    raise ValueError('Offset score equation did not converge')


def authorize(root, authorization):
    prep.require(authorization is not None and Path(authorization).is_file(), 'exact owner run authorization required')
    proposal = prep.validate_proposal(root)
    auth = read_json(Path(authorization))
    prep.require(auth.get('kind') == 'napoleonic_temporal_calibration_owner_run_authorization'
                 and auth.get('approved') is True and auth.get('proposal_sha256') == digest(root / prep.PROPOSAL)
                 and auth.get('command') == proposal['command'] and auth.get('scope') == proposal['scope']
                 and isinstance(auth.get('owner_request'), str) and bool(auth['owner_request'].strip()),
                 'missing, false or mismatched exact owner run authorization')
    return auth


def summarize(predictions, protocol):
    return {'entries': len(predictions), 'campaign_groups': len({p['campaign_group'] for p in predictions}),
            'metrics': {w: {model: scoring.metrics(predictions, model, 'battle' if w == 'battle' else 'equal_group')
                            for model in prep.MODELS} for w in protocol['weightings']},
            'calibration': {w: {model: scoring.calibration(predictions, model, 'battle' if w == 'battle' else 'equal_group',
                                                          protocol['calibration_edges']) for model in prep.MODELS}
                            for w in protocol['weightings']}}


def evaluate(rows, labels, population_plan, protocol):
    """Pure evaluator. Unit tests provide constructed rows and labels only."""
    indexed = {r['battle_id']: r for r in rows}
    prep.require(set(indexed) == set(labels) and len(indexed) == len(rows)
                 and all(y in (0, 1) for y in labels.values()), 'evaluation grain/labels')
    feature = lambda b: advantage(indexed[b]['sides']['A']['primary_value'], indexed[b]['sides']['B']['primary_value'])
    predictions, parameters = [], []
    for fold in population_plan['folds']:
        record = {key: fold[key] for key in ('target_year', 'cutoff', 'calibration_start', 'region', 'status', 'reasons',
                                            'base_ids', 'calibration_ids', 'expanding_ids', 'test_ids')}
        if fold['status'] != 'planned':
            parameters.append(record)
            continue
        base, calibration, test = (fold[k] for k in ('base_ids', 'calibration_ids', 'test_ids'))
        expanding = fold['expanding_ids']
        prep.require(not set(base) & set(calibration) and not (set(base) | set(calibration)) & set(test)
                     and set(expanding) == set(base) | set(calibration)
                     and len(base) >= protocol['minimum_base_rows']
                     and len(calibration) >= protocol['minimum_calibration_rows'], 'fit membership/support')
        prep.require(fold['calibration_start'] is not None
                     and all(indexed[b]['end_date'] and indexed[b]['end_date'] < fold['calibration_start'] for b in base)
                     and all(indexed[b]['end_date'] and indexed[b]['end_date'] < fold['cutoff'] for b in expanding),
                     'base/calibration/test temporal separation')
        base_model = fit_logistic([feature(b) for b in base], [labels[b] for b in base], protocol['force_ridge'])
        offset = fit_offset([base_model.intercept + base_model.slope * feature(b) for b in calibration],
                            [labels[b] for b in calibration], protocol['offset_ridge'])
        expanding_model = fit_logistic([feature(b) for b in expanding], [labels[b] for b in expanding], protocol['force_ridge'])
        prior = (sum(labels[b] for b in expanding) + 1) / (len(expanding) + 2)
        recent = (sum(labels[b] for b in calibration) + 1) / (len(calibration) + 2)
        record.update(status='scored', base_intercept=base_model.intercept, base_slope=base_model.slope, **offset,
                      expanding_intercept=expanding_model.intercept, expanding_slope=expanding_model.slope,
                      expanding_prior=prior, recent_prior=recent)
        parameters.append(record)
        for b in test:
            row = indexed[b]; x = feature(b)
            forecasts = {'offset_force': sigmoid(base_model.intercept + base_model.slope * x + offset['offset']),
                         'same_base_force': base_model.predict(x), 'expanding_force': expanding_model.predict(x),
                         'expanding_prior': prior, 'recent_prior': recent, 'equal_odds': .5}
            prep.require(all(math.isfinite(p) and 0 <= p <= 1 for p in forecasts.values()), 'finite forecast')
            predictions.append({'battle_id': b, 'target_year': fold['target_year'], 'region': fold['region'],
                                'campaign_group': row['campaign_group'], 'held_out_group': row['campaign_group'],
                                'force_balance': x, 'y': labels[b], **forecasts})
    predictions.sort(key=lambda p: p['battle_id'])
    regions = {region: summarize([p for p in predictions if p['region'] == region], protocol)
               for region in ('decision', 'reused_1813_secondary')}
    per_year = {str(y): summarize([p for p in predictions if p['target_year'] == y], protocol)
                for y in protocol['target_years']}
    per_group = {g: summarize([p for p in predictions if p['campaign_group'] == g], protocol)
                 for g in sorted({p['campaign_group'] for p in predictions})}
    contributions = {comparator: sorted([
        {'battle_id': p['battle_id'], 'target_year': p['target_year'], 'region': p['region'],
         'log_loss_difference': scoring.losses(p['offset_force'], p['y'])[1] - scoring.losses(p[comparator], p['y'])[1],
         'brier_difference': scoring.losses(p['offset_force'], p['y'])[0] - scoring.losses(p[comparator], p['y'])[0]}
        for p in predictions], key=lambda p: (-abs(p['log_loss_difference']), p['battle_id']))
        for comparator in prep.MODELS[1:]}
    concentration = {}
    for comparator, values in contributions.items():
        concentration[comparator] = {}
        for region in regions:
            losses = [abs(v['log_loss_difference']) for v in values if v['region'] == region]
            total = math.fsum(losses)
            concentration[comparator][region] = {'sum_absolute_log_loss_differences': total,
                                                'top_shares': {str(n): math.fsum(losses[:n]) / total if total else None
                                                               for n in (1, 5, 10)}}
    return {'eligible_entries': len(rows), 'parameters': parameters, 'predictions': predictions,
            'unscored_ids': sorted(set(indexed) - {p['battle_id'] for p in predictions}),
            'regions': regions, 'per_year': per_year, 'per_group': per_group,
            'paired_loss_contributions': contributions, 'absolute_loss_concentration': concentration}


def continuation(results, protocol):
    """Fixed exploratory decision; 1813 scores are never read here."""
    prep.require(protocol['decision_years'] == list(range(1808, 1813)) and protocol['secondary_years'] == [1813],
                 '1813 cannot enter the continuation years')
    primary = results['primary']; sensitivity = results['unqualified_totals']
    comparisons = []
    tolerance = protocol['decision_tolerance']
    years = [str(y) for y in protocol['decision_years']]
    def annual_available(result, year):
        row = result['per_year'].get(year)
        return row is not None and row['entries'] > 0 and all(
            row['metrics']['battle'].get(model) is not None for model in ('offset_force', 'expanding_force'))
    if len(years) != 5 or any(not annual_available(result, y) for result in (primary, sensitivity) for y in years):
        return {'status': 'not_assessable', 'reason': 'missing_required_decision_year', '1813_used': False}
    for weighting in protocol['weightings']:
        main = primary['regions']['decision']['metrics'][weighting]
        screen = sensitivity['regions']['decision']['metrics'][weighting]
        if any(main[m] is None for m in prep.MODELS) or any(screen[m] is None for m in ('offset_force', 'expanding_force')):
            return {'status': 'not_assessable', 'reason': 'missing_required_scores', '1813_used': False}
        for comparator in prep.MODELS[1:]:
            dll = main['offset_force']['log_loss'] - main[comparator]['log_loss']
            db = main['offset_force']['brier'] - main[comparator]['brier']
            comparisons.append({'population': 'primary', 'weighting': weighting, 'comparator': comparator,
                                'log_loss_difference': dll, 'brier_difference': db,
                                'satisfied': dll < -tolerance and db <= tolerance})
        dll = screen['offset_force']['log_loss'] - screen['expanding_force']['log_loss']
        db = screen['offset_force']['brier'] - screen['expanding_force']['brier']
        comparisons.append({'population': 'unqualified_totals', 'weighting': weighting, 'comparator': 'expanding_force',
                            'log_loss_difference': dll, 'brier_difference': db,
                            'satisfied': dll <= tolerance and db <= tolerance})
    improved_years = [int(y) for y in years if primary['per_year'][y]['metrics']['battle']['offset_force']['log_loss']
                      - primary['per_year'][y]['metrics']['battle']['expanding_force']['log_loss'] < -tolerance]
    passed = all(c['satisfied'] for c in comparisons) and len(improved_years) >= 3
    return {'status': 'passes_exploratory_continuation_rule' if passed else 'does_not_pass',
            'comparisons': comparisons, 'improved_years_against_expanding_force': improved_years,
            '1813_used': False, 'authorizes_final_use_or_feature_admission': False}


def load_outcomes(root, ids):
    return scoring.load_outcomes(root, ids)


def run(root, authorization, output):
    auth = authorize(root, authorization)  # Before outcome access and every fit.
    prep.require(output == prep.RESULT and not (root / output).exists(), 'proposed new result path must not exist')
    prep.check(root)
    scope, protocol = read_json(root / prep.SCOPE), read_json(root / prep.PROTOCOL)
    data, plan = read_json(root / prep.DATA), read_json(root / (prep.ARTIFACT + '.json'))
    labels = load_outcomes(root, scope['development_ids'])
    results = {}
    for population in prep.POPULATIONS:
        rows = prep.benchmark.population_rows(data, population)
        results[population] = evaluate(rows, {r['battle_id']: labels[r['battle_id']] for r in rows},
                                       plan['populations'][population], protocol)
    output_record = {'kind': 'napoleonic_temporal_calibration_run', 'version': 1,
                     'status': 'exploratory_compiler_record_prediction_not_command_effect',
                     'environment': {'python': platform.python_version(), 'implementation': platform.python_implementation()},
                     'proposal_sha256': digest(root / prep.PROPOSAL), 'authorization_sha256': digest(Path(authorization)),
                     'executed_bindings': prep.proposal(root)['bindings'], 'owner_request': auth['owner_request'],
                     'reserved_final_used': False, 'populations': results, 'continuation': continuation(results, protocol)}
    write_json(root / output, output_record)
    return output_record


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--authorization', type=Path, required=True)
    p.add_argument('--out', required=True)
    args = p.parse_args()
    run(args.root, args.authorization, args.out)


if __name__ == '__main__':
    main()
