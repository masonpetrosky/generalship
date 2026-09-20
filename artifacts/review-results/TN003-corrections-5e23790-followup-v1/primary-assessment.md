# Primary assessment of the Shiloh correction pass

The versioned implementation is `54e763905b767570565302b185599535ef12cc20`;
its metadata-validation correction is `5e23790289a9c799dea5aa6706f662a92f3749c6`.
The dossier remains SHA-256
`fb622c81b48110d1d7b25212b5c3f10881c4a7724a9ccbb93ef793816cf100ee`,
and the registry remains SHA-256
`3430c1ef145256fc8edd8638fdf565f7f0c0ae4e5feed237b3cd5db6cf4322e7`.

## Evidence dispositions

The [focused reviewer response](../TN003-corrections-54e7639-astra-xhigh-v1/review.md)
accepted all changed evidence fields. The primary agent agrees after inspecting
the pinned passages and validating the exact source hashes, citation references
and preserved fields.

- **TN003-R1 implemented:** 40 estimation classifications and 49 supporting
  citations. Eleven are explicitly estimated, two are totals with estimated
  components, and 27 have no explicit qualifier for that observation in the
  inspected passage. The latter is not an accuracy claim. Reed's 735, 7,553,
  7,552 and 3,825 retain their printed precision while their estimation is typed;
  the 7,545 and 17,918 totals retain their estimated-component provenance.
- **TN003-R2 implemented:** 15 historical section dates, nine dated and six null,
  with two explicit editorial exclusions. Ammen's diary and Nelson's return
  sections do not inherit the April 10 report dates. No event/knowledge date is
  imputed.
- **TN003-R3 implemented:** the new OR p.112 detail metadata shares the return's
  dependence group and image. The original record and raw file are preserved;
  the new metadata adds no historical witness.
- **TN003-R4 implemented:** the claim separates arrival at Pittsburg Landing
  from subsequent debarkation. No completion time or new readiness estimate is
  supplied; p.355 remains a text-only check.

## Validator finding and correction

The focused review found **TN003-C1**, a P2 omission-handling gap. The primary
agent independently reproduced both bypasses: deleting `supersedes` skipped
predecessor binding, and deleting the section map allowed a false diary-date
fallback. This was a defect in validation, not a defect in the committed evidence.

The fix requires `supersedes`, `revision_kind` and `revision_note` together,
with a textual nonempty note and valid predecessor. Section metadata without
its date map fails before validation or date lookup can use a source-wide date.
Legitimate standalone legacy date notes remain valid. The new mutation tests
exercise the validator, helper and ordinary CLI. All **52 tests** and the
offline contract check pass. The [same reviewer's bounded follow-up](review.md)
accepted commit `5e23790` and closed TN003-C1 with no further findings. Its
independent mutation probes reject all four original CLI cases while preserving
15 section dates, two editorial nulls and four legacy date notes. The primary
agent verified the returned commit/input hashes and agrees with this disposition.

## Preservation and remaining limits

All 50 prior source entries and raw files, every pre-existing quantity field,
all 26 events, the three null unknowns, historical disputes and replacement
boundaries are preserved. The previous dossier is archived with its original
hash. There are now 53 metadata entries for the same 50 raw files. Migration
replay is deterministic and idempotent and rejects divergent edits.

The initial source review and both actual focused-review responses are retained
as separate records; acceptance must never overwrite a corrections-needed
response. The focused review inspected 22 supplied scan selections. It is not a
second complete dossier audit: 35 of the original 65 cited source/section pairs
remain text/CSV-only, and no new image or historical source has been fetched.

The draft remains 62 claims, 40 quantities and 26 events. No feature is admitted.
Baseline predictions are byte-identical: 23/127 engagements in 13 eligible
campaign groups within a 36-campaign frame, Brier 0.276882 versus 0.250000 for
equal odds. Next design a reviewed feature-admission contract that preserves
these uncertainties and explicitly separates predictive inputs from causal
attribution.
