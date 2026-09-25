# Modelled side strength (grade E) and the all-battles rating test

Status: **accepted for implementation after separate review**, 2026-09-25
([review](../artifacts/review-results/imputation-design-2779bb6-opus-high-v1/review.md); all eight
required corrections applied). Nothing here has been run. This design extends the accepted
[best-estimate strength design](strength-estimates.md) and the
[commander residual-rating design](commander-ratings.md) under the owner's decision of 2026-09-25
([record](../data/estimates/owner-decision-grade-e-2026-09-25.json)):

> "I don't think we should be omitting battles. Can't we estimate troop strength?" … "I think we
> should replace the test, right? If we use this standard, we're going to have like 0 ancient
> battles that can meet the standard."

The owner chose to replace the test after run 2's verdict was known, over the author's recommended
option of adding a second test. The reviewed v2 ledgers, run 2 of the ratings and its record are
unchanged. Every choice below is fixed before any grade E value or rating is computed.

**What this supersedes.** For grade E outputs and rating run 3 only, this design supersedes
strength-estimates §4 rule 8 ("There is no imputation") and the §8 non-goals "No imputation for
grade D" and "No borrowing of strengths across engagements", and commander-ratings §3's primary row
set, §5's verdict configuration and §4's statement that intervals leave out strength uncertainty.
The ledgers still record these sides as grade D; grade E lives only in
`artifacts/strength-imputation-v1.json`. Run 2's verdict remains the record of run 2 and is not
re-scored.

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
`post_start_information` label, on both ledgers' 305 in-scope engagements. No outcome enters. The
response mixes bases (engaged, effective, present for duty, present) and includes opponent-only
points under the ledger's declared conventions; a view trains on A–B sides only (§6). The model is
calibrated on sides that had a reported count, so its coverage on grade D sides is an assumption.

**Response.** The natural log of that point.

**Predictors** (all fixed now, all available without the outcome):

- **Echelon** of the side's responsible command, from the v2 command ledger (`army`,
  `corps_or_wing`, `division`, `brigade`, `regiment`, `detachment_or_post`, `flotilla`, `unknown`).
  A side with no chosen commander uses its ledger echelon as recorded. A side labelled
  `joint_command` uses `unknown`, in training and in imputation, because commander-ratings §2 rule 5
  chooses its commander by the force that compelled the result; such a grade E side is labelled
  `joint_command_echelon_unknown`.
- **Side**: US or Confederate.
- **Period**: 1861–1862, 1863, 1864–1865, from the frozen start date.
- **Theater**: the campaign theater in the frozen `data/raw/cwsac_campaigns.csv` (Eastern, Western,
  Trans-Mississippi, Lower Seaboard, Pacific Coast).

Any level of any predictor with fewer than five training rows is merged: echelon levels into
`unknown`, and a theater or period level into the adjacent level named in the output. On the v2
ledgers this merges `regiment` (1 training row) and `flotilla` (3) into `unknown`; no theater or
period level merges (Pacific Coast has no in-scope engagement). Every merge and its training count
is recorded in the output. A grade E side whose ledger echelon is `flotilla` is modelled as a land
side of unknown echelon, which is not evidence about crew size; it is labelled `naval_side`.

**Fit.** Minimize Σ residual² + 1.0 × Σ (non-intercept coefficient)², with indicator columns for
every non-reference level after merges (reference levels `unknown`, US, 1863, Eastern). σ is the
root mean squared residual scaled by √(n / (n − p)), where p is the number of columns including the
intercept. The model is fitted once, on all training rows; it is not refitted within the §5 folds
(it uses no outcome).

