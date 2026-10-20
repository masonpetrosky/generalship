# Napoleonic compiler-strength benchmark run v1

Primary-verified. Share with caveats. The owner authorized the exact frozen development-only proposal.

**Force size improves campaign- and war-held-out prediction of Bodart’s recorded winners. Transfer to 1813 is weak and sensitivity-dependent.** These are compiler-record predictions; no commander, tactical or campaign-contribution effect is estimated.

## Scope and fixed method

- 273 development engagements / 546 sides / 13 complete campaign groups. 194 paired compiler totals are eligible (71.1%); 79 engagements remain excluded. 82 side extracts are missing, 32 ambiguous and 44 otherwise eligible sides lack an eligible opponent.
- All 52 final-evaluation entries remain reserved. The 273-entry denominator and every exclusion remain in the [prepared dataset](../../artifacts/napoleonic-benchmark-v1.md).
- One ridge-1 logistic model uses `(A-B)/(A+B)` from the two printed personnel totals. A is France and its allies. Both intercept and slope are penalized. Comparators are equal odds and the training-only Laplace-smoothed A-win share. No tuning, model selection or commander term.
- Campaign holdouts retain 13 groups; war holdouts retain six. The forward view trains through 1812 and scores the fixed 1813 development entries. Battle weighting gives each scored entry equal weight; equal-group weighting gives each held-out group equal weight. The forward view has one held-out year, so its two weightings coincide.

## Scores in every fixed population

Lower scores are better. Log loss uses natural logarithms. Every model uses the same rows within each population/evaluation. Populations change coverage; their score differences are not paired estimates of an annotation effect. `Scored / eligible` separates the forward test rows from its training rows; training-only rows listed as unscored in the raw result are expected.

### Log loss

| Population | Evaluation | Scored / eligible | Groups | Force, battle | Prior, battle | Equal odds, battle | Force, group | Prior, group | Equal odds, group |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| primary | leave_campaign_out | 194 / 194 | 13 | 0.559365 | 0.680716 | 0.693147 | 0.550669 | 0.648723 | 0.693147 |
| primary | leave_war_out | 194 / 194 | 6 | 0.560831 | 0.683644 | 0.693147 | 0.529927 | 0.681874 | 0.693147 |
| primary | forward_1813 | 37 / 194 | 1 | 0.691122 | 0.873458 | 0.693147 | 0.691122 | 0.873458 | 0.693147 |
| exclude_indecisive | leave_campaign_out | 194 / 194 | 13 | 0.559365 | 0.680716 | 0.693147 | 0.550669 | 0.648723 | 0.693147 |
| exclude_indecisive | leave_war_out | 194 / 194 | 6 | 0.560831 | 0.683644 | 0.693147 | 0.529927 | 0.681874 | 0.693147 |
| exclude_indecisive | forward_1813 | 37 / 194 | 1 | 0.691122 | 0.873458 | 0.693147 | 0.691122 | 0.873458 | 0.693147 |
| exclude_no_combat | leave_campaign_out | 193 / 193 | 13 | 0.561335 | 0.681225 | 0.693147 | 0.552250 | 0.648979 | 0.693147 |
| exclude_no_combat | leave_war_out | 193 / 193 | 6 | 0.562621 | 0.684058 | 0.693147 | 0.531561 | 0.681802 | 0.693147 |
| exclude_no_combat | forward_1813 | 37 / 193 | 1 | 0.690395 | 0.870417 | 0.693147 | 0.690395 | 0.870417 | 0.693147 |
| unqualified_totals | leave_campaign_out | 163 / 163 | 13 | 0.591466 | 0.685880 | 0.693147 | 0.590381 | 0.651527 | 0.693147 |
| unqualified_totals | leave_war_out | 163 / 163 | 6 | 0.594007 | 0.691344 | 0.693147 | 0.567636 | 0.694252 | 0.693147 |
| unqualified_totals | forward_1813 | 30 / 163 | 1 | 0.716775 | 0.878862 | 0.693147 | 0.716775 | 0.878862 | 0.693147 |

### Brier score

