"""How sure is a rating run's held-out verdict? (docs/research/commander-ratings-v3.md, "How sure")

Computed from a committed run's stored held-out predictions; nothing is refitted and no run or
verdict of record changes. It reports a campaign-clustered bootstrap of the held-out log-loss
difference, a sign test over campaigns, how much of the difference rests on single commanders,
and the difference on row subsets that drop leakage-prone rows. Every subset figure reuses the
committed predictions, so it shows where the gain sits, not what a refit without those rows
would give. Sums use math.fsum, so results do not depend on the Python version.
"""

from collections import defaultdict
import math
import random

from .sources import digest, read_json, safe_path

RUNS = {2: {'output': 'artifacts/commander-ratings-v2.json', 'command': 'data/command/responsibility-v2.json',
            'strength': 'data/estimates/side-strength-v2.json'},
        3: {'output': 'artifacts/commander-ratings-v3.json', 'command': 'data/command/responsibility-v2.json',
            'strength': 'data/estimates/side-strength-v2.json'}}
RESAMPLES = 20000
SEED = 20261006
QUANTILES = (0.025, 0.05, 0.1, 0.5, 0.9, 0.95, 0.975)
SIDES = ('US', 'Confederate')


def log_loss(y, p):
    """The clipped binary log loss used by every scored run (baseline.scores)."""
    p = min(1 - 1e-15, max(1e-15, p))
    return -(y * math.log(p) + (1 - y) * math.log1p(-p))


def differences(predictions):
    """Per-row log-loss difference, commander model minus strength only (negative favours commanders)."""
    return [{'battle_id': p['battle_id'], 'campaign': p['campaign'],
             'd': log_loss(p['union_outcome'], p['commander_model']) - log_loss(p['union_outcome'], p['strength_only'])}
            for p in predictions]


def weighted(rows):
    """(battle-weighted, campaign-weighted) mean difference."""
    by = defaultdict(list)
    for r in rows:
        by[r['campaign']].append(r['d'])
    battle = math.fsum(r['d'] for r in rows) / len(rows)
    campaign = math.fsum(math.fsum(v) / len(v) for v in by.values()) / len(by)
    return battle, campaign


def quantile(xs, q):
    """The value at position floor(q·n) of the sorted sample (the convention of ratings.rank_intervals)."""
    xs = sorted(xs)
    return xs[min(len(xs) - 1, max(0, int(math.floor(q * len(xs)))))]


def bootstrap(rows, resamples=RESAMPLES, seed=SEED):
    """Resample whole campaigns with replacement; both weightings of the mean difference."""
    by = defaultdict(list)
    for r in rows:
        by[r['campaign']].append(r['d'])
    camps = sorted(by)
    sums = [math.fsum(by[c]) for c in camps]
    counts = [len(by[c]) for c in camps]
    means = [s / n for s, n in zip(sums, counts)]
    rng = random.Random(seed)
    battle, campaign = [], []
    for _ in range(resamples):
        pick = [rng.randrange(len(camps)) for _ in camps]
        battle.append(math.fsum(sums[i] for i in pick) / sum(counts[i] for i in pick))
        campaign.append(math.fsum(means[i] for i in pick) / len(pick))
    out = {}
    for name, xs in (('battle_weighted', battle), ('campaign_weighted', campaign)):
        out[name] = {f'q{q:g}': quantile(xs, q) for q in QUANTILES}
        out[name]['share_at_or_above_zero'] = sum(x >= 0 for x in xs) / len(xs)
    return out


def sign_test(rows):
    """Campaigns where the commander model's mean log loss was lower, higher or equal; exact two-sided p."""
    by = defaultdict(list)
    for r in rows:
        by[r['campaign']].append(r['d'])
    better = sum(math.fsum(v) < 0 for v in by.values())
    worse = sum(math.fsum(v) > 0 for v in by.values())
    n = better + worse
    tail = lambda k: math.fsum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n
    p = min(1.0, 2 * min(tail(better), tail(worse))) if n else 1.0
    return {'commander_model_better': better, 'strength_only_better': worse, 'ties': len(by) - n,
            'two_sided_p': p}


