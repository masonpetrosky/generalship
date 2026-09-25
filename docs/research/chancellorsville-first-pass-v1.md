# Chancellorsville Campaign: bounded first pass

Prepared 2026-09-25. All **three frozen records** in **Chancellorsville Campaign
[April-May 1863]** now have draft dossiers: **27 claims, 3 explicit null unknowns and
131 citation occurrences** after review correction. All seven dimensions are
represented in each record. Separate Claude Opus 5.5 `high` [review](../../artifacts/review-results/chancellorsville-c3a4911-opus-high-v1/review.md) found
ten required corrections, all applied and verified by the primary. All dossiers remain
drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| VA032 — Chancellorsville | 1863-04-30 to 05-06 | 9 | 1 | 58 | 3 |
| VA034 — Fredericksburg II | 1863-05-03 | 9 | 1 | 35 | 3 |
| VA033 — Salem Church | 1863-05-03 to 05-04 | 9 | 1 | 38 | 3 |

Coverage is **90/127 draft dossiers**, **37 without**, and **22/36 complete source
campaigns by dossier presence**. All 87 earlier dossiers and all historical revisions
are unchanged.

## Inspection and stopping record

Read all three frozen battle, force and commander row sets and the three retained NPS
summaries in full. NPS/CWSAC and the Arnold tables are one family.

- **VA032** adds **Doubleday**, *Chancellorsville and Gettysburg* (1882), pinned
  from a University of Toronto scan with catalog metadata, and **Lee's** September 21
  report. Doubleday says he was "to a considerable extent, an actor" in the events;
  he commanded a division at Chancellorsville, so his is an interested participant
  history. The six selected passages cover strengths, May 1, the May 2 warning order and
  the XI Corps, Hooker's injury, the council and recrossing, and the losses table.
- **VA033** adds **Sedgwick's** May 15 report and Lee's report.
- **VA034** adds Sedgwick's report and **Early's** May 7 report.

The three reports are selections from the already pinned *Official Records* Series I,
Volume XXV, Part 1. After review correction, Doubleday locators account for OCR
headers the first draft missed:

- Hooker's injury is on p.53: it follows the p.53 running head and precedes the
  legible (OCR-misspelled) p.54 header; the May 3 date comes from that running head,
  outside the selected range.
- The losses table is on an inferred p.71: it follows an unnumbered running head
  between the legible p.70 and p.72 markers.
- The XI Corps passage is on an inferred p.25, the chapter IV opening page between the
  p.24 and p.26 markers.

No maps, returns, Hooker's testimony or print pages were inspected. Stop after this
batch.

Twelve new source records bring the registry to **429 entries / 426 raw paths**,
preserving the earlier **417/414**: three NPS HTML/text pairs, Doubleday's catalog
metadata, full OCR and selection, and three OR selections.

## Decisions and limits

- **Nesting.** Salem Church and Fredericksburg II lie inside Chancellorsville's frozen
  interval (April 30–May 6). Doubleday's campaign losses table (17,197 Union, 13,019
  Confederate), Sedgwick's 4,925 and Early's division figures all span more than one
  engagement and are not assigned or added.
- **Opening strengths remain unknown.** VA032 has frozen structured bounds (97,382 /
  57,352), which are imported and unchanged. Doubleday gives Hooker about 124,500 of all
  arms and doubts he had over 113,000 for actual combat; he relays Forbes's 114,500 total
  effective and Forbes's 62,000 for Lee, and says Lee's army numbered about 62,000 by
  Confederate official reports. VA033 and VA034 have
  unit-level frozen text ("Corps") and no counts; Sedgwick's "15,000 strong" column is a
  report he received.
- **Casualties**: frozen 24,000 (VA032), 5,000 (VA033) and 2,000 (VA034) against live
  zeros; no engagement-specific report figure was found in the inspected passages.
- **Command roles**: Doubleday's criticisms of Hooker (the May 1 withdrawal, his
  condition after being stunned, the retreat ordered against the council's majority)
  and of Howard are his judgments. Lee credits Jackson, Stuart and Wilcox and records
  McLaws declining a joint attack. Early records a flag of truce "received ...
  improperly" before the Marye's Hill assault. The live heading ranks Lee Major
  General, and the frozen Jackson rank (Major General) differs from Lee's
  "Lieutenant-General"; neither heading rank is adopted. No
  listed commander receives automatic sole credit.
- Terrain, logistics and command claims stay `unresolved`; no `inherited` tag is used.

The three null unknowns are the opening strengths. No morale/readiness score,
probability, causal effect or new commander ranking is introduced. Cohort and both
admission proposals remain unchanged, with **zero promoted rows**. The baseline still
uses **23/127 engagements in 13 eligible groups**, with strength Brier **0.276882**
versus **0.250000** for equal odds.

## Review correction and validation

The reviewer found ten required corrections, all verified against the retained text and
the parent OCR (each new quote occurs once) and applied:

- **CV-R1 to CV-R3** correct the three Doubleday locators above.
- **CV-R4 to CV-R7** restore Doubleday's qualifications and Lee's credit to Jackson,
  replace "apathy" with Doubleday's words, read "lost" rather than "leaving", and attribute
  the table's inaccuracy to hearsay while recording its OCR arithmetic.
- **CV-R8** scopes Sedgwick's captures "according to the best information".
- **CV-R9** records the CWSAC/NPS "left flank" and "Lt. Gen." against Lee and Doubleday.
- **CV-R10** fixes the memo's strength wording above.

Five optional notes are adopted as wording or citations; the series-numeral note is
deferred. A `metadata_only` revision (`doubleday-chancellorsville-selections-v2`)
corrects the selection's inspection note, and VA032 cites it. Citations rise from 119 to
131; claims and unknowns are unchanged. The originals are retained as
`data/evidence/history/VA032.v1.json`, `VA033.v1.json` and `VA034.v1.json`, linked by
`supersedes`. The [primary assessment](../../artifacts/review-results/chancellorsville-c3a4911-opus-high-v1/primary-assessment.md) closes all ten
findings; no second reviewer pass is claimed.

Next by frozen campaign start is **Streight's Raid in Alabama and Georgia [April
1863]**: AL001. Do not start that group within this batch.
