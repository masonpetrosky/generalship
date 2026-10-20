# Napoleonic temporal probability-correction run v1

Primary-verified. The owner authorized the exact frozen proposal. No separate review occurred.

**The correction fails the fixed exploratory continuation rule. Retain the uncorrected force baseline and close this correction branch.** In the main 1808–1812 region, corrected log loss is 0.663652 versus 0.632991 for expanding force, and Brier is 0.234834 versus 0.223525 (battle weighted; lower is better). Equal-campaign scores and the unqualified-total sensitivity also worsen. Only two of five decision years improve in log loss. The reused 1813 scores improve but cannot affect or rescue the decision.

This is an exploratory prediction of compiler records, not a commander, tactical or campaign-contribution effect. No feature is admitted and all 52 final entries remain unused numerically.

## Fixed scope, coverage and method

The [frozen design](../napoleonic-temporal-calibration-v1.md), [protocol](../../data/napoleonic/temporal-calibration-v1/protocol.json) and [complete plan](../../artifacts/napoleonic-temporal-calibration-plan-v1.md) remain unchanged. Their preparation-only status records the earlier task; the later actual authorization is a separate record. All 273 development entries / 13 source groups remain in the denominator. No source, dossier, outcome, personnel total, original grouping or exclusion is changed.

| Population | Eligible / 273 | Warmup eligible / 68 | Main scored / 141 | Main excluded | Secondary scored / 64 | Secondary excluded |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| primary | 194 | 42 | 115 | 26 | 37 | 27 |
| exclude_indecisive | 194 | 42 | 115 | 26 | 37 | 27 |
| exclude_no_combat | 193 | 41 | 115 | 26 | 37 | 27 |
| unqualified_totals | 163 | 30 | 103 | 38 | 30 | 34 |

The 1805–1807 warmup has no outer predictions. Main scores use five annual folds/seven source groups; secondary 1813 uses one annual fold/two groups. The primary 273-entry denominator is 68 warmup + 141 main + 64 secondary. Printed-indecisive exclusion is a no-op; non-combat exclusion removes one warmup row, which can change later training fits. Unqualified totals screen approximate figures or numeric notes anywhere in the cited passage; this does not adjudicate a note’s applicability.

Each target year uses only whole groups ending before January 1. The base contains earlier completed groups; calibration contains all groups in the latest available completion year. Every base group must finish before every calibration member starts. Availability uses every member, including numerically excluded rows. Unknown dates, overlap or fewer than ten eligible rows in either training block cause no score and no fallback. Original roles/exclusions and controlling entry/date locators remain in the plan.

One ridge-1 force fit on base rows uses `(A-B)/(A+B)`, with A = France and its allies. Its intercept and slope stay frozen while one ridge-1 logit offset is fitted on the disjoint calibration block. Comparators are that same base with zero offset, force refitted on base plus calibration, Laplace priors on expanding/recent training labels, and equal odds. No penalty, time window or model is selected after the result. Within each fold the offset retains the same base ordering.

## All fixed population and model scores

Lower is better; log loss uses natural logarithms. Battle weighting gives each scored entry equal weight. Equal-campaign weighting averages the original source-group means within the stated region. Each model uses exactly the same test rows in a population. Cross-population differences are not paired effects of qualifiers.

### Main: 1808–1812

