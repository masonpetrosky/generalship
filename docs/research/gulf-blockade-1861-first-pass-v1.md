# Operations of the Gulf Blockading Squadron, 1861: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
frozen record in **Operations of the Gulf Blockading Squadron [October 1861]** now has a draft
dossier: **9 claims, 1 explicit null unknown and 50 citation occurrences**, with all seven dimensions
represented. It is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| FL001 — Santa Rosa Island | 1861-10-09 | 9 | 1 | 50 | 3 |

It was drafted in a parallel worktree with five other 1861 western campaigns. Dossier presence is not
first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and the
Arnold tables are one family. The two report families come from **Official Records, Series I, Volume
VI** (1882; University of Illinois scan `warofrebellion06unit`, whose title page confirms Series I
Volume VI):

- **Harvey Brown's** reports of October 9, 11, 12 and 17 (No. 1, pp.438–443). The table of distances
  and the October 22 letter were read but not selected.
- **R. H. Anderson's** October 23 report (No. 15, pp.460–463). The p.461 and p.463 heads read "4G1"
  and "4G3" in OCR.

Passages of Bragg's No. 14 papers were located by keyword and not selected. Tower's, Arnold's,
Wilson's and the other Union subordinate reports, the Confederate battalion reports, returns, maps and
print pages were not inspected. No nineteenth-century history covering the action was selected. No
targeted follow-up was used. Stop after this record.

This pass adds **6 source records**: the NPS HTML/text pair; OR VI catalog metadata and full OCR
(`ia-or6-illinois-metadata-v1`, `or6-illinois-ocr-v1`); and two selections
(`or6-brown-santa-rosa-selections-v1`, `or6-anderson-santa-rosa-selections-v1`). New author groups:
`brown-santa-rosa-reports` and `anderson-santa-rosa-report`; the container is
`or-series-i-volume-vi`.

## Decisions and limits

- **Scope.** The Pensacola harbor defences and later reconnaissances on the island are context only.
- **Opening strength remains unknown.** The frozen bounds are US 600 and CS 1,200; the live field
  gives CS 1,200 and US 0. Brown estimated the landing force at 1,200 or 1,500, reports his officers'
  almost unanimous 1,500 and later a Confederate acknowledgment of 1,500, and says fewer than 200
  regulars and some 50 volunteers pursued. Anderson lists battalions of 350, 400 and 260 and a company
  of 53 (1,063 before an uncounted artillery company). No inspected passage gives the garrison's
  strength, so the frozen 600 is untraced. None is adopted.
- **Disputes preserved** (3 claims marked `disputed`):
  - **Force scope,** as above.
  - **Result.** Brown says the enemy destroyed no quartermaster's or commissary stores; Anderson
    reports very great destruction of provisions, clothing, equipage, arms and ammunition.
  - **Casualties.** Brown's three accounts of his own loss differ (October 9, 11 and 17). Anderson's
    18 killed, 39 wounded and 30 prisoners sum to the CWSAC Confederate 87; that equality is not
    independent confirmation. Brown's 14 killed, 7 wounded and 27 prisoners in hand, a Pensacola
    paper's 21, 38 and 22 and a Confederate paper's 175, and Anderson's estimate of 50 or 60 Union
    killed and 100 wounded are all kept.
- **Command roles and ranks.** Brown directed from Fort Pickens, sending Vogdes and Arnold out and
  ordering Wilson to attack; Vogdes was captured before a shot was fired and Arnold succeeded to the
  command. NPS's "Col. Harvey Brown sallied" is not adopted over Brown's own account. Brown's October 12
  letter says the volunteer regiment did not behave well. The live page gives Anderson as Major
  General; the rank is not adopted. No listed commander receives automatic sole credit.
- **Objectives.** NPS says the aim included capturing Fort Pickens; Anderson's report states orders to
  capture guards, get between the fort and the camp and damage batteries and camps, not to take the
  fort. Brown's statement that the enemy was to spike the battery guns is his own inference.
- **Tags.** The island ground is tagged `inherited`; other claims stay `unresolved` or `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
commander ranking is introduced. No model input, frozen baseline or admission proposal is changed.

## Validation

`python3 -m generalship check` passes and `python3 -m unittest discover -s tests` passes (134 tests)
in the worktree.

## Separate review pending

No separate review has been run for this pass.
