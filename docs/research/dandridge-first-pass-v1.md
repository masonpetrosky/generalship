# Operations about Dandridge: bounded first pass

Prepared 2026-09-25. All **three frozen records** in **Operations about Dandridge
[December 1863-January 1864]** now have draft dossiers: **27 claims, 3 explicit null
unknowns and 145 citation occurrences** after review correction. All seven dimensions are
represented in each record. Separate Claude Opus 5.5 `high` [review](../../artifacts/review-results/dandridge-668c58f-opus-high-v1/review.md) found
seven required corrections, all applied and verified by the primary. All dossiers remain
drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| TN027 — Mossy Creek | 1863-12-29 | 9 | 1 | 53 | 3 |
| TN028 — Dandridge | 1864-01-17 | 9 | 1 | 43 | 3 |
| TN029 — Fair Garden | 1864-01-27 | 9 | 1 | 49 | 3 |

This is the last frozen group. Coverage is **127/127 draft dossiers**, **0 without**, and
**36/36 complete source campaigns by dossier presence**. All 124 earlier dossiers and all
historical revisions are unchanged. Dossier presence is not first-pass acceptance,
separate review or model eligibility.

## Inspection and stopping record

Read all three frozen battle, force and commander row sets and the three retained NPS
pages in full. NPS/CWSAC and the Arnold tables are one family. Each record uses two
further families:

- **Sturgis's** dispatches and reports, one Union family across two volumes:
  - Mossy Creek, from the pinned *Official Records* Series I, Volume XXXI, Part 1
    (`or31-1-illinois-ocr-v1`): the December 29 dispatches, the January 8 report with
    Foster's transmittal, and the January 1 casualty letter (pp.646–650). The p.649 head
    reads "049" in OCR.
  - Dandridge and Fair Garden, from newly pinned Volume XXXII, Part 1 (1891 imprint), with
    catalog metadata: the January 16 dispatch and February 4 report (pp.79–81), and the
    January 26–29 dispatches and February 4 report (pp.131–138).
- **Martin's** January 8 report (No. 77, Volume XXXI Part 1, pp.545–549), for Mossy Creek.
- **Longstreet's** January 19 report (pp.93–94; Lawton's indorsement on p.94 read but not selected) and his January 29
  and February 1 telegrams (pp.149–150), from Volume XXXII Part 1, for Dandridge and Fair
  Garden.

The following were read but not selected:

- Foster's Mossy Creek telegram and Fair Garden telegrams;
- Parke's January 18 Dandridge report;
- Sturgis's complimentary orders and the Fair Garden addenda.

The compiled Mossy Creek casualty return is garbled in OCR, and Martin's casualty table is
not printed. No maps, sketches, Elliott's, McCook's or other subordinate reports, or print
pages were inspected. Stop after this batch.

Twelve new source records bring the registry to **580 entries / 560 raw paths**,
preserving the earlier **568/548**:

- three NPS HTML/text pairs;
- OR XXXII Part 1 catalog metadata and full OCR;
- two Sturgis selections, one Martin selection and one Longstreet selection.

## Decisions and limits

- **Scope.** The December 24 and 27 actions, the January 14 advance, the January 16
  skirmishes, the January 26 skirmishes and the January 28 Indian Creek fight fall outside
  the frozen dates and are context only.
- **Opening strengths remain unknown.**
  - Mossy Creek: the frozen Confederate bound of 2,000 is imported and the Union bound is
    blank. The frozen force text attributes to Sturgis a supporting brigade of infantry; its
    following "approx. 2,000 men" is not clearly part of that attribution. The inspected Sturgis passages instead give about 6,000 cavalry and, in a
    dispatch, a division of infantry. Martin gives 2,000 men of his own and says he faced
    not more than 4,000 at first.
  - Dandridge and Fair Garden: the frozen bounds are blank. Sturgis's three infantry
    brigades and Wolford's 900 are partial figures.

  None is adopted.
