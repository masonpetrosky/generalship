# Shiloh: Confederate return audit, reports 136 and 137

Research date: 2026-09-20. **Draft; no independent historical review.**

This memo preserves the Confederate-return revision. Its dossier is archived as
[TN003.v3.json](../../data/evidence/history/TN003.v3.json); the subsequent
[Union availability audit](shiloh-union-availability.md) documents the next
43-claim revision. The latest [Ohio reinforcement audit](shiloh-ohio-reinforcements.md)
documents the 62-claim draft. Counts and validation below describe this earlier revision.

Reports 136 and 137 have now been inspected visually in the same pinned volume
as the earlier p.396 return. They establish alternative printed figures and
population warnings, but do not reconcile the earlier return or establish an
April 6 opening strength. Two internal infantry subtotal discrepancies in report
137 also remain unresolved. No source value has been corrected or averaged.

## Inspected evidence

All three returns are in *The War of the Rebellion*, Series I, Volume X, Part I
(Washington: Government Printing Office, 1884). Printed pages 396, 398 and 399
are PDF pages 420, 422 and 423. The locally inspected
[parent volume](https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf)
matches the previously registered SHA-256:
`86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978`.

| Source ID | Locator and inspected content | Snapshot SHA-256 |
|---|---|---|
| `or-confederate-return` | [p.396, Inclosure E](../../data/raw/shiloh/or-confederate-return.txt): earlier before/after effective totals and disagreement footnote | `6c127e6c1945754097a4b54a6efd98a9f7a35e3b009c7b9c5cd49056b0400c0c` |
| `or-confederate-report-136-v1` | [p.398, report 136](../../data/raw/shiloh/or-confederate-report-136-v1.txt): selected columns, heading, Hill footnote and Bragg forwarding line | `28e6ed7c4886cb04d4690469c824bb343f66b6c761f8da3334ef58decdc5d1e7` |
| `or-confederate-report-137-v1` | [p.399, report 137](../../data/raw/shiloh/or-confederate-report-137-v1.txt): selected columns, heading, composition note and Bragg forwarding line | `675efae865fa9d112b9f8aa6c3585221c8b742fbe092dfc5a130a38b43fb0f72` |

The registered [report 136 facsimile](../../data/raw/shiloh/or-confederate-report-136-v1.png)
and [report 137 facsimile](../../data/raw/shiloh/or-confederate-report-137-v1.png)
retain each entire page, rotated for reading. Their hashes and rendering
transformation are in [the manifest](../../data/sources.json). Manual transcriptions
retain every command row's for-duty and effective columns, selected summary
columns, and complete printed notes. Other category cells remain in the scans;
this is not an exhaustive cell audit. Editorial cautions occupy a separate
`transcription-scope` section, not the cited historical passage section.

These documents share the Army of the Mississippi reporting chain. Bragg's
signature does not make his returns independent corroboration of Jordan and
Beauregard, and a transcription and its scan are one source.

## What each count describes

| Printed return | Date/scope in heading | Effective total | Other printed population columns | Submission/forwarding |
|---|---|---:|---|---|
| p.396, Inclosure E | Before battle; exact muster date unstated | 40,335 | Infantry/artillery 35,953; cavalry 4,382 | April 21, Jordan/Beauregard |
| p.398, report 136 | Forces that marched from Corinth to the Tennessee River, April 3 | 38,773 | Present total 46,425; present aggregate 49,444; present-and-absent total 57,252; aggregate 59,774 | June 30, Bragg; date printed in brackets |
| p.396, Inclosure E | After battle; exact muster date unstated | 29,636 | Infantry/artillery 25,555; cavalry 4,081 | April 21, Jordan/Beauregard |
| p.399, report 137 | After battle, April 10 | 32,212 | Present total 44,588; present aggregate 47,493; present-and-absent total 60,961; aggregate 64,500 | June 30, Bragg; date printed in brackets |

The tables distinguish **For duty**, **Effective total**, **Total**, and
**Aggregate**, with additional present/absent categories. They are not equivalent
counts. For example, report 136's printed for-duty officers plus enlisted men
give 2,587 + 37,011 = **39,598**, not its 38,773 effective total. Report 137 gives
2,184 + 29,910 = **32,094**, not 32,212. These sums are arithmetic diagnostics,
not additional source-reported quantities or proposed corrected strengths.
This audit does not establish a universal accounting rule for the effective column.

April 3 describes the march in report 136's heading; no separate exact muster
time is supplied. Its typed observations retain null period dates with that
heading preserved in the scope label. Report 137 has April 10 in its heading,
which is retained as its return date, not proof of simultaneous unit musters.
The June 30 dates are submission/forwarding dates. None establishes when a
commander knew the figures, and April 10 cannot be assigned to p.396's undated
after-battle population.

