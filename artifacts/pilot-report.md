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

## Admission proposal checks

The offline validator retains all 127 engagements / 36 campaign groups in its [coverage ledger](admission-check.json).
It checks 40 Shiloh troop observations: 18 blocked, 22 excluded, 0 eligible candidates, and 0 invalid.
There are 0 complete candidate rows and 0 promoted rows. Missing mappings remain unknown; no canonical opening force is inferred.
The ledger separates dossier availability, candidate status, side coverage and baseline eligibility. These counts are mechanical checks, not historical adjudication or forecast improvement.

## Next research action

The [Shiloh research memo](../docs/research/shiloh.md) preserves competing returns, dated orders, reinforcement phases, and disputed responsibility. No canonical opening strength or effective command-transfer time has been adjudicated.
The [Confederate return audit](../docs/research/shiloh-confederate-returns.md) and [Union availability audit](../docs/research/shiloh-union-availability.md) retain source and population disputes. The [Ohio reinforcement audit](../docs/research/shiloh-ohio-reinforcements.md) separates crossing, landing, formation and participation while preserving conflicting clocks, the untraced 600-person basis, mixed-date estimates and Reed's 7,553/7,552 discrepancy.
The fresh-context Astra xhigh [source review](review-results/TN003-a42f063-astra-xhigh-v1/review.md) checked all 62 claims, 40 quantities, 26 events and 26 supplied scan selections. Of 65 cited source/section pairs, 35 remain text/CSV-only. The [versioned correction pass](../docs/research/shiloh-review-corrections.md) implements estimation provenance, section-specific document dates, same-return dependence and Crittenden arrival wording. Focused review accepted all changed evidence; the [validator follow-up](review-results/TN003-corrections-5e23790-followup-v1/review.md) closed the sole implementation finding. The [feature-admission design](../docs/feature-admission.md) and [13 source-bound cases](../docs/research/shiloh-admission-examples.md) have a separate Astra xhigh [design review](review-results/feature-admission-838189f-astra-xhigh-v1/review.md) with no required corrections. The cases reference 26/62 claims, 27/40 quantities and 8/26 events, emitting zero model rows. The [offline validator](../docs/admission-validator.md) now checks all 40 Shiloh troop observations and retains the complete frame without promotion. The Astra xhigh [implementation review and focused follow-up](review-results/admission-implementation-1264e21-followup-v1/primary-assessment.md) accepted fixes for observation reuse, joint scenario coverage and calendar-date ordering. All 82 tests pass. Historical boundary and population mappings still require evidence-use review; no feature is admitted and historical disputes remain open.
The separate [opening-boundary/population proposal](../docs/research/shiloh-opening-boundary-v1.md) has an explicit [v2 ledger](admission/shiloh-opening-v2-check.json): 7 blocked / 33 excluded across the same 40 observations and complete frame, with zero complete or promoted rows. The default v1 ledger above is unchanged. Its [Astra xhigh review and primary assessment](review-results/shiloh-opening-330599b-astra-xhigh-v1/primary-assessment.md) accept the bounded proposal with one nonblocking precision clarification. First-contact identification, the mapped area and both full populations remain unresolved. The [contact-and-location packet](../docs/research/shiloh-contact-location-v1.md) now compares nine participant reports, 16 visually inspected book pages and two maps, with 14 attributed assertions and no input promotion. Astra xhigh reviewed the packet; two literal transcription errors are [corrected in versioned sources](../docs/research/shiloh-contact-location-corrections-v1.md) with primary verification and no historical assertion change. The [April 3–5 contact-chain packet](../docs/research/shiloh-precontact-segmentation-v1.md) recommends April 3–4 as precursors using return/reset evidence, with weaker event-specific closure for April 3. Ten assertions bind 24 passage anchors across 19 inspected pages. Its separate Astra xhigh review found two literal wording errors in one Jordan passage, [corrected in a new source version](../docs/research/shiloh-precontact-segmentation-corrections-v1.md) and closed by primary image verification. The [Howell trace](../docs/research/shiloh-howell-trace-v1.md) now records Medkirk's retrospective account, disputed testimony selections in Worthington, Reed's 1903 printing, one plaque transcription and two archival guides: 7 assertions / 14 anchors, 12 inspected pages and 3 HTML sources, with 133 registry entries / 130 raw paths at that stage. Separate Astra xhigh [review and primary assessment](review-results/shiloh-howell-67b5c30-astra-xhigh-v1/primary-assessment.md) accepted the bounded Howell packet with no required corrections. The participant-to-Reed link and Saturday-to-Sunday continuity remain unresolved. The [regimental and post comparison](../docs/research/shiloh-regimental-posts-v1.md) adds Reid's overnight lead on an unnamed 46th Ohio picket line, two 72d narratives, disputed post distances and the map cited by Medkirk. Seven assertions bind 21 anchors / 19 source-section pairs across 16 inspected pages; the prepared registry has 151 entries / 148 raw paths. Separate Astra xhigh review found two literal map transcription errors, [corrected in a new source version](../docs/research/shiloh-regimental-posts-corrections-v1.md) and closed by primary image verification. The current registry has 152 entries / 149 raw paths. The map depicts April 6–7; no Saturday post match, continuous firing chain or feature admission is established. Next trace the contributor or original evidence behind Reid II p.286's overnight narrative. First-contact timing, map control, ford guards and the afloat rule remain open.
Then expand by complete campaign, retaining every unscorable engagement in the coverage denominator.

## Reproduce and inspect

Run `make check` and `make reproduce` from the repository root.
[Evaluation and fold membership](baseline.json), [coverage](quality.json), [run receipt](receipt.json),
[research queue](research-queue.json), [source manifest](../data/sources.json), [methodology](../docs/methodology.md).

Data: Jeffrey B. Arnold, American Civil War Battle Data (CWSAC tables), derived from U.S. National Park Service summaries; CC-BY-4.0 attribution.
[Pinned upstream data](https://github.com/jrnold/acw_battle_data/tree/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data).