- **Disputes preserved.**
  - Mossy Creek's withdrawal: Sturgis says the enemy was driven back in great confusion;
    Martin says his retreat was orderly.
  - Mossy Creek losses:
    - Sturgis's two totals, 100 (read "LOO" in OCR; a computation from the components)
      and 96;
    - his 44 prisoners against about 50;
    - the frozen CS unknown against live CS 0 (both give US 151).
  - Dandridge losses: Longstreet's estimate that the two days' casualties could not
    exceed 150 (read as his own; no side is named) must not be equated with the frozen
    Union 150, whose basis is not established. Sturgis's 83 is for the cavalry over two days.
  - Fair Garden losses and captures: Sturgis's report and dispatch differ on prisoners
    (about 150 against over 100) and guns (rifled 10-pounders against 3-inch steel).
    Longstreet gives Martin's loss as 200.
  - Dandridge's pursuit: NPS says the Confederates could not pursue for lack of cannons,
    ammunition and shoes; Longstreet gives shoes as the reason his infantry could not
    pursue and says his cavalry, short of clothing and horseshoes, was sent forward to
    distress the enemy.
- **Command roles and ranks.**
  - The live pages give Sturgis as Major General and Martin as Colonel, and Longstreet as
    Major General. The frozen ranks are Brigadier General, Major General and Lieutenant
    General. The live ranks are not adopted.
  - Sturgis reports that Parke, not a listed commander, ordered him to retire the
    cavalry; the selected passages do not cite the order for the infantry's withdrawal
    (Parke's January 18 report was read but not selected).
  - No listed commander receives automatic sole credit.
- **Tags.** No works or ground are tagged `inherited`; all positions were taken during the
  operations. All claims stay `unresolved` or `post_outcome`.

The three null unknowns are the opening strengths. No morale/readiness score, probability,
causal effect or new commander ranking is introduced. The cohort and both admission
proposals are unchanged, with **zero promoted rows**. The baseline still uses **23/127
engagements in 13 eligible groups**, with strength Brier **0.276882** against **0.250000**
for equal odds.

## Review correction and validation

The reviewer found seven required corrections. Each was verified against the retained
text (every new quote occurs once) and applied:

- **DAN-R1** attributes the 400 and 250–300 Mossy Creek estimates to Elliott and others,
  and Sturgis's own 300–400 to his January 1 letter.
- **DAN-R2** restates Longstreet's pursuit reasons: shoes for the infantry, while the
  cavalry was sent forward. Two citations are added.
- **DAN-R3** reads the frozen force text's 2,000 as not clearly part of the attribution
  to Sturgis, and drops the claim that each commander gives the larger number to the
  other side.
- **DAN-R4** adds a `metadata_only` revision,
  `or32-1-longstreet-dandridge-selections-v2`. It removes Lawton's indorsement from the
  author and dependency note, since the selected range ends before it. The TN028 and
  TN029 citations are retargeted to v2.
- **DAN-R5** gives Sturgis's pursuit wording and the two-month scope of the parched corn,
  with a citation.
- **DAN-R6** narrows Parke's role to ordering the cavalry to retire.
- **DAN-R7** marks Longstreet's 150 as read as his own losses; the frozen Union 150's
  basis is not established.

Advisories are adopted:

- A1: no causal link in the Dandridge reconnaissance dispatch.
- A2: an open-question typo.
- A3: this memo's loss bullet.
- A4: the "LOO" footnote outside the range, and Sturgis's 6 p.m. postscript on pushing
  Wolford and Garrard up, which is cited as an intra-source difference.
- A5: the Fair Garden captures are not counted twice, and the Morgan/Armstrong
  identification is dated to the 26th.

Citations rise from 141 to 145 (TN027 53, TN028 43, TN029 49): the reviewer's three plus
the A4 postscript. Claims and unknowns are unchanged. The registry is now **581 entries /
560 raw paths**; no raw file changes. The originals are retained as
`data/evidence/history/TN027.v1.json`, `TN028.v1.json` and `TN029.v1.json`, linked by
`supersedes`. The [primary assessment](../../artifacts/review-results/dandridge-668c58f-opus-high-v1/primary-assessment.md) closes all seven
findings; no second reviewer pass is claimed.

All 36 frozen campaign groups now have bounded first-pass dossiers with a recorded
separate review. Coverage, separate review and feature admission stay distinct: no
features are admitted and the baseline is unchanged.
