# Commander residual ratings v3: all battles, with modelled strengths

Run 2026-09-25 under the reviewed [grade E design](../strength-imputation.md), which extends the
[commander-rating design](../commander-ratings.md) on the owner's decision that battles should
not be omitted for want of a reported strength and that the all-battles test is the single
verdict. This is an exploratory diagnostic, not a ranking of record, a measure of skill or a
causal estimate. The baseline is unchanged. **Status: separately reviewed
([review](../../artifacts/review-results/ratings-v3-review-e1e0784-opus-high-v1/review.md)); its five
required corrections are applied.**

## Authorization

The owner authorized the run for the exact files named in the question: "You're good to run it"
([record](../../data/command/rating-authorization-v3.json)). The run refuses to start unless the
design (`15bdb6a2…`), the grade E output (`f798faf3…`), both v2 ledgers (`7855d4d3…`,
`495cef30…`), the registry (`91fc2526…`) and the campaign table (`93813220…`) match. Code
`82901a9`; `make commander-ratings-v3`; outputs `artifacts/commander-ratings-v3.{json,md}`.

## Grade E

`artifacts/strength-imputation-v1.json` fills the 262 grade D sides with a typical-size model
(command echelon, side, period, theater) fitted on 328 sides with reported counts. Calibration
widened σ by k = 1.08 (leave-one-out 80% coverage 0.78 before, 0.80 after; 0.80 leave one campaign
out); the median absolute error is 0.67 on the log scale, about a factor of two. 70 sides are
clipped by an applicable lower bound and 11 by an upper bound; 63 had a bound set aside under the
rule 7 test; 15 are naval and 15 joint-command sides use an unknown echelon. (Design §2 counts 3
`flotilla` training rows by ledger echelon; the output records 2, because one is a joint-command
side coded `unknown`. Both merge into `unknown`, so the fit is unaffected.)

## The verdict: lower held-out log loss on all battles

301 battles in 108 campaigns; 162 have a modelled side and 17 a post-start side. Leave one
campaign out, probabilities averaged over 20 imputations.

| Model | Log loss, battle-weighted | Log loss, campaign-weighted |
| --- | ---: | ---: |
| Commander model | 0.6476 | 0.6586 |
| Strength only | 0.6597 | 0.6651 |

- Lower under both weightings, by 0.0121 and 0.0065. By the design's rule this is an improvement,
  read only as: held-out log loss was lower on these rows. It is not evidence of skill (design §5).
- Descriptive, not part of the verdict: the difference is similar on imputations 1–10 (−0.0122 /
  −0.0068) and 11–20 (−0.0120 / −0.0062); the commander model did better in 61 of 108 campaigns;
  243 of 301 held-out rows had a commander seen in another campaign; the 1861–1863→1864–1865
  split gives 0.6530 against 0.6606.
- The view `strength_graded_only` reproduces run 2's fit exactly.

## What the estimates look like

94 commanders have two or more modelled battles (52 US, 42 Confederate).

- **One 80% interval excludes zero:** Forrest, +0.62 (12 battles, 9–3; 80% +0.12 to +1.12). No 95%
  interval excludes zero. Posterior SDs are 0.73–0.96 of the prior's.
- **Confederate, by median rank:** Forrest, Beauregard (+0.54, 6–1) and Jackson (+0.45, 6–2) are
  listed first; Hood (−0.43, 1–8), Wheeler (−0.39, 0–5) and Taylor (−0.32, 1–6) last. Lee is +0.16 (18
  battles, 8–10).
- **US:** Grant is listed first (+0.51, 11 battles, 10–1; 80% −0.02 to +1.03), then Warren,
  Farragut and McNeil; Hancock (−0.51, 0–4), Gillmore and Butler last. Sherman is −0.17 (10 battles, 5–5).
- **Ranks remain very uncertain.** Forrest's 80% rank interval is 1–19 of 42, Grant's 2–27 of 52;
  most span half the list or more. 19 of the 94 are `not_connected`: they share no component with another ranked commander of their side, so their place relative to that side's other commanders rests on α, β and the prior, not on shared opponents (design §4).
- **Robustness.** No commander is `view_sensitive` across the robustness views; 34 of the 94 are `unranked_in_view` in at least one of them.
- **The force term weakens.** The pooled force coefficient is 0.63 on the 301 rows, against 1.12 on
  run 2's 126 rows (reproduced by `strength_graded_only`). On the same 301 rows it is 0.86 with grade
  E sides at their medians (`median_imputation`) and 0.43 when the imputation SD is doubled
  (`wide_imputation`), which is consistent with noisy modelled strengths attenuating it; the fall
  from 1.12 to 0.86 also changes the rows and is not isolated. A weaker force term may leave more of
  each result to commanders or the prior; no view tests this. This is a limit of the method, not a
  finding about force size.

## What this means

- **Filling the gaps did not remove the improvement.** On all battles, with the uncertainty of
  modelled strengths carried through, the commander model again had lower held-out log loss under
  both weightings (by 0.0121 and 0.0065, against 0.0093 and 0.0049 in run 2). The two runs differ in
  rows, folds and the size of the force term, so the sizes are not directly comparable, and neither
  is evidence of skill. Descriptively (from the stored predictions), the improvement is not
  concentrated on rows with a modelled side (−0.0086 there, −0.0153 on run 2's rows), though that
  does not rule out commander terms absorbing mismeasured force.
- **It is still not a ranking of skill.** The residual includes army quality, subordinates, theater,
  opponents, coding choices and the typical-size model's errors; the ledgers are reviewed
  estimates, not adjudication, and extraction was not blind.
- **Individual places are uncertain.** Rank intervals overlap widely; the report's order is a point
  summary under the design.

## Limits

- Grade E is a typical size, not an observation; it can pull unusual forces toward the typical,
  and it borrows strength across engagements.
- Grade E fills gaps but does not remove selection: which battles and sides are well documented
  still depends on outcome, size and fame (design §8). Descriptively, grade D sides won 134 and lost
  128; graded sides won 171 and lost 177 (`selection_descriptive`).
- Every result carries `whole_engagement_leakage`, `conditional_on_source_availability`,
  `not_causal`, `side_relative` and, where used, `modelled_strength`.
- The twelve records with a Native American belligerent remain outside the two-sided model.
- The separate review is an AI review, not human historical adjudication.