**Calibration, fixed in advance.** Leave-one-out over the training rows: refit without row i and
score it against N(μ₋ᵢ, σ₋ᵢ²). Let c be the share of held-out log points inside the central 80% of
their predictive normal. If c < 0.80, σ is multiplied by the smallest k on the grid 1.00, 1.01, …
for which the leave-one-out share inside the central 80% of N(μ₋ᵢ, (kσ₋ᵢ)²) is at least 0.80. σ is
never shrunk (k = 1 if c ≥ 0.80). The output reports c, k, the leave-one-out median absolute log
error overall and by echelon, and, descriptively, the leave-one-campaign-out 80% coverage at k.

**Bounds.** A grade D side's input constrains its distribution only if its `bound` is `lower` or
`upper` and, apart from its `one_sided_bound`, `partial_scope` or `partial_interval` codes, it
would be class A or B under strength-estimates §3 (the eligibility test of §4 rule 7). The
`point_basis` condition of rule 7 is not applied, because a grade D side has no point basis and the
response mixes bases. A bound's value is its printed value (the midpoint of a printed range, as
`printed_value` in `generalship/estimates.py`). L is the largest applicable lower bound and U the
smallest applicable upper bound, in people. A lower bound coded `partial_scope` or
`partial_interval` is still a lower bound on the whole side. Inputs with `bound: null`, bound
inputs that fail the eligibility test (opponent or hearsay, post-start, applicability unresolved),
and class A–C or unusable inputs of a grade D side are not used. Each is listed in the output with
its reason, and the side is labelled `bound_not_applied` when any directional bound was set aside.
No grade E value uses post-start information.

**Predictive distribution.** For a grade E side, log strength ~ N(μ, (kσ)²) truncated to
[log L, log U] where given. If L > U (a conflict between applicable bounds), neither bound is
applied and the side is labelled `bound_conflict`. If the truncation interval has probability below
1e-12 under N(μ, (kσ)²), the side is placed at the nearer bound (point, low and high all equal to
it) and labelled `bound_dominates`.

**Point and range.** The point is the median of the truncated distribution; the range is its 10th
to 90th percentiles; all three are rounded to 10 (halves up; floor 10), as the ledger rounds.
Labels: `modelled_estimate`, `echelon_basis`, and `bounded_lower`, `bounded_upper`,
`bound_not_applied`, `bound_conflict`, `bound_dominates`, `naval_side` or
`joint_command_echelon_unknown` where they apply.

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
rounding); sides graded A–C keep their ledger point. Draws use one `random.Random(20260926)`
stream, taken in the order imputation m = 1…20, then grade E sides sorted by battle ID and side (US
before Confederate). A draw is Φ⁻¹(Φ(a) + u(Φ(b) − Φ(a))) on the standardized truncation limits
a, b (−∞/+∞ where absent), with `statistics.NormalDist`; a `bound_dominates` side takes its fixed
value. The same M imputed data sets are used in every fold, view and model. The force feature is
unchanged: x = (US − CS)/(US + CS) on each imputation's strengths (`advantage` in
`generalship/baseline.py`).

**Estimates.** In each imputation the model is fitted as in run 2. The reported pooled point
estimate of θ is the mean of the M modes (it is not a mode); the 80% and 95% intervals and the rank
intervals come from pooling an equal number of Laplace draws from each imputation (20,000 in all,
1,000 per imputation).

**Held-out test (the single verdict).** Leave one campaign out over the all-battles rows. In each
fold and imputation both models (commander, strength-only) are fitted on the training rows and
predict the held-out rows; each held-out row's probability is the mean over the M imputations. Log
loss is computed on those averaged probabilities, battle-weighted and campaign-weighted. The
commander model **improves** only if its log loss is strictly lower under both weightings. The
reading is as in design §5: "held-out log loss was lower on these rows", not evidence of skill.
Without an improvement the report gives no ordered ranking.

The effective denominator (held-out rows with a commander seen in another campaign) is reported,
as before. Descriptively and outside the verdict, the output also reports the two log-loss
differences recomputed on imputations 1–10 and 11–20 (a Monte Carlo check), the campaigns where
each model did better, and a temporal split (1861–1863 train, 1864–1865 test).

## 6. Views (declared now; none changes the verdict)

