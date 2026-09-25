# Bristoe Campaign: bounded first pass

Prepared 2026-09-25. All **five frozen records** in **Bristoe Campaign
[October-November 1863]** now have draft dossiers: **45 claims, 5 explicit null unknowns
and 197 citation occurrences** after review correction. All seven dimensions are
represented in each record. Separate Claude Opus 5.5 `high` [review](../../artifacts/review-results/bristoe-dc77737-opus-high-v1/review.md) found
four required corrections, all applied and verified by the primary. All dossiers remain
drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| VA039 — Auburn | 1863-10-13 | 9 | 1 | 34 | 3 |
| VA040 — Bristoe Station | 1863-10-14 | 9 | 1 | 42 | 3 |
| VA041 — Auburn (Coffee Hill) | 1863-10-14 | 9 | 1 | 35 | 3 |
| VA042 — Buckland Mills | 1863-10-19 | 9 | 1 | 38 | 3 |
| VA043 — Rappahannock Station | 1863-11-07 | 9 | 1 | 48 | 3 |

Coverage is **115/127 draft dossiers**, **12 without**, and **29/36 complete source
campaigns by dossier presence**. All 110 earlier dossiers and all historical revisions
are unchanged.

## Inspection and stopping record

Read all five frozen battle, force and commander row sets and the five retained NPS
summaries in full. NPS/CWSAC and the Arnold tables are one family. Each battle uses two
further families:

- **Humphreys**, *From Gettysburg to the Rapidan* (1883), reused through a new selection
  from the pinned OCR (`humphreys-ocr-v2`). Five Chapter II passages are used:
  - the night of October 13 (OCR pp.20–22);
  - Auburn on the 14th (pp.22–23);
  - Bristoe Station (pp.23–30; p.30's running head reads "3<3");
  - Buckland (pp.33–35);
  - Rappahannock Station (pp.37–48; p.40's running head reads "4-0").

  Humphreys was the Army of the Potomac's chief of staff in 1863–64 by his publisher's
  list, so his history is interested.
- **One Confederate report family per battle** from newly pinned *Official Records*
  Series I, Volume XXIX, Part 1, with catalog metadata, each author its own group:
  - **Stuart's** October 20 Buckland dispatch and the Auburn and Buckland passages of
    his February 13, 1864 report (pp.438–452), for both Auburn records and Buckland
    Mills;
  - **A. P. Hill's** October 26 report, with the indorsements by Lee, Seddon and Davis
    printed with it (pp.426–428), for Bristoe Station;
  - **Lee's** November 7 telegram and letter, November 10 letter and November 20 report
    (pp.609–616; pp.614–615 carry only running heads in the OCR), for Rappahannock
    Station.

  Indorsements printed with a report belong to that report and do not count as separate
  families.

No Union reports, maps, returns or print pages were inspected. Stop after this batch.

Sixteen new source records bring the registry to **531 entries / 512 raw paths**,
preserving the earlier **515/496**. They are:

- five NPS HTML/text pairs;
- OR XXIX Part 1 catalog metadata and full OCR;
- the Stuart, Hill and Lee selections;
- a Humphreys selection.

## Decisions and limits

- **Overlaps and scope.**
  - The two Auburn records (October 13 and 14) and Bristoe Station (October 14) are kept
    separate.
  - Humphreys' combined Auburn-and-Bristoe losses (Second Corps: 30 officers and 403 men
    killed and wounded; Confederates: 782) are not assigned to either record.
  - Rodes's Kelly's Ford losses are not added to Rappahannock Station. Whether that
    frozen record includes Kelly's Ford is not established.
- **Dates.** Stuart's October 20 dispatch puts Buckland "yesterday", matching the frozen
  October 19; Humphreys narrates it on the 20th. The frozen date is retained.
- **Opening strengths remain unknown.** All five records have blank frozen side bounds.
  Returns and engaged figures differ in scope and none is adopted:
  - Humphreys: Warren's 3,000 on the field against the Second Corps' 8,243; Hill's 17,223;
    6,867 Confederate against 3,500 Union cavalry at Buckland; 2,117 attackers against
    about 1,950 defenders at Rappahannock Station.
  - Lee: "three army corps".
- **Disputes preserved.**
  - Composition at the Auburn actions: NPS, Stuart and Humphreys name different brigades,
    and NPS's "Harry Hays's division" conflicts with Humphreys' Union General Alexander
    Hays.
  - Which Federal corps Hill first saw at Bristoe: the Third (Hill) or the Fifth
    (Humphreys).
  - Kilpatrick's rank: frozen Major General against Brigadier General in Stuart and in the
    live heading.
  - Rappahannock Station's works: "slight" (Lee) against a strong, well-fortified
    position (Wright, relayed by Humphreys).
  - Rappahannock Station's result: the frozen record's two result fields disagree ("Union
    victory" and "Inconclusive").
  - Casualties, where figures differ. Humphreys' Buckland components sum to the frozen 230
    (a computation here).
- **Command roles.** Judgments are attributed to their authors:
  - Hill's self-criticism and the Lee, Seddon and Davis indorsements;
  - NPS's account of Lee's rebuke, which is not in the inspected reports;
  - Stuart's credit to Fitzhugh Lee;
  - Lee's explanation of the Rappahannock loss.

  No listed commander receives automatic sole credit.
- **Tags.** The Bristoe railroad embankment, the summer works, and the pre-existing
  Rappahannock earthworks are tagged `inherited`. Other terrain, logistics and command
  claims stay `unresolved`.

The five null unknowns are the opening strengths. No morale/readiness score,
probability, causal effect or new commander ranking is introduced. The cohort and both
admission proposals are unchanged, with **zero promoted rows**. The baseline still uses
**23/127 engagements in 13 eligible groups**, with strength Brier **0.276882** against
**0.250000** for equal odds.

## Review correction and validation

The reviewer found four required corrections, all verified against the retained text
(each new quote occurs once) and applied:

- **BR-R1** labels two p.40 locators as inferred from the OCR head "4-0".
- **BR-R2** reports OCR and source readings instead of normalizing them:
  - "the loth of October";
  - "2-J" and "2£" miles;
  - NPS's "Owens";
  - Stuart's "the old First".
- **BR-R3** attributes Lomax's and Russell's relayed accounts to their reports.
- **BR-R4** gives Humphreys' printed components for Early's losses and marks the sums as
  computations.

Advisories A3 (Davis's indorsement on the corps dispute), A4 (Stuart's "On the next day,
October 20", from the same family) and A5 (Russell's brigade sums as a computation) are
adopted. A1 and A2 need no change now. Citations rise from 190 to 197; claims and unknowns
are unchanged, and no source record changes. The originals are retained as
`data/evidence/history/*.v1.json`, linked by `supersedes`. The
[primary assessment](../../artifacts/review-results/bristoe-dc77737-opus-high-v1/primary-assessment.md) closes all four findings; no second
reviewer pass is claimed.

Next by frozen campaign start is **Reopening the Tennessee River [October 1863]**:
TN021. Do not start that group within this batch.
