# Shiloh review corrections, 2026-09-20

This bounded migration implements TN003-R1–R4 from the actual
[Astra xhigh source review](../../artifacts/review-results/TN003-a42f063-astra-xhigh-v1/review.md)
and [primary assessment](../../artifacts/review-results/TN003-a42f063-astra-xhigh-v1/primary-assessment.md).
It changes evidence representation, not troop counts or model inputs. The
current draft remains **62 claims, 40 quantities, 26 events and three null
unknowns**. The [focused Astra review](../../artifacts/review-results/TN003-corrections-54e7639-astra-xhigh-v1/review.md)
accepted every changed evidence field and identified one validator gap,
TN003-C1. Its code correction is implemented and awaits a bounded follow-up.

## Changes and source support

**TN003-R1 — estimation provenance.** Dossier schema v3 separates
`estimation_status` from `estimate_kind`, with an explanatory note and exact
estimation citations. All 40 observations were classified from their pinned
passages: 11 explicitly estimated, two aggregates containing estimates, and 27
reported without an explicit qualifier for that observation in the inspected
passages. The last category does not mean measured or historically exact.

The four reviewed explicit estimates are Wisconsin's 735 (Reed p.96, asterisk
defined on p.97), McCook's 7,553 (p.100, marker defined on p.101) and 7,552
(p.102, quoted estimate in p.111 note j), and Crittenden's 3,825 (p.101).
The Sixth Division's 7,545 and Ohio army's 17,918 contain identified estimates;
their primary rows and qualifying component/footnote passages are linked.
The related explicit Wagner estimate and the already quoted “about”/probable
figures receive the same typed treatment. Force's unqualified “sixty-five hundred”
retains the prior `approximate` precision label but is not labeled explicitly
estimated merely because it is round. Source IDs, sections and exact passages
are in each quantity's `estimation_citations`; the registry retains their hashes.

**TN003-R2 — section dates.** `or-ammen-crossing-v2` and
`or-nelson-reinforcements-v2` reuse their original raw files. April 10 dates
Ammen's report heading/p.328 and Nelson's report sections through p.325. Ammen's
four diary sections and Nelson's two return sections remain null. The maps cover
all 15 historical sections: nine dated and six null. Two local transcription-scope
sections are explicitly editorial. Source-wide dates are null. Dates of events,
returns, publication and command knowledge remain distinct.

**TN003-R3 — same return.** `or-union-return-detail-v3` assigns the OR p.112
detail to `or-union-returns` and links `or-union-return-scan`, matching the existing
summary and image. Both transcripts show the 5,463 subtotal on the same parent
page. They cannot count as independent corroboration. No unseen regimental
return or missing omission identity has been reconstructed.

**TN003-R4 — arrival before debarkation.** Crittenden's claim now says his
command reached Pittsburg Landing about 21:00, with debarkation following as
soon as practicable. His report says “We reached Pittsburg Landing at about 9
o'clock p. m.” and then describes the debarkation order. The original pinned
`or-crittenden-reinforcements-v1`, section `p355`, SHA-256
`235b01590b21cbf161ebe63162db73cf45184bd234f4025deae555040f317391`
supports that sequence. No completion time or revised readiness claim is inferred.
This passage remains text-only in the supplied scan sample.

## Versioning and reproduction

The previous dossier is archived byte-for-byte as
[`TN003.v5.json`](../../data/evidence/history/TN003.v5.json), SHA-256
`1107b7149f9aa3877478e003a01ae2383b5d0729a15d6a90106e427350d49780`.
The original 50 registry entries remain unchanged. Three new metadata entries
raise the registry to **53 entries representing the same 50 raw files**; each
binds its predecessor's complete metadata hash and retains its raw path/hash.
Twenty-four claim citation source IDs now select the corrected metadata. Quotes,
locators, periods, recorded dates, quantity values and events are unchanged.

The [machine-readable migration ledger](../../artifacts/migrations/TN003-review-corrections-v1.json)
lists all source aliases, metadata/input/output hashes, 40 estimation statuses
and the exact wording change. The [migration script](../../scripts/migrate_shiloh_review_corrections.py)
rebuilds these outputs from the frozen local snapshots and actual review:

```sh
python3 scripts/migrate_shiloh_review_corrections.py
make check
make reproduce
make packet
make review-bundle
```

The migration is offline and idempotent. It rejects divergent live inputs or
existing outputs before writing; it is not a general overwrite command for
later research. The original review response, assignment, coverage, source
bundle and its ZIP remain immutable. `make review-bundle` continues to build
that historical assignment, not a new review of the changed dossier.

## Validation and limits

All 52 tests and the offline contract check pass. New regression checks cover
estimated integers with exact printed precision, wrong-page qualifiers, schema
downgrade, section-date omissions/fallbacks, version binding, facsimile dependence,
migration replay/idempotence and refusal to overwrite divergent edits. They also
compare every prior source entry, quantity field, event and claim outside the
explicit migration against its archived input.

The focused review checked 40 classifications, 49 estimation citations, 15
section dates, 24 citation-ID replacements and 22 supplied scan selections.
TN003-C1 exposed two ways to bypass validation by deleting a required metadata
field. The fix makes revision fields reciprocal and rejects an orphaned
`editorial_sections` declaration before either validation or date lookup can
fall back to the report date. Mutation tests exercise the ordinary CLI as well
as the helper, while preserving legitimate legacy date notes. The original
finding and response remain unchanged; follow-up acceptance is recorded separately.

This is a representation correction. Historical disputes TN003-D1–D7, the
600-person basis, conflicting clocks, 7,553/7,552, missing original returns and
command boundaries remain unresolved. The original scan review covered 30/65
cited source/section pairs; the other 35 remain text/CSV-only. No additional page
images, independent historical testimony, enriched features or causal estimates
are introduced. The baseline still covers **23/127 engagements in 13 eligible
campaign groups within the 36-campaign frame**: Brier **0.276882**, worse than
equal odds at **0.250000**.