| Population | Evaluation | Scored / eligible | Groups | Force, battle | Prior, battle | Equal odds, battle | Force, group | Prior, group | Equal odds, group |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| primary | leave_campaign_out | 194 / 194 | 13 | 0.190518 | 0.243379 | 0.250000 | 0.188712 | 0.227805 | 0.250000 |
| primary | leave_war_out | 194 / 194 | 6 | 0.191262 | 0.244805 | 0.250000 | 0.177496 | 0.243873 | 0.250000 |
| primary | forward_1813 | 37 / 194 | 1 | 0.251057 | 0.335418 | 0.250000 | 0.251057 | 0.335418 | 0.250000 |
| exclude_indecisive | leave_campaign_out | 194 / 194 | 13 | 0.190518 | 0.243379 | 0.250000 | 0.188712 | 0.227805 | 0.250000 |
| exclude_indecisive | leave_war_out | 194 / 194 | 6 | 0.191262 | 0.244805 | 0.250000 | 0.177496 | 0.243873 | 0.250000 |
| exclude_indecisive | forward_1813 | 37 / 194 | 1 | 0.251057 | 0.335418 | 0.250000 | 0.251057 | 0.335418 | 0.250000 |
| exclude_no_combat | leave_campaign_out | 193 / 193 | 13 | 0.191358 | 0.243650 | 0.250000 | 0.189377 | 0.227937 | 0.250000 |
| exclude_no_combat | leave_war_out | 193 / 193 | 6 | 0.192037 | 0.245030 | 0.250000 | 0.178175 | 0.243862 | 0.250000 |
| exclude_no_combat | forward_1813 | 37 / 193 | 1 | 0.250710 | 0.334091 | 0.250000 | 0.250710 | 0.334091 | 0.250000 |
| unqualified_totals | leave_campaign_out | 163 / 163 | 13 | 0.204089 | 0.245896 | 0.250000 | 0.204680 | 0.229151 | 0.250000 |
| unqualified_totals | leave_war_out | 163 / 163 | 6 | 0.205398 | 0.248560 | 0.250000 | 0.193189 | 0.249915 | 0.250000 |
| unqualified_totals | forward_1813 | 30 / 163 | 1 | 0.262276 | 0.338326 | 0.250000 | 0.262276 | 0.338326 | 0.250000 |

The primary forward check trains on 157 entries and scores 37. The recorded A-win share changes from 107/157 in training to 13/37 in testing; its fixed training prior is 0.679245. Force log loss is 0.691122 versus equal odds 0.693147, while force Brier is 0.251057 versus 0.250000. The unqualified-total forward view has 133 training and 30 test entries; both force scores are worse than equal odds.

The indecisive exclusion removes zero eligible rows and duplicates the primary result. The non-combat exclusion retains 193 pairs. Screening approximate totals or numeric notes anywhere in the cited strength passage retains 163. Notes can apply to entry context or the other side; the screen does not newly adjudicate their applicability.

## Descriptive campaign bootstrap

Force minus comparator log loss: negative favors force. These are paired held-out-campaign loss intervals (10,000 resamples, seed 20261020, percentile 95%), with weights recomputed in each draw. They condition on the saved predictions and selected source data; they do not refit training folds or propagate source/label uncertainty. Overlapping training sets and one compiler family remain dependencies. No interval is claimed for the six-war or one-year views. No pass/fail skill rule was specified.

| Population | Comparator | Battle-weighted difference | 95% interval | Equal-group difference | 95% interval |
| --- | --- | ---: | --- | ---: | --- |
| primary | equal_odds | -0.133782 | [-0.208725, -0.070281] | -0.142478 | [-0.216154, -0.070745] |
| primary | training_prior | -0.121351 | [-0.169028, -0.060386] | -0.098054 | [-0.154708, -0.037710] |
| exclude_indecisive | equal_odds | -0.133782 | [-0.208725, -0.070281] | -0.142478 | [-0.216154, -0.070745] |
| exclude_indecisive | training_prior | -0.121351 | [-0.169028, -0.060386] | -0.098054 | [-0.154708, -0.037710] |
| exclude_no_combat | equal_odds | -0.131812 | [-0.205603, -0.069002] | -0.140897 | [-0.213393, -0.070173] |
| exclude_no_combat | training_prior | -0.119889 | [-0.167715, -0.058927] | -0.096729 | [-0.153408, -0.037203] |
| unqualified_totals | equal_odds | -0.101681 | [-0.172537, -0.042931] | -0.102766 | [-0.172567, -0.037218] |
| unqualified_totals | training_prior | -0.094415 | [-0.142093, -0.039602] | -0.061146 | [-0.127856, +0.013096] |

