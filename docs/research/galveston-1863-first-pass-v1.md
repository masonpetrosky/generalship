# Operations Against Galveston, 1862-63: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
**frozen record** in **Operations Against Galveston [December 1862-January 1863]** now has a draft
dossier: **10 claims, 1 explicit null unknown and 51 citation occurrences**. All seven dimensions are
represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| TX003 — Galveston | 1863-01-01 | 10 | 1 | 51 | 3 |

It was drafted in a parallel worktree with eight other frontier and Texas-coast campaigns. Dossier
presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family.

- **Official Records, Series I, Volume XV** (1886; University of Illinois scan
  `warofrebellion15unit`, registered with the Texas coast 1862 pass):
  - **Davis's** January 10, 1863 report by the adjutant of the Forty-second Massachusetts, with the
    compiler's report list (No. 2, pp.199 and 206–207);
  - **Magruder's** reports of January 1 (with a January 3 postscript) and January 2, 1863, and his
    February 26, 1863 report through the burial of the dead (No. 4, pp.210–219).

Read, not selected: Banks's No. 1 reports with Burt's statement and part of Burrell's December 29
letter, the closing lines of the Cambria purser's statement, Long's No. 3 report and Jefferson
Davis's January 28 letter. Not inspected: the rest of Magruder's February report, his orders and
flag-of-truce correspondence, the naval reports the compiler refers to the Secretary of the Navy's
1863 annual report, Long's map and returns. No targeted follow-up was used. Stop after this record.

This pass adds **4 source records**: one NPS HTML/text pair and the selections
`or15-davis-galveston-selections-v1` and `or15-magruder-galveston-selections-v1`, both from the
Volume XV parent `or15-illinois-ocr-v1`. Davis is in the new group `charles-a-davis-galveston-report`.
Magruder is placed in his existing group `magruder-big-bethel-reports`, whose name reflects his 1861
reports.

## Decisions and limits

- **Scope.** Magruder's preparations from November 1862, the Cambria episode of January 3 and the
  continued blockade are context only.
- **Opening strength remains unknown.** The frozen force field names Companies D, G and I of the
  42nd Massachusetts, the blockading ships, four Confederate gunboats and district troops, without
  figures; the live field reads 0. Davis estimates not less than 3,000 on shore with some twenty guns
  and, by the Confederates' own account, as many on the boats. Magruder gives a call for 300
  volunteers, a storming party of about 500, six siege pieces, a railroad-mounted 8-inch gun and
  fourteen field pieces. None is adopted.
- **Disputes preserved** (3 claims marked `disputed`):
  - Force figures (above).
  - Flags of truce: Davis says the companies were marched off while flags of truce were flying;
    Magruder says the Union vessels left under a flag of truce in violation of military propriety.
  - Casualties: frozen and live 650 (US 600; CS 50); Magruder's prisoners about 600 (January 1),
    350 exclusive of officers (January 2) and 300 or 400 (February); his loss not over 25 killed and
    50 wounded (January 2) or 26 killed and 117 wounded (February); Davis thinks not over 20 of his
    men were wounded.
- **Command roles.** The frozen commanders are Major General Magruder, Colonel Burrell and Commander
  Renshaw (navy). Burrell and Renshaw left no inspected report; both sides say Renshaw was killed
  when the Westfield was blown up. No listed commander receives automatic sole credit.
- **Tags.** No claim is tagged `inherited`; the wharf position was prepared by the Union companies.
  Outcomes are `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
commander ranking is introduced. No model input, frozen baseline or admission proposal is changed.

## Validation

`python3 -m generalship check` passes and `python3 -m unittest discover -s tests` passes (134 tests)
in the worktree.

## Separate review pending

No separate review has been run for this pass.
