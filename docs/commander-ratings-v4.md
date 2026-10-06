# Commander residual ratings, run 4: context comparator, estimated τ and leakage handling

Status: **primary-verified design, fixed before run 4 computed any held-out result**, 2026-10-06. It
extends the [commander-rating design](commander-ratings.md) and the
[grade E design](strength-imputation.md). Runs 1–3, their records and the frozen baseline are
unchanged.

On 2026-10-06 the author listed eight improvements. Item 1 was:

> Run 3's verdict is fragile, and its uncertainty isn't reported.

and item 8 was:

> Before starting the Napoleonic Wars: make the code work for any war.

The owner replied "Sounds good, go ahead and fix all 8"
([authorization record](../data/command/rating-authorization-v4.json)). Under the owner's
self-verification policy of the same day, the primary designed, implemented and verified this run with
no separate review. The record binds the hashes of this design, every input and the code the run
executes; the run refuses to start if any differs.

**Order of work.** The code was tested on synthetic data and smoke-tested end to end on the real rows
with outcomes shuffled, so that no real held-out result was seen. This design, the code and the
authorization were then committed before the run. Run 3's results and their
[uncertainty analysis](../artifacts/commander-ratings-v3-uncertainty.md) were known when this design
was written; it responds to them, and its own rule is fixed before its own numbers exist.

## 1. Why

Run 3 found lower held-out log loss for the commander model than for force size alone, under both
weightings (by 0.0121 and 0.0065). Four weaknesses limit what that shows:

1. **Uncertainty.** A campaign bootstrap puts the campaign-weighted gain's 95% interval at −0.0102 to
   +0.0226, which includes zero. Forrest's 12 rows carry 38% of the net gain.
2. **Leakage-prone rows.** Two kinds of row may carry outcome information:
   - 17 rows have a side whose strength uses post-start information;
   - 18 rows have a side whose commander rule 5 chose as "the force compelling the result".

   Without both, the stored predictions give 0.0088 and 0.0021.
3. **No context comparator.** Commanders are tied to theaters and periods, so a commander term can
   absorb when and where a battle was fought. Run 3 compared commanders only with force size.
4. **τ was a convention.** The commander spread was fixed at 0.5, never estimated. Yet whether
   commanders differ at all is the question τ answers.

## 2. Inputs and the pre-start view

**Inputs.** Run 4 uses:

- the [v3 strength ledger](ledgers-v3.md);
- the v2 command ledger and registry;
- the frozen CWSAC battle and campaign tables.

The rows are those of run 3 (§3). The war is described by a profile (§10).

**The pre-start view.** The proposal said to "exclude those rows from the test". Run 4 instead removes
the outcome-dependent information and keeps the battles. This follows the owner's decision of
2026-09-25 that battles should not be omitted for want of a strength
([record](../data/estimates/owner-decision-grade-e-2026-09-25.json)), and it scales to sparser wars.
The exclusion is still reported as a check (§7).

For each side whose ledger estimate carries `post_start_information` (20 sides in 17 rows), the frozen
engine (`estimate_side`, [strength design](strength-estimates.md) §4) re-estimates the side after
removing every input in a dependence group that matches §3 row 3.

- A whole group is removed, so a copy of a post-start figure cannot survive as a clean candidate.
- A side left with a class A–C candidate keeps that pre-start estimate. This applies to two sides:
  - **VA111, US:** grade A, 8,500 (8,080–8,930). An opponent's post-start figure had raised its high
    end to 10,000.
  - **WV010, US:** grade C, 11,500 (8,050–14,950). The surrender count has been removed.
- A side left with no candidate becomes grade D in the view and is modelled (grade E). This applies
  to the other 18 sides. They are labelled `post_start_modelled`, and their bounds come only from the
  remaining inputs.

**Grade E v2** (`artifacts/strength-imputation-v2.json`, `generalship/imputation_v2.py`).

