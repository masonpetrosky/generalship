# Commander residual ratings v3: all battles, with modelled strengths

Run 2026-09-25 under the reviewed [grade E design](../strength-imputation.md), which extends the
[commander-rating design](../commander-ratings.md) on the owner's decision that battles should
not be omitted for want of a reported strength and that the all-battles test is the single
verdict. This is an exploratory diagnostic, not a ranking of record, a measure of skill or a
causal estimate. The baseline is unchanged. **Status: separate review pending.**

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
rule 7 test; 15 are naval and 15 joint-command sides use an unknown echelon.

## The verdict: lower held-out log loss on all battles

301 battles in 108 campaigns; 162 have a modelled side and 17 a post-start side. Leave one
campaign out, probabilities averaged over 20 imputations.

| Model | Log loss, battle-weighted | Log loss, campaign-weighted |
| --- | ---: | ---: |
| Commander model | 0.6476 | 0.6586 |
| Strength only | 0.6597 | 0.6651 |

- Lower under both weightings, by 0.0121 and 0.0065. By the design's rule this is an improvement,
  read only as: held-out log loss was lower on these rows. It is not evidence of skill (design §5).
- Descriptive, not part of the verdict: the difference is the same on imputations 1–10 (−0.0122 /
  −0.0068) and 11–20 (−0.0120 / −0.0062); the commander model did better in 61 of 108 campaigns;
  243 of 301 held-out rows had a commander seen in another campaign; the 1861–1863→1864–1865
  split gives 0.6530 against 0.6606.
- The view `strength_graded_only` reproduces run 2's fit exactly.

## What the estimates look like

94 commanders have two or more modelled battles (52 US, 42 Confederate).

- **One 80% interval excludes zero:** Forrest, +0.62 (12 battles, 9–3; 80% +0.12 to +1.12). No 95%
  interval excludes zero. Posterior SDs are 0.73–0.96 of the prior's.
- **Confederate, by median rank:** Forrest, Beauregard (+0.54, 6–1), Jackson (+0.45, 6–2) lead;
  Hood (−0.43, 1–8), Wheeler (−0.39, 0–5) and Taylor (−0.32, 1–6) trail. Lee is +0.16 (18
  battles, 8–10).
- **US:** Grant leads (+0.51, 11 battles, 10–1; 80% −0.02 to +1.03), then Warren, Farragut and
  McNeil; Hancock (−0.51, 0–4), Gillmore and Butler trail. Sherman is −0.17 (10 battles, 5–5).
- **Ranks remain very uncertain.** Forrest's 80% rank interval is 1–19 of 42, Grant's 2–27 of 52;
  most span half the list or more. 19 of the 94 are `not_connected`.
- **Robustness.** No commander is `view_sensitive` across the robustness views.
- **The force term weakens.** The pooled force coefficient is 0.63, against 1.12 in run 2. Noisy
  modelled strengths attenuate it, which leaves more of each result to be attributed to commanders
  or the prior. This is a limit of the method, stated here, not a finding about force size.

## What this means

- **Filling the gaps did not remove the signal.** On all battles, with the uncertainty of modelled
  strengths carried through, commander identity again lowers held-out log loss under both
  weightings, by more than on the 126 well-sourced battles.
- **It is still not a ranking of skill.** The residual includes army quality, subordinates, theater,
  opponents, coding choices and the typical-size model's errors; the ledgers are reviewed
  estimates, not adjudication, and extraction was not blind.
- **Individual places are uncertain.** Rank intervals overlap widely; the report's order is a point
  summary under the design.

## Limits

- Grade E is a typical size, not an observation; it can pull unusual forces toward the typical,
  and it borrows strength across engagements.
- Every result carries `whole_engagement_leakage`, `conditional_on_source_availability`,
  `not_causal`, `side_relative` and, where used, `modelled_strength`.
- The twelve records with a Native American belligerent remain outside the two-sided model.
- A separate AI review of the code and results is pending; it is not human historical
  adjudication.
