"""An Arsht-style residual summary beside saved Civil War estimates; no fitting or fetching."""

import argparse
from collections import Counter, defaultdict
import math
from pathlib import Path

from .compare import differences
from .sources import digest, read_csv, read_json, write_json
from .uncertainty import log_loss

RUN = 'artifacts/commander-ratings-v4.json'
COMMAND = 'data/command/responsibility-v2.json'
COHORT = 'data/pilot/cohort-v2.json'
BATTLES = 'data/raw/cwsac_battles.csv'
OUTPUT = 'artifacts/commander-comparison-v1.json'
REPORT = 'artifacts/commander-comparison-v1.md'
SIDES = ('US', 'Confederate')
MODELS = ('strength_only', 'commander', 'commander_no_context')
REFERENCE = {
    'source_id': 'arsht-military-rankings-notebook-d2d77e8',
    'url': 'https://github.com/ethanarsht/military_rankings/blob/'
           'd2d77e89c054b2eae45320c0e5c69f0821f85ffa/battle_project.ipynb',
    'sha256': '85500155549b0aa432530a9eed9d086c3664ddf21a50ce76411a81710a02f5a3',
    'locators': {'fit': 'zero-based cells 159-167', 'score': 'zero-based cells 196-198'},
    'inspected_on': '2026-10-21',
    'use': 'computational reference only; not a historical input; notebook not redistributed',
}


def require(condition, message):
    if not condition:
        raise ValueError('Commander comparison: ' + message)


def ranks(rows, key):
    """Within-side competition ranks; exact ties share a rank."""
    return {r['id']: 1 + sum(o[key] > r[key] for o in rows if o['side'] == r['side']) for r in rows}


def score(preds):
    def metrics(rows, key):
        return {'brier': math.fsum((r[key] - r['outcome']) ** 2 for r in rows) / len(rows),
                'log_loss': math.fsum(log_loss(r['outcome'], r[key]) for r in rows) / len(rows)}
    campaigns = sorted({r['campaign'] for r in preds})
    grouped = [[r for r in preds if r['campaign'] == c] for c in campaigns]
    return {'battle_weighted': {k: metrics(preds, k) for k in MODELS},
            'campaign_weighted': {k: {m: math.fsum(metrics(g, k)[m] for g in grouped) / len(grouped)
                                      for m in ('brier', 'log_loss')} for k in MODELS}}


