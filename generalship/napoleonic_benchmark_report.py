"""Verify and report the authorized saved run. Never fit or select a model."""

import argparse
from collections import Counter, defaultdict
import json
import math
from pathlib import Path
import random
from statistics import fmean

from .sources import digest, read_json, write_json

BASE = 'data/napoleonic/benchmark-v1/'
RESULT = 'artifacts/napoleonic-benchmark-run-v1.json'
RESULT_SHA = '35ed5cc7066cf40287e26afc03b16409a9012e81157b472abf212727faa5d505'
REPORT = 'docs/research/napoleonic-benchmark-run-v1.md'
VERIFICATION = 'artifacts/napoleonic-benchmark-run-v1-verification.json'
CODE = 'generalship/napoleonic_benchmark_report.py'
MODELS = ('force', 'equal_odds', 'training_prior')
EVALUATIONS = ('leave_campaign_out', 'leave_war_out', 'forward_1813')
POPULATIONS = ('primary', 'exclude_indecisive', 'exclude_no_combat', 'unqualified_totals')


def require(condition, message):
    if not condition:
        raise ValueError('Napoleonic saved-run verification: ' + message)


def near(actual, expected):
    require(math.isclose(actual, expected, rel_tol=0, abs_tol=2e-12), f'{actual} != {expected}')


def loss(p, y, metric):
    if metric == 'brier':
        return (p - y) ** 2
    p = min(1 - 1e-15, max(1e-15, p))
    return -math.log(p if y else 1 - p)


def score(predictions, model, metric, weighting):
    values = defaultdict(list)
    for p in predictions:
        values[p['held_out_group']].append(loss(p[model], p['y'], metric))
    if weighting == 'battle':
        return fmean(v for group in values.values() for v in group)
    return fmean(fmean(group) for group in values.values())


def bootstrap_bounds(predictions, comparator, protocol):
    """Resample actual row-loss lists, separately from the runner's sufficient statistics."""
    by_group = defaultdict(list)
    for p in predictions:
        by_group[p['held_out_group']].append(loss(p['force'], p['y'], 'log_loss')
                                            - loss(p[comparator], p['y'], 'log_loss'))
    blocks = [by_group[g] for g in sorted(by_group)]
    rng = random.Random(protocol['seed'])
    samples = {'battle': [], 'equal_group': []}
    for _ in range(protocol['draws']):
        draw = [blocks[rng.randrange(len(blocks))] for _ in blocks]
        samples['battle'].append(fmean(value for block in draw for value in block))
        samples['equal_group'].append(fmean(fmean(block) for block in draw))
    bounds = {}
    for weighting, values in samples.items():
        ordered = sorted(values)
        bounds[weighting] = []
        for q in protocol['interval']:
            i = q * (len(ordered) - 1)
            low = int(i)
            bounds[weighting].append(ordered[low] * (1 - (i - low)) + ordered[math.ceil(i)] * (i - low))
    return bounds