Run on the grade E points (one imputation at the medians), except where stated. That
single-imputation fit on the 301 rows is reported as the view `median_imputation`, and it is the
reference for `view_sensitive` and `unranked_in_view` in the robustness views.

- **Robustness views:** every run-2 robustness view (τ 0.25 and 1.0, α sd 3, grades A–B for
  command, superior, command-changed excluded and successor, alternative candidates), and the four
  endpoint refits, with each A–C side at its ledger `low` or `high` and each grade E side at its
  10th or 90th percentile;
- `strength_graded_only`: the run-2 rows only (both sides A–C, no post-start); it must reproduce
  run 2's primary fit, and the report states whether it does;
- `no_post_start`: drops rows with a `post_start_information` side;
- `no_bound_conflict`: drops rows with a `bound_conflict` side;
- `no_naval_grade_e`: drops rows with a grade E side labelled `naval_side`;
- `train_graded_ab`: multiple imputation (M = 20, same seed) with the grade E model trained on
  sides graded A–B only;
- `wide_imputation`: multiple imputation (M = 20, same seed) with the predictive SD doubled;
- `all_bounds`: multiple imputation (M = 20, same seed) in which every recorded `lower` or `upper`
  bound of a grade D side is applied, whatever its class; sides whose applied bounds include a §3
  row 3 input carry `post_start_information`;
- `ledger_echelon_joint`: multiple imputation (M = 20, same seed) using the ledger echelon for
  `joint_command` sides;
- `drop_nesting_unresolved`: drops each unresolved contained record (TN035);
- `outcome_only_all`: no force term, as in run 2.

`view_sensitive` and `unranked_in_view` follow design §6 over the robustness views, compared with
`median_imputation`. The other views are reported beside the primary with their differences and do
not set `view_sensitive`.

## 7. Outputs and checks

- `artifacts/strength-imputation-v1.json`: the fitted model (coefficients, σ, k, merges, training
  counts, leave-one-out statistics overall and by echelon, leave-one-campaign-out coverage), a
  composition table (training and grade D rows by echelon, period, theater and side), a fixed
  descriptive table of grade D status against the recorded result, and every grade E side with its
  inputs, applied and set-aside bounds (with reasons), point, range and labels.
- `artifacts/commander-ratings-v3.{json,md}`: the run, with the verdict first.
- The per-commander sum of outcome minus p uses, for p, the §5 held-out strength-only probability
  averaged over the M imputations.
- An offline checker reproduces the imputation from the reviewed ledgers and frozen tables.
- A separate Claude Opus 5.5 `high` review checks the code and results after the run.

## 8. Limits

- Grade E is a model of typical force size given command level, side, period and theater. It is not
  evidence about the particular battle beyond its bounds, and it pulls unusual forces toward the
  typical. Its wide ranges are carried into the ratings, but a biased model would still bias the
  force feature.
- Grade E borrows strength across engagements: each value is a typical size for sides that had a
  reported count, not an observation of this side. It is not an estimate-layer entry, not an
  admitted feature and not historical adjudication.
- The training and grade D sides differ in composition (for example more corps and more 1864–65
  sides among grade D); the output reports the table.
- Echelon is itself an extraction judgment; `unknown` sides get the least specific estimate.
- Which battles are well documented still depends on outcome, size and fame; grade E fills the gaps
  but cannot remove that selection.
- The predictors are specific to this war and its CWSAC listings. A sparser era needs its own
  predictors, reference levels and training rows. With few reported counts, such a model has little
  to learn from and its ranges will be wide; this design does not show that it transfers.
- Every result keeps the flags `whole_engagement_leakage`, `conditional_on_source_availability`,
  `not_causal` and `side_relative`, plus `modelled_strength` on rows with a grade E side.

## 9. Authorization

The run needs the owner's authorization naming the hashes of this design, the imputation output,
both v2 ledgers, the registry and `data/raw/cwsac_campaigns.csv`.