def attributions(root, command_path):
    """{battle_id: [commander IDs credited on either side]} under the primary attribution."""
    out = {}
    for e in read_json(safe_path(root, command_path))['engagements']:
        out[e['battle_id']] = [e['sides'][s]['commander_id'] for s in SIDES if e['sides'][s]['commander_id']]
    return out


def labelled_rows(root, strength_path, command_path):
    """Battle IDs with a post-start strength side and with a joint-command side."""
    post = {e['battle_id'] for e in read_json(safe_path(root, strength_path))['engagements']
            if any('post_start_information' in e['sides'][s]['estimate']['labels'] for s in SIDES)}
    joint = {e['battle_id'] for e in read_json(safe_path(root, command_path))['engagements']
             if any('joint_command' in e['sides'][s]['labels'] for s in SIDES)}
    return post, joint


def analyse(root, version=3):
    run = RUNS[version]
    result = read_json(safe_path(root, run['output']))
    test = result['heldout_test']
    rows = differences(test['predictions'])
    battle, campaign = weighted(rows)
    reported = tuple(test[w]['commander_model']['log_loss'] - test[w]['strength_only']['log_loss']
                     for w in ('battle_weighted', 'campaign_weighted'))
    if any(abs(a - b) > 1e-12 for a, b in zip((battle, campaign), reported)):
        raise ValueError('Stored predictions do not reproduce the run\'s reported log losses')
    credited = attributions(root, run['command'])
    names = {c: v['name'] for c, v in result['commanders'].items()}
    gain = defaultdict(lambda: [0.0, 0])
    for r in rows:
        for c in credited.get(r['battle_id'], []):
            gain[c][0] -= r['d']
            gain[c][1] += 1
    contributions = sorted(({'commander': c, 'name': names.get(c, c), 'rows': n, 'net_gain': g}
                            for c, (g, n) in gain.items()), key=lambda x: (-x['net_gain'], x['commander']))
    total_gain = -math.fsum(r['d'] for r in rows)
    drop_one = []
    for c, (_, n) in gain.items():
        if n < 2:
            continue
        kept = [r for r in rows if c not in credited.get(r['battle_id'], [])]
        b, w = weighted(kept)
        drop_one.append({'commander': c, 'name': names.get(c, c), 'rows_dropped': n,
                         'battle_weighted': b, 'campaign_weighted': w})
    drop_one.sort(key=lambda x: (-x['battle_weighted'], x['commander']))
    post, joint = labelled_rows(root, run['strength'], run['command'])
    subsets = {}
    for name, drop in (('without_post_start_rows', post), ('without_joint_command_rows', joint),
                       ('without_either', post | joint)):
        kept = [r for r in rows if r['battle_id'] not in drop]
        b, w = weighted(kept)
        subsets[name] = {'rows': len(kept), 'battle_weighted': b, 'campaign_weighted': w}
    top = contributions[:2]
    kept = [r for r in rows if not set(credited.get(r['battle_id'], [])) & {c['commander'] for c in top}]
    b, w = weighted(kept)
    subsets['without_top_two_contributors'] = {'commanders': [c['name'] for c in top], 'rows': len(kept),
                                               'battle_weighted': b, 'campaign_weighted': w}
    return {'kind': 'rating_verdict_uncertainty', 'version': 1, 'run_version': version,
            'status': 'descriptive_from_committed_predictions_no_refit',
            'run': {'path': run['output'], 'sha256': digest(safe_path(root, run['output']))},
            'bindings': {k: {'path': run[k], 'sha256': digest(safe_path(root, run[k]))} for k in ('command', 'strength')},
            'convention': 'difference = commander-model log loss minus strength-only log loss; negative favours commanders',
            'rows': len(rows), 'campaigns': len({r['campaign'] for r in rows}),
            'point': {'battle_weighted': battle, 'campaign_weighted': campaign},
            'bootstrap': {'resamples': RESAMPLES, 'seed': SEED, 'unit': 'campaign', **bootstrap(rows)},
            'sign_test': sign_test(rows),
            'total_net_gain': total_gain,
            'commander_contributions': contributions,
            'drop_one_commander': drop_one,
            'subsets_no_refit': subsets,
            'limits': ['Uses the committed held-out predictions; nothing is refitted, so a subset shows where the gain '
                       'sits, not what a model fitted without those rows would give.',
                       'A row counts toward both of its credited commanders.',
                       'The bootstrap treats campaigns as exchangeable; it does not cover attribution, strength or '
                       'source uncertainty.',
                       'Not a new verdict: the run\'s own rule and result stand as recorded.']}


