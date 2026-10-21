"""Presentation of saved v2 estimates and paired comparison; never fits a model."""

from collections import Counter

from . import bodart_aliases as aliases
from . import bodart_ratings as v1
from .sources import read_json


def report(root, cohort, run):
    old = read_json(root / v1.RUN)
    manifest = read_json(root / aliases.ALIASES)
    before, after = cohort['before'], cohort['after']
    names = {g['canonical_unit']: g['display_name'] for g in manifest['groups']}
    estimates = run['estimates']
    ordered = [e for e in estimates if e['rank'] is not None]
    previous = {e['unit']: e for e in old['estimates']}
    current = {e['unit']: e for e in estimates}
    lines = ['# Bodart: names consolidated, same battles', '',
             f'**{after["engagements"]} unchanged engagements · {len(manifest["groups"])} supported alias groups · '
             f'{after["labels"]} estimated labels · {after["ordered_labels"]} provisional orders.** '
             'Bonaparte and Napoleon I now contribute to one scoped identity. This is a bounded cleanup '
             'using Bodart’s own index, followed by the same model and evaluation settings.', '',
             '[Download estimates](bodart-ratings-v2.csv) · [Saved run and folds](bodart-ratings-v2.json) · '
             '[Alias evidence](../data/bodart/aliases-v1/aliases.json) · '
             '[Migration and coverage](../data/bodart/ratings-v2/cohort.json) · '
             '[Fixed design](../docs/bodart-ratings-v2.md) · [First run](bodart-ratings-v1.md)', '',
             '## What changed?', '', '| Quantity | First run | Alias cleanup |', '| --- | ---: | ---: |']
    for key, title in [('engagements', 'Engagements'), ('labels', 'Command labels'),
                       ('ordered_labels', 'Labels with at least three appearances'), ('components', 'Opponent components'),
                       ('largest_component_labels', 'Labels in largest component'), ('personnel_checked', 'Checked force pairs')]:
        lines.append(f'| {title} | {before[key]} | {after[key]} |')
    lines += ['', f'The map covers {cohort["alias_occurrences"]} side appearances; '
              f'{cohort["changed_occurrences"]} side appearances receive a different canonical key. '
              f'{cohort["orientation_flips"]} rows reverse their alphabetic A/B orientation, with forces '
              'swapped, log force ratio negated and outcome complemented. No outcome or force reading changes. '
              'No excluded row is rescued and all 52 reserved-final entries stay excluded.', '',
              '| Consolidated name | First-run labels | Included appearances | Old component/orders | New component/order |',
              '| --- | ---: | ---: | --- | --- |']
    for g in manifest['groups']:
        e = current[g['canonical_unit']]
        old_orders = ', '.join(f'C{previous[u]["component"]}: {previous[u]["rank"] or "unranked"}' for u in g['members'])
        lines.append(f'| {g["display_name"]} | {len(g["members"])} | {e["battles"]} | {old_orders} | C{e["component"]}: {e["rank"]} |')
    lines += ['', 'These orders use different label rosters and connected components; the movement is '
              'descriptive. Merging labels also changes partial pooling and the effective prior structure. '
              'It does not isolate a change in personal skill.', '',
              '## Same held-out battles and folds', '',
              'Leave each of the same calendar decades out of training in turn. Lower log loss and '
              'Brier score are better. This remains development evaluation: campaigns may cross decade '
              'boundaries and it is not a final or forward test.', '',
              '| Model | Battle log loss | Equal-decade log loss | Battle Brier | Equal-decade Brier |',
              '| --- | ---: | ---: | ---: | ---: |']
    for data, key, title in [(old, 'equal_odds', 'Equal odds'), (old, 'force_only', 'Force only'),
                              (old, 'commander', 'First-run command labels'), (run, 'commander', 'Consolidated command labels')]:
        b, d = data['metrics']['battle_weighted'][key], data['metrics']['decade_weighted'][key]
        lines.append(f'| {title} | {b["log_loss"]:.6f} | {d["log_loss"]:.6f} | {b["brier"]:.6f} | {d["brier"]:.6f} |')
    delta = {w: run['metrics'][w]['commander']['log_loss'] - old['metrics'][w]['commander']['log_loss']
             for w in run['metrics']}
    seen = Counter(p['seen_labels'] for p in run['predictions'])
    old_seen = Counter(p['seen_labels'] for p in old['predictions'])
    lines += ['', f'Cleanup minus first-run log loss: **{delta["battle_weighted"]:+.6f} per battle** and '
              f'**{delta["decade_weighted"]:+.6f} per decade**. '
              'The force-only and equal-odds comparators reproduce unchanged losses on the paired rows. '
              'These point differences do not establish correct skill ranks or isolate AI’s benefit.', '',
              f'Equal-decade log loss is {run["metrics"]["decade_weighted"]["commander"]["log_loss"]:.6f}, '
              f'versus {run["metrics"]["decade_weighted"]["equal_odds"]["log_loss"]:.6f} for equal odds.', '',
              f'Held-out labels seen in training (first run → cleanup): both {old_seen[2]} → {seen[2]}, '
              f'one {old_seen[1]} → {seen[1]}, neither {old_seen[0]} → {seen[0]}, out of {len(cohort["rows"])}. '
              'Unseen labels use prior mean zero.', '',
              '## Provisional orders', '',
              'Order only labels with at least three appearances, within each connected opponent component. '
              'θ is a shrunk conditional log-odds association. The 95% intervals are approximate marginal '
              'Laplace intervals conditional on the model and recorded inputs. They omit source/OCR, '
              'identity, army, campaign and model uncertainty; overlapping intervals do not settle adjacent '
              'ranks. Most labels remain unresolved strings despite these eight mappings. '
              'There is no cross-component ranking or causal WAR.', '']
    sensitivity = {k: {e['unit']: e for e in s['estimates']} for k, s in run['sensitivities'].items()}
    for component in sorted({e['component'] for e in ordered}):
        group = sorted((e for e in ordered if e['component'] == component), key=lambda e: (e['rank'], e['unit']))
        lines += ['', f'### Opponent component {component}', '',
                  f'{len(group)} ordered out of {sum(e["component"] == component for e in estimates)} estimated labels.', '',
                  '| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |',
                  '| ---: | --- | --- | ---: | ---: | --- | --- |']
        for e in group:
            lo, hi = e['interval_95']
            priors = [sensitivity[k][e['unit']]['rank'] for k in ('prior_sd_0.5', 'prior_sd_2')]
            lines.append(f'| {e["rank"]} | {names.get(e["unit"], e["unit"])} | {e["years"][0]}–{e["years"][1]} | '
                         f'{e["battles"]} ({e["wins"]}) | {e["checked_personnel_battles"]} | '
                         f'{e["theta"]:+.3f} ({lo:+.3f}, {hi:+.3f}) | {priors[0]} / {priors[1]} |')
    lines += ['', '## Evidence for the eight mappings', '',
              'Primary-verified against eight retained index images and nine selected passages. These are '
              'all one Bodart source family. Index co-reference supports scoped compiler identity, '
              'not independent biographical truth or verified command responsibility. '
              'The alias download retains all original labels, exact row/side occurrences, citations and hashes.', '']
    for g in manifest['groups']:
        lines += [f'### {g["display_name"]}', '', g['interpretation'], '',
                  'Original units: ' + ', '.join('`' + u + '`' for u in g['members']) + '.', '']
        for c in g['citations']:
            quote = ' '.join(c['quote'].split())
            lines += ['> ' + quote, '', f'[{c["locator"]}]({c["scan_url"]}); '
                      f'[source and SHA-256](https://masonpetrosky.github.io/generalship/sources.html#{c["source_id"]}).', '']
        if g['index_unlisted_battle_ids']:
            lines += ['Index page-reference omissions: ' + ', '.join(g['index_unlisted_battle_ids']) + '. '
                      'The scoped same-literal mapping is retained; the omission is not silently repaired.', '']
    checked = run['sensitivities']['checked_personnel_only']
    lines += ['## Limits and verification', '',
              f'{after["labels"] - after["ordered_labels"]} labels have fewer than three appearances and receive '
              f'no order. Source/force coverage is unchanged: {after["personnel_checked"]}/{len(cohort["rows"])} '
              'force pairs checked. OCR names and years remain uncertain; no new per-battle historical check '
              'is implied. Title strings including “Marquis Wellesley” remain as printed.', '',
              f'The fixed personnel-checked sensitivity uses {checked["rows"]} rows, '
              f'{len(checked["model"]["theta"])} labels and '
              f'{sum(e["rank"] is not None for e in checked["estimates"])} orders, on a different cohort. '
              'Prior sensitivity columns are alternative point orders, not rank confidence intervals. '
              'All settings, priors and folds match v1; no post-result tuning was performed.', '',
              f'The saved run records base commit `{run["base_commit"]}` and SHA-256s for the fixed '
              'mapping, source snapshots, prepared migration, protocol and reused fitting engine. '
              'Primary verification checks exact source passages and scope, orientation, identical '
              'battle/fold membership, penalized gradients, inverse-Hessian intervals, saved predictions '
              'and paired metrics without refitting historical outcomes. Army confounding and the fact '
              'that force advantages can be commander-created remain.', '',
              '`python3 -m generalship.bodart_ratings_v2 --write` rebuilds this report and estimates CSV '
              'from the saved run. The default verifies them. Ordinary reproduction does not run the '
              'historical fitting job. The first report and all frozen inputs remain available.', '']
    return '\n'.join(lines)
