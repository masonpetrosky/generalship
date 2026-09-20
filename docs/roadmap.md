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
zero features. An [offline validator and coverage ledger](admission-validator.md)
now implements the non-promoting checks. Astra `xhigh` implementation review and
[focused follow-up](../artifacts/review-results/admission-implementation-1264e21-followup-v1/primary-assessment.md)
are complete: three structural findings were fixed and accepted. All 82 tests
pass; no historical feature admission is implied.

The validator checks all 40 Shiloh troop observations: 18 blocked and 22 excluded,
with zero complete rows across the retained 127-engagement / 36-campaign frame.
Synthetic fixtures exercise positive reviewed-manifest replay and rejection cases.
The current baseline remains unchanged. A separate
[opening-boundary/population proposal](research/shiloh-opening-boundary-v1.md)
now revisits all 18 blocked mappings using 51 pinned passage anchors. Its explicit
v2 ledger has 7 blocked / 33 excluded; v1 remains unchanged. Eleven direct-use
exclusions follow timing/population evidence; zero complete rows are created.
Astra `xhigh` [accepted the bounded proposal](../artifacts/review-results/shiloh-opening-330599b-astra-xhigh-v1/primary-assessment.md)
with one nonblocking precision clarification. The first-contact identification,
exact area and full memberships remain unresolved.

The [contact-and-location packet](research/shiloh-contact-location-v1.md) now
compares nine full participant reports (OCR context), 16 visually inspected
book pages and two maps cataloged to 1862. Its 14 attributed assertions and
two map-reading records preserve conflicting first-fire clocks, prior April 4
contact and map phase limits. There are 32 new source records; the draft dossier
and both admission proposals remain unchanged. Separate Astra `xhigh` review
found two literal errors; [versioned corrections and primary verification](research/shiloh-contact-location-corrections-v1.md)
close both findings without changing the historical assertions. There are now
87 source entries / 84 raw paths at that correction. The new
[April 3–5 contact-chain packet](research/shiloh-precontact-segmentation-v1.md)
adds 24 source records and recommends treating
April 3–4 as precursors based on return/reset evidence. Its explicit continuity
rule leaves the Saturday Howell link unresolved and qualifies weaker April 3
closure. Separate Astra `xhigh` review found two literal wording errors in one
Jordan passage, now [corrected in a new source version](research/shiloh-precontact-segmentation-corrections-v1.md)
and closed by primary verification. The registry at that correction was 112 entries / 109 raw paths.
The [Howell trace](research/shiloh-howell-trace-v1.md) adds Medkirk's retrospective
account, Worthington's disputed testimony selections, the earlier Reed printing,
one plaque transcription and two archival guides. Seven assertions bind 14
anchors; that packet's registry has 133 entries / 130 raw paths. No participant-to-Reed
attribution or Saturday-to-Sunday continuity is established, and no historical
feature is admitted. Original proceedings and commission correspondence remain
uninspected archival targets.
Separate Astra `xhigh` [review and primary assessment](../artifacts/review-results/shiloh-howell-67b5c30-astra-xhigh-v1/primary-assessment.md)
accepted the bounded Howell packet with no required corrections; historical
provenance and continuity questions remain open.

The [regimental and post comparison](research/shiloh-regimental-posts-v1.md)
adds an overnight lead from Reid's 46th Ohio narrative but no located post or
continuous firing chain. The inspected 72d narratives skip Saturday; their omission
is not quiet. Worthington's distances remain disputed and approximate, and the
map cited by Medkirk depicts April 6–7. Seven assertions bind 21 anchors / 19
source-section pairs across 16 inspected pages. All prior records are preserved;
the prepared registry has 151 entries / 148 raw paths. Next trace the contributor or
underlying evidence for Reid II p.286. Map control, full unit locations,
ford-guard identities and the transport/afloat rule remain unresolved, followed
by population/return evidence for the seven blockers. Continue across the complete
source campaign.
Separate Astra `xhigh` review covered all 7 assertions, 21 anchors and 16 images.
Two literal map findings are [corrected in a new source version](research/shiloh-regimental-posts-corrections-v1.md)
and closed by primary verification; the current registry has 152 entries / 149
raw paths. Historical interpretations and all model/admission inputs are unchanged.

Historical admission still requires actual evidence-use review of a complete
proposal and an immutable release manifest; this partial proposal is no release.

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
