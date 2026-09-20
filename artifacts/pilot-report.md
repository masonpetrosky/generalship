# Pilot baseline and evidence coverage

**Exploratory pipeline result. No validated general rankings or causal effects.**

The frozen frame contains 127 engagements in 36 campaign groups.
Only 23/127 (18.1%) meet the numerical-strength, decisive-outcome, and grain rules.
All imported historical rows remain unreviewed. A checksum confirms the input bytes, not historical truth.

## Coverage

Exclusion reasons overlap; counts must not be added.

| Reason | Engagements | Share of frame |
|---|---:|---:|
| aggregate_operation | 1 | 0.8% |
| inconclusive_outcome | 35 | 27.6% |
| missing_numeric_strength | 102 | 80.3% |

| Theater | Frame | Eligible |
|---|---:|---:|
| Eastern | 69 | 14 |
| Western | 58 | 9 |

## Campaign-held-out baseline

Each of the 13 eligible campaign groups is held out in full while fitting on the other groups.
Every battle appears once in evaluation. Union win is the positive class; inconclusive cases are excluded, not encoded as half-wins.
Lower Brier score and log loss are better. All baselines use the same eligible rows.

| Model | Battle-weighted Brier | Battle-weighted log loss | Campaign-weighted Brier |
|---|---:|---:|---:|
| strength_logistic | 0.276882 | 0.749509 | 0.276527 |
| equal_odds | 0.250000 | 0.693147 | 0.250000 |
| training_prior | 0.281273 | 0.756087 | 0.274624 |

These are diagnostics on a small, selected subset. They do not establish better generalship measurement.
The source's campaign boundaries may leave dependence between related operations; commanders also recur across folds.
Strength sensitivity varies the held-out range endpoints with a fixed fitted model. It excludes training-data and model uncertainty.

## Draft evidence dossiers

Exact passage checks verify provenance only. These drafts do not modify model inputs. Shiloh's four source-review corrections and the focused validator follow-up are accepted; historical disputes remain open.

| Battle | Claims | Explicit unknowns | Quantities | Events | Status |
|---|---:|---:|---:|---:|---|
| [MD003](../data/evidence/MD003.json) | 9 | 5 | 0 | 0 | draft |
| [MS009](../data/evidence/MS009.json) | 7 | 3 | 0 | 0 | draft |
| [TN003](../data/evidence/TN003.json) | 62 | 3 | 40 | 26 | draft |

## Next research action

The [Shiloh research memo](../docs/research/shiloh.md) preserves competing returns, dated orders, reinforcement phases, and disputed responsibility. No canonical opening strength or effective command-transfer time has been adjudicated.
The [Confederate return audit](../docs/research/shiloh-confederate-returns.md) and [Union availability audit](../docs/research/shiloh-union-availability.md) retain source and population disputes. The [Ohio reinforcement audit](../docs/research/shiloh-ohio-reinforcements.md) separates crossing, landing, formation and participation while preserving conflicting clocks, the untraced 600-person basis, mixed-date estimates and Reed's 7,553/7,552 discrepancy.
The fresh-context Astra xhigh [source review](review-results/TN003-a42f063-astra-xhigh-v1/review.md) checked all 62 claims, 40 quantities, 26 events and 26 supplied scan selections. Of 65 cited source/section pairs, 35 remain text/CSV-only. The [versioned correction pass](../docs/research/shiloh-review-corrections.md) implements estimation provenance, section-specific document dates, same-return dependence and Crittenden arrival wording. Focused review accepted all changed evidence; the [validator follow-up](review-results/TN003-corrections-5e23790-followup-v1/review.md) closed the sole implementation finding. The [feature-admission design](../docs/feature-admission.md) and [13 source-bound cases](../docs/research/shiloh-admission-examples.md) have a separate Astra xhigh [design review](review-results/feature-admission-838189f-astra-xhigh-v1/review.md) with no required corrections. The cases reference 26/62 claims, 27/40 quantities and 8/26 events, emitting zero model rows. Next implement the offline admission validator and complete-frame coverage ledger without promotion. Historical boundary and population mappings still require evidence-use review; no feature is admitted and historical disputes remain open.
Then expand by complete campaign, retaining every unscorable engagement in the coverage denominator.

## Reproduce and inspect

Run `make check` and `make reproduce` from the repository root.
[Evaluation and fold membership](baseline.json), [coverage](quality.json), [run receipt](receipt.json),
[research queue](research-queue.json), [source manifest](../data/sources.json), [methodology](../docs/methodology.md).

Data: Jeffrey B. Arnold, American Civil War Battle Data (CWSAC tables), derived from U.S. National Park Service summaries; CC-BY-4.0 attribution.
[Pinned upstream data](https://github.com/jrnold/acw_battle_data/tree/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data).