| Population | Model | Log loss, battle | Brier, battle | Log loss, campaign | Brier, campaign |
| --- | --- | ---: | ---: | ---: | ---: |
| primary | offset_force | 0.663652 | 0.234834 | 0.638446 | 0.224999 |
| primary | same_base_force | 0.650751 | 0.228249 | 0.638678 | 0.222543 |
| primary | expanding_force | 0.632991 | 0.223525 | 0.623785 | 0.220290 |
| primary | expanding_prior | 0.746519 | 0.265311 | 0.698610 | 0.245438 |
| primary | recent_prior | 0.753157 | 0.263927 | 0.705749 | 0.245509 |
| primary | equal_odds | 0.693147 | 0.250000 | 0.693147 | 0.250000 |
| exclude_indecisive | offset_force | 0.663652 | 0.234834 | 0.638446 | 0.224999 |
| exclude_indecisive | same_base_force | 0.650751 | 0.228249 | 0.638678 | 0.222543 |
| exclude_indecisive | expanding_force | 0.632991 | 0.223525 | 0.623785 | 0.220290 |
| exclude_indecisive | expanding_prior | 0.746519 | 0.265311 | 0.698610 | 0.245438 |
| exclude_indecisive | recent_prior | 0.753157 | 0.263927 | 0.705749 | 0.245509 |
| exclude_indecisive | equal_odds | 0.693147 | 0.250000 | 0.693147 | 0.250000 |
| exclude_no_combat | offset_force | 0.661276 | 0.234005 | 0.636615 | 0.224318 |
| exclude_no_combat | same_base_force | 0.649338 | 0.227773 | 0.637165 | 0.222052 |
| exclude_no_combat | expanding_force | 0.631916 | 0.223100 | 0.622846 | 0.219908 |
| exclude_no_combat | expanding_prior | 0.742808 | 0.264203 | 0.695904 | 0.244624 |
| exclude_no_combat | recent_prior | 0.748475 | 0.262829 | 0.702359 | 0.244715 |
| exclude_no_combat | equal_odds | 0.693147 | 0.250000 | 0.693147 | 0.250000 |
| unqualified_totals | offset_force | 0.684243 | 0.242121 | 0.654524 | 0.230105 |
| unqualified_totals | same_base_force | 0.681214 | 0.240580 | 0.662220 | 0.232078 |
| unqualified_totals | expanding_force | 0.653679 | 0.232354 | 0.636769 | 0.225408 |
| unqualified_totals | expanding_prior | 0.737278 | 0.261801 | 0.697999 | 0.245411 |
| unqualified_totals | recent_prior | 0.785404 | 0.267613 | 0.735651 | 0.250286 |
| unqualified_totals | equal_odds | 0.693147 | 0.250000 | 0.693147 | 0.250000 |

### Secondary: reused 1813

| Population | Model | Log loss, battle | Brier, battle | Log loss, campaign | Brier, campaign |
| --- | --- | ---: | ---: | ---: | ---: |
| primary | offset_force | 0.601049 | 0.207721 | 0.618066 | 0.216606 |
| primary | same_base_force | 0.757658 | 0.281451 | 0.765794 | 0.284848 |
| primary | expanding_force | 0.691122 | 0.251057 | 0.702117 | 0.256359 |
| primary | expanding_prior | 0.873458 | 0.335418 | 0.867033 | 0.332348 |
| primary | recent_prior | 0.763015 | 0.284516 | 0.759924 | 0.282987 |
| primary | equal_odds | 0.693147 | 0.250000 | 0.693147 | 0.250000 |
| exclude_indecisive | offset_force | 0.601049 | 0.207721 | 0.618066 | 0.216606 |
| exclude_indecisive | same_base_force | 0.757658 | 0.281451 | 0.765794 | 0.284848 |
| exclude_indecisive | expanding_force | 0.691122 | 0.251057 | 0.702117 | 0.256359 |
| exclude_indecisive | expanding_prior | 0.873458 | 0.335418 | 0.867033 | 0.332348 |
| exclude_indecisive | recent_prior | 0.763015 | 0.284516 | 0.759924 | 0.282987 |
| exclude_indecisive | equal_odds | 0.693147 | 0.250000 | 0.693147 | 0.250000 |
| exclude_no_combat | offset_force | 0.601762 | 0.208020 | 0.618618 | 0.216816 |
| exclude_no_combat | same_base_force | 0.756243 | 0.280857 | 0.764335 | 0.284241 |
| exclude_no_combat | expanding_force | 0.690395 | 0.250710 | 0.701338 | 0.255988 |
| exclude_no_combat | expanding_prior | 0.870417 | 0.334091 | 0.864072 | 0.331056 |
| exclude_no_combat | recent_prior | 0.763015 | 0.284516 | 0.759924 | 0.282987 |
| exclude_no_combat | equal_odds | 0.693147 | 0.250000 | 0.693147 | 0.250000 |
| unqualified_totals | offset_force | 0.619713 | 0.215715 | 0.628251 | 0.220440 |
| unqualified_totals | same_base_force | 0.810186 | 0.304581 | 0.794778 | 0.296962 |
| unqualified_totals | expanding_force | 0.716775 | 0.262276 | 0.711471 | 0.259889 |
| unqualified_totals | expanding_prior | 0.878862 | 0.338326 | 0.854790 | 0.326794 |
| unqualified_totals | recent_prior | 0.748699 | 0.277586 | 0.739547 | 0.273039 |
| unqualified_totals | equal_odds | 0.693147 | 0.250000 | 0.693147 | 0.250000 |

The secondary primary correction improves battle-weighted log loss from 0.691122 to 0.601049 and Brier from 0.251057 to 0.207721 against expanding force. These cases motivated the test and were already inspected. They are neither a fresh validation set nor a reason to override the main failure. The 1813 expanding probabilities match the original saved benchmark within absolute tolerance 2e-12 in every population. Its earlier forward report treated the whole year as one held-out group; this report’s equal-campaign view instead gives its two original source groups equal weight, so those aggregate scores differ.

