# Primary assessment of the Astra source review

This is the primary agent's reconciliation, separate from the reviewer's own
response. It concerns the frozen `TN003-a42f063-v1` dossier, SHA-256
`1107b7149f9aa3877478e003a01ae2383b5d0729a15d6a90106e427350d49780`.
The reviewer was dispatched as GPT-6 Astra at `xhigh` with fresh context. Its
actual [response](review.md) and [coverage ledger](review-result.json) are
preserved unchanged alongside this assessment.

The [intake validation](intake-validation.json) confirms the exact assignment
IDs, file and source hashes, quoted-passage presence, finding references and
coverage arithmetic: 62/62 claims, 40/40 quantities, 26/26 events and 26/26
supplied scan selections. All three unknowns remain null. Of 65 cited
source/section pairs, 30 have supplied image comparisons and 35 remain
text/CSV-only. Automated checks verify these records' consistency, not the
quality of the reviewer's reasoning or historical truth. The source-based
primary checks below address the four findings, not a second full dossier audit.

## Findings checked against the supplied evidence

### TN003-R1: Estimation status and printed precision

Accept the need for a structured distinction before feature admission. The
existing contract explicitly defines `reported_exact` as precision as written,
not proven accuracy, and the affected records preserve estimates in their notes.
Consequently this is a schema limitation, not evidence that the printed counts
were transcribed incorrectly or that the current records violate their contract.

The primary agent inspected Reed's pinned pp.96,100-101 images and the current
quantity records. The Eighteenth Wisconsin row bears an estimation marker;
McCook and Crittenden carry the approximation marker explained on p.101. The
7,553/7,552 disagreement remains a real source discrepancy. Preserve those
printed values. A future version should distinguish numeric precision from
source-estimated/reconstructed provenance, including totals with estimated parts.
Do not mechanically replace every exact-looking value with a rounded estimate.

### TN003-R2: Dates on mixed-document snapshots

Accept section-scoped date metadata as a needed clarification. Both
`or-ammen-crossing-v1` and `or-nelson-reinforcements-v1` have a source-wide
`document_date` of 1862-04-10. Their selected sections include an undated diary
and compiler material with different or unknown dates. The pinned scope notes
already explain this, and the March quantity retains null exact dates, but the
registry does not express the distinction structurally.

The primary agent checked the source records, snapshot sections and documented
date rules. Current baseline code does not consume `document_date`, so this is
not an existing model-input leak. Address it through versioned metadata that
qualifies the report date and retains null diary/compiler dates; do not rewrite
the frozen registry or infer missing dates from adjacent letters.

### TN003-R3: One return appearing under different dependence labels

Accept the metadata correction. `or-union-return-detail-v2` is tagged `or-grant`,
while `or-union-return-april4-5` and `or-union-return-scan` use `or-union-returns`.
Their parent hash and p.112 locator identify the same underlying return, and
the overlapping 5,463 total is not independent corroboration. The primary agent
verified all three registry entries and their locators. A versioned correction
should align the dependence grouping and explicitly link the common document.
Grouping labels alone still do not establish independence between other sources.

### TN003-R4: Crittenden arrival versus disembarkation

Accept the narrower wording. The `crittenden-arrival-phases` claim says
"landing about 21:00," but its p.355 source says the command reached Pittsburg
Landing at about 9 p.m. and was then debarked as soon as it could be done.
The event note and rationale already separate those stages. The primary agent
checked the complete pinned p.355 passage.

Proposed replacement for the claim's value:

> Crittenden reports reaching Pittsburg Landing about 21:00 April 6, with
> debarkation following as soon as practicable; he reports being conducted to his
> position about 05:00 April 7 and the Third Kentucky Cavalry remaining opposite
> the landing for lack of transport.

No exact completion time for debarkation is established. This is a wording
correction, not a revised troop count or a resolved dawn-strength census.

## Disposition

The source review can satisfy the separate AI review step within its documented
coverage. It does not turn source testimony into historical certainty. The
standing policy does not impose a human reviewer by default; further review is
needed only for specific unresolved requirements or an owner request.

The findings above are accepted for a subsequent versioned correction pass.
This task establishes the reviewer policy and records the actual review and
primary assessment. It does not change the dossier, source registry, frozen
review bundle or model inputs, and no feature is admitted. Preserve the existing
600-person uncertainty, conflicting clocks and return discrepancies.

The useful next implementation is a bounded evidence-contract revision covering
estimation provenance, section-level document dates, the duplicate return's
dependence label and the Crittenden wording, with a new dossier/source version
where needed and focused re-review of the changed fields.

## Repository validation

All 41 tests and the offline contract check passed. `make reproduce`, `make packet`
and `make review-bundle` completed. The generated report now reflects this review;
the dossier, registry, baseline predictions, coverage and research packet remain
byte-identical to evidence commit `a42f063`. The frozen ZIP retains SHA-256
`f1e1f7bc2aec3074b02408649fd29184ba380bfd2486d77f2184341f6aff8a13`.
The baseline remains 23/127 engagements in 13 eligible campaign groups within a
36-campaign frame, with Brier 0.276882 versus 0.250000 for equal odds.
