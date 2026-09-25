# Modelled side strength (grade E) and the all-battles rating test

Status: **draft for separate review**, 2026-09-25. Nothing here has been run. This design extends
the accepted [best-estimate strength design](strength-estimates.md) and the
[commander residual-rating design](commander-ratings.md) under the owner's decision of 2026-09-25
([record](../data/estimates/owner-decision-grade-e-2026-09-25.json)):

> "I don't think we should be omitting battles. Can't we estimate troop strength?" … "I think we
> should replace the test, right? If we use this standard, we're going to have like 0 ancient
> battles that can meet the standard."

The reviewed v2 ledgers, run 2 of the ratings and its record are unchanged. Every choice below is
fixed before any grade E value or rating is computed.

## 1. Why

Run 2 used only the 126 of 305 in-scope engagements with both strength sides graded A–C and no
post-start side. 262 sides are grade D: 88 have only a lower bound, 16 a lower and an upper bound,
9 only an upper bound, 85 only formation names ("Three divisions", "IV Corps"), 8 only unusable
inputs and 56 nothing. Dropping those battles discards most of the war, and a standard that needs a
reported count for both sides would admit almost no ancient battle. Grade E replaces the blank with
a modelled estimate whose range states how little is known.

## 2. Grade E: the model

**Which sides.** Every side of an in-scope engagement whose ledger grade is D. Sides graded A–C
keep their ledger estimate unchanged, including post-start sides (§4).

**Training data.** The ledger point of every side graded A–C that carries no
`post_start_information` label, on both ledgers' 305 in-scope engagements. No outcome enters.

**Response.** The natural log of that point.

**Predictors** (all fixed now, all available without the outcome):

- **Echelon** of the side's responsible command, from the v2 command ledger (`army`,
  `corps_or_wing`, `division`, `brigade`, `regiment`, `detachment_or_post`, `flotilla`,
  `unknown`). A side with no chosen commander uses its ledger echelon as recorded.
- **Side**: US or Confederate.
- **Period**: 1861–1862, 1863, 1864–1865, from the frozen start date.
- **Theater**: the frozen CWSAC campaign theater (Eastern, Western, Trans-Mississippi, Lower
  Seaboard; Pacific Coast merges with Trans-Mississippi, as it has too few rows).

Levels with fewer than five training rows are merged into `unknown` for echelon (so `regiment`
merges), and the merge is recorded in the output.

**Fit.** Ordinary least squares with a ridge penalty of 1.0 on every coefficient except the
intercept (predictors are indicator columns; the reference levels are `unknown`, US, 1863 and
Eastern). The residual standard deviation σ is the root mean squared residual scaled by
√(n / (n − p)).

**Calibration, fixed in advance.** Leave-one-out over the training rows (refit without each row;
predict it). Let c be the share of held-out log points inside the central 80% of their predictive
normal N(μ, σ²). If c < 0.80, σ is multiplied by the factor k ≥ 1 that makes the leave-one-out 80%
coverage 0.80 (smallest such k on a grid of 0.01). σ is never shrunk. The LOO median absolute log
error, c and k are reported.

**Bounds.** Each grade D side's ledger inputs of class `bound` constrain its distribution: the
largest lower bound L and the smallest upper bound U (in people; one-sided bounds only). A lower
bound coded `partial_scope` or `partial_interval` is still a lower bound on the whole side.

**Predictive distribution.** For a grade E side, log strength ~ N(μ, (kσ)²) truncated to
[log L, log U] where given. If L > U (a `bound_conflict`), the truncation uses [log U, log L]
(both bounds kept as the range) and the side carries `bound_conflict`.

**Point and range.** The point is the median of the truncated distribution; the range is its 10th
to 90th percentiles; all three are rounded to 10 (halves up; floor 10), as the ledger rounds.
Labels: `modelled_estimate`, `echelon_basis`, and `bounded_lower`, `bounded_upper` or
`bound_conflict` where they apply. Grade E carries every row flag of §4.

**Not used.** Casualty figures (they depend on the outcome), recorded results, reputation, and any
source outside the reviewed ledgers and the frozen CWSAC tables. Formation counts in free text are
not parsed; the echelon carries the size information.

