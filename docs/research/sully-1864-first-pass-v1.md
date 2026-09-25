# Sully's Expedition Against the Sioux, 1864: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
**frozen record** in **Sully's Expedition Against the Sioux in Dakota Territory [July 1864]** now has
a draft dossier: **9 claims, 1 explicit null unknown and 37 citation occurrences**. All seven
dimensions are represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| ND005 — Killdeer Mountain | 1864-07-28 to 1864-07-29 | 9 | 1 | 37 | 4 |

It was drafted in a parallel worktree with eight other frontier and Texas-coast campaigns. Dossier
presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family.

- **Official Records, Series I, Volume XLI, Part 1** (1893; the registered University of Illinois
  OCR `or41-1-illinois-ocr-v1`, reused without re-registration):
  - **Sully's** July 31, 1864 report on Tahkahokuty Mountain, with the compiler's report list and his
    footnote on the omitted nominal list of casualties (No. 2, pp.131 and 141–144);
  - **Thomas's** August 1, 1864 report on the Second Brigade (No. 9, pp.165–166);
  - **Brackett's** August 1, 1864 report on his battalion (No. 5, p.161), as the **targeted
    follow-up** for the casualty figures.

Read, not selected: the opening of Pope's No. 1 report, the opening pages of Sully's August 13
report on the Little Missouri, Brackett's August 13 report and the opening of Thomas's August 13
report. Not inspected: the reports of Pollock, Pattee, Miner, Stufft, Pope's battery, Rogers, Camp,
McLaren and Adams, the list of property destroyed (p.172), any Dakota account and maps. Stop after
this record.

This pass adds **5 source records**: one NPS HTML/text pair and the selections
`or41-1-sully-tahkahokuty-selections-v1`, `or41-1-thomas-tahkahokuty-selections-v1` and
`or41-1-brackett-tahkahokuty-selections-v1`. Sully is in `sully-sioux-reports` with his 1863 report.
New author groups: `minor-thomas-sioux-report` and `brackett-sioux-report`; the container is
`or-series-i-volume-xli`.

## Decisions and limits

- **Scope.** Pope's plan, the establishment of Fort Rice, the emigrant train and the August 8–9
  fighting in the Little Missouri badlands are context only.
- **Opening strength remains unknown.** The frozen 2,200 (US bounds 2,200 and 2,200) agrees with
  Sully's "about 2,200" on the field on July 28; NPS's 2,500 is Pope's planned force. Sully estimates
  over 1,600 lodges and at least 5,000 or 6,000 warriors of the Unkpapas, Sans Arcs, Blackfeet,
  Minneconjous, Yanktonais and Santee; Thomas also gives 1,600 lodges. None is adopted as a matched
  opening strength.
- **Disputes preserved** (2 claims marked `disputed`):
  - **Parley and white flag.** NPS says Sully met some chiefs before attacking; the inspected July 31
    report does not mention such a meeting, but says that the day after the fight Indians planted a
    white flag, were fired on by some of his men, and that he saw the flag too late.
  - **Casualties.** Frozen Unknown; live 46 (US 15; CS 31). Sully judges the Indian killed at 100 to
    150; Brackett's battalion found 27 dead in its sector; the compiler's note gives 5 killed and 10
    wounded across four units; Thomas reports two pickets killed on the 29th.
- **Command roles.** The frozen commanders are Brigadier General Sully and Inkpaduta (no rank; the
  live page tags him [CS], not adopted). **The inspected reports do not name Inkpaduta.** Sully
  directed Brackett's charge, which Brackett says he requested; Thomas commanded the Second Brigade.
  No listed commander receives automatic sole credit.
- **No Dakota account was inspected**; numbers, aims and losses come from opponents' estimates.
- **Tags.** The mountain and ravines are tagged `inherited`. Outcomes are `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
commander ranking is introduced. No model input, frozen baseline or admission proposal is changed.

## Validation

`python3 -m generalship check` passes and `python3 -m unittest discover -s tests` passes (134 tests)
in the worktree.

## Separate review pending

No separate review has been run for this pass.