## Fixed continuation decision

Candidate minus comparator: negative favors correction. Primary comparisons require strictly lower log loss and nonhigher Brier under both weightings; the sensitivity permits no worsening of either. Absolute decision tolerance is 1e-12.

| Population | Weighting | Comparator | Log-loss difference | Brier difference | Satisfied |
| --- | --- | --- | ---: | ---: | --- |
| primary | battle | same_base_force | +0.012902 | +0.006585 | no |
| primary | battle | expanding_force | +0.030662 | +0.011309 | no |
| primary | battle | expanding_prior | -0.082866 | -0.030476 | yes |
| primary | battle | recent_prior | -0.089505 | -0.029092 | yes |
| primary | battle | equal_odds | -0.029495 | -0.015166 | yes |
| unqualified_totals | battle | expanding_force | +0.030565 | +0.009767 | no |
| primary | equal_campaign | same_base_force | -0.000232 | +0.002456 | no |
| primary | equal_campaign | expanding_force | +0.014661 | +0.004709 | no |
| primary | equal_campaign | expanding_prior | -0.060163 | -0.020439 | yes |
| primary | equal_campaign | recent_prior | -0.067302 | -0.020511 | yes |
| primary | equal_campaign | equal_odds | -0.054701 | -0.025001 | yes |
| unqualified_totals | equal_campaign | expanding_force | +0.017756 | +0.004697 | no |

The primary correction fails against both force comparators under battle weighting. Against the same base, equal-campaign log loss improves by only 0.000232 while Brier worsens by 0.002456; that comparison also fails. Against expanding force, both scores worsen under equal-campaign weighting, and the unqualified-total veto fails under both weightings. Primary log loss improves against expanding force in **1810 and 1811 only (2/5; required ≥3)**. The result is **does_not_pass**. The decision function never reads 1813 scores.

## Training support, offsets and annual variation

Primary population. Repeated blocks are deliberate: no newer complete group becomes available in 1809 or 1811–1812. Small support and shared fits limit replication.

| Target year | Base n | Calibration n | Test eligible / scored | Base intercept | Base slope | Offset | Expanding intercept | Expanding slope |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1805 | 0 | 0 | 14 / 0 | not estimable | not estimable | not estimable | not estimable | not estimable |
| 1806 | 0 | 14 | 15 / 0 | not estimable | not estimable | not estimable | not estimable | not estimable |
| 1807 | 0 | 14 | 13 / 0 | not estimable | not estimable | not estimable | not estimable | not estimable |
| 1808 | 14 | 28 | 14 / 14 | +0.747771 | +1.289035 | +0.977889 | +1.397934 | +1.657062 |
| 1809 | 14 | 28 | 47 / 47 | +0.747771 | +1.289035 | +0.977889 | +1.397934 | +1.657062 |
| 1810 | 42 | 61 | 11 / 11 | +1.397934 | +1.657062 | -0.627376 | +1.036869 | +2.599291 |
| 1811 | 42 | 61 | 13 / 13 | +1.397934 | +1.657062 | -0.627376 | +1.036869 | +2.599291 |
| 1812 | 42 | 61 | 30 / 30 | +1.397934 | +1.657062 | -0.627376 | +1.036869 | +2.599291 |
| 1813 | 103 | 54 | 37 / 37 | +1.036869 | +2.599291 | -0.613410 | +0.798931 | +2.530819 |

| Year | Region | Scored n | Corrected log loss | Expanding log loss | Difference | Corrected Brier | Expanding Brier |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1808 | main | 14 | 0.540950 | 0.478421 | +0.062529 | 0.188732 | 0.162062 |
| 1809 | main | 47 | 0.736825 | 0.658792 | +0.078033 | 0.261248 | 0.231110 |
| 1810 | main | 11 | 0.514639 | 0.525747 | -0.011107 | 0.174420 | 0.181082 |
| 1811 | main | 13 | 0.760643 | 0.834555 | -0.073912 | 0.279808 | 0.305400 |
| 1812 | main | 30 | 0.618885 | 0.616679 | +0.002206 | 0.217631 | 0.220408 |
| 1813 | secondary | 37 | 0.601049 | 0.691122 | -0.090073 | 0.207721 | 0.251057 |

## Source-group variation and paired loss concentration

