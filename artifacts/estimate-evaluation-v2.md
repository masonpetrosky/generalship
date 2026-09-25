# Estimate-layer evaluation (diagnostic)

**Exploratory estimate-layer diagnostic under design §6 option (a). Not the baseline, not an admitted feature, not a ranking of commanders.**

Ledger `data/estimates/side-strength-v2.json` (SHA-256 `7855d4d3c8853f7eb94849cb3701c0ca3e3bd759df11b8ffcb5e086cc92deed8`), authorized by the owner on 2026-09-25 ([record](../data/estimates/evaluation-authorization-v2.json)).
Model `strength-logistic-v1`, unchanged: ridge 1.0 logistic regression on the rounded point strengths, leave one campaign out. Scores are `diagnostic_union_score` values, not win probabilities.
Rows with a `post_start_information` side: 17 (GA006, GA018, LA017, LA021, MS003, MS011, NC007, TN002, TN024, VA017, VA070, VA071, VA072, VA075, VA079, VA111, WV010); excluded from fits: set1_A 1, set2_AB 1, set3_ABC 13.

## Row sets

Brier score, battle-weighted / campaign-weighted. Lower is better; equal odds scores 0.2500.

| Row set | Rows | Campaigns | Union wins | Side grades | Strength model | Equal odds | Training prior |
|---|---:|---:|---:|---|---:|---:|---:|
| set1_A | 61 | 38 | 27 | A 122 | 0.2508 / 0.2560 | 0.2500 / 0.2500 | 0.2611 / 0.2542 |
| set2_AB | 80 | 47 | 43 | A 133 B 27 | 0.2506 / 0.2648 | 0.2500 / 0.2500 | 0.2584 / 0.2572 |
| set3_ABC | 126 | 66 | 74 | A 154 B 40 C 58 | 0.2349 / 0.2452 | 0.2500 / 0.2500 | 0.2478 / 0.2447 |

Per-set §5 label counts, folds and every prediction are in `estimate-evaluation-v2.json`.

Frozen baseline reference (23 rows, 13 campaigns): 0.2769 / 0.2765.

## Common and newly covered rows

Common rows have both a frozen baseline row and an estimate row; both models are refit on the same common training rows in each fold. Newly covered rows are compared only with equal odds and the prior.

| Row set | Common rows | Identical by construction | Estimates | Frozen refit | Equal odds | Prior | New rows | Estimates | Equal odds | Prior |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| set1_A | 46 | 39 | 0.2529 / 0.2575 | 0.2546 / 0.2583 | 0.2500 / 0.2500 | 0.2645 / 0.2532 | 15 | 0.2625 / 0.2549 | 0.2500 / 0.2500 | 0.2630 / 0.2643 |
| set2_AB | 48 | 41 | 0.2547 / 0.2637 | 0.2564 / 0.2645 | 0.2500 / 0.2500 | 0.2655 / 0.2581 | 32 | 0.2481 / 0.2558 | 0.2500 / 0.2500 | 0.2481 / 0.2454 |
| set3_ABC | 50 | 41 | 0.2532 / 0.2627 | 0.2543 / 0.2631 | 0.2500 / 0.2500 | 0.2643 / 0.2575 | 76 | 0.2205 / 0.2204 | 0.2500 / 0.2500 | 0.2322 / 0.2288 |

## Sensitivity refits

Strength-model Brier, battle-weighted, with rows used. "NE" is not evaluable (fewer than 6 rows, 3 campaigns or both outcomes).

| Variant | set1_A | set2_AB | set3_ABC |
|---|---:|---:|---:|
| endpoint_refit_us_low_cs_low | 0.2516 (61) | 0.2514 (80) | 0.2343 (126) |
| endpoint_refit_us_low_cs_high | 0.2444 (61) | 0.2488 (80) | 0.2347 (126) |
| endpoint_refit_us_high_cs_low | 0.2549 (61) | 0.2518 (80) | 0.2359 (126) |
| endpoint_refit_us_high_cs_high | 0.2474 (61) | 0.2488 (80) | 0.2355 (126) |
| exclude_opponent_estimate_point | 0.2508 (61) | 0.2506 (80) | 0.2424 (97) |
| exclude_applicability_unresolved | 0.2449 (43) | 0.2362 (56) | 0.2262 (75) |
| exclude_derivation_unknown | NE (4) | 0.1964 (14) | 0.1864 (35) |
| exclude_bound_conflict | 0.2490 (59) | 0.2487 (78) | 0.2347 (118) |
| rule4_factor_1 | 0.2508 (61) | 0.2506 (80) | 0.2358 (126) |
| alternative_basis_order | 0.2514 (61) | 0.2512 (80) | 0.2343 (125) |
| upper_middle_median | 0.2475 (61) | 0.2493 (80) | 0.2332 (126) |

## Limits

- Predictions are diagnostic_union_score values, not win probabilities or command effects.
- Which sides have figures, and so which rows and grades exist, may depend on the outcome, size and fame.
- Results from different row sets, grades or sensitivity variants are not improvements over one another.
- No significance test was run; at these row counts no difference is presented as significant or as evidence that the estimates are accurate.
- No commander attribution, ranking or causal effect is produced.
- Every result carries `whole_engagement_leakage`, `conditional_on_source_availability`.
