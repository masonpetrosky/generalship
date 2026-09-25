# Commander residual ratings v2: full-war run

Run 2026-09-25 under the accepted [design](../commander-ratings.md), unchanged, on the reviewed
[cohort-v2 ledgers](ledgers-v2.md). This is an exploratory diagnostic. It is not a ranking of
record, a measure of command skill or a causal estimate. The baseline is unchanged. **Status:
separately reviewed ([review](../../artifacts/review-results/ratings-v2-review-8befd97-opus-high-v1/review.md)); its six required corrections are applied.**

## Authorization

The owner authorized both runs for the exact files named in the question, answering "Run both
(Recommended)" ([ratings record](../../data/command/rating-authorization-v2.json),
[evaluation record](../../data/estimates/evaluation-authorization-v2.json)):

| File | SHA-256 |
| --- | --- |
| Strength ledger `data/estimates/side-strength-v2.json` | `7855d4d3…2deed8` |
| Command ledger `data/command/responsibility-v2.json` | `495cef30…da06ac` |
| Commander registry `data/command/commanders-v2.json` | `91fc2526…5e3768` |

The code is at `cef8f3f`: run 1 reproduces the committed v1 outputs byte for byte, and run 2
(`make commander-ratings-v2`, which first runs `make estimate-evaluation-v2`) binds the v2 files
and builds its rows from cohort v2. Outputs: `artifacts/estimate-evaluation-v2.{json,md}` and
`artifacts/commander-ratings-v2.{json,md}`.

## Strength alone (estimate-layer evaluation, design §6 option (a))

| Row set | Rows | Campaigns | Strength model | Equal odds | Training prior |
| --- | ---: | ---: | ---: | ---: | ---: |
| Both sides A | 61 | 38 | 0.2508 / 0.2560 | 0.2500 | 0.2611 / 0.2542 |
| Both sides A–B | 80 | 47 | 0.2506 / 0.2648 | 0.2500 | 0.2584 / 0.2572 |
| Both sides A–C | 126 | 66 | 0.2349 / 0.2452 | 0.2500 | 0.2478 / 0.2447 |

Brier score, battle-weighted / campaign-weighted, leave one campaign out. On the A–C rows the
strength model does better than equal odds under both weightings and better than the training
prior battle-weighted, but not campaign-weighted (0.2452 against 0.2447). On the A and A–B rows it
does no better than equal odds. Size alone remains a weak predictor. 17 rows with a post-start side
are excluded (13 from the A–C set).

## The verdict: a small held-out improvement

The design fixed the test in advance (§5): leave one campaign out on the primary rows (the 126 A–C
rows), τ = 0.5, primary attribution; the commander model must have strictly lower held-out log loss
than the strength-only model under both the battle and the campaign weighting.

| Model | Log loss, battle-weighted | Log loss, campaign-weighted |
| --- | ---: | ---: |
| Commander model | 0.6540 | 0.6795 |
| Strength only | 0.6633 | 0.6844 |

- The commander model is lower under both weightings, by 0.0093 and 0.0049. By the design's rule
  this is an improvement, read only as: held-out log loss was lower on these rows. The Markdown
  report therefore orders commanders by median rank.
- It did better in 39 of 66 held-out campaigns and worse in 27 (descriptive; not part of the
  verdict).
- 87 of 126 held-out rows had a commander seen in another campaign (the effective denominator),
  against 21 of 37 in run 1.
- The descriptive split carries no verdict and does not support the verdict (design §5). Its years,
  trained on 1861–1863 (79 rows) and tested on 1864–1865 (47 rows), are an author's run-2 choice, set
  in the code at `cef8f3f` before the run commit; the design fixed only the v1 1862→1863 split. There
  the commander model's log loss was 0.6592 against 0.6666 on the same rows as the held-out test.

**Reading, fixed in advance.** A lower held-out log loss is not evidence of a persistent commander
effect or of skill (design §5). The margins are small, no significance test was run, and the
ratings still carry every limit below.

## What the estimates look like

40 commanders have two or more modelled battles (21 US, 19 Confederate); the report lists them
with their intervals. θ is on the log-odds scale and relative to the commander's own side.

- **No interval excludes zero** in the primary view, at 80% or 95%. The widest shift from the prior
  is Forrest's (posterior SD 0.84 of the prior's); the others are 0.86–0.96, so the ratings are
  still mostly the prior.
- **Top and bottom by mode.** Confederate: Forrest +0.50 (8 battles, 6–2; 80% interval −0.04 to
  +1.04), Beauregard +0.39, Jackson +0.32; Hood −0.39 (5 battles, 0–5). US: McNeil +0.23,
  Prentiss +0.20, Sheridan +0.20 (3–0); Gillmore −0.29, McDowell −0.25.
- **Ranks overlap completely.** On each side every pair's 80% rank intervals overlap. Forrest's 80% rank interval is 1–11 of 19, Hood's 8–19; the
  US 80% rank intervals run from 2–17 to 6–21 of 21.
- **Connections.** 15 of the 40 are `not_connected`, including Forrest, Marmaduke, Early and Morgan:
  they share no chain of opponents with another ranked commander of their side, so their places
  rest partly on the prior.
- **Robustness.** No commander is `view_sensitive` across the 68 robustness views (the three outcome-only views do not set it, design §6). Several are
  `unranked_in_view` in views that drop or reassign their rows (listed in the report).
- **Coverage shapes the list.** Lee has 19 attributed battles but 7 modelled, Grant 11 and 5; the
  JSON lists each commander's out-of-model battles and reasons.
- **Outcome-only views** (no force term, `includes_force_size_advantage`, a different quantity).
  On the 301 in-scope decisive rows (the 305 two-sided engagements less GA012, LA009, VA033 and
  VA034, dropped as nested; a further view also drops TN035, whose nesting is unresolved), the
  largest moves among the 40 ranked commanders are Grant (+0.40) and Sherman (−0.30) (among all
  modelled commanders, James H. Wilson moves −0.34); Forrest, Beauregard and Grant have 80% intervals above zero
  there. These credit force concentration and every other advantage the commander did not create,
  and have no held-out test.

## What this means

- **The verdict changed with the wider frame.** On the 1862–63 pilot (37 rows) the commander
  model's held-out log loss was not lower under both weightings; on the full war (126 rows, 87 with
  a commander seen elsewhere) it was lower under both, by 0.0093 and 0.0049. The rows, campaigns
  and years all differ between the runs, so this does not show which change moved it. The rule was
  fixed before either run.
- **It is not a ranking of skill.** The residual includes army quality, subordinates, theater,
  opponents and coding choices; commander-created advantages are only partly separated from force
  size; the ledgers are reviewed estimates, not adjudication, and extraction was not blind.
- **Individual places are uncertain.** Intervals are wide and rank intervals overlap for nearly
  everyone. The report's order is a point summary under the design, not a finding that one
  commander was better than another.

## Limits

- Every result carries `whole_engagement_leakage`, `conditional_on_source_availability`,
  `not_causal` and `side_relative` (design §8).
- Which battles have usable strengths may depend on outcome, size and fame.
- The twelve records with a Native American belligerent are outside the two-sided model.
- The separate review is an AI review, not human historical adjudication.
