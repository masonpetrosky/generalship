# Operations Against Fort Pulaski: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
frozen record in **Operations Against Fort Pulaski [April 1862]** now has a draft dossier: **9
claims, 1 explicit null unknown and 51 citation occurrences** (49 before the review correction
below). All seven dimensions are represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| GA001 — Fort Pulaski | 1862-04-10 to 04-11 | 9 | 1 | 51 | 3 |

This pass was drafted in one batch with eight other Atlantic-coast campaigns (Charleston 1862
and 1863, Tampa, St. John's Bluff, Fort McAllister, Fort Brooke, Olustee and Natural Bridge).
Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full.
NPS/CWSAC and the Arnold tables are one family. Two further families:

- **Gillmore's** reports, *Official Records* Series I, Volume VI (1882 imprint; the already
  registered `or6-illinois-ocr-v1`, deduplicated at merge; catalog volume v.6 and OCR title
  checked). The whole of No. 5 (pp.144–165) was read. Selected:
  - the April 12, 1862 preliminary report (pp.144–147);
  - from his report dated Hilton Head, October 20, 1865, "compiled from my original report
    to the Chief Engineer": the opening, the description of the fort and the December 1861
    project, which reprints his December 1 and 5, 1861 letters (pp.148–150); the investment
    and batteries on Tybee from February 19 to April 9 (pp.153–156); and the bombardment and
    surrender (pp.157–159). These three sections are mapped to the 1865 report date.
- **Samuel Jones, *The Siege of Charleston*** (Neale, 1911; Cornell scan
  `cu31924030918316`), chapter V from "Early in December Captain Q. A. Gillmore" to the
  report of the fort's reduction (OCR pp.79–86). The book was published posthumously from an
  unfinished manuscript; its Fort Pulaski narrative repeats Gillmore's figures (the 385-man
  garrison, the battery list) and is not independent of his report. Jones was a Confederate
  general and is placed in the author group `samuel-jones-east-tennessee-reports`, reused from
  the main registry.

Read but not selected: Hunter's April 13 report (in part), Gillmore's April 23, 1862 letter on
Viele's report, the journal of the Savannah River investment and General Orders No. 17. The
volume's Fort Pulaski report list names Hunter, Benham, Viele, O'Rorke, Gillmore, Cooper,
Pemberton and Lawton; no report by Olmstead is listed, and none of the Confederate reports
was inspected. No targeted follow-up was used. Stop after this record.

## New source records

This campaign adds **4 records**: the GA001 NPS HTML/text pair, the Gillmore selection and the
Jones Fort Pulaski selection. The Gillmore selection's parent is the already registered Volume
VI OCR (`or6-illinois-ocr-v1`); this pass's byte-identical copy and catalog record were
deduplicated at merge. The Jones parent OCR and metadata are counted with Charleston 1862.
Gillmore's selection reuses the author group `gillmore-petersburg-june-9-report` from the main
registry; separately registered reports by one author are not mutually independent
corroboration.

## Decisions and limits

- **Scope.** The January–March investment by batteries on the Savannah River and the
  blockade from February 22 are context. The record is April 10–11.
- **Opening strength remains unknown.** The frozen bounds are blank and the live force field
  reads zero. Every figure is recorded with its date and scope, and none is adopted:
  - Gillmore's December 1, 1861 estimate of "probably" 700 good troops in the fort;
  - the 385-man garrison found at the surrender (Gillmore 1865; Jones, who gives five
    companies of the First Georgia);
  - Union units named without numbers;
  - armament: 48 guns in the fort with 20 bearing on Tybee (Gillmore 1865) against 46 with
    twenty of the heaviest bearing (Jones); thirty-six Union pieces (Gillmore 1862, Jones)
    against "30 pieces" as the 1865 report reads in OCR; that report's own itemized table in the
    same section lists 36 pieces (a computation from its rows), so the OCR figure is probably a
    misreading, not an independent count.
- **Disputes preserved.** Isolation: Jones says the Lazaretto Creek force and the Venus Point
  and Bird Island batteries "effectually isolated" Pulaski; Gillmore says perfect isolation
  proved impossible and messengers passed (Jones is not independent of Gillmore). Casualties:
  frozen 365 (US 1; CS 364) against live 2 (US 1; CS 1); Gillmore reports one Union man killed
  and several of the garrison wounded, one fatally. The frozen CS 364 appears to count a
  different population from the live CS 1; neither basis is stated in an inspected passage.
- **Command roles and ranks.** The frozen commanders are Hunter (Major General), Gillmore
  (Captain) and Olmstead (Colonel); the live page lists Hunter and Olmstead. Gillmore was the
  engineer and commander of the forces on Tybee; Hunter took command of the department on
  March 31, made no change to the works and sent the summons. Jones says Gillmore was given
  brigadier's rank. No inspected passage by Olmstead describes his decisions. No listed
  commander receives automatic sole credit.
- **Tags.** All claims stay `unresolved` or `post_outcome`. The fort is prewar construction,
  but the battery sites and screening were the besiegers' choices; nothing is tagged
  `inherited`.

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

GA001 is revised under `fort-pulaski-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/GA001.v1.json`.

- **R1** (`concealment-and-messengers`): the rationale said no Confederate report is listed; the
  Volume VI report list names Pemberton's (No. 7) and Lawton's (No. 8). The rationale now says
  they are listed and were not inspected, and that no report by Olmstead is listed.
- **R2** (`reported-force-scope`): Jones's "eleven batteries mounting thirty-six guns" is now
  cited (p.82), and the rationale records that the 1865 report's "30 pieces" conflicts with its
  own battery table (3+3+3+3+1+3+2+4+6+4+4 = 36, a computation from the listed rows).
- **R11** (this memo): the Volume VI paragraph and the record count predated the merge
  deduplication. The memo now names the registered parent and gives 4 records, not 6.

Advisories:

- **Adopted:** A1 (`casualty-records` rationale: "possibly captured garrison against battle
  casualties; neither basis is stated") and A2 (`siege-labor-and-isolation`: Jones's "effectually
  isolated" is cited, p.81, and its difference from Gillmore's statement is recorded; this memo's
  disputes list adds it).

The review correction adds no source records. Citations rise from 49 to 51; claims (9), unknowns
(1) and disputed claims (2) are unchanged. No model input, cohort file, admission proposal or
baseline is changed.

After the review correction, `python3 -m generalship check` and `python3 -m unittest discover -s
tests` pass (134 tests) in the main repository, and `gs.MISSES` is empty.
