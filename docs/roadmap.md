# Roadmap and current handoff

## Milestone 0 — Working research foundation (complete)

- Public repository, Python package/CLI, local test and reproduction commands.
- Frozen 127-engagement Civil War cohort with complete source campaign groups.
- Pinned inputs, attribution, integrity checks, and exclusion accounting.
- Force-size logistic baseline with campaign-held-out evaluation and comparators.
- Three draft evidence dossiers and a prepared Shiloh research assignment.
- Deterministic coverage, predictions, research queue, report, and hash receipt.

“Complete” applies to this infrastructure milestone only. Historical validation,
AI extraction quality, command attribution, and improved generalship estimation
have not been established.

## Milestone 1 — First independently reviewed campaign dossiers (in progress)

The first [Shiloh source-enrichment pass](research/shiloh.md) is complete **as a
draft**, with 22 claims, 12 typed troop observations and seven chronology events.
Ten source artifacts from that pass include original reports, orders, return
transcriptions, two independently authored histories, and two facsimiles.
The subsequent [Confederate return audit](research/shiloh-confederate-returns.md)
inspected reports 136/137 and added four versioned source artifacts. The
[Union availability audit](research/shiloh-union-availability.md) adds 12 artifacts
and a unit-by-phase table. The [Ohio reinforcement audit](research/shiloh-ohio-reinforcements.md)
adds 17 artifacts and separates Savannah/opposite-bank arrival, crossing, landing,
formation and participation. The current draft has **62 claims, 40 troop
observations and 26 events**. Five preceding revisions are archived. Neither
canonical opening strengths nor effective command-transfer times have been
adjudicated. A separate fresh-context Astra `xhigh` source review is now recorded;
the dossier remains a draft. The four accepted corrections are implemented in
[schema v3 and versioned metadata](research/shiloh-review-corrections.md). Focused
review accepted the evidence changes; its sole validator finding was fixed and
accepted in the follow-up.

The versioned correction pass implements the four findings accepted in the
[primary assessment](../artifacts/review-results/TN003-a42f063-astra-xhigh-v1/primary-assessment.md):
separate estimation provenance from printed precision, scope document dates to
individual report/diary/compiler sections, align dependence metadata for the same
OR p.112 return, and distinguish Crittenden's arrival from later debarkation.
The frozen evidence and review are preserved and the migration is documented.
The [focused review and follow-up](research/shiloh-review-corrections.md#validation-and-limits)
are complete under the [standing subagent policy](../AGENTS.md).
The [feature-admission design](feature-admission.md) and
[13 source-bound Shiloh cases](research/shiloh-admission-examples.md) now have a
separate Astra `xhigh` design review with no required corrections. See the
[actual review and primary assessment](../artifacts/review-results/feature-admission-838189f-astra-xhigh-v1/primary-assessment.md).
The examples reference 26/62 claims, 27/40 quantities and 8/26 events and admit
zero features. The runtime admission mechanism is still unimplemented.

Start now by implementing the offline validator and complete-frame coverage
ledger against this reviewed specification, initially without promotion. Use
explicit synthetic fixtures to exercise positive admission and the required
rejection cases. Preserve the current baseline. Historical feature admission
requires further boundary/population evidence-use review and an immutable release
manifest; design acceptance does not grant that approval.

The [actual AI review](../artifacts/review-results/TN003-a42f063-astra-xhigh-v1/review.md)
covers 62/62 claims, 40/40 quantities, 26/26 events and 26/26 supplied scan
selections. It found no substantive transcription mismatch in those selections;
35 of 65 cited source/section pairs remain text/CSV-only. This purposive sample
does not estimate an extraction-error rate or establish historical truth.
The [frozen handoff](research/shiloh-review-handoff.md) remains reproducible with
`make review-bundle`; actual review and dispatch records are stored separately.
The crossing clocks, handbook's 600-person basis, mixed-date reconstruction and
Reed's 7,553/7,552 discrepancy remain open. The earlier full omission mapping,
ten-man comparison residual, and Michigan narrative/table and casualty-day
conflicts also remain open.
The Confederate reports' differences from p.396, report 137's two inspected infantry
subtotal discrepancies, and the accounting of late/detached formations remain
explicit questions for historical review. The updated packet is
available with `python3 -m generalship packet TN003`. After the validator and
coverage ledger, continue evidence work across all pilot engagements in the same
source campaign, including Fort Henry, Fort Donelson, and Corinth.
Use Antietam to test outcome ambiguity and Champion Hill to test inherited orders
versus commander-created circumstances.

Deliverables:

- Campaign records and resolved commander/army identities (Shiloh now has local
  entity IDs and phase records; cross-engagement identity resolution remains).
- Source-dependent alternative estimates and a typed quantity schema (v3 now
  implemented and reviewed for Shiloh; historical reconciliation remains).
- Explicit replacement boundaries and contemporary information sets.
- Named separate review records and an extraction-error audit (Shiloh's bounded
  AI review is recorded; broader transcription coverage remains incomplete).
- A feature-admission mapping tied to immutable sources and dossier versions.

Acceptance: every admitted fact has traceable evidence, source alternatives remain
visible, reviewers agree on population/timing or retain a dispute, and the v1
opening profile excludes post-boundary state and participation, including indirect
use through transformations.

## Milestone 2 — Baseline audit and expanded coverage

Document an exact reproduction route for the original Arsht analysis and access/
redistribution terms. Keep that track separate from the current reduced baseline.
Enrich the full frozen pilot by complete campaigns; add credible troop estimates
without selecting only famous or easily scored battles. Audit coverage by outcome,
commander, campaign, engagement scale, and evidence quality.

Acceptance: an immutable cohort, exclusion ledger, independent extraction sample,
and paired comparison rows defined before model selection. Sparse evidence must
not quietly turn into mediocre commander scores.

## Milestone 3 — Enriched prediction and command inference

Predefine the campaign estimand and causal graph. Add justified conditions and
opponent/army context, investigate commander-assignment confounding, and fit
hierarchical partial-pooling alternatives only when coverage supports them.
Evaluate by grouped held-out campaigns and a locked final test set; check temporal
generalization separately. Report calibration and clustered uncertainty.

Acceptance: improved out-of-sample prediction on comparable rows, robust source
and coding sensitivities, and a separately defended causal interpretation. A
familiar-looking greatest-generals list is not evidence of correctness.

## Milestone 4 — Inspectable research interface

Create the commander → campaign → engagement → assumption → passage explorer.
Show cumulative results, opportunity-adjusted estimates, coverage, uncertainty,
and source disputes separately. Provide scenario toggles and explain what changes.
No battle/campaign double counting and no unqualified cross-era rankings.

## Deferred implementation choices

Separate AI reviews use GPT-6 Astra at `xhigh` effort under the owner-set repository
policy. Broader research authoring and paid automation policies remain undecided.
Evidence packets also work with the user's chosen external researcher. LangExtract or another
extraction library can be evaluated later against a measured source-alignment need.
No web framework or hosting stack is selected before the evidence contract matures.
Use local tests; no hosted workflow is configured.