## 3. Rows

The all-battles set is every in-scope engagement of cohort v2 (305) less the contained records of
pairs recorded `nested` (rule 7): GA012, LA009, VA033 and VA034, so 301 rows. Pairs recorded
`nesting_unresolved` keep both records, with a view that drops the contained one (§6).

## 4. Post-start sides

Sides graded A–C with `post_start_information` keep their ledger estimate and the row enters the
all-battles set with the label `post_start_information`. A view drops those rows (§6).

## 5. The rating model and the verdict (replaces design §5's row set)

The rating model, priors (τ = 0.5), attribution, Laplace approximation and rank method of
`docs/commander-ratings.md` §§3–4 are unchanged. What changes is the row set and how grade E
uncertainty is carried.

**Multiple imputation.** M = 20 imputations, seed 20260926. In imputation m, each grade E side's
strength is a draw from its truncated predictive distribution (log scale, then exponentiated; no
rounding); sides graded A–C keep their ledger point. The force feature x is the same log-ratio as
before.

**Estimates.** In each imputation the model is fitted as in run 2. The reported θ mode is the mean
of the M modes; the 80% and 95% intervals and the rank intervals come from pooling an equal number
of Laplace draws from each imputation (20,000 in all, 1,000 per imputation).

**Held-out test (the single verdict).** Leave one campaign out over the all-battles rows. In each
fold and imputation both models (commander, strength-only) are fitted on the training rows and
predict the held-out rows; each held-out row's probability is the mean over the M imputations.
Log loss is computed on those averaged probabilities, battle-weighted and campaign-weighted. The
commander model **improves** only if its log loss is strictly lower under both weightings. The
reading is as in design §5: "held-out log loss was lower on these rows", not evidence of skill.
Without an improvement the report gives no ordered ranking.

The effective denominator (held-out rows with a commander seen in another campaign) is reported,
as before. A descriptive temporal split (1861–1863 train, 1864–1865 test) is reported with no
verdict.

## 6. Views (declared now; none changes the verdict)

Run on the grade E points (one imputation at the medians), except where stated:

- every run-2 robustness view (τ 0.25 and 1.0, α sd 3, grades A–B for command, superior,
  command-changed excluded and successor, alternative candidates);
- `strength_graded_only`: the run-2 rows only (both sides A–C, no post-start), as a comparison;
- `no_post_start`: drops rows with a `post_start_information` side;
- `no_bound_conflict`: drops rows with a `bound_conflict` side;
- `wide_imputation`: multiple imputation with the predictive SD doubled (M = 20);
- `drop_nesting_unresolved`: drops each unresolved contained record (TN035);
- `outcome_only_all`: no force term, as in run 2.

`view_sensitive` and `unranked_in_view` follow design §6 over the robustness views.

## 7. Outputs and checks

- `artifacts/strength-imputation-v1.json`: the fitted model (coefficients, σ, k, merges, LOO
  statistics) and every grade E side with its inputs, bounds, point, range and labels.
- `artifacts/commander-ratings-v3.{json,md}`: the run, with the verdict first.
- An offline checker reproduces the imputation from the reviewed ledgers and frozen tables.
- A separate Claude Opus 5.5 `high` review checks this design before implementation, and the
  code and results after the run.

## 8. Limits

- Grade E is a model of typical force size given command level, side, period and theater. It is
  not evidence about the particular battle beyond its bounds, and it pulls unusual forces toward
  the typical. Its wide ranges are carried into the ratings, but a biased model would still bias
  the force feature.
- Echelon is itself an extraction judgment; `unknown` sides get the least specific estimate.
- Which battles are well documented still depends on outcome, size and fame; grade E fills the
  gaps but cannot remove that selection.
- Every result keeps the flags `whole_engagement_leakage`, `conditional_on_source_availability`,
  `not_causal` and `side_relative`, plus `modelled_strength` on rows with a grade E side.

## 9. Authorization

The run needs the owner's authorization naming the hashes of this design (after review), the
imputation output, both v2 ledgers and the registry.
