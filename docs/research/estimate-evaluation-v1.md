# Estimate-layer evaluation v1

Run 2026-09-25 under the locked plan in [design §6](../strength-estimates.md#6-use-in-evaluation).
**This is an exploratory estimate-layer diagnostic.** It is not the baseline, not an admitted
feature and not a ranking of commanders. The frozen baseline and `artifacts/baseline.json` are
unchanged.

## Authorization

The owner authorized the run on 2026-09-25, in reply to a question that named the reviewed
ledger and its SHA-256: "Okay yeah that's fine go ahead and run." The
[authorization record](../../data/estimates/evaluation-authorization-v1.json) keeps the
question, the reply, the ledger hash
`0656b03cbdaa088849dc3795f9c6a9e9d6762be10f53f28e4285be46f7fcde89` and commit `4ba48a1`. It
takes design §6 option (a): an exploratory diagnostic outside the admission contract.
`python3 -m generalship estimate-evaluate` (`make estimate-evaluation`) refuses to fit unless
the record names the current ledger's hash, and it replays the ledger with `estimate-check`
first.

The owner added: "think about ancient battles. We're going to have way way less information
than the civil war, so we just need to make the best estimate we can." That supports graded
best estimates over nulls; it changes nothing in this locked plan.

## Method

The plan was fixed before any fit (design §6):

- **Model.** `strength-logistic-v1`, unchanged: ridge 1.0 logistic regression on
  (US − Confederate)/(US + Confederate), using each side's rounded point.
- **Validation.** Leave one campaign out, over the campaigns present in each row set.
- **Comparators.** Equal odds and the Laplace-smoothed training prior.
- **Leakage exclusion.** Rows with a `post_start_information` side do not enter any fit.
- **Row sets.** Three nested sets; the grade-A set is the strictest.
- **Sensitivity refits.** Every refit named in design §6.
- **Comparisons.** Estimates against a frozen-baseline refit on common rows; equal odds and
  the prior only on newly covered rows.

The outputs are [`artifacts/estimate-evaluation.md`](../../artifacts/estimate-evaluation.md) and
[`artifacts/estimate-evaluation.json`](../../artifacts/estimate-evaluation.json). The JSON has
every fold, every prediction and the §5 label counts.

**One implementation fix was needed.** The shared optimizer in `generalship/baseline.py` raised
"did not converge" on some held-out folds. It was not diverging: after two or three Newton
steps it sat at the optimum, where the predicted decrease (about 1e-15) is below the
objective's floating-point rounding, and the Armijo line search then accepted
vanishing steps until the 100-iteration limit. The fit now stops when the Newton decrement
`g·d` is below 1e-12 and takes the full step. The objective, ridge, feature and model are
unchanged. The frozen `artifacts/baseline.json` is byte-identical before and after. A
regression test uses the exact failing fold.

## Results

Brier score (lower is better; equal odds scores 0.2500). "Battle" weights every row equally;
"campaign" averages per-campaign scores.

| Row set | Rows / campaigns | Strength model, battle / campaign | Equal odds | Training prior, battle / campaign |
| --- | ---: | ---: | ---: | ---: |
| Both sides grade A | 21 / 12 | 0.2792 / 0.2683 | 0.2500 | 0.2934 / 0.2739 |
| Both sides A or B | 29 / 15 | 0.2483 / 0.2274 | 0.2500 | 0.2700 / 0.2361 |
| Both sides A, B or C | 37 / 19 | 0.2357 / 0.2132 | 0.2500 | 0.2456 / 0.2112 |
| Frozen baseline (reference) | 23 / 13 | 0.2769 / 0.2765 | 0.2500 | — |

Log loss follows the same pattern (A–C: strength 0.664, equal odds 0.693, prior 0.693).
Seven rows are excluded as post-start: MS003, MS011, NC007, TN002, TN024, VA017 and WV010.

**Common rows.** At A–C, 21 rows have both a frozen baseline row and an estimate row; 18 of
them are identical by construction, because the estimate equals the frozen figure before
rounding. Refit on the same training rows, the estimate and frozen models score almost the same
(0.2947 and 0.2941, battle-weighted). Both are worse than equal odds on these rows.

**Newly covered rows.** At A–C, the 16 new rows score 0.1603 for the strength model, 0.1662 for
the prior and 0.2500 for equal odds. Most of these rows are Union wins, which the training
prior already expects.

**Sensitivity.** The refits move the A–C strength-model Brier between 0.212 and 0.263. Moving
every side to its range endpoints gives 0.227–0.244. Dropping rows labelled
`applicability_unresolved` (27 rows left) gives 0.263, and dropping `opponent_estimate_point`
rows (30 left) gives 0.256. The rule-4 factor, basis-order and median variants change little.
Dropping `derivation_unknown` rows leaves the A and A–B sets not evaluable (1 and 5 rows).

## What this shows

- **Army size alone is a weak predictor in this cohort.** On the strictest set (21 rows,
  both sides grade A) the strength model does worse than a coin flip, as the frozen 23-row
  baseline does.
- **The widest set looks better, but not clearly better than the base rate.** At A–C the
  battle-weighted Brier is below equal odds, but the campaign-weighted Brier (0.2132) is no
  better than the training prior (0.2112). Most of the gain is in newly covered rows, where the
  prior does almost as well.
- **The best estimates add rows, not a changed answer.** On common rows the estimates and the
  frozen figures give the same predictions, as expected, since most are the same figures.
- **None of these differences is significant** at 21–37 rows, and results across row sets or
  variants are not improvements over one another (design §6). Which sides have figures may
  depend on the outcome, size and fame, so every result carries `whole_engagement_leakage` and
  `conditional_on_source_availability`.

## Limits and next step

This evaluation predicts outcomes from strength; it says nothing yet about generals. Rating
commanders needs, at least:

- who held decision responsibility on each side of each engagement (no automatic attribution to
  every listed commander);
- a campaign-level unit, so battles and campaigns are not double counted;
- a model that separates strength-predicted outcomes from residuals, with partial pooling and
  honest uncertainty (roadmap Milestone 3).

Those are design decisions for the owner, not consequences of this run.
