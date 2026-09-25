# Expedition from Brazos Santiago, 1865: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
**frozen record** in **Expedition from Brazos Santiago [May 1865]** now has a draft dossier: **9
claims, 1 explicit null unknown and 40 citation occurrences**. All seven dimensions are represented.
The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| TX005 — Palmito Ranch | 1865-05-12 to 1865-05-13 | 9 | 1 | 40 | 3 |

It was drafted in a parallel worktree with eight other frontier and Texas-coast campaigns. Dossier
presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family.

- **Official Records, Series I, Volume XLVIII, Part 1** (1896; University of Illinois scan
  `warofrebellion481unit`, whose OCR title reads Series I Volume XLVIII, Part I):
  - **Barrett's** August 10, 1865 report to the Adjutant-General, written three months later because
    his earlier detailed reports may not have arrived, with the compiler's report list (No. 1,
    pp.265–267);
  - **Branson's** May 18, 1865 report on the Sixty-second U.S. Colored Infantry detachment, with the
    compiler's note on his omitted casualty list (No. 2, pp.267–269).

The inspected report list has no Confederate report, so the pass has only two Union families and
NPS. Not inspected: any Confederate account (Ford's or Giddings's), the detailed reports Barrett says
went to New Orleans, the 34th Indiana's account, returns and maps. No targeted follow-up was used.
Stop after this record.

This pass adds **6 source records**: one NPS HTML/text pair; OR XLVIII part 1 catalog metadata and
full OCR (`ia-or48-1-illinois-metadata-v1`, `or48-1-illinois-ocr-v1`); and the selections
`or48-1-barrett-palmetto-ranch-selections-v1` and `or48-1-branson-palmetto-ranch-selections-v1`. New
author groups: `barrett-palmetto-ranch-report` and `branson-palmetto-ranch-report`; the container is
`or-series-i-volume-xlviii`.

## Decisions and limits

- **Scope.** The crossing from Brazos Santiago on May 11 and the return to Boca Chica and
  re-embarkation on May 14 are context only.
- **Opening strength remains unknown.** Every figure is recorded with its date and none adopted:
  250 of the 62nd and 50 dismounted men of the 2nd Texas Cavalry crossing on May 11; about 200 of the
  34th Indiana joining on May 13; an outpost of sixty-five expected at White's Ranch and about 190
  men and horses in the Palmetto Ranch camp before noon on May 12; an enemy body 250 strong with two
  guns and six 12-pounder field pieces on the afternoon of May 13. These are Union estimates; no
  Confederate figure was inspected.
- **Disputes preserved** (2 claims marked `disputed`):
  - **The Mexican bank.** Branson says people on the Mexican shore gave the alarm while Imperial
    soldiers marched up that bank; Barrett says his men were fired on from the Mexican side and
    reports an Imperial cavalry crossing on what seemed good authority; NPS calls the reports
    unproven.
  - **Casualties.** Frozen US 118 and CS unknown; the live field reads 148 (US 30; CS 118), placing 118
    on the Confederate side; Barrett's 4 officers and 111 men killed, wounded and captured, including 48
    men of the 34th Indiana captured as skirmishers; Branson's two missing and the compiler's five
    wounded.
- **Informal truce.** NPS says a gentleman's agreement had precluded fighting on the Rio Grande since
  March 1865; neither inspected report mentions it. It is recorded as the NPS summary's statement.
- **Command roles.** The frozen commanders are Colonels Barrett and John S. "Rip" Ford. Branson
  commanded on May 12 and Barrett in person on May 13. **The inspected reports do not name Ford**;
  only NPS places the Confederate cavalry under him. No listed commander receives automatic sole
  credit.
- **Tags.** The river and chaparral are tagged `inherited`. Outcomes are `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
commander ranking is introduced. No model input, frozen baseline or admission proposal is changed.

## Validation

`python3 -m generalship check` passes and `python3 -m unittest discover -s tests` passes (134 tests)
in the worktree.

## Separate review pending

No separate review has been run for this pass.
