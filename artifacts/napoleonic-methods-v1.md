# Napoleonic methods checkpoint v1

**Primary-verified. No historical outcomes fitted; no historical ranking or causal estimate.**

Schedule: 325 cohort entries, 16 frozen war/year groups, 650 side slots. 297 entries enter the synthetic schedule; 28 have missing, joint/complex or identical labels and remain in the cohort. The usable schedule contains 357 literal labels.

Conservative printed keys: 375 labels; 75 recur; 42 occur in multiple groups. There are 114 opponent components; the largest contains 94 labels. The JSON retains every component.

Held-out availability: 197/325 rows have at least one label in another group; 41 have both. These are printed labels, not resolved people or credited command appointments.

**Commander versus army identification: not assessed.** There are 0 verified historical army labels for 650 side slots in this checkpoint. The source-backed pilot shows overlapping authority, but does not establish army continuity. Connectivity cannot fill this gap.

**Campaign pilot: not estimable.** Local orders and authority distinctions replay from their sources. Campaign-onset boundaries, eligible replacements, inherited resources, information and the campaign outcome vector remain unknown. No battle results are added into campaign contribution.

## Synthetic recovery

100 recoveries and 20 validation repetitions per scenario; seed 20261018. All army labels, force covariates and outcomes here are simulated. Fixed tau, reduced additive logistic model; this is not the complete run-4 selection procedure. Recovery gives each usable printed label equal weight after global centering; disconnected and side/intercept offsets remain prior-dependent. Ranges in the JSON describe repetitions, not historical confidence intervals.

| Scenario | Centered theta RMSE | Estimated theta SD | Recovery correlation | Recovery slope |
|---|---:|---:|---:|---:|
| null | 0.1711 | 0.1711 | undefined (true spread zero) | undefined (true spread zero) |
| commander | 0.5711 | 0.1787 | 0.2954 | 0.0884 |
| stable_army_alias | 0.1821 | 0.1821 | undefined (true spread zero) | undefined (true spread zero) |
| switching_armies | 0.5846 | 0.1782 | 0.2504 | 0.0741 |
| source_bias | 0.1729 | 0.1729 | undefined (true spread zero) | undefined (true spread zero) |

The stable-army scenario has zero true commander effect and identical army/commander columns. Its estimated commander spread measures misattribution under this assumption, not discovered skill. The source-bias scenario tests whether commander labels absorb biased strength measurement.

| Scenario | Test | Rows / groups | Commander minus force, battle | Equal-group | Commander minus prior, battle | Equal-group |
|---|---|---:|---:|---:|---:|---:|
| null | war_year | 297 / 16 | +0.0059 | +0.0065 | -0.0021 | -0.0031 |
| null | whole_war | 297 / 16 | +0.0021 | +0.0011 | -0.0057 | -0.0079 |
| null | forward_time | 107 / 5 | +0.0026 | +0.0008 | -0.0056 | -0.0085 |
| commander | war_year | 297 / 16 | -0.0055 | -0.0054 | -0.0109 | -0.0104 |
| commander | whole_war | 297 / 16 | -0.0027 | -0.0028 | -0.0071 | -0.0064 |
| commander | forward_time | 107 / 5 | -0.0040 | -0.0056 | -0.0082 | -0.0099 |
| stable_army_alias | war_year | 297 / 16 | -0.0136 | -0.0135 | -0.0174 | -0.0168 |
| stable_army_alias | whole_war | 297 / 16 | -0.0089 | -0.0087 | -0.0125 | -0.0120 |
| stable_army_alias | forward_time | 107 / 5 | -0.0083 | -0.0065 | -0.0124 | -0.0089 |
| switching_armies | war_year | 297 / 16 | -0.0012 | -0.0010 | -0.0053 | -0.0055 |
| switching_armies | whole_war | 297 / 16 | -0.0018 | -0.0021 | -0.0057 | -0.0060 |
| switching_armies | forward_time | 107 / 5 | +0.0015 | +0.0070 | -0.0036 | +0.0025 |
| source_bias | war_year | 297 / 16 | +0.0083 | +0.0074 | +0.0083 | +0.0067 |
| source_bias | whole_war | 297 / 16 | +0.0051 | +0.0033 | +0.0056 | +0.0036 |
| source_bias | forward_time | 107 / 5 | +0.0063 | +0.0067 | +0.0093 | +0.0066 |

Negative log-loss differences favor the commander model. A gain in the army or source-bias scenario would show why predictive gain alone does not identify a commander contribution. Forward-time scores cover a different test subset; do not rank strategies as though their rows were identical.

## Observing the invented army assignments

| Scenario | Commander RMSE without army terms | With observed synthetic army terms | Estimated theta SD with army terms |
|---|---:|---:|---:|
| stable_army_alias | 0.1821 | 0.1384 | 0.1384 |
| switching_armies | 0.5846 | 0.5811 | 0.1613 |

Permanent pairing is still structurally confounded when both columns are supplied; priors allocate the shared effect. Rotating assignments are only an invented sensitivity case, not evidence of historical crossovers.

## Fixed evaluation and research handoff

Development: 273 entries through 1813. Reserved final: 52 entries of 1814–1815 in three intact groups. The reservation concerns future numerical model selection; historical events have already been seen. No historical outcome fit is authorized by this checkpoint.

The versioned design fixes group and temporal sensitivities and requires comparison with force only, context only, the training prior and equal odds. Three final groups provide limited replication.

The calibration sample is prepared and unscored; no independent review was performed. The research screen flags digit/locator/family issues for primary inspection, and cannot verify entailment.

Reproduce the experiment explicitly with `make napoleonic-methods`. `make reproduce` rebuilds this report and preparation artifacts from the stored result without a model job. The JSON carries exact bindings, scenario distributions, exclusions and environment. See `docs/napoleonic-methods-v1.md`.
