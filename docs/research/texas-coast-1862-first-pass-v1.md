# Operations to Blockade the Texas Coast, 1862: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both **frozen
records** in **Operations to Blockade the Texas Coast [September 1862-January 1863]** now have draft
dossiers: **18 claims, 2 explicit null unknowns and 69 citation occurrences**. All seven dimensions
are represented in each record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| TX001 — Sabine Pass | 1862-09-24 to 1862-09-25 | 9 | 1 | 35 | 4 |
| TX002 — Galveston | 1862-10-04 | 9 | 1 | 34 | 3 |

It was drafted in a parallel worktree with eight other frontier and Texas-coast campaigns. Dossier
presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and both retained NPS pages in full.
NPS/CWSAC and the Arnold tables are one family.

| Record | Second family | Third family | Targeted follow-up |
| --- | --- | --- | --- |
| TX001 | Spaight | Crocker (ORN) | Debray |
| TX002 | Cook | Renshaw (ORN) | none |

- **Official Records, Series I, Volume XV** (1886; University of Illinois scan
  `warofrebellion15unit`, whose OCR title reads Series I Volume XV):
  - **Spaight's** September 26, 1862 report from Beaumont on the Sabine Pass battery, which Major
    Irvine commanded in his absence (No. 2, pp.144–145);
  - **Debray's** September 25, 1862 report from Houston (No. 1, pp.143–144), written from an express
    and a messenger, as the targeted follow-up for the frozen 30 and 25;
  - **Cook's** October 9, 1862 report on Galveston, with the compiler's report list, which dates the
    action October 5 (No. 3, pp.147–153).
- **Official Records of the Union and Confederate Navies, Series I, Volume 19** (1905; Trent
  University scan `officialrecordso0019unse`):
  - **Crocker's** October 2, 1862 report on the Sabine Pass expedition (pp.217–219);
  - **Renshaw's** October 5 and 8, 1862 reports on Galveston (pp.254–260).

Read, not selected: Spaight's September 29 and October 2 reports, Hebert's No. 1 and Debray's No. 2
Galveston reports with Documents A and B, the opening of Hooper's report and of Farragut's October 14
reply. Not inspected: Irvine's and Keith's reports (none seen), Pennington's report, Wainwright's,
Guest's and Law's reports, returns and charts. Stop after this batch.

This pass adds **13 source records**: two NPS HTML/text pairs; OR XV catalog metadata and full OCR
(`ia-or15-illinois-metadata-v1`, `or15-illinois-ocr-v1`) and ORN 19 catalog metadata and full OCR
(`ia-orn19-trent-metadata-v1`, `orn19-trent-ocr-v1`); and the selections
`or15-spaight-sabine-pass-selections-v1`, `or15-debray-sabine-pass-selections-v1`,
`or15-cook-galveston-selections-v1`, `orn19-crocker-sabine-pass-selections-v1` and
`orn19-renshaw-galveston-selections-v1`. The two parent OCR files are byte-identical to the copies a
parallel Gulf pass fetched and use the same record IDs and archival identifiers, so the primary can
deduplicate them at merge. New author groups: `spaight-sabine-reports`, `debray-texas-reports`,
`cook-galveston-report`, `crocker-texas-coast-reports` (also used for Crocker's 1863 report) and
`renshaw-galveston-reports`; the containers are `or-series-i-volume-xv` and `orn-series-i-volume-19`.
No earlier registry group exists for these authors in the main registry.

## Decisions and limits

- **Scope.** The Taylor's Bayou raid, the capture of blockade runners and Crocker's Calcasieu and
  Mermentau expeditions (Sabine), and the evacuation of the island during the truce and the later
  occupation (Galveston) are context only.
- **Opening strengths remain unknown.** Every figure is recorded and none adopted:
  - Sabine Pass: the frozen 30 at the fort and 25 mounted men 3 1/2 miles off (bounds 55 and 55)
    match Debray's second-hand figures of September 25; Spaight adds a detachment of 26 arriving at
    nightfall on the 24th. Crocker names his three vessels only; the live field reads 0.
  - Galveston: the frozen force field reads None and the live field 0. Renshaw names five vessels;
    Cook gives eight vessels off the bar, about twenty guns firing on one 10-inch gun, and two
    24-pounders on the bay side.
- **Disputes preserved** (1 claim marked `disputed`): the terms of the unwritten Galveston truce.
  Cook says the Confederates were not to build or strengthen defenses and the fleet not to approach;
  Renshaw says everything was to remain as it was, and that the unwritten agreement let the
  Confederates carry off guns.
- **Casualties.** Sabine Pass: frozen Unknown, live 0; Crocker reports no loss on his side. Galveston:
  frozen None and 0; neither report gives a figure. Absence of a figure is not a measured zero.
- **Command roles.** The frozen commanders are Acting Master Crocker and Major Irvine (Sabine Pass)
  and Colonels Cook and Debray and Commander Renshaw (Galveston). The live page gives Crocker as
  lieutenant; not adopted. Debray's Galveston role is described only by Cook. No listed commander
  receives automatic sole credit.
- **Tags.** No claim is tagged `inherited`: the Sabine bar-and-range claim mixes gun range with the
  bar, and the Galveston harbor claim includes a dummy battery. Outcomes are `post_outcome`.

The two null unknowns are the opening strengths. No morale/readiness score, probability, causal
effect or commander ranking is introduced. No model input, frozen baseline or admission proposal is
changed.

## Validation

`python3 -m generalship check` passes and `python3 -m unittest discover -s tests` passes (134 tests)
in the worktree.

## Separate review pending

No separate review has been run for this pass.