The unqualified-total equal-group interval against the training prior includes zero (-0.127856 to +0.013096). Its lower point score alone does not establish robust improvement.

## Campaign variation and error concentration

| Held-out campaign | Scored entries | Force log loss | Prior log loss | Difference |
| --- | ---: | ---: | ---: | ---: |
| fifth-coalition 1809 | 29 | 0.566651 | 0.700197 | -0.133546 |
| fourth-coalition 1806 | 13 | 0.424681 | 0.527355 | -0.102674 |
| fourth-coalition 1807 | 13 | 0.435283 | 0.599848 | -0.164565 |
| liberation 1813 | 29 | 0.665395 | 0.856718 | -0.191323 |
| peninsula 1808 | 14 | 0.425286 | 0.622148 | -0.196862 |
| peninsula 1809 | 18 | 0.645583 | 0.620107 | +0.025476 |
| peninsula 1810 | 11 | 0.519523 | 0.615892 | -0.096369 |
| peninsula 1811 | 13 | 0.799649 | 0.705022 | +0.094627 |
| peninsula 1812 | 4 | 0.691094 | 0.603466 | +0.087628 |
| peninsula 1813 | 8 | 0.672179 | 0.792126 | -0.119947 |
| russia-1812 1812 | 26 | 0.559972 | 0.707444 | -0.147472 |
| third-coalition 1805 | 14 | 0.309617 | 0.594344 | -0.284727 |
| third-coalition 1806 | 2 | 0.443788 | 0.488735 | -0.044946 |

Force has lower log loss than the prior in 10 of 13 campaigns and higher loss in three. The largest one, five and ten absolute entry contributions account for 2.32%, 9.01% and 15.73% of the total absolute difference. This denominator includes gains and losses without cancelling them; it is not a share of net gain.

| Entry | Printed place | Force-minus-prior log loss |
| --- | --- | ---: |
| B406c | Preßburg | +1.253568 |
| B429a | Tarifa | +0.992131 |
| B409a | Graz | +0.979995 |
| B398a | Regensburg | -0.829588 |
| B434a | Kobrin | -0.820858 |
| B464a | Pampeluna | -0.759037 |
| B412b | Vlissingen | -0.744965 |
| B447b | Möckern | +0.731728 |
| B424b | Figueras | +0.712304 |
| B396b | Innsbruck | -0.686783 |

All signed entry contributions and every group result for all populations/evaluations remain in the raw result. These prediction errors assign no command credit.

## Force-model calibration

Primary population; bins are left-closed/right-open, with 1 included in the last bin. Counts are unweighted; probability and recorded A-win means use the stated weights. Empty bins remain unknown. All three models’ calibration bins for every population are published in the raw result.