def report_text(r):
    f = lambda x: f'{x:+.4f}'
    bw, cw = r['bootstrap']['battle_weighted'], r['bootstrap']['campaign_weighted']
    s = r['sign_test']
    lines = [f"# How sure is rating run {r['run_version']}'s verdict?", '',
             f"Descriptive, from the committed held-out predictions of [run {r['run_version']}]({r['run']['path'].rsplit('/', 1)[-1].replace('.json', '.md')}) "
             f"(SHA-256 `{r['run']['sha256'][:12]}…`). Nothing is refitted and the run's own verdict stands as recorded. "
             f"Differences are commander-model log loss minus strength-only log loss, so **negative favours commanders**.", '',
             f"{r['rows']} held-out rows in {r['campaigns']} campaigns.", '',
             '| Weighting | Difference | 95% interval (campaign bootstrap) | 80% interval | Resamples ≥ 0 |',
             '|---|---:|---:|---:|---:|',
             f"| Battle-weighted | {f(r['point']['battle_weighted'])} | {f(bw['q0.025'])} to {f(bw['q0.975'])} | "
             f"{f(bw['q0.1'])} to {f(bw['q0.9'])} | {bw['share_at_or_above_zero']:.1%} |",
             f"| Campaign-weighted | {f(r['point']['campaign_weighted'])} | {f(cw['q0.025'])} to {f(cw['q0.975'])} | "
             f"{f(cw['q0.1'])} to {f(cw['q0.9'])} | {cw['share_at_or_above_zero']:.1%} |", '',
             f"Campaigns: commander model better in {s['commander_model_better']}, strength only better in "
             f"{s['strength_only_better']}, ties {s['ties']}; exact two-sided sign-test p = {s['two_sided_p']:.3f}.", '',
             '## Where the difference sits (no refit)', '',
             '| Rows kept | Rows | Battle-weighted | Campaign-weighted |', '|---|---:|---:|---:|',
             f"| All | {r['rows']} | {f(r['point']['battle_weighted'])} | {f(r['point']['campaign_weighted'])} |"]
    labels = {'without_post_start_rows': 'Without rows with a post-start strength side',
              'without_joint_command_rows': 'Without rows with a joint-command side',
              'without_either': 'Without either',
              'without_top_two_contributors': 'Without the rows of ' + ' and '.join(r['subsets_no_refit']['without_top_two_contributors']['commanders'])}
    for k, label in labels.items():
        v = r['subsets_no_refit'][k]
        lines.append(f"| {label} | {v['rows']} | {f(v['battle_weighted'])} | {f(v['campaign_weighted'])} |")
    lines += ['', f"Net log-loss gain over all rows: {r['total_net_gain']:.3f}. The commanders whose rows carry the most "
              'and the least of it (a row counts for both of its commanders):', '',
              '| Commander | Rows | Net gain |', '|---|---:|---:|']
    for c in r['commander_contributions'][:8] + r['commander_contributions'][-5:]:
        lines.append(f"| {c['name']} | {c['rows']} | {c['net_gain']:+.3f} |")
    lines += ['', '## Limits', ''] + [f'- {x}' for x in r['limits']] + ['']
    return '\n'.join(lines)
