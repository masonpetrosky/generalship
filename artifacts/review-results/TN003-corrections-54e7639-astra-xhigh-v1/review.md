# Focused Shiloh correction review

**Conclusion: corrections needed.** The committed evidence changes are source-consistent; one material validation gap remains (TN003-C1). No troop value, estimation classification, historical date, or claim wording needs another source-driven correction in this bounded review.

Reviewer: AI task `/root/shiloh_corrections_review`, configured `gpt-6-astra`, `xhigh`, fresh context, no delegation. Date: 2026-09-20.

Reviewed commit: `54e763905b767570565302b185599535ef12cc20` against `ba5571fa8bd3efe9eb8988d4496aa38ca9a87296`.

Verified dossier SHA-256: `fb622c81b48110d1d7b25212b5c3f10881c4a7724a9ccbb93ef793816cf100ee`. Registry SHA-256: `3430c1ef145256fc8edd8638fdf565f7f0c0ae4e5feed237b3cd5db6cf4322e7`. Exact input, source and image hashes, all per-quantity decisions and locator checks are preserved in [review-result.json](review-result.json).

## TN003-C1 — reject partial metadata contracts (P2)

Both new contracts are gated only by the field whose presence they must protect. A metadata_only record with revision_kind/revision_note but no supersedes skips predecessor binding. A section-dated record retaining editorial_sections and its note but missing document_dates_by_section skips complete-section/null-fallback validation; restoring April 10 then makes the diary appear dated. The committed registry is correct. The ordinary offline check accepts these malformed future edits, so migration idempotence alone does not enforce the documented source contract.

Locations: `generalship/sources.py:69–90` (conditional validation) and `:54–66` (date fallback), at the reviewed commit.

This reproduces on the exact reviewed implementation:

```python
from copy import deepcopy
from pathlib import Path
from generalship.sources import source_registry, validate_source_metadata, source_document_date
root = Path(".")
registry = source_registry(root)
# Case A: one omitted field defeats predecessor binding.
a = deepcopy(registry)
del a["or-ammen-crossing-v2"]["supersedes"]
a["or-ammen-crossing-v1"]["document_date"] = None
validate_source_metadata(root, a)  # incorrectly succeeds
# Case B: an omitted map defeats the null diary date.
b = deepcopy(registry)
del b["or-ammen-crossing-v2"]["document_dates_by_section"]
b["or-ammen-crossing-v2"]["document_date"] = "1862-04-10"
validate_source_metadata(root, b)  # incorrectly succeeds
assert source_document_date(b["or-ammen-crossing-v2"], "p334-diary") == "1862-04-10"
```

With both omissions and the restored source-wide date serialized in an isolated `/tmp` checkout, `python3 -m generalship check` also exits **0**. Raw file hashes still match, so they cannot catch the incorrect metadata. Current committed records themselves are correct, and the bounded migration rejects a divergent registry; the issue affects the normal validation/helper path outside that migration.

Required correction:

1. Treat supersedes, revision_kind and revision_note as one contract: if any is present, require all, a nonempty textual note, valid metadata_only kind, and a valid differently named predecessor with matching full metadata hash and unchanged raw fields. Keep legacy entries with none of these fields valid.
2. Reject editorial_sections without document_dates_by_section in validate_source_metadata and source_document_date before legacy fallback. Continue checking mapped nulls and full historical-section coverage. Do not require a map merely because document_date_note exists: legacy Confederate scans have legitimate standalone date notes.
3. Add mutation regressions for omitted supersedes, omitted entire date map, wrong source-wide date after map omission, and direct helper calls on malformed partial metadata; exercise the ordinary check path. Preserve the three existing records and all raw bytes.

## Original findings

| Finding | Disposition | Evidence conclusion |
|---|---|---|
| TN003-R1 | accepted | 40/40 source-consistent estimation classifications and 49/49 passage citations; printed precision and values preserved. Schema v3 checks and backward compatibility are meaningful. |
| TN003-R2 | data accepted contract correction needed | All 15 historical section dates and both editorial exclusions are correct. Partial-field handling can reinstate false diary-date fallback; see TN003-C1. |
| TN003-R3 | data accepted shared revision contract correction needed | Same p.112 return correctly shares group and image with preserved old entries. The general metadata_only predecessor contract can be bypassed by omitted supersedes; see TN003-C1. |
| TN003-R4 | accepted | Updated wording matches the p.355 reach-then-debark sequence and about-05:00 positioning, with cavalry exclusion from p.354. No completion time inferred; p.355 remains image-unverified. |

## Actual coverage and preservation

I inspected all **40/40** estimation classifications and **49/49** estimation-citation occurrences (22 unique source/locator pairs), including table context and cross-page footnotes. The split is **11 explicit estimates, 2 aggregates containing estimates, 27 without an explicit qualifier in the supplied passage**. Force’s unqualified sixty-five hundred correctly remains separate from the adjacent about clauses. Reed’s p.93 detachment asterisks are correctly distinguished from the pp.96–97 estimation asterisks. Roundness alone is not treated as evidence of estimation.

I checked **3/3** source revisions, **15/15** historical section dates (**9 dated, 6 null**), both editorial exclusions, all **24/24** claim citation source-ID replacements, and the one changed Crittenden sentence. Ammen’s report and diary remain distinct; Nelson’s report, action table and March abstract retain their distinct date roles. OR p.112 summary/detail/image share the same return identity and current dependence group.

Visual coverage is **22 of the 26 supplied page selections**, restricted to the relevant rows, markers, dates and passages listed below. This is not a renewed certification of every cell or a complete historical-dossier audit.

