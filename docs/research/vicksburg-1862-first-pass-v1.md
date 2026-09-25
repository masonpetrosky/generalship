# Operations Against Vicksburg, December 1862–January 1863: bounded first pass

Prepared 2026-09-24. Both **frozen records** in **Operations Against Vicksburg
[December 1862-January 1863]** now have draft dossiers: **19 claims, 2 explicit null
unknowns and 69 citation occurrences** after review correction. All seven dimensions
are represented in each record. Separate Claude Opus 5.5 `high`
[review](../../artifacts/review-results/vicksburg-1862-7cbb971-opus-high-v1/review.md) covered both dossiers; its six required corrections are fixed
and verified by the primary. All dossiers remain drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| MS003 — Chickasaw Bayou | 1862-12-26 to 12-29 | 9 | 1 | 35 | 2 |
| AR006 — Arkansas Post | 1863-01-09 to 01-11 | 10 | 1 | 34 | 2 |

Coverage is **67/127 draft dossiers**, **60 without**, and **17/36 complete source
campaigns by dossier presence**. All 65 earlier dossiers and all historical
revisions are unchanged.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and both retained NPS summaries
in full. NPS/CWSAC and the Arnold tables are one family.

The follow-up reuses the already pinned OCR of Francis Vinton Greene, *The
Mississippi* (1882), through one new selection; the existing metadata and OCR are
unchanged. Inspected: title/preface and two Chapter III passages, Chickasaw Bayou
(OCR pp.73–81) and Arkansas Post from Sherman's quoted January 5 letter (pp.83–88).
Greene did not serve in the war and founded the book on the Official Records; the
Sherman letter is quoted, not inspected. No maps, returns or print pages were inspected.

Five new source records bring the registry to **349 entries / 346 raw paths**,
preserving the earlier **344/341**: two NPS HTML/text pairs and one Greene selection
whose parent is the existing `greene-mississippi-ocr-v1`.

## Decisions and limits

- **Opening strengths remain unknown.** Greene gives Sherman's expedition about 32,000
  with 60 guns, at least 12,000 Confederates in front instead of the 6,000-man garrison,
  and not more than 6,000 in the assaulting brigades. The frozen side-specific strength
  bounds are blank for both records (`missing_numeric_strength`). At Arkansas Post he gives the
  garrison about 5,000, while the Sherman letter he quotes says seven thousand; no Union
  infantry count is given. None is adopted.
- **Casualties differ** (frozen/live): Chickasaw Bayou **1,983 (US 1,776; CS 207) /
  1,963 (US 1,776; CS 187)**, with Greene's undated Union "exact total" of 1,929 and
  Confederate 187 for December 27–29 (matching the live figure). Arkansas Post **6,547 / 6,096**, with Greene's Union 977 plus 31 on
  the gunboats, and Confederate about 200 killed and wounded and 4,791 prisoners.
- **Arkansas Post's surrender initiation is disputed in Greene**: the white flag was
  raised "by order of General Churchill", but Churchill and his brigade commanders
  denied authorizing it and its origin "cannot be traced".
- **Information**: Greene says Sherman's movement was reported to Pemberton twice a
  day and that Sherman knew nothing of the Confederate reinforcements. At Arkansas
  Post, McClernand brought the first news that Grant had fallen back.
- **Command roles**: Sherman's assault was carried by two brigades and one regiment,
  unsupported; Arkansas Post was a joint army-navy operation under McClernand and
  Porter, against Churchill. The live heading omits McClernand. Live headings rank Sherman "General" and Porter "Rear Admiral" against the
  frozen Major General and Acting Rear Admiral; neither is adopted. The Chickasaw
  ground and Fort Hindman's works are tagged `inherited`.

The two null unknowns are the opening strengths. No morale/readiness score,
probability, causal effect or new commander ranking is introduced. Cohort and both
admission proposals remain unchanged, with **zero promoted rows**. The baseline still
uses **23/127 engagements in 13 eligible groups**, with strength Brier **0.276882**
versus **0.250000** for equal odds.

## Review correction and validation

The reviewer found six required corrections, all verified against the retained text
(each new quote occurs once) and applied: **VB-R1** replaces the unknown-strength
rationale, which implied imported estimates, with the blank frozen bounds
(`missing_numeric_strength`) in both dossiers; **VB-R2** names Churchill as the frozen
Confederate commander and records that the live heading omits McClernand; **VB-R3**
dates only Greene's Confederate 187; **VB-R4** records that Sherman's letter does not
name who captured the Blue Wing; **VB-R5** makes Thompson's Lake the obstacle and the
causeway its only crossing; **VB-R6** restores the high-water qualifier and cites the
five crossings. Both optional citations are adopted. Notes VB-N1 to VB-N5 need no
change. Citations rise from 62 to 69; claims and unknowns are unchanged. The originals
are retained as `data/evidence/history/MS003.v1.json` and `AR006.v1.json`, linked by
`supersedes`. The [primary assessment](../../artifacts/review-results/vicksburg-1862-7cbb971-opus-high-v1/primary-assessment.md) closes all six
findings; no second reviewer pass is claimed.

The VB-R1 template rationale also appears in earlier dossiers with blank frozen
bounds. It is corrected there in a separate, recorded propagation, not in this review.

Next by frozen campaign start is **Middle Tennessee Operations [February-April
1863]**: TN012–TN016. Do not start that group within this batch.