def summarize(run, command, battles, cohort):
    preds = run['heldout']['predictions']
    ledger = {e['battle_id']: e for e in command['engagements']}
    require(len(ledger) == len(command['engagements']), 'duplicate ledger engagement')
    nested = {n['contained'] for n in command['nesting'] if n['outcome'] == 'nested'}
    ids = [p['battle_id'] for p in preds]
    require(len(ids) == len(set(ids)), 'duplicate forecast')
    require(set(ids) == set(ledger) - nested, 'forecast population differs from the ledger minus nested records')
    require(set(ledger) <= set(cohort), 'ledger outside cohort')
    require(len(cohort) == len(set(cohort)), 'duplicate cohort engagement')
    credited = defaultdict(list)
    battle_rows = []
    for p in sorted(preds, key=lambda r: r['battle_id']):
        b = p['battle_id']
        require(p['outcome'] in (0, 1), 'nonbinary outcome')
        require(p['outcome'] == {'Union': 1, 'Confederate': 0}.get(battles[b]['result']), 'outcome orientation')
        require(p['campaign'] == battles[b]['campaign'], 'campaign mismatch')
        for k in MODELS:
            require(isinstance(p[k], (int, float)) and math.isfinite(p[k]) and 0 <= p[k] <= 1,
                    'invalid saved probability')
        residual = p['outcome'] - p['strength_only']
        sides = {}
        for s, sign in zip(SIDES, (1, -1)):
            entry = ledger[b]['sides'][s]
            c = entry['commander_id']
            joint = 'joint_command' in entry['labels']
            sides[s] = {'commander': c if not joint else None,
                        'uncredited_reason': 'joint_command' if joint else ('unresolved' if not c else None),
                        'residual': sign * residual}
            if c and not joint:
                require(c in run['commanders'], 'credited commander absent from saved run')
                require(run['commanders'][c]['side'] == s, 'commander on wrong side')
                credited[c].append({'battle_id': b, 'campaign': p['campaign'], 'residual': sign * residual,
                                    'win': p['outcome'] if s == 'US' else 1 - p['outcome']})
        battle_rows.append({'battle_id': b, 'campaign': p['campaign'], 'outcome_us': p['outcome'],
                            'p_us_strength_only': p['strength_only'], 'sides': sides})
    metrics = score(preds)
    for weighting in ('battle_weighted', 'campaign_weighted'):
        require(not differences(metrics[weighting], {k: run['heldout'][weighting][k] for k in MODELS}),
                'saved metrics do not reproduce from forecasts')
    require(len(preds) == run['model']['rows'] == run['heldout']['n_rows'], 'saved row count mismatch')
    require(len({p['campaign'] for p in preds}) == run['model']['campaigns'], 'campaign count mismatch')
    rows = []
    for c, old in sorted(run['commanders'].items()):
        appearances = credited[c]
        require(len(appearances) == old['battles_modelled'], c + ': credited denominator mismatch')
        require(sum(a['win'] for a in appearances) == old.get('wins_in_model', 0), c + ': wins mismatch')
        require(len(appearances) - old.get('wins_in_model', 0) == old.get('losses_in_model', 0), c + ': losses mismatch')
        total = math.fsum(a['residual'] for a in appearances) if appearances else None
        require(old['ranked'] == (len(appearances) >= 2), c + ': saved ordering eligibility changed')
        rows.append({'id': c, 'name': old['name'], 'side': old['side'], 'ordered': old['ranked'],
                     'battles': len(appearances), 'campaigns': len({a['campaign'] for a in appearances}),
                     'wins': old.get('wins_in_model', 0), 'losses': old.get('losses_in_model', 0),
                     'modelled_strength_rows': old.get('modelled_strength_rows', 0),
                     'raw_total': total, 'raw_per_battle': total / len(appearances) if appearances else None,
                     'theta': old.get('theta'), 'theta_95': old.get('interval_95'),
                     'model_rank_80': old.get('rank_80'), 'model_rank_95': old.get('rank_95'),
                     'raw_order': None, 'per_battle_order': None, 'model_order': None, 'order_change': None,
                     'labels': old['labels'], 'battle_ids': sorted(a['battle_id'] for a in appearances)})
    ordered = [r for r in rows if r['ordered']]
    for field, out in (('raw_total', 'raw_order'), ('raw_per_battle', 'per_battle_order'), ('theta', 'model_order')):
        for c, rank in ranks(ordered, field).items():
            next(r for r in ordered if r['id'] == c)[out] = rank
    for r in ordered:
        r['order_change'] = r['raw_order'] - r['model_order']
    counts = Counter(r['battles'] for r in rows if not r['ordered'])
    comparisons = {k: run['heldout']['comparisons'][k] for k in
                   ('commander_minus_strength_only', 'commander_no_context_minus_strength_only')}
    for comparison in comparisons.values():
        for weighting in ('battle_weighted', 'campaign_weighted'):
            d = metrics[weighting][comparison['first']]['log_loss'] - metrics[weighting]['strength_only']['log_loss']
            require(math.isclose(d, comparison[weighting], abs_tol=1e-12), 'comparison mismatch')
    return {'kind': 'commander_score_comparison', 'version': 1,
            'status': 'primary_verified_exploratory_ordering_from_saved_results',
            'new_fit': False, 'exact_arsht_reproduction': False, 'reference': REFERENCE,
            'coverage': {'cohort': len(cohort), 'outside_ledger': sorted(set(cohort) - set(ledger)),
                         'ledger': len(ledger), 'nested_excluded': sorted(nested), 'scored_battles': len(preds),
                         'campaigns': run['model']['campaigns'],
                         'battles_with_modelled_strength': run['model']['rows_with_modelled_strength'],
                         'saved_commanders': len(rows), 'estimated_commanders': sum(r['theta'] is not None for r in rows),
                         'ordered_commanders': len(ordered),
                         'ordered_by_side': dict(Counter(r['side'] for r in ordered)),
                         'single_battle_commanders': counts[1], 'zero_battle_commanders': counts[0],
                         'uncredited_sides': sum(s['commander'] is None for b in battle_rows for s in b['sides'].values())},
            'metrics': metrics, 'comparisons': comparisons, 'original_verdict': run['verdict'],
            'commanders': rows, 'battles': battle_rows}


def build(root):
    root = Path(root)
    run = read_json(root / RUN)
    require(run.get('run_version') == 4, 'expected saved rating run 4')
    bindings = {RUN: digest(root / RUN), COHORT: digest(root / COHORT)}
    for record in run['bindings']['files'].values():
        require(digest(root / record['path']) == record['sha256'], 'changed bound input: ' + record['path'])
        bindings[record['path']] = record['sha256']
    result = summarize(run, read_json(root / COMMAND),
                       {r['battle']: r for r in read_csv(root / BATTLES)}, read_json(root / COHORT)['battle_ids'])
    result['input_sha256'] = bindings
    return result