| Source group | Scored n | Corrected log loss | Expanding log loss | Difference |
| --- | ---: | ---: | ---: | ---: |
| fifth-coalition 1809 | 29 | 0.810152 | 0.702878 | +0.107273 |
| liberation 1813 | 29 | 0.588083 | 0.682744 | -0.094661 |
| peninsula 1808 | 14 | 0.540950 | 0.478421 | +0.062529 |
| peninsula 1809 | 18 | 0.618688 | 0.587765 | +0.030923 |
| peninsula 1810 | 11 | 0.514639 | 0.525747 | -0.011107 |
| peninsula 1811 | 13 | 0.760643 | 0.834555 | -0.073912 |
| peninsula 1812 | 4 | 0.602671 | 0.621134 | -0.018462 |
| peninsula 1813 | 8 | 0.648048 | 0.721489 | -0.073441 |
| russia-1812 1812 | 26 | 0.621379 | 0.615994 | +0.005386 |

The correction has lower log loss in three of seven main source groups and higher loss in four. The annual 1812 aggregate worsens slightly even though its small Peninsular group improves. Every model’s year/group scores, bins and every signed case difference in all populations remain in the raw result and are checked during reproduction.

The concentration denominator is the sum of absolute paired log-loss differences, retaining gains and losses without cancellation. These shares are not shares of net gain or command credit.

| Region | Comparator | Absolute-difference total | Largest one | Largest five | Largest ten |
| --- | --- | ---: | ---: | ---: | ---: |
| decision | same_base_force | 38.026868 | 2.25% | 10.23% | 19.63% |
| reused_1813_secondary | same_base_force | 10.331821 | 4.97% | 20.77% | 39.21% |
| decision | expanding_force | 15.383860 | 3.53% | 13.54% | 24.86% |
| reused_1813_secondary | expanding_force | 6.329508 | 4.55% | 19.75% | 37.67% |
| decision | expanding_prior | 18.703773 | 4.62% | 19.52% | 33.36% |
| reused_1813_secondary | expanding_prior | 14.542913 | 6.26% | 27.56% | 47.94% |
| decision | recent_prior | 21.252527 | 4.45% | 17.82% | 31.15% |
| reused_1813_secondary | recent_prior | 9.936095 | 6.84% | 29.66% | 50.52% |
| decision | equal_odds | 60.669494 | 3.04% | 11.10% | 19.47% |
| reused_1813_secondary | equal_odds | 9.137693 | 9.60% | 30.00% | 52.24% |

## Probability bins

Primary correction and expanding force. Counts are unweighted; means use the stated weights. Bins are left-closed/right-open with 1 included in the last bin. Empty bins remain unknown. All six models’ bins in every population/year/group are retained in the raw result.

| Region | Model | Bin | n | Mean p, battle | Recorded A-win share, battle | Mean p, campaign | Recorded A-win share, campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| decision | offset_force | 0.0–0.2 | 0 | unknown | unknown | unknown | unknown |
| decision | offset_force | 0.2–0.4 | 1 | 0.344239 | 0.000000 | 0.344239 | 0.000000 |
| decision | offset_force | 0.4–0.6 | 11 | 0.530264 | 0.454545 | 0.528539 | 0.596869 |
| decision | offset_force | 0.6–0.8 | 48 | 0.717253 | 0.458333 | 0.708832 | 0.482578 |
| decision | offset_force | 0.8–1.0 | 55 | 0.851697 | 0.800000 | 0.850200 | 0.823647 |
| decision | expanding_force | 0.0–0.2 | 0 | unknown | unknown | unknown | unknown |
| decision | expanding_force | 0.2–0.4 | 2 | 0.303389 | 0.000000 | 0.303389 | 0.000000 |
| decision | expanding_force | 0.4–0.6 | 13 | 0.526600 | 0.461538 | 0.512938 | 0.592376 |
| decision | expanding_force | 0.6–0.8 | 59 | 0.733370 | 0.491525 | 0.729194 | 0.508090 |
| decision | expanding_force | 0.8–1.0 | 41 | 0.861667 | 0.878049 | 0.871204 | 0.883691 |
| reused_1813_secondary | offset_force | 0.0–0.2 | 0 | unknown | unknown | unknown | unknown |
| reused_1813_secondary | offset_force | 0.2–0.4 | 7 | 0.308375 | 0.142857 | 0.279658 | 0.103896 |
| reused_1813_secondary | offset_force | 0.4–0.6 | 19 | 0.507110 | 0.157895 | 0.507550 | 0.256809 |
| reused_1813_secondary | offset_force | 0.6–0.8 | 10 | 0.736860 | 0.800000 | 0.731107 | 0.696721 |
| reused_1813_secondary | offset_force | 0.8–1.0 | 1 | 0.823092 | 1.000000 | 0.823092 | 1.000000 |
| reused_1813_secondary | expanding_force | 0.0–0.2 | 0 | unknown | unknown | unknown | unknown |
| reused_1813_secondary | expanding_force | 0.2–0.4 | 3 | 0.350040 | 0.000000 | 0.317349 | 0.000000 |
| reused_1813_secondary | expanding_force | 0.4–0.6 | 12 | 0.509591 | 0.250000 | 0.521863 | 0.326087 |
| reused_1813_secondary | expanding_force | 0.6–0.8 | 15 | 0.670521 | 0.266667 | 0.666765 | 0.259804 |
| reused_1813_secondary | expanding_force | 0.8–1.0 | 7 | 0.837221 | 0.857143 | 0.837401 | 0.896104 |

