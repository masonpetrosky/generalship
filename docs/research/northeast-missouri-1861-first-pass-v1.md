# Operations in Northeast Missouri, 1861: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both **frozen
records** in **Operations in Northeast Missouri [December 1861]** now have draft dossiers: **18
claims, 2 explicit null unknowns and 63 citation occurrences** (62 before the review correction
below). All seven dimensions are represented
in each record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| MO010 — Mount Zion Church | 1861-12-28 | 9 | 1 | 30 | 3 |
| MO011 — Roan's Tan Yard | 1862-01-08 | 9 | 1 | 33 | 3 |

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
  - **Roan's Tan-Yard command.** Torrence says he marched his command and was joined by Hunt and
    Hubbard, but states the assignment of the carbine force to Hunt and the First Iowa charge in the
    passive, without naming who gave the orders; Turner's relayed account credits Hubbard with the
    attack and rout.
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
in the worktree. After the review correction, both pass again (134 tests) in the main repository.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the six 1861
western and Trans-Mississippi first passes together at commit `8a97ac1` as
`w1861-review-8a97ac1-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": fourteen
required findings (W61-R1 to W61-R14) and twelve advisories (W61-A1 to W61-A12) across the six passes.
It is an AI review within its stated scope, not human historical adjudication, proof of source
independence or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the retained NPS
text) before any change; every new quote occurs once in its section, and the dossiers were regenerated
from the builder.

MO011 is revised under `northeast-missouri-1861-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/MO011.v1.json`. MO010 is unchanged.

- **W61-R13** (MO011 `command-roles` and this memo): the claim is `disputed` on who commanded, and
  Torrence reports the assignment to Hunt and the charge in the passive. The value now says so, the
  rationale notes the passive, and "I marched my command to Boone ville" (p.50) is added.

Advisories:

- **Adopted:** A6 (MO011 open questions: the third family is Hubbard's account relayed by Turner,
  Hubbard's own report would belong to it, and both inspected report families are Union).

The review correction adds no source records. Citations rise from 62 to 63; claims (18), unknowns (2),
disputed claims (5) and `inherited` tags (1) are unchanged. No model input, cohort file, admission
proposal or baseline is changed.