def report(d):
    c = d['coverage']
    lines = ['# Civil War: Arsht-style scores versus commander estimates', '',
             '**Result: a better ranking is not demonstrated.** The full commander model has slightly lower '
             'held-out log loss per battle, but slightly higher loss when campaigns count equally. '
             'The saved simpler commander variant has lower point losses under both weightings, '
             'with campaign uncertainty spanning no improvement.', '',
             f'**{c["scored_battles"]} battles · {c["campaigns"]} campaign groups · '
             f'{c["ordered_commanders"]} provisional commander orders.** '
             'Primary-verified, using saved results; no new fit. These are within-side descriptions, '
             'not verified skill ranks or causal wins above replacement.', '',
             '[Union orders](#union) · [Confederate orders](#confederate) · '
             '[Methods](#what-is-compared) · [Coverage](#coverage)', '']
    methods = ['## What is compared', '',
             'The [Arsht notebook](' + REFERENCE['url'] + ') adds each commander’s outcome-minus-model-expectation '
             'residuals. Here the same scoring idea uses total personnel and the saved strength-only '
             'forecasts for campaigns excluded from training. For a Union side: residual = recorded Union '
             'outcome − predicted Union outcome; the Confederate residual is its negative. '
             'We show both the cumulative total and the mean per battle.', '',
             'The shrunk estimate θ comes from the existing force + context + commander model: '
             'it adjusts for opponent commander and theater/period and pulls sparse estimates toward zero. '
             'θ is in log-odds units; raw residual totals are in residual-outcome units. Their numerical '
             'sizes cannot be subtracted or interpreted as the same quantity. Order changes also reflect '
             'exposure, opponent/context adjustments and different units, not shrinkage alone.', '',
             '**This is an Arsht-style adaptation on our Civil War data, not a reproduction of his published '
             'rankings.** His notebook uses multiple force categories, in-sample fitting, different missing-data '
             'rules and attribution. Our comparison uses the same saved battles and attribution for both '
             'columns. Its strength-only baseline already includes AI-researched ledger inputs; this does '
             'not isolate the benefit of AI versus his source data. Rating run 4 and its unsuccessful '
             'pre-registered verdict remain unchanged.', '',
             '## Coverage', '',
             f'- {c["cohort"]} engagements in the frozen cohort; {len(c["outside_ledger"])} outside the two-sided decisive ledger.',
             f'- {c["ledger"]} ledger engagements minus {len(c["nested_excluded"])} nested records = '
             f'{c["scored_battles"]} scored battles across {c["campaigns"]} source campaign groups.',
             f'- {c["battles_with_modelled_strength"]}/{c["scored_battles"]} battles use at least one modelled strength, '
             'rather than two usable ledger estimates.',
             f'- {c["ordered_commanders"]}/{c["saved_commanders"]} saved commanders have at least two credited battles: '
             f'{c["ordered_by_side"]["US"]} Union and {c["ordered_by_side"]["Confederate"]} Confederate. '
             f'The {c["single_battle_commanders"]} single-battle and {c["zero_battle_commanders"]} zero-battle '
             'commanders remain in the downloadable data with no assigned order.',
             f'- {c["uncredited_sides"]} battle-sides receive no commander credit under the saved attribution rules; '
             'joint command is not automatically assigned to every named officer.', '']
    lines += ['## Does the commander model predict better?', '',
             'Each campaign was held out as a whole. Every model shown predicts the identical 301 battles. '
             'Lower log loss and Brier score are better. This tests prediction of recorded outcomes, '
             'not the historical truth of a commander ranking.', '',
             '| Model | Battle log loss | Campaign log loss | Battle Brier | Campaign Brier |',
             '| --- | ---: | ---: | ---: | ---: |']
    names = {'strength_only': 'Strength-only baseline', 'commander': 'Full commander model (θ below)',
             'commander_no_context': 'Simpler commander variant (saved diagnostic)'}
    for k in MODELS:
        b, w = (d['metrics'][v][k] for v in ('battle_weighted', 'campaign_weighted'))
        lines.append(f'| {names[k]} | {b["log_loss"]:.6f} | {w["log_loss"]:.6f} | {b["brier"]:.6f} | {w["brier"]:.6f} |')
    lines += ['', 'Differences below are commander minus strength-only log loss, with the saved 95% '
              'campaign-bootstrap intervals. Negative favors the commander model.', '',
              '| Comparison | Battle difference [95%] | Campaign difference [95%] |',
              '| --- | ---: | ---: |']
    for comp in d['comparisons'].values():
        cells = []
        for w in ('battle_weighted', 'campaign_weighted'):
            bs = comp['bootstrap'][w]
            cells.append(f'{comp[w]:+.6f} [{bs["q0.025"]:+.6f}, {bs["q0.975"]:+.6f}]')
        lines.append('| ' + names[comp['first']] + ' | ' + ' | '.join(cells) + ' |')
    lines += ['', 'These comparisons reuse the October 6 development results, not a new final test. '
              'The simpler variant was inspected alongside other variants and does not establish a new winner. '
              'No historical ranking ground truth exists here. Force size can itself reflect a commander’s '
              'preparation, and remaining army, assignment, documentation and source errors can affect every estimate.', '',
              '## What changes in the ordering?', '']
    ordered = [r for r in d['commanders'] if r['ordered']]
    for side, title in (('US', 'Union'), ('Confederate', 'Confederate')):
        group = [r for r in ordered if r['side'] == side]
        raw_top = min(group, key=lambda r: (r['raw_order'], r['id']))
        model_top = min(group, key=lambda r: (r['model_order'], r['id']))
        same = sum(r['raw_order'] == r['model_order'] for r in group)
        largest = sorted(group, key=lambda r: (-abs(r['order_change']), r['name']))[:2]
        examples = '; '.join(f'{r["name"]} {r["raw_order"]} → {r["model_order"]}' for r in largest)
        lines.append(f'- {title}: raw leader {raw_top["name"]}; model leader {model_top["name"]}. '
                     f'{same}/{len(group)} retain the same point position. Largest shifts: {examples}.')
    lines += ['', 'These shifts describe the models’ choices. They do not establish that the new order is more accurate.', '',
              '## Provisional commander orders', '',
              'Both orders use the same commanders with at least two credited battles, separately within '
              'each side. **Raw order** sorts cumulative residuals; **model order** sorts the stored θ point '
              'estimates. Exact ties share an order. The raw mean is also shown to expose the effect of battle '
              'count. Intervals for θ and model rank are the saved model-based approximations, conditional '
              'on its assumptions. Raw-score uncertainty was not estimated. Broad overlapping rank intervals '
              'make fine ordinal differences unreliable.', '',
              'The opponent network has disconnected components. Comparing θ across them depends on '
              'shared model priors, rather than an identified chain of opponents. '
              f'**† marks {sum("not_connected" in r["labels"] for r in ordered)} commanders with no other eligible '
              'same-side commander in their component**, preserving the saved run’s `not_connected` flag. '
              'The displayed point order should not be read as an established comparison between components.', '']
    for side, title in (('US', 'Union'), ('Confederate', 'Confederate')):
        lines += ['### ' + title, '',
                  '| Model order | Commander | W–L | Modelled strength battles | Raw order | Raw total / battle | θ [95%] | Rank [80%] |',
                  '| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |']
        for r in sorted((r for r in d['commanders'] if r['ordered'] and r['side'] == side),
                        key=lambda r: (-r['theta'], r['name'])):
            link = f'https://masonpetrosky.github.io/generalship/commanders/{r["id"]}.html'
            name = r['name'] + (' †' if 'not_connected' in r['labels'] else '')
            lines.append(f'| {r["model_order"]} | [{name}]({link}) | {r["wins"]}–{r["losses"]} | '
                         f'{r["modelled_strength_rows"]}/{r["battles"]} | {r["raw_order"]} | '
                         f'{r["raw_total"]:+.3f} / {r["raw_per_battle"]:+.3f} | '
                         f'{r["theta"]:+.3f} [{r["theta_95"][0]:+.3f}, {r["theta_95"][1]:+.3f}] | '
                         f'{r["model_rank_80"][0]}–{r["model_rank_80"][1]} |')
        lines.append('')
    lines += methods
    lines += ['## Reproduce and inspect', '',
              '`python3 -m generalship.commander_comparison --write` regenerates this comparison offline '
              'from saved results. With no flag it checks the committed JSON and this report. '
              'Neither command fits a model, fetches sources or changes frozen inputs.', '',
              '[Download all commander and battle rows](commander-comparison-v1.json). '
              '[Original rating run](commander-ratings-v4.md). '
              '[Strength and command evidence](../docs/ledgers-v3.md). '
              '[Source conventions](../docs/sources.md#audit-of-the-original-project).', '',
              'The JSON retains exact input SHA-256 bindings, exclusions, battle-level residuals, '
              'all 313 saved commanders and the unchanged original verdict. The computational reference '
              f'is `{REFERENCE["source_id"]}`, SHA-256 `{REFERENCE["sha256"]}`, '
              'zero-based notebook cells 159–167 and 196–198, inspected 2026-10-21. '
              'The external notebook is referenced, not redistributed.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    result = build(root)
    text = report(result)
    if args.write:
        write_json(root / OUTPUT, result)
        (root / REPORT).write_text(text, encoding='utf-8')
    else:
        require(not differences(read_json(root / OUTPUT), result), 'committed JSON differs; regenerate')
        require((root / REPORT).read_text(encoding='utf-8') == text, 'committed report differs; regenerate')
    print(f'Commander comparison: {result["coverage"]["scored_battles"]} battles, '
          f'{result["coverage"]["ordered_commanders"]} provisional orders; no fit')


if __name__ == '__main__':
    main()