## Interpretation and stopping disposition

This fixed correction does not transfer consistently across the earlier development years. Retain the expanding uncorrected comparator as the descriptive baseline. The failure ends this correction branch; it does not trigger a window search, another correction, final-set evaluation, commander model or wider evidence extraction.

The design was frozen before this execution, but all development outcomes were historically familiar and 1813 had motivated the question. Five main years/seven groups, repeated calibration blocks, overlapping training sets, long operations and one compiler family provide limited replication. No significance test, bootstrap interval or confirmatory generalization claim is made.

Event completion is a retrospective training-availability proxy, not a publication or contemporary information date. Whole-entry forces still lack an established opening clock/population. Compiler selection, rounded/qualified strength totals, strength-dependent winner coding and missing pairs remain the [prepared source-context limits](../../data/napoleonic/benchmark-v1/context.json), not repaired by a probability offset. The six convention passages were rechecked against `bodart-1908-transcription-v1`, printed pp. 45–47, and the three pinned page images. Raw SHA-256: `bf12437b6d19226ce127ce5d81e59d20358a5b1999ffe00f5ac6a8f8c20ef986`. The unchanged context retains exact quotes, locators and image hashes. Date roles retain the plan’s original raw/frame SHA-256 bindings and entry/field locators; no new historical adjudication occurs.

The frozen baseline inputs, all previous numerical results, draft evidence and packets remain unchanged. The 52-entry final reservation remains intact; the two 1813 operations that finish in 1814 retain their original development IDs. Wider opening research and the appointment branch stay stopped. Extraction-review calibration remains prepared and unscored. No second-opinion prompt, separate review or subagent ran.

## Execution and primary verification

- Immutable [raw result](../../artifacts/napoleonic-temporal-calibration-run-v1.json), SHA-256 `39213035280b48ffa6ef10031ba6631715dba58b6bdcb0d95e034e17585067a2`; [exact proposal](../../data/napoleonic/temporal-calibration-v1/run-proposal.json), SHA-256 `b6b58138ba1b396160a0d9185e18a3b756f83788fb89da5f3431000a9d84b5f7`.
- [Actual owner run authorization](../../data/napoleonic/temporal-calibration-v1/owner-run-authorization.json), SHA-256 `e4b3faa644689e135aab8893114533fb83d0f9c02b5ea79eb8cb02ba66e7caae`, records the owner’s verbatim reply accepting execution. It binds the proposal, exact command and development-only scope. The 16 executing input/code/plan bindings are retained in the raw result.
- The exact proposal command ran once with CPython 3.14.7: `python3 -m generalship.napoleonic_temporal_calibration_run --authorization data/napoleonic/temporal-calibration-v1/owner-run-authorization.json --out artifacts/napoleonic-temporal-calibration-run-v1.json`. The runner refuses overwrite.
- The run performed 72 parameter fits across 24 scorable population/year folds: 48 force fits and 24 offsets, including deliberate repeated blocks and the indecisive no-op. These are fit calls, not 72 independent replications. There are 589 population-entry prediction rows / 3,534 probability values, with repeated entries across sensitivities.
- [Primary arithmetic verification](../../artifacts/napoleonic-temporal-calibration-run-v1-verification.json) checks all 36 annual role assignments, every force/offset score equation, all 589 rows and 3,534 probabilities, 80 summaries / 1632 score values / 4800 bins, all paired losses/concentration and the continuation decision. It matches 141 original forward prediction rows across four populations. Arithmetic uses a second implementation with no fitting; this is primary verification, not a separate historical review.
- Absolute tolerances are 2e-12 for saved arithmetic, 1e-7 for force score equations and 1e-9 for offset score equations. The strictly convex penalized objectives make the stationary parameters sufficient to check the saved fits without rerunning optimization.
- `python3 -m generalship.napoleonic_temporal_calibration_report` verifies this saved result. `--write` regenerates only this memo and its verification record. `make check` and `make reproduce` use the metadata planner and saved-result verifier; neither executes the historical job. Tests fit constructed cases only.
