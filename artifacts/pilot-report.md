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
| [KY005](../data/evidence/KY005.json) | 11 | 1 | 0 | 0 | draft |
| [KY006](../data/evidence/KY006.json) | 11 | 2 | 0 | 0 | draft |
| [MD001](../data/evidence/MD001.json) | 11 | 2 | 0 | 0 | draft |
| [MD003](../data/evidence/MD003.json) | 9 | 5 | 0 | 0 | draft |
| [MO012](../data/evidence/MO012.json) | 11 | 3 | 0 | 0 | draft |
| [MS009](../data/evidence/MS009.json) | 7 | 3 | 0 | 0 | draft |
| [MS016](../data/evidence/MS016.json) | 12 | 2 | 0 | 0 | draft |
| [NC002](../data/evidence/NC002.json) | 9 | 1 | 0 | 0 | draft |
| [NC003](../data/evidence/NC003.json) | 9 | 2 | 0 | 0 | draft |
| [NC004](../data/evidence/NC004.json) | 10 | 2 | 0 | 0 | draft |
| [NC005](../data/evidence/NC005.json) | 10 | 2 | 0 | 0 | draft |
| [NC006](../data/evidence/NC006.json) | 9 | 3 | 0 | 0 | draft |
| [TN001](../data/evidence/TN001.json) | 10 | 1 | 0 | 0 | draft |
| [TN002](../data/evidence/TN002.json) | 11 | 1 | 0 | 0 | draft |
| [TN003](../data/evidence/TN003.json) | 62 | 3 | 40 | 26 | draft |
| [TN004](../data/evidence/TN004.json) | 10 | 2 | 0 | 0 | draft |
| [VA008](../data/evidence/VA008.json) | 10 | 5 | 0 | 0 | draft |
| [VA009](../data/evidence/VA009.json) | 9 | 2 | 0 | 0 | draft |
| [VA010](../data/evidence/VA010.json) | 9 | 3 | 0 | 0 | draft |
| [VA011](../data/evidence/VA011.json) | 9 | 2 | 0 | 0 | draft |
| [VA012](../data/evidence/VA012.json) | 10 | 2 | 0 | 0 | draft |
| [VA013](../data/evidence/VA013.json) | 9 | 2 | 0 | 0 | draft |
| [VA014](../data/evidence/VA014.json) | 9 | 2 | 0 | 0 | draft |
| [VA015](../data/evidence/VA015.json) | 10 | 3 | 0 | 0 | draft |
| [VA016](../data/evidence/VA016.json) | 10 | 3 | 0 | 0 | draft |
| [VA017](../data/evidence/VA017.json) | 9 | 2 | 0 | 0 | draft |
| [VA018](../data/evidence/VA018.json) | 9 | 2 | 0 | 0 | draft |
| [VA019](../data/evidence/VA019.json) | 10 | 2 | 0 | 0 | draft |
| [VA020](../data/evidence/VA020.json) | 9 | 2 | 0 | 0 | draft |
| [VA020A](../data/evidence/VA020A.json) | 10 | 2 | 0 | 0 | draft |
| [VA020B](../data/evidence/VA020B.json) | 10 | 2 | 0 | 0 | draft |
| [VA021](../data/evidence/VA021.json) | 10 | 3 | 0 | 0 | draft |
| [VA100](../data/evidence/VA100.json) | 10 | 3 | 0 | 0 | draft |

## Admission proposal checks

The offline validator retains all 127 engagements / 36 campaign groups in its [coverage ledger](admission-check.json).
It checks 40 Shiloh troop observations: 18 blocked, 22 excluded, 0 eligible candidates, and 0 invalid.
There are 0 complete candidate rows and 0 promoted rows. Missing mappings remain unknown; no canonical opening force is inferred.
The ledger separates dossier availability, candidate status, side coverage and baseline eligibility. These counts are mechanical checks, not historical adjudication or forecast improvement.

## Next research action

Prioritize comparable first-pass dossiers across the complete frozen cohort. 33 engagements have dossiers; 94 have none. Dossier presence, separate review, baseline eligibility and feature admission are different measures.
The [Peninsula first pass](../docs/research/peninsula-first-pass-v1.md) adds all 16 frozen records: 152 claims, 39 explicit unknowns and one or two source families per record. Casualty differences, opening populations and combined/component overlap remain visible; separate Astra xhigh review accepted all 152 claims and 209 citations with no required corrections. Next take Jackson's complete seven-engagement Valley Campaign. Earlier passes and reviews remain in the [current roadmap](../docs/roadmap.md).
Use the [bounded first-pass protocol](../docs/methodology.md#research-depth-and-coverage): up to three source families per battle and one targeted follow-up for the most consequential gap. Keep unsupported dimensions unknown, move to the next engagement, and review by campaign. Deeper work requires a concrete decision and stopping point or an explicit owner request.
Shiloh's Agate and overnight-provenance investigations are parked. The [completed research and review history](../docs/roadmap.md#milestone-1--first-independently-reviewed-campaign-dossiers-in-progress) retains all findings and unresolved questions; neither further article collation nor original-newspaper recovery is the next task. No historical feature is admitted by this change in research priority.

## Reproduce and inspect

Run `make check` and `make reproduce` from the repository root.
[Evaluation and fold membership](baseline.json), [coverage](quality.json), [run receipt](receipt.json),
[research queue](research-queue.json), [source manifest](../data/sources.json), [methodology](../docs/methodology.md).

Data: Jeffrey B. Arnold, American Civil War Battle Data (CWSAC tables), derived from U.S. National Park Service summaries; CC-BY-4.0 attribution.
[Pinned upstream data](https://github.com/jrnold/acw_battle_data/tree/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data).