| Evaluation | Bin | Entries | Mean probability, battle | Recorded A-win share, battle | Mean probability, group | Recorded A-win share, group |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| leave_campaign_out | 0.0–0.2 | 2 | 0.153398 | 0.000000 | 0.153642 | 0.000000 |
| leave_campaign_out | 0.2–0.4 | 23 | 0.319543 | 0.260870 | 0.315003 | 0.378403 |
| leave_campaign_out | 0.4–0.6 | 58 | 0.509292 | 0.517241 | 0.506674 | 0.636963 |
| leave_campaign_out | 0.6–0.8 | 71 | 0.685510 | 0.676056 | 0.684170 | 0.641917 |
| leave_campaign_out | 0.8–1.0 | 40 | 0.860638 | 0.900000 | 0.867806 | 0.927624 |
| leave_war_out | 0.0–0.2 | 3 | 0.156732 | 0.000000 | 0.155279 | 0.000000 |
| leave_war_out | 0.2–0.4 | 24 | 0.317749 | 0.291667 | 0.313828 | 0.217401 |
| leave_war_out | 0.4–0.6 | 60 | 0.507721 | 0.516667 | 0.505378 | 0.497050 |
| leave_war_out | 0.6–0.8 | 70 | 0.689480 | 0.685714 | 0.687987 | 0.695095 |
| leave_war_out | 0.8–1.0 | 37 | 0.862470 | 0.918919 | 0.857533 | 0.936543 |
| forward_1813 | 0.0–0.2 | 0 | unknown | unknown | unknown | unknown |
| forward_1813 | 0.2–0.4 | 3 | 0.350040 | 0.000000 | 0.350040 | 0.000000 |
| forward_1813 | 0.4–0.6 | 12 | 0.509591 | 0.250000 | 0.509591 | 0.250000 |
| forward_1813 | 0.6–0.8 | 15 | 0.670521 | 0.266667 | 0.670521 | 0.266667 |
| forward_1813 | 0.8–1.0 | 7 | 0.837221 | 0.857143 | 0.837221 | 0.857143 |

The smallest primary campaign calibration bin has only two entries. These are descriptive checks of recorded labels, not calibrated historical command probabilities.

## Source limits and interpretation

Bodart selects entries by consequence, assembled forces or losses; his so-called indecisive winner rule can use relative strength. His strength convention includes available nearby troops that did not fight, and figures are rounded. These conventions are inspected in the prepared source context: `bodart-1908-transcription-v1`, pp. 45–47, raw SHA-256 `bf12437b6d19226ce127ce5d81e59d20358a5b1999ffe00f5ac6a8f8c20ef986`.

The [six exact passages, English renderings and three page-image hashes](../../data/napoleonic/benchmark-v1/context.json) remain inspectable. They also appear in the [prepared report](../../artifacts/napoleonic-benchmark-v1.md#inspected-source-conventions). The indecisive no-op does not remove strength-dependent coding, shared-source error or selection. The dataset is outcome-unused preparation, not historical blinding.

The grouped scores support a descriptive force-size baseline for these compiler records. The forward result and unqualified-total interval limit claims of generalization. No feature is admitted to the frozen baseline, no commander ranking is produced, and no causal or campaign-contribution conclusion follows. Wider strict-opening extraction stays paused; the stopped appointment pilots and unscored extraction calibration are unchanged.

## Reproduction and primary verification

- Immutable [raw result](../../artifacts/napoleonic-benchmark-run-v1.json), SHA-256 `35ed5cc7066cf40287e26afc03b16409a9012e81157b472abf212727faa5d505`. It retains every fold, coefficient, prediction, score, calibration bin, group result, contribution and planned bootstrap.
- [Owner run authorization](../../data/napoleonic/benchmark-v1/owner-run-authorization.json) has SHA-256 `f847c992aecf69e28af3986205014b1826094879d5da6091b723e749031d15d2` and records the actual owner reply. [Frozen proposal](../../data/napoleonic/benchmark-v1/run-proposal.json) SHA-256 `f33cbea825c477e6a831960cd43ff4da8d91391e1b8642b701c5f4faf970981d`.
- The executed command was `python3 -m generalship.napoleonic_benchmark_run --authorization data/napoleonic/benchmark-v1/owner-run-authorization.json --out artifacts/napoleonic-benchmark-run-v1.json`. The runner refuses to overwrite the result. The recorded environment is CPython 3.14.7.
- [Arithmetic verification](../../artifacts/napoleonic-benchmark-run-v1-verification.json) checks 80 folds and 1629 saved predictions, score equations, training-only priors, all summary/group scores, calibration bins, signed contributions and all bootstrap bounds. It uses a second arithmetic implementation and performs no fitting. This is primary verification, with no separate review.
- `python3 -m generalship.napoleonic_benchmark_report` verifies the saved run and report. `--write` regenerates only this report and its verification record. `make check` and `make reproduce` use this saved-result path; they do not invoke the historical runner.