- **Method.** The [grade E method](strength-imputation.md#2-grade-e-the-model) is unchanged. It reuses
  `imputation.py`'s model, calibration, bounds and truncation, with profile-driven predictors.
- **Training sides.** It trains on the sides graded A–C in the pre-start view: 429, the 328 of run 3
  plus the 99 filled by ledger v3 and the 2 re-estimated sides.
- **Calibration.** Leave-one-out 80% coverage is 0.7995 before widening, so k = 1.01. At k, coverage
  leaving out one campaign is 0.797. `regiment` (1 training row) and `flotilla` (2) merge into
  `unknown`.
- **Modelled sides.** It models the 181 sides graded D in the view: 163 grade D in the ledger and 18
  post-start sides.
- **Reproduction.** Without the pre-start view, run on the v2 ledger, it reproduces
  `artifacts/strength-imputation-v1.json` exactly, with every option of run 3's views
  (`tests/test_imputation_v2.py`).

## 3. Rows and attribution

- **Rows.** Every in-scope engagement less the contained records of nested pairs: 301 rows in 108
  campaigns, as in run 3.
  - 120 rows have a modelled side.
  - 17 rows had a post-start side in the ledger; 15 of them now have a modelled side.
  - 18 rows have a joint-command side.
- **Outcome.** 1 if side A (the US) won. Every in-scope result maps to a decisive outcome under the
  profile; the run refuses any that does not.
- **Attribution.** The run-3 rules apply, with one change. A side labelled `joint_command` (rule 5,
  20 sides) **gets no commander term**:
  - the row still enters through α, β, the context terms and the other side's commander;
  - the view `joint_command_credited` restores run 3's attribution;
  - an alternative-candidate view still credits its candidate.
- **Sign.** A commander's term enters with the sign of the side they commanded in that row, not a
  fixed registry side. Within-side ranks use the registry side, as before.

## 4. Models

For battle *i*, with force ratio x_i = (A − B)/(A + B):

```
logit P(side A wins) = α + β·x_i + γ[theater_i] + δ[period_i] + η[theater_i × period_i] + θ[a_i] − θ[b_i]
α, β ~ Normal(0, 1)
γ, δ, η ~ Normal(0, κ²), κ = 0.5          (the context effects)
θ_k ~ Normal(0, τ²), independently          (the commanders)
```

- **The models.**
  - **Commander model:** the full model.
  - **Context model:** the same without θ (τ = 0).
  - **Strength only:** α + β·x, the baseline's ridge logistic.
- **Context terms.** Theater is the campaign theater. Period is 1861–1862, 1863 or 1864–1865, from the
  frozen start date. Because the outcome is oriented to side A, the theater-by-period effects are the
  "side × theater × period" effects the proposal named. 19 context terms occur.
- **Fit.** The posterior mode is found by Newton's method with a Cholesky solve, exactly as in
  `ratings.fit`. Parameters are ordered α, β, context terms, then commanders. Without context terms
  the arithmetic is `ratings.fit`'s, term for term, and the results are identical
  (`tests/test_ratings_v4.py`). A context term or commander unseen in training predicts with 0.
- **Evidence.** The Laplace approximation to the log marginal likelihood is
  −objective(ŵ) + ½ Σ log(prior precision) − ½ log det H(ŵ); the 2π terms cancel. A unit test
  checks it against quadrature.
- **The τ grid.** 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.25 and 1.5.
  - τ-hat is the grid value with the highest mean log evidence over the imputations.
  - A tie goes to the smaller τ.
  - τ = 0 is the context model.

## 5. Multiple imputation

There are M = 20 imputations, drawn as in run 3 (grade E design §5) with seed 20261006. Every fold,
view and model uses the same imputed data sets.

## 6. The held-out test: the single verdict, pre-registered

Leave one campaign out over the 301 rows. In each fold, for each imputation:

- the context model and the commander model at every grid τ are fitted on the training rows;
- **τ-hat for the fold** is chosen from the training rows' evidence alone, by the §4 rule;
- the commander model's prediction for a held-out row is the mean, over the 20 imputations, of the
  τ-hat fit's predictions;
- the context model's prediction is the mean of its own fits.

**The difference.** For each row, d is the commander model's log loss minus the context model's. This
is the clipped log loss of every scored run. Its mean is taken battle-weighted and campaign-weighted.

**The rule.**

1. Resample the 108 campaigns with replacement 20,000 times (seed 20261008), using the floor-index
   percentile convention of `uncertainty.py`.
2. The commander model **improves** only if the bootstrap's 95th percentile of the mean difference is
   below zero under **both** weightings. That is a one-sided 95% bound on each.

**Reading the result.**

- **An improvement** reads only as "held-out log loss was lower than the context model's, beyond
  campaign-resampling noise, on these rows". It is not evidence of skill or of a causal effect.
- **Without an improvement:**
  - the report states that commander identity adds no detectable predictive signal beyond force size
    and context;
  - it gives no ordered ranking;
  - every estimate stays in the JSON, labelled `no_heldout_signal`.
- **Point improvement.** Whether both point differences are below zero (run 3's rule) is reported as
  `point_lower_both`. It does not decide anything.

## 7. Reported beside the verdict (descriptive, not part of it)

**Other held-out models.** Each comes from the same folds and imputations, and each comparison gets
the same bootstrap.

| Model | Description |
| --- | --- |
| Commander + context at τ = 0.5 | Run 3's convention with context |
| Commander, no context, τ = 0.5 | Run 3's model on run 4's rows |
| Strength only | Force size alone |

**Comparisons.** Every model is compared with the context model or with strength only.

**Bridge.** This is run 3's configuration on the v3 ledger:

- post-start sides at their ledger estimates;
- rule-5 commanders credited;
- no context;
- τ = 0.5;
- the v3 ledger's grade E without the pre-start view.

The commander model minus strength only, with its bootstrap, separates the ledger change from the
method changes.

**Leakage rows.** The verdict difference is recomputed without the rows that had a post-start side in
the ledger or a joint-command side, using the stored predictions (no refit).

**Concentration** (leave one commander out, stored predictions, no refit):

- each credited commander's share of the net gain;
- the difference after dropping each commander's rows;
- the difference and 95th percentiles after dropping the largest contributor.

**Other diagnostics.**

- **Sign test** over campaigns.
- **Monte Carlo check:** the difference on imputations 1–10 and 11–20.
- **Effective denominator:** held-out rows with a commander seen in another campaign.
- **Per-fold τ-hat.**

**τ on all rows.**

- **Profile.** The mean log evidence at each grid τ, relative to τ = 0, and τ-hat. Grid values within
  1.92 log units of the peak form an approximate 95% profile interval. The Laplace approximation and
  the boundary at zero make that interval approximate.
- **Calibration.** Outcomes are simulated 100 times (seed 20261009) from the context model's fitted
  probabilities, the mean over the first 5 imputations. That is a world with no commander differences.
  - Each simulation computes the largest mean log-evidence gain over the grid on those 5 imputations.
  - The observed gain on the same imputations is compared with them, giving p = (1 + count ≥
    observed) / 101.
  - A shuffled-outcome smoke test of the pipeline showed why this is needed: with no real signal, τ-hat
    can still land above zero.

**Temporal split.** Training on 1861–1863 and testing on 1864–1865, every model is fitted with τ-hat
chosen on the training years. It has no verdict.

## 8. Ratings

Pooled estimates follow run 3's method (grade E design §5), with these changes:

- **τ.** The commander model uses τ = τ-hat on all rows. If τ-hat is 0, it uses the 0.5 convention,
  labelled `tau_hat_zero_convention_0.5`.
- **Draws.** Imputation m draws its 1,000 Laplace draws per commander, and its joint rank draws, from
  `random.Random(20261007 + 1 + m)`.

Ranks, rank sets (two or more modelled battles), connectivity and prior dominance follow design §4.
Each commander also reports:

- **wins and losses** by the side they commanded in each row;
- **the residual sum** against the context model's held-out probability;
- **coverage:** every in-scope attribution, including those dropped as nested and the joint-command
  battles that were not credited.

## 9. Views

**Base.** Views run at the grade E medians, at the ratings' τ, unless stated. The single fit at the
medians is the reference view `median_imputation`.

**Robustness views.** These set `view_sensitive` and `unranked_in_view` by the rules of design §6:

- τ half and double the ratings' τ;
- κ = 0.25 and 1.0;
- α SD 3;
- grades A–B for command;
- superior directing;
- command changed (excluded, and successor credited);
- `joint_command_credited`;
- the four strength endpoints;
- one view per alternative candidate.

**Other views:**

- `tau_convention_0.5`;
- `no_context`;
- `strength_graded_only` (both sides A–C in the pre-start view);
- `no_post_start_rows`;
- `no_bound_conflict`;
- `no_naval_grade_e`;
- `drop_nesting_unresolved`;
- `outcome_only_all` (no force term);
- with multiple imputation (M = 20): `wide_imputation`, `train_graded_ab`, `all_bounds` and
  `ledger_echelon_joint`.

**Storage.** Run 3 copied every view into every commander, which made its output 40 MB. Run 4 stores
views compactly. For each commander with two or more modelled battles, each view keeps only these
numbers in a single table:

- θ;
- the 80% interval;
- the 80% rank interval.

## 10. A profile for each war

`generalship/frame.py` describes a war:

- its sides;
- how a frozen result maps to an outcome;
- the battle and campaign tables;
- the ledgers and registry;
- the grade E levels and reference levels;
- the temporal split.

`imputation_v2.py` and `ratings_v4.py` read the profile instead of Civil War constants. The commander
sign comes from each row, so a commander may command either side, as coalition wars need.

**Still Civil War–specific:**

- the strength-estimate engine and its checker;
- the command checker's rank orders;
- the ledger formats.

Runs 1–3 keep their own frozen code.

## 11. Outputs, checks and gate

**Outputs:**

- `make strength-imputation-v2` writes `artifacts/strength-imputation-v2.json`, with bindings.
- `make commander-ratings-v4` writes `artifacts/commander-ratings-v4.{json,md}`, verdict first. The
  output also records:
  - the Python version;
  - the hash of every bound file and module.

**Checks before the run.** The run refuses unless:

- the authorization binds every input and every module it executes, at their current hashes;
- both ledgers replay through their bound views;
- the grade E output rebuilds identically from the ledgers.

**Tests.** `tests/test_ratings_v4.py` and `tests/test_imputation_v2.py` cover:

- the fit's identity with run 3's;
- the evidence against quadrature;
- the attribution rules;
- that a held-out outcome cannot move its own prediction or its fold's τ-hat;
- the serial and parallel paths;
- the verdict rule and the scoring;
- the authorization gate;
- that the committed report regenerates from the committed output.

Model runs are not part of the tests.

Outputs never enter `artifacts/baseline.json`. The run admits no feature.

## 12. Limits

- **Not causal.** The rating is not command skill. Context terms absorb only when and where a battle
  was fought. Army quality, subordinates, opponents and supply stay in the residual.
- **Context is coarse.** It uses four theaters and three periods. A commander tied to one army can
  still carry that army's effect.
- **Approximations.** Laplace evidence and a grid τ are approximations. The calibration (§7) guards
  against reading a small τ-hat as a finding.
- **Selection.** Grade E fills gaps but does not remove selection: which sides are well documented
  depends on outcome, size and fame. Every result carries `whole_engagement_leakage`,
  `conditional_on_source_availability`, `not_causal` and `side_relative`, and `modelled_strength`
  where it applies.
- **Not blind.** The design was written after run 3's results were known. Its rule is fixed only
  against run 4's own numbers.
- **Not a review.** This is the primary's own verified work, not an independent review or historical
  adjudication.
