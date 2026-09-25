# Estimate-layer evaluation (diagnostic)

**Exploratory estimate-layer diagnostic under design §6 option (a). Not the baseline, not an admitted feature, not a ranking of commanders.**

Ledger `data/estimates/side-strength-v1.json` (SHA-256 `0656b03cbdaa088849dc3795f9c6a9e9d6762be10f53f28e4285be46f7fcde89`), authorized by the owner on 2026-09-25 ([record](../data/estimates/evaluation-authorization-v1.json)).
Model `strength-logistic-v1`, unchanged: ridge 1.0 logistic regression on the rounded point strengths, leave one campaign out. Scores are `diagnostic_union_score` values, not win probabilities.
Rows with a `post_start_information` side: 7 (MS003, MS011, NC007, TN002, TN024, VA017, WV010); excluded from fits: set1_A 0, set2_AB 0, set3_ABC 6.

## Row sets

Brier score, battle-weighted / campaign-weighted. Lower is better; equal odds scores 0.2500.

| Row set | Rows | Campaigns | Union wins | Side grades | Strength model | Equal odds | Training prior |
|---|---:|---:|---:|---|---:|---:|---:|
| set1_A | 21 | 12 | 11 | A 42 | 0.2792 / 0.2683 | 0.2500 / 0.2500 | 0.2934 / 0.2739 |
| set2_AB | 29 | 15 | 18 | A 47 B 11 | 0.2483 / 0.2274 | 0.2500 / 0.2500 | 0.2700 / 0.2361 |
| set3_ABC | 37 | 19 | 25 | A 48 B 12 C 14 | 0.2357 / 0.2132 | 0.2500 / 0.2500 | 0.2456 / 0.2112 |

Per-set §5 label counts, folds and every prediction are in `estimate-evaluation.json`.

Frozen baseline reference (23 rows, 13 campaigns): 0.2769 / 0.2765.

## Common and newly covered rows

Common rows have both a frozen baseline row and an estimate row; both models are refit on the same common training rows in each fold. Newly covered rows are compared only with equal odds and the prior.

| Row set | Common rows | Identical by construction | Estimates | Frozen refit | Equal odds | Prior | New rows | Estimates | Equal odds | Prior |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| set1_A | 18 | 16 | 0.3021 / 0.2881 | 0.3023 / 0.2884 | 0.2500 / 0.2500 | 0.3073 / 0.2874 | 3 | 0.2112 / 0.2112 | 0.2500 / 0.2500 | 0.2581 / 0.2581 |
| set2_AB | 20 | 18 | 0.2913 / 0.2692 | 0.2915 / 0.2694 | 0.2500 / 0.2500 | 0.2989 / 0.2674 | 9 | 0.1860 / 0.1861 | 0.2500 / 0.2500 | 0.2205 / 0.2244 |
| set3_ABC | 21 | 18 | 0.2947 / 0.2838 | 0.2941 / 0.2830 | 0.2500 / 0.2500 | 0.2934 / 0.2739 | 16 | 0.1603 / 0.1436 | 0.2500 / 0.2500 | 0.1662 / 0.1546 |

## Sensitivity refits

Strength-model Brier, battle-weighted, with rows used. "NE" is not evaluable (fewer than 6 rows, 3 campaigns or both outcomes).

| Variant | set1_A | set2_AB | set3_ABC |
|---|---:|---:|---:|
| endpoint_refit_us_low_cs_low | 0.2826 (21) | 0.2501 (29) | 0.2360 (37) |
| endpoint_refit_us_low_cs_high | 0.2935 (21) | 0.2606 (29) | 0.2443 (37) |
| endpoint_refit_us_high_cs_low | 0.2772 (21) | 0.2447 (29) | 0.2268 (37) |
| endpoint_refit_us_high_cs_high | 0.2877 (21) | 0.2541 (29) | 0.2377 (37) |
| exclude_opponent_estimate_point | 0.2792 (21) | 0.2483 (29) | 0.2563 (30) |
| exclude_applicability_unresolved | 0.3046 (18) | 0.2692 (25) | 0.2626 (27) |
| exclude_derivation_unknown | NE (1) | NE (5) | 0.2124 (13) |
| exclude_bound_conflict | 0.2834 (20) | 0.2524 (28) | 0.2397 (35) |
| rule4_factor_1 | 0.2792 (21) | 0.2483 (29) | 0.2376 (37) |
| alternative_basis_order | 0.2797 (21) | 0.2491 (29) | 0.2360 (37) |
| upper_middle_median | 0.2833 (21) | 0.2530 (29) | 0.2357 (37) |

## Limits

- Predictions are diagnostic_union_score values, not win probabilities or command effects.
- Which sides have figures, and so which rows and grades exist, may depend on the outcome, size and fame.
- Results from different row sets, grades or sensitivity variants are not improvements over one another.
- No significance test was run; at these row counts no difference is presented as significant or as evidence that the estimates are accurate.
- No commander attribution, ranking or causal effect is produced.
- Every result carries `whole_engagement_leakage`, `conditional_on_source_availability`.