def verify(root):
    require(digest(root / RESULT) == RESULT_SHA, 'the immutable executed result changed')
    run = read_json(root / RESULT)
    proposal = read_json(root / (BASE + 'run-proposal.json'))
    auth = read_json(root / (BASE + 'owner-run-authorization.json'))
    require(run['proposal_sha256'] == digest(root / (BASE + 'run-proposal.json')), 'proposal binding')
    require(run['authorization_sha256'] == digest(root / (BASE + 'owner-run-authorization.json')), 'authorization binding')
    require(auth['approved'] is True and auth['proposal_sha256'] == run['proposal_sha256']
            and auth['command'] == proposal['command'] and auth['scope'] == proposal['scope']
            and auth['owner_request'] == run['owner_request'], 'owner authorization')
    require(run['executed_bindings'] == proposal['bindings'], 'executed input/code bindings')
    for path, sha in run['executed_bindings'].items():
        require(digest(root / path) == sha, 'changed executing input/code: ' + path)
    scope, protocol = (read_json(root / (BASE + p + '.json')) for p in ('scope', 'protocol'))
    for path, sha in scope['bindings'].items():
        require(digest(root / path) == sha, 'changed frozen frame input: ' + path)
    data = read_json(root / 'artifacts/napoleonic-benchmark-v1.json')
    rows = data['entries']
    require([r['battle_id'] for r in rows] == scope['development_ids'] and len(rows) == 273, 'development membership')
    reserved = set(scope['reserved_final_ids'])
    require(len(reserved) == 52 and not reserved & set(scope['development_ids'])
            and run['reserved_final_used'] is False, 'reserved-final separation')
    frame = {r['id']: r for r in read_json(root / 'data/napoleonic/frame-v1.json')['entries']}
    labels = {b: frame[b]['outcome_side_a'] for b in scope['development_ids']}
    require(all(y in (0, 1) for y in labels.values()), 'binary development labels')
    require(tuple(run['populations']) == POPULATIONS, 'all fixed populations')
    counts = Counter()
    for population, evaluations in run['populations'].items():
        selected = [r for r in rows if r['eligible']]
        if population == 'exclude_indecisive':
            selected = [r for r in selected if not r['indecisive_printed']]
        elif population == 'exclude_no_combat':
            selected = [r for r in selected if not r['no_combat_printed']]
        elif population == 'unqualified_totals':
            selected = [r for r in selected if not any(s['approximate'] or s['footnote_markers']
                                                       or s['context_footnote_markers'] for s in r['sides'].values())]
        indexed = {r['battle_id']: r for r in selected}
        require(tuple(evaluations) == EVALUATIONS, 'all fixed evaluations')
        for evaluation, result in evaluations.items():
            require(result['eligible_entries'] == len(selected), 'eligible denominator')
            predictions = result['predictions']
            require(len(predictions) == result['scored_entries']
                    and len({p['battle_id'] for p in predictions}) == len(predictions), 'prediction grain')
            require(result['unscored_ids'] == sorted(set(indexed) - {p['battle_id'] for p in predictions}), 'unscored IDs')
            groups = (['1813'] if evaluation == 'forward_1813' else sorted(scope['development_groups'])
                      if evaluation == 'leave_campaign_out' else sorted({r['war'] for r in rows}))
            require([f['held_out_group'] for f in result['folds']] == groups, 'complete fold design')
            require(result['groups_in_design'] == len(groups), 'group denominator')
            predicted_by_fold = defaultdict(list)
            for p in predictions:
                predicted_by_fold[p['held_out_group']].append(p)
            require(result['groups_scored'] == len(predicted_by_fold), 'scored group count')
            for fold in result['folds']:
                g = fold['held_out_group']
                field = 'campaign_group' if evaluation == 'leave_campaign_out' else 'war'
                train = [r for r in selected if r['start_year'] <= 1812] if evaluation == 'forward_1813' else [
                    r for r in selected if r[field] != g]
                test = [r for r in selected if r['start_year'] == 1813] if evaluation == 'forward_1813' else [
                    r for r in selected if r[field] == g]
                require(fold['train_ids'] == [r['battle_id'] for r in train]
                        and fold['test_ids'] == [r['battle_id'] for r in test], 'fold membership')
                require(not set(fold['train_ids']) & set(fold['test_ids'])
                        and not reserved & (set(fold['train_ids']) | set(fold['test_ids'])), 'fold leakage')
                expected_status = 'empty_test' if not test else 'insufficient_training' if len(train) < 2 else 'scored'
                require(fold['status'] == expected_status, 'fold estimability')
                counts['folds_checked'] += 1
                if expected_status != 'scored':
                    require(not predicted_by_fold[g], 'unestimable fold predictions')
                    continue
                prior = (sum(labels[r['battle_id']] for r in train) + 1) / (len(train) + 2)
                near(fold['training_prior'], prior)
                a, b = fold['intercept'], fold['slope']
                def feature(row):
                    x, y = (row['sides'][s]['primary_value'] for s in ('A', 'B'))
                    require(x > 0 and y > 0, 'positive personnel inputs')
                    return (x - y) / (x + y)
                def probability(row):
                    return 1 / (1 + math.exp(-(a + b * feature(row))))
                residuals = [probability(r) - labels[r['battle_id']] for r in train]
                require(abs(protocol['ridge'] * a + math.fsum(residuals)) < 1e-7
                        and abs(protocol['ridge'] * b + math.fsum(v * feature(r) for v, r in zip(residuals, train))) < 1e-7,
                        'penalized optimizer score equations')
                counts['optimizer_stationarity_checks'] += 1
                require({p['battle_id'] for p in predicted_by_fold[g]} == set(fold['test_ids']), 'complete test predictions')
                for p in predicted_by_fold[g]:
                    row = indexed[p['battle_id']]
                    require(p['y'] == labels[p['battle_id']] and p['campaign_group'] == row['campaign_group'], 'prediction source')
                    near(p['equal_odds'], 0.5); near(p['training_prior'], prior); near(p['force'], probability(row))
                    counts['predictions_checked'] += 1
            for weighting in ('battle', 'equal_group'):
                sizes = Counter(p['held_out_group'] for p in predictions)
                weights = [1 if weighting == 'battle' else 1 / sizes[p['held_out_group']] for p in predictions]
                for model in MODELS:
                    for metric in ('brier', 'log_loss'):
                        near(result['metrics'][weighting][model][metric], score(predictions, model, metric, weighting))
                        counts['summary_metric_values_checked'] += 1
                    for i, bin_record in enumerate(result['calibration'][weighting][model]):
                        low, high = protocol['calibration_edges'][i:i + 2]
                        bucket = [(p, w) for p, w in zip(predictions, weights)
                                  if low <= p[model] < high or (i == 4 and p[model] == high)]
                        require(bin_record['lower'] == low and bin_record['upper'] == high
                                and bin_record['n'] == len(bucket), 'calibration membership')
                        for key, field in (('mean_probability', model), ('recorded_a_win_share', 'y')):
                            if bucket:
                                near(bin_record[key], math.fsum(p[field] * w for p, w in bucket) / math.fsum(w for p, w in bucket))
                            else:
                                require(bin_record[key] is None, 'empty calibration bin is not zero')
                        counts['calibration_bins_checked'] += 1
            for group, models in result['per_group'].items():
                subset = predicted_by_fold[group]
                for model in MODELS:
                    for metric in ('brier', 'log_loss'):
                        near(models[model][metric], score(subset, model, metric, 'battle'))
                        counts['per_group_metric_values_checked'] += 1
            deltas = sorted([{'battle_id': p['battle_id'], 'held_out_group': p['held_out_group'],
                              'log_loss_difference': loss(p['force'], p['y'], 'log_loss') - loss(p['training_prior'], p['y'], 'log_loss')}
                             for p in predictions], key=lambda x: (-abs(x['log_loss_difference']), x['battle_id']))
            for actual, expected in zip(result['force_minus_prior_by_engagement'], deltas, strict=True):
                require(actual['battle_id'] == expected['battle_id'] and actual['held_out_group'] == expected['held_out_group'],
                        'loss concentration order')
                near(actual['log_loss_difference'], expected['log_loss_difference'])
            if evaluation == 'leave_campaign_out':
                for comparator in ('equal_odds', 'training_prior'):
                    expected = bootstrap_bounds(predictions, comparator, protocol['bootstrap'])
                    actual = result['bootstrap'][comparator]
                    require(actual['groups'] == len(groups) and actual['draws'] == 10000 and actual['seed'] == 20261020,
                            'bootstrap design')
                    for weighting, bounds in expected.items():
                        for x, y in zip(actual['force_minus_comparator_log_loss'][weighting], bounds, strict=True):
                            near(x, y); counts['bootstrap_interval_endpoints_checked'] += 1
            else:
                require('bootstrap' not in result, 'no confidence claim for coarse war/forward views')
    require(run['populations']['primary'] == run['populations']['exclude_indecisive'], 'indecisive exclusion is a no-op')
    verification = {'kind': 'napoleonic_benchmark_primary_arithmetic_verification', 'version': 1,
                    'status': 'share_with_caveats', 'separate_review': False, 'historical_refits_performed': 0,
                    'bindings': {p: digest(root / p) for p in (RESULT, BASE + 'owner-run-authorization.json',
                                 BASE + 'run-proposal.json', CODE)}, 'checks': dict(counts),
                    'absolute_score_equation_tolerance': 1e-7, 'absolute_arithmetic_tolerance': 2e-12,
                    'reserved_final_entries_used': 0}
    return run, data, labels, verification