| Page image | Inspected scope |
|---|---|
| `data/raw/shiloh/reed-1909-union-p96-facsimile-v1.png` | Eighteenth Wisconsin 735 and its asterisk; estimated components of Sixth Division. |
| `data/raw/shiloh/reed-1909-union-p97-facsimile-v1.png` | Sixth Division 7,545 and * Estimated footnote. |
| `data/raw/shiloh/reed-reinforcement-p100-facsimile-v1.png` | April 30 9,118 return separated from marked April 7 7,553; Nelson March return heading. |
| `data/raw/shiloh/reed-reinforcement-p101-facsimile-v1.png` | 5,535 return and 4,541 report; Crittenden 3,825 marker; * Approximated, Note j; missing return notes. |
| `data/raw/shiloh/reed-reinforcement-p102-facsimile-v1.png` | Wagner 2,000 estimated late arrival; 7,552 recap and 17,918 total. |
| `data/raw/shiloh/reed-1909-union-p93-facsimile-v1.png` | Detachment asterisks, 1,727 and 5,837; Ohio regiment/cavalry return rows. Asterisks here do not mean estimated. |
| `reviews/TN003-a42f063-v1/pages/reed-p111.png` | Estimation note j including McCook 7,552 and mixed return dates; Sixth Division arrival notes. Confederate notes below j were not audited. |
| `data/raw/shiloh/or-union-return.png` | Same-return identity, Sixth Division rows and 5,463, grand total 44,895, Third Division 7,564, compiler omissions. |
| `reviews/TN003-a42f063-v1/pages/or-p323.png` | Nelson report heading and April 10 dateline; crossing/action paragraphs. |
| `reviews/TN003-a42f063-v1/pages/or-p324.png` | Nelson report continuation: night, morning and artillery passages; no separate document date. |
| `data/raw/shiloh/or-reinforcement-p326-facsimile-v1.png` | Report signature, attached action table including 380 and 4,541, compiler/cavalry footnotes, separate April 12 letter. |
| `data/raw/shiloh/or-reinforcement-p327-facsimile-v1.png` | Separate April 16 letter; March abstract 6,724 and staff note; Ammen report April 10 heading. |
| `reviews/TN003-a42f063-v1/pages/or-p328.png` | Ammen report continuation and crossing passage. |
| `reviews/TN003-a42f063-v1/pages/or-p329.png` | Ammen report ending, attached casualties, separate diary heading; diary composition date not established. |
| `reviews/TN003-a42f063-v1/pages/or-p330.png` | Ammen diary event labels and April 5 Savannah arrival; event dates are not composition dates. |
| `reviews/TN003-a42f063-v1/pages/or-p333.png` | Diary crossing and boat passages, continued narrative. |
| `reviews/TN003-a42f063-v1/pages/or-p334.png` | Diary night formation and midnight return passages, continued narrative. |
| `data/raw/shiloh/or-confederate-return.png` | 40,335/29,636 return, discrepancy footnote and April 21 forwarding; no explicit estimation qualifier for these cells on page. |
| `data/raw/shiloh/or-confederate-report-136-v1.png` | Four selected effective totals, headings, Hill arrival footnote, June 30 forwarding; no estimation marker. |
| `data/raw/shiloh/or-confederate-report-137-v1.png` | Four selected effective totals and explanatory note; printed discrepancies remain; no estimation marker. |
| `data/raw/shiloh/reed-1909-union-p98-facsimile-v1.png` | 5,837 Third Division reinforcement row and its relation to p.93. |
| `reviews/TN003-a42f063-v1/pages/or-p337.png` | Grose report: eight companies about 400 strong; report date and Sunday formation context. |

The four supplied page selections not re-audited are Michigan p.41 and Reed pp.60, 61 and 112. Crittenden p.355 has no supplied image and remains a text-only wording check. Nelson p.325 is also text-only here; its report context supports the document date. Force, handbook, Rousseau and NPS classifications rely on their pinned text within the stated scope.

The original **50 source records and all 50 distinct raw paths** remain preserved; the three aliases introduce **no new historical witnesses**. The previous dossier is byte-identically archived. All pre-existing fields on **40 quantities**, all **26 events**, all **3 null unknowns**, the open questions, dispute statuses and replacement boundaries are unchanged. The only claim-field changes are the 24 source aliases and Crittenden wording. Frozen review/bundle files, cohort, model inputs and baseline output are unchanged.

## Validation

- `make check`: **50 tests passed**, and offline CLI validation passed on an isolated archive of the reviewed commit.
- `make reproduce` and `make packet`: succeeded; baseline, report, quality, receipt and packet match committed bytes.
- Migration expected-output comparison: all four files match; rerun writes zero files. The regression suite replays the original transition, tests idempotence and rejects a divergent dossier before writing the pending ledger.
- Omitted-field mutation probes: reproduce TN003-C1 through both metadata validation/date helper and ordinary CLI check. All mutation experiments were confined to memory or `/tmp`.

The generated report preserves the unimproved baseline: **23/127 engagements**, **13 eligible campaign groups within 36**, Brier **0.276882** versus **0.250000** for equal odds. No model improvement is claimed.

## Limits

This is a separate AI implementation review, not human historical adjudication or proof of independent testimony. Source-backed statements can still be historically wrong. Conflicting clocks, the handbook’s 600-person basis, mixed dates, untraced original returns, return discrepancies and Reed’s 7,553/7,552 remain unresolved. No feature admission, uncertainty interval or causal estimate is approved. The review should be followed by a bounded check of the metadata-contract correction; the accepted evidence decisions need not be reauthored.
