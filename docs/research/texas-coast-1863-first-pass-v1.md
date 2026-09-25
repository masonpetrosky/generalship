# Operations to Blockade the Texas Coast, 1863: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
**frozen record** in **Operations to Blockade the Texas Coast [September 1863]** now has a draft
dossier: **9 claims, 1 explicit null unknown and 51 citation occurrences** (46 before the review
correction below). All seven dimensions are represented. The dossier is a draft; no features are
admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| TX006 — Sabine Pass II | 1863-09-08 | 9 | 1 | 51 | 4 |

It was drafted in a parallel worktree with eight other frontier and Texas-coast campaigns. Dossier
presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family.

- **Official Records, Series I, Volume XXVI, Part 1** (1889; University of Illinois scan
  `warofrebellion261unit`, whose OCR title reads Series I Volume XXVI, Part I):
  - **Franklin's** September 11 and 14, 1863 reports, with the compiler's report list (No. 3,
    pp.285–286 and 294–298);
  - **Dowling's** September 9, 1863 report from Fort Griffin (No. 10, pp.311–312);
  - **Crocker's** September 12, 1863 report, written at Houston as a prisoner and found in the files
    of the District of Texas (No. 6, pp.301–302), as the **targeted follow-up** for the command
    dispute.

Read, not selected: Banks's No. 1 reports (partly), Weitzel's No. 4 report and the itineraries,
Magruder's No. 7 reports and orders (partly), Odlum's No. 9 reports and the opening of the
congressional resolution (No. 11). Not inspected: the naval reports the compiler refers to the
Secretary of the Navy's 1863 annual report, returns and charts. Stop after this record.

This pass adds **5 source records**: one NPS HTML/text pair and the selections
`or26-1-franklin-sabine-pass-selections-v1`, `or26-1-dowling-sabine-pass-selections-v1` and
`or26-1-crocker-sabine-pass-selections-v1`. The parent OCR is byte-identical to the copy a parallel
Gulf pass fetched and uses the same record ID and archival identifier, and was deduplicated at
merge; the selections reuse `or26-1-illinois-ocr-v1`. New author groups:
`franklin-sabine-pass-reports` and `dowling-sabine-pass-report`; Crocker is in
`crocker-texas-coast-reports` with his 1862 report. The container is `or-series-i-volume-xxvi`. No
main-registry group for Franklin or Dowling was found.

## Decisions and limits

- **Scope.** The embarkation from New Orleans on September 4, the return by September 11 and the
  later Rio Grande expedition are context only.
- **Opening strength remains unknown.** The frozen and live CS 44 (Davis Guards) and the frozen
  gunboats and transports are recorded with Dowling's 47 men in the fort on September 8 and
  Franklin's figures of different moments: about 1,000 infantry in Weitzel's advance at embarkation,
  700 inside the bar and 700 aground at about 10 a.m. on September 8, and 1,200 landable after the
  engagement. Magruder's 40 and 15,000 were read, not selected. None is adopted.
- **Disputes preserved** (3 claims marked `disputed`):
  - Force figures (44 against 47, and the Union figures of different scope).
  - **Responsibility.** Crocker says the Granite City and the General Banks made no attempt to follow
    and blames Franklin's failure to co-operate; Franklin says the plan was adopted with Crocker and
    refers to Weitzel's report for why the landing could not be made. Neither account is adopted.
  - Casualties: frozen US 230 and CS unknown; live 350 (US 350; CS 0); NPS about 200 prisoners;
    Dowling about 350 prisoners, two gunboats and thirteen guns. Prisoner counts may include naval crews.
- **Command roles.** The frozen commanders are Lieutenant Dowling, Major General Franklin and Captain
  Crocker (navy). The live page gives Franklin as brigadier general; not adopted. No listed commander
  receives automatic sole credit.
- **Tags.** The bar, marsh and channels are tagged `inherited`; the fort and its field of fire are
  excluded from that tag. Outcomes are `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
commander ranking is introduced. No model input, frozen baseline or admission proposal is changed.

## Validation

`python3 -m generalship check` passes and `python3 -m unittest discover -s tests` passes (134 tests)
in the worktree. After the review correction, both pass again (134 tests) in the main repository,
and `gs.MISSES` is empty.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the nine frontier
and Texas-coast first passes together at prepared commit `d57de7e` as
`frontier-review-d57de7e-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": fifteen
required findings (FRC-01 to FRC-15) and fourteen advisories (FRA-01 to FRA-14) across the nine
passes. It is an AI review within its stated scope, not human historical adjudication, proof of
source independence or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the registry
record) before any change; every new quote occurs in its cited section, and the dossiers were
regenerated from the builder. Each changed dossier's reviewed version is archived byte-for-byte as
`data/evidence/history/<ID>.v1.json` and linked by `supersedes` under the revision
`texas-coast-1863-review-correction-2026-09-25`.

- **FRC-01 (accepted, applied).** The record count is corrected from 7 to 5 and the merge
  deduplication of the Volume XXVI part 1 parent is stated above.
- **FRC-12 (accepted, applied).** TX006 `command-roles` now records the clock dispute beneath Crocker's
  charge: Crocker's 4 p.m. before Franklin was ready, Franklin's movement at 3 and Dowling's fleet out
  of range until 3.40.
- **FRA-05 (applied).** Crocker signs as Acting Volunteer Lieutenant; Franklin calls him
  Lieutenant-Commander and Captain; the frozen rank Captain is recorded, not adopted.
- **FRA-08 (applied).** "Prisoner counts include naval crews" is softened to "may include".

TX006 is revised (`texas-coast-1863-review-correction-2026-09-25`). No source record is added by the
correction.
