# Expedition to Hillsboro River, 1863: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
frozen record in **Expedition to Hillsboro River [October 1863]** now has a draft dossier: **9
claims, 1 explicit null unknown and 40 citation occurrences** (36 before the review correction
below). All seven dimensions are represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| FL004 — Fort Brooke | 1863-10-16 to 10-18 | 9 | 1 | 40 | 3 |

This pass was drafted in one batch with eight other Atlantic-coast campaigns. Dossier presence
is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full.
NPS/CWSAC and the Arnold tables are one family. Two further families:

- **Semmes's** report (pp.572–574) from newly pinned *Official Records of the Navies* Series I,
  Volume 17 (1903 imprint; Trent University copy; `orn17-trent-ocr-v1`). It is dated October
  20, 1863 with a continuation dated October 22, so its section date is mapped null. Semmes
  planned the expedition and refers the shore details to Acting Master Harris's enclosed report.
- **Westcott's** October 18 report with its postscript (p.735) from *Official Records* Series I,
  Volume XXVIII, Part 1 (registered with Charleston 1863), a short report by the Confederate
  commander at Fort Brooke that promises a detailed report (not found).

Read but not selected: Bailey's October 26 report, Harris's October 18 report, Stodder's October
19 report, the surgeons' casualty reports and the letters of congratulation (Navies volume 17,
pp.570–579), and Finegan's and Beauregard's indorsements on Westcott's report (p.736). No
history covering the action was found. No targeted follow-up was used for this record (the
volume was also searched for the Tampa follow-up). Stop after this record.

## New source records

This campaign adds **6 records**: the FL004 NPS HTML/text pair, the Navies volume 17 catalog
metadata and full OCR, and the Semmes and Westcott selections.

## Decisions and limits

- **Scope.** The December 25, 1863 engagement at Fort Brooke is a separate action and context
  only.
- **Opening strength remains unknown.** The frozen bounds are blank and the live force field
  reads zero. Semmes landed a force of 100 exclusive of officers and guides; Westcott says 130
  landed, printed as "120 men and 20 guides", and that his own force was too small. Harris's
  estimate of the Confederate force (read, not selected) is not used. None is adopted.
- **Disputes preserved.**
  - The landing party's size (above).
  - Result: NPS and Semmes describe the capture and burning of the Scottish Chief and the Kate
    Dale; Westcott says the Confederates burned the A. B. Noyes and badly whipped the party at
    its boats.
  - Casualties: frozen Unknown against live 16 (US 16; CS 0); Semmes names 3 killed, 10 wounded
    and 4 prisoners, and also reports holding 2 prisoners of war and 5 blockade runners, one
    severely wounded, against the live CS 0; Westcott reports 5 prisoners and believes about 50
    were killed and wounded.
- **Command roles and ranks.** The frozen commanders are Lieutenant Commander A. A. Semmes (US,
  navy) and Captain John Westcott (CS). Harris commanded the landing party; Westcott had assumed
  command at Tampa two days before the shelling. No listed commander receives automatic sole
  credit.
- **Tags.** All claims stay `unresolved` or `post_outcome`. Semmes's staked feint and diversionary
  shelling were his own design but are not separately tagged.

The one null unknown is the opening strength. No morale/readiness score, probability, causal
effect or new commander ranking is introduced. The cohort, the admission proposals and the
baseline are unchanged, with zero promoted rows.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the nine
Atlantic-coast first passes (15 dossiers) together at prepared commit `0e6063c` as
`atlantic-review-0e6063c-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": eleven
required findings (R1 to R11) and thirteen advisories (A1 to A13) across the nine passes. It is
an AI review within its stated scope, not human historical adjudication, proof of source
independence or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the registry
record) before any change; every new quote occurs in its cited section, and the dossiers were
regenerated from the builder.

FL004 is revised under `hillsboro-1863-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/FL004.v1.json`.

- **R10** (`casualty-records` and this memo): Semmes's statement that he holds 2 prisoners of war
  and 5 blockade runners, one severely wounded, is added against the live CS 0 and cited (p.573),
  and the head of his wounded list is cited for the value's 10 wounded.

Advisories:

- **Adopted:** A13 (`destroy-the-runners`): Semmes's passage on the cotton-loaded vessels ready to
  run the blockade, and his staked feint, are now cited as the direct support for the stated
  object and the diversions.

The review correction adds no source records. Citations rise from 36 to 40; claims (9), unknowns
(1) and disputed claims (3) are unchanged. No model input, cohort file, admission proposal or
baseline is changed.

After the review correction, `python3 -m generalship check` and `python3 -m unittest discover -s
tests` pass (134 tests) in the main repository, and `gs.MISSES` is empty.