Two printed notes prevent a simple before/after interpretation:

- Report 136, First Corps infantry footnote: "Colonel Hill's regiment
  (Tennessee) came upon the [field] during the engagement on Monday."
  The note identifies a late arrival but gives neither its strength nor a
  numerical adjustment. It does not settle the regiment's accounting in the table.
- Report 137 attributes differences from the preceding return to losses and
  "the arrival of Carroll's brigade and a portion of the cavalry, heretofore
  detached." This supplies a composition warning, not a quantified bridge or
  the arrivals' dates. The difference 38,773 - 32,212 = **6,561** is therefore
  not a casualty estimate. Nor does the note explain the separate p.396 totals.

Both quotations are from the respective `p398`/`p399` sections linked above.

## Arithmetic comparison, without historical harmonization

Positive differences mean the detailed report prints more than p.396.
Infantry plus artillery in reports 136/137 is calculated from their **printed
branch subtotals**, so it can be compared with p.396's combined category.

| Broad category | p.396 before | Report 136 | Difference | p.396 after | Report 137 | Difference |
|---|---:|---:|---:|---:|---:|---:|
| Infantry + artillery | 35,953 | 34,727 + 1,973 = 36,700 | +747 | 25,555 | 26,697 + 1,682 = 28,379 | +2,824 |
| Cavalry | 4,382 | 2,073 | -2,309 | 4,081 | 3,833 | -248 |
| Grand total | 40,335 | 38,773 | **-1,562** | 29,636 | 32,212 | **+2,576** |

This localizes the differences by broad category. It does not identify which
units, dates, inclusion rules or errors caused them. All figures remain
source-specific; matching a category label does not establish equal populations.

Report 137 also has internal discrepancies in the inspected print:

| Infantry column | Four corps rows, as printed | Row sum | Printed subtotal | Row sum minus subtotal |
|---|---|---:|---:|---:|
| Effective total | 7,582 + 9,118 + 4,865 + 5,232 | 26,797 | 26,697 | +100 |
| For duty, enlisted men | 7,198 + 8,453 + 4,305 + 4,334 | 24,290 | 24,692 | -402 |

The effective branch subtotals **26,697 + 1,682 + 3,833 = 32,212** do match
the printed grand total. Using the four infantry rows instead would yield
32,312. That is a diagnostic alternative calculation, **not a corrected return**
or an admitted observation. Inspection alone cannot distinguish errors in the
underlying returns, compilation, printing, or our reading; independent checking
against unit returns or another edition remains necessary.

## Migration and limits

The prior 22-claim draft is preserved byte-for-byte as
[TN003.v2.json](../../data/evidence/history/TN003.v2.json), SHA-256
`9e662b64c3448a0733d4b9f37d1ede4bcec7e99f59e8703600e3986f2c52cfed`.
This revision's `supersedes` links to it; that archive retains its link to
the original v1 draft. Schema version remains 2; this is an evidence revision,
not a new quantity schema. Existing claim and quantity IDs persist. The previous
after-battle claim is now explicitly disputed, and its 29,636 observation remains.

This revision has **28 claims, 20 typed troop observations and seven events**.
Six claims and eight observations were added: each new report's effective grand
total and three branch subtotals remain separate. Subtotals overlap their grand
total and must never be added to it. Four source artifacts were added; earlier
raw inputs and source IDs/hashes were preserved. No independent review record,
model feature admission, cohort change or commander attribution was created.

The NPS **44,968** remains a separately recorded whole-engagement figure with
an untraced numerical basis. This audit neither derives it nor disproves it.
The unchanged baseline still covers **23/127 engagements in 13 eligible campaign
groups**, within the **36-campaign** pilot. Held-out Brier score remains
**0.276882**, versus **0.250000** for equal odds. These additions have not improved
model coverage or predictive performance.

The subsequent [Union audit](shiloh-union-availability.md) examines omitted units
and phase-specific availability, including Michigan and Wallace. For
independent review, the focused Confederate questions are the two report 137
subtotal discrepancies, the timing/accounting of Hill and Carroll, and the
unexplained differences from p.396. A reviewed comparison population is still
required before selecting an opening-strength row.

## Validation of this revision

`make check` passed all **38 tests** and source/evidence/pipeline validation.
`make reproduce` regenerated the report and receipt, and `make packet` updated
the prepared assignment. The generated report was inspected. A separate byte
comparison against the prior Git revision confirmed all 17 earlier source
records and files unchanged, the archived dossier identical to its predecessor,
and the frozen cohort, battle predictions and coverage unchanged. The quality
artifact changed only to include the four new source hashes. All receipt hashes
match the files, and the prepared packet regenerates identically. These checks
verify preservation and consistency, not independent historical entailment.
