# Operations in Northeast Missouri, 1861: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both **frozen
records** in **Operations in Northeast Missouri [December 1861]** now have draft dossiers: **18
claims, 2 explicit null unknowns and 62 citation occurrences**. All seven dimensions are represented
in each record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| MO010 — Mount Zion Church | 1861-12-28 | 9 | 1 | 30 | 3 |
| MO011 — Roan's Tan Yard | 1862-01-08 | 9 | 1 | 32 | 3 |

MO011's frozen date falls after the campaign's December 1861 label; the record is kept as frozen. The
pass was drafted in a parallel worktree with five other 1861 western campaigns. Dossier presence is
not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets. The live MO010 page is an **empty Battle Detail
template** (registered as a diagnostic HTML snapshot only), so the frozen CWSAC row is the NPS/CWSAC
family's evidence for that record; the MO011 page was read in full.

| Record | Second family | Third family |
| --- | --- | --- |
| MO010 | Prentiss | Britton |
| MO011 | Torrence | Turner (relaying Hubbard) |

- **Official Records, Series I, Volume VIII** (registered with the Indian Territory pass as
  `or8-illinois-ocr-v1`):
  - **Prentiss's** January 4, 1862 report on the Hallsville skirmish and Mount Zion Church (pp.43–45);
  - **Torrence's** January 10, 1862 report (No. 3, pp.50–51);
  - **Turner's** January 14, 1862 report (No. 2, p.49), relaying Major Hubbard's account at second
    hand. It is treated as a separate family from Torrence's.
- **Britton**, *The Civil War on the Border*, volume I (1891), registered with the Missouri 1861 pass:
  the title page and preface and the Mount Zion Church passage of Chapter XV (pp.192–195). Britton
  does not name Roan's Tan-Yard.

Palmer's No. 1 and Merrill's No. 4 reports on Roan's Tan-Yard, printed with Torrence's and Turner's,
were read while delimiting and not selected. Hubbard's own report, the Confederate side of both
actions, returns and maps were not inspected; no nineteenth-century history covers Roan's Tan-Yard in
the inspected passages. No targeted follow-up was used. Stop after this batch.

This pass adds **7 source records**: the MO010 empty-template HTML snapshot; the MO011 NPS HTML/text
pair; three OR VIII selections (`or8-prentiss-mount-zion-selections-v1`,
`or8-torrence-roans-tan-yard-selections-v1`, `or8-turner-roans-tan-yard-selections-v1`); and
`britton-border-1-mount-zion-selections-v1`. **Prentiss** is placed in his existing group
`or-prentiss` (Shiloh); `torrence-roans-tan-yard-report` and `turner-roans-tan-yard-report` are new.

## Decisions and limits

- **Scope.** The December 27 skirmish near Hallsville, Prentiss's march from Palmyra, and the January
  5–7 reconnaissances and return march are context only.
- **Opening strengths remain unknown.** The frozen bounds are MO010 US 440 (240 and 200) and MO011 US
  450; the Confederate sides are blank. Prentiss and Britton give 470 marching (five cavalry troops and
  five sharpshooter companies, against the frozen description's two sharpshooter companies) and near
  900 for the enemy. Torrence gives 500 mounted men and 600 (read "COO" in OCR) to 800 enlisted men
  with as many sympathizers for Poindexter; Turner, relaying Hubbard, gives 900. None is adopted.
- **Disputes preserved** (5 claims marked `disputed`: two force-scope, two casualty and one
  command-role claim):
  - **Mount Zion casualties.** Prentiss's 3 killed, 17 severely and 46 slightly wounded include the
    previous evening's skirmish, so they must not be assigned to MO010 alone; the frozen US 72 and CS
    210 against Prentiss's 25 killed, 150 wounded and 30 prisoners.
  - **Roan's Tan-Yard command.** Torrence describes his own dispositions and charge; Turner's relayed
    account credits Hubbard with the attack and rout.
  - **Roan's Tan-Yard casualties.** Torrence's not less than 80 to 100 enemy killed and wounded (the
    CWSAC CS 80 matches his lower bound) against Hubbard's 40 killed and 60 wounded; Hubbard's own 6
    killed and 19 wounded against the frozen US 11.
- **Command roles and ranks.** Prentiss directed the Mount Zion attack; Glover and the reserve
  companies are named in his report. Dorsey's name reads "Horsey" in OCR. No listed commander receives
  automatic sole credit.
- **Tags.** The Roan's Tan-Yard ravines and fog are tagged `inherited`; other claims stay `unresolved`
  or `post_outcome`.

The two null unknowns are the opening strengths. No morale/readiness score, probability, causal effect
or commander ranking is introduced. No model input, frozen baseline or admission proposal is changed.

## Validation

`python3 -m generalship check` passes and `python3 -m unittest discover -s tests` passes (134 tests)
in the worktree.

## Separate review pending

No separate review has been run for this pass.