def report(run, data, labels, verification):
    populations = run['populations']
    primary = populations['primary']['leave_campaign_out']
    names = {r['battle_id']: r['place'] for r in data['entries']}
    out = ['# Napoleonic compiler-strength benchmark run v1', '',
           'Primary-verified. Share with caveats. The owner authorized the exact frozen development-only proposal.', '',
           '**Force size improves campaign- and war-held-out prediction of Bodart’s recorded winners. '
           'Transfer to 1813 is weak and sensitivity-dependent.** These are compiler-record predictions; '
           'no commander, tactical or campaign-contribution effect is estimated.', '',
           '## Scope and fixed method', '',
           '- 273 development engagements / 546 sides / 13 complete campaign groups. '
           '194 paired compiler totals are eligible (71.1%); 79 engagements remain excluded. '
           '82 side extracts are missing, 32 ambiguous and 44 otherwise eligible sides lack an eligible opponent.',
           '- All 52 final-evaluation entries remain reserved. The 273-entry denominator and every exclusion '
           'remain in the [prepared dataset](../../artifacts/napoleonic-benchmark-v1.md).',
           '- One ridge-1 logistic model uses `(A-B)/(A+B)` from the two printed personnel totals. '
           'A is France and its allies. Both intercept and slope are penalized. Comparators are equal odds '
           'and the training-only Laplace-smoothed A-win share. No tuning, model selection or commander term.',
           '- Campaign holdouts retain 13 groups; war holdouts retain six. The forward view trains through '
           '1812 and scores the fixed 1813 development entries. Battle weighting gives each scored entry equal '
           'weight; equal-group weighting gives each held-out group equal weight. The forward view has one '
           'held-out year, so its two weightings coincide.', '',
           '## Scores in every fixed population', '',
           'Lower scores are better. Log loss uses natural logarithms. Every model uses the same rows within '
           'each population/evaluation. Populations change coverage; their score differences are not paired '
           'estimates of an annotation effect. `Scored / eligible` separates the forward test rows from its '
           'training rows; training-only rows listed as unscored in the raw result are expected.', '']
    for metric, title in (('log_loss', 'Log loss'), ('brier', 'Brier score')):
        out += [f'### {title}', '',
                '| Population | Evaluation | Scored / eligible | Groups | Force, battle | Prior, battle | Equal odds, battle | Force, group | Prior, group | Equal odds, group |',
                '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
        for pop, evaluations in populations.items():
            for evaluation, result in evaluations.items():
                numbers = [result['metrics'][w][m][metric] for w in ('battle', 'equal_group')
                           for m in ('force', 'training_prior', 'equal_odds')]
                out.append(f'| {pop} | {evaluation} | {result["scored_entries"]} / {result["eligible_entries"]} | '
                           f'{result["groups_scored"]} | ' + ' | '.join(f'{v:.6f}' for v in numbers) + ' |')
        out.append('')
    forward = populations['primary']['forward_1813']
    fold = forward['folds'][0]
    out += ['The primary forward check trains on 157 entries and scores 37. The recorded A-win share changes '
            f'from {sum(labels[b] for b in fold["train_ids"])}/157 in training to '
            f'{sum(p["y"] for p in forward["predictions"])}/37 in testing; its fixed training prior is '
            f'{fold["training_prior"]:.6f}. Force log loss is 0.691122 versus equal odds 0.693147, '
            'while force Brier is 0.251057 versus 0.250000. The unqualified-total forward view has '
            '133 training and 30 test entries; both force scores are worse than equal odds.', '',
            'The indecisive exclusion removes zero eligible rows and duplicates the primary result. '
            'The non-combat exclusion retains 193 pairs. Screening approximate totals or numeric notes '
            'anywhere in the cited strength passage retains 163. Notes can apply to entry context or the '
            'other side; the screen does not newly adjudicate their applicability.', '',
            '## Descriptive campaign bootstrap', '',
            'Force minus comparator log loss: negative favors force. These are paired held-out-campaign '
            'loss intervals (10,000 resamples, seed 20261020, percentile 95%), with weights recomputed '
            'in each draw. They condition on the saved predictions and selected source data; they do '
            'not refit training folds or propagate source/label uncertainty. Overlapping training sets '
            'and one compiler family remain dependencies. No interval is claimed for the six-war or '
            'one-year views. No pass/fail skill rule was specified.', '',
            '| Population | Comparator | Battle-weighted difference | 95% interval | Equal-group difference | 95% interval |',
            '| --- | --- | ---: | --- | ---: | --- |']
    for pop, evaluations in populations.items():
        result = evaluations['leave_campaign_out']
        for comparator in ('equal_odds', 'training_prior'):
            cells = []
            for w in ('battle', 'equal_group'):
                delta = result['metrics'][w]['force']['log_loss'] - result['metrics'][w][comparator]['log_loss']
                bounds = result['bootstrap'][comparator]['force_minus_comparator_log_loss'][w]
                cells += [f'{delta:+.6f}', f'[{bounds[0]:+.6f}, {bounds[1]:+.6f}]']
            out.append(f'| {pop} | {comparator} | ' + ' | '.join(cells) + ' |')
    out += ['', 'The unqualified-total equal-group interval against the training prior includes zero '
            '(-0.127856 to +0.013096). Its lower point score alone does not establish robust improvement.', '',
            '## Campaign variation and error concentration', '',
            '| Held-out campaign | Scored entries | Force log loss | Prior log loss | Difference |',
            '| --- | ---: | ---: | ---: | ---: |']
    for group, models in primary['per_group'].items():
        n = sum(p['held_out_group'] == group for p in primary['predictions'])
        force, prior = (models[m]['log_loss'] for m in ('force', 'training_prior'))
        out.append(f'| {group} | {n} | {force:.6f} | {prior:.6f} | {force-prior:+.6f} |')
    contributions = primary['force_minus_prior_by_engagement']
    total = sum(abs(c['log_loss_difference']) for c in contributions)
    shares = [sum(abs(c['log_loss_difference']) for c in contributions[:n]) / total for n in (1, 5, 10)]
    out += ['', 'Force has lower log loss than the prior in 10 of 13 campaigns and higher loss in three. '
            'The largest one, five and ten absolute entry contributions account for '
            f'{shares[0]:.2%}, {shares[1]:.2%} and {shares[2]:.2%} of the total absolute difference. '
            'This denominator includes gains and losses without cancelling them; it is not a share of net gain.', '',
            '| Entry | Printed place | Force-minus-prior log loss |', '| --- | --- | ---: |']
    for c in contributions[:10]:
        out.append(f'| {c["battle_id"]} | {names[c["battle_id"]]} | {c["log_loss_difference"]:+.6f} |')
    out += ['', 'All signed entry contributions and every group result for all populations/evaluations '
            'remain in the raw result. These prediction errors assign no command credit.', '',
            '## Force-model calibration', '',
            'Primary population; bins are left-closed/right-open, with 1 included in the last bin. '
            'Counts are unweighted; probability and recorded A-win means use the stated weights. '
            'Empty bins remain unknown. All three models’ calibration bins for every population are '
            'published in the raw result.', '',
            '| Evaluation | Bin | Entries | Mean probability, battle | Recorded A-win share, battle | Mean probability, group | Recorded A-win share, group |',
            '| --- | --- | ---: | ---: | ---: | ---: | ---: |']
    for evaluation, result in populations['primary'].items():
        for a, b in zip(result['calibration']['battle']['force'], result['calibration']['equal_group']['force'], strict=True):
            values = [a['mean_probability'], a['recorded_a_win_share'], b['mean_probability'], b['recorded_a_win_share']]
            cells = ' | '.join('unknown' if v is None else f'{v:.6f}' for v in values)
            out.append(f'| {evaluation} | {a["lower"]:.1f}–{a["upper"]:.1f} | {a["n"]} | {cells} |')
    out += ['', 'The smallest primary campaign calibration bin has only two entries. These are descriptive '
            'checks of recorded labels, not calibrated historical command probabilities.', '',
            '## Source limits and interpretation', '',
            'Bodart selects entries by consequence, assembled forces or losses; his so-called indecisive '
            'winner rule can use relative strength. His strength convention includes available nearby troops '
            'that did not fight, and figures are rounded. These conventions are inspected in the prepared '
            'source context: `bodart-1908-transcription-v1`, pp. 45–47, raw SHA-256 '
            '`bf12437b6d19226ce127ce5d81e59d20358a5b1999ffe00f5ac6a8f8c20ef986`.', '',
            'The [six exact passages, English renderings and three page-image hashes](../../data/napoleonic/benchmark-v1/context.json) '
            'remain inspectable. They also appear in the [prepared report](../../artifacts/napoleonic-benchmark-v1.md#inspected-source-conventions). '
            'The indecisive no-op does not remove strength-dependent coding, shared-source error or selection. '
            'The dataset is outcome-unused preparation, not historical blinding.', '',
            'The grouped scores support a descriptive force-size baseline for these compiler records. '
            'The forward result and unqualified-total interval limit claims of generalization. '
            'No feature is admitted to the frozen baseline, no commander ranking is produced, and no '
            'causal or campaign-contribution conclusion follows. Wider strict-opening extraction stays '
            'paused; the stopped appointment pilots and unscored extraction calibration are unchanged.', '',
            '## Reproduction and primary verification', '',
            f'- Immutable [raw result](../../{RESULT}), SHA-256 `{RESULT_SHA}`. It retains every fold, '
            'coefficient, prediction, score, calibration bin, group result, contribution and planned bootstrap.',
            '- [Owner run authorization](../../data/napoleonic/benchmark-v1/owner-run-authorization.json) '
            f'has SHA-256 `{run["authorization_sha256"]}` and records the actual owner reply. '
            f'[Frozen proposal](../../data/napoleonic/benchmark-v1/run-proposal.json) SHA-256 `{run["proposal_sha256"]}`.',
            '- The executed command was `python3 -m generalship.napoleonic_benchmark_run '
            '--authorization data/napoleonic/benchmark-v1/owner-run-authorization.json '
            '--out artifacts/napoleonic-benchmark-run-v1.json`. The runner refuses to overwrite the result. '
            'The recorded environment is CPython ' + run['environment']['python'] + '.',
            f'- [Arithmetic verification](../../{VERIFICATION}) checks '
            f'{verification["checks"]["folds_checked"]} folds and '
            f'{verification["checks"]["predictions_checked"]} saved predictions, score equations, '
            'training-only priors, all summary/group scores, calibration bins, signed contributions '
            'and all bootstrap bounds. It uses a second arithmetic implementation and performs no fitting. '
            'This is primary verification, with no separate review.',
            '- `python3 -m generalship.napoleonic_benchmark_report` verifies the saved run and report. '
            '`--write` regenerates only this report and its verification record. '
            '`make check` and `make reproduce` use this saved-result path; they do not invoke the historical runner.', '']
    return '\n'.join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    run, data, labels, verification = verify(args.root)
    text = report(run, data, labels, verification)
    if args.write:
        (args.root / REPORT).write_text(text, encoding='utf-8')
        write_json(args.root / VERIFICATION, verification)
    require((args.root / REPORT).read_text(encoding='utf-8') == text, 'stale report')
    require(read_json(args.root / VERIFICATION) == verification, 'stale verification record')
    print(json.dumps(verification, indent=2))


if __name__ == '__main__':
    main()
