# Operations to Suppress the Sioux Uprising, 1862: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both **frozen
records** in **Operations to Suppress the Sioux Uprising [August-September 1862]** now have draft
dossiers: **18 claims, 2 explicit null unknowns and 85 citation occurrences** (84 before the review
correction below). All seven dimensions are represented in each record. All dossiers are drafts; no
features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| MN001 — Fort Ridgely | 1862-08-20 to 1862-08-22 | 9 | 1 | 42 | 3 |
| MN002 — Wood Lake | 1862-09-23 | 9 | 1 | 43 | 3 |

It was drafted in a parallel worktree with eight other frontier and Texas-coast campaigns. Dossier
presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and both retained NPS pages in full.
NPS/CWSAC and the Arnold tables are one family.

| Record | Second family | Third family |
| --- | --- | --- |
| MN001 | Sheehan | Jones |
| MN002 | Sibley | Marshall |

- **Official Records, Series I, Volume XIII** (1885; University of Illinois scan
  `warofrebellion13unit`, whose OCR title reads Series I Volume XIII):
  - **Sheehan's** August 26, 1862 report on Fort Ridgely with the return of casualties in the
    garrison (No. 1, pp.248–249; the return's columns are garbled in OCR);
  - **Jones's** August 26, 1862 report on the post artillery (No. 2, pp.249–250);
  - **Sibley's** September 23, 1862 report on Wood Lake to Governor Ramsey, with his explanatory
    note of November 18, 1865 (No. 1, pp.278–280);
  - **Marshall's** September 23, 1862 report on the five companies of the Seventh Minnesota (No. 2,
    pp.280–281).

Sibley's September dispatches in the correspondence were seen only as text-search hits. Not
inspected: any Dakota account, the returns of the expedition, histories of the war (for example
Heard's 1863 history) and maps. No targeted follow-up was used. Stop after this batch.

This pass adds **8 source records**: two NPS HTML/text pairs and the selections
`or13-sheehan-fort-ridgely-selections-v1`, `or13-jones-fort-ridgely-selections-v1`,
`or13-sibley-wood-lake-selections-v1` and `or13-marshall-wood-lake-selections-v1`. New author
groups: `sheehan-fort-ridgely-report`, `john-jones-fort-ridgely-report`, `sibley-sioux-reports`
(also used for Sibley's 1863 Dakota report) and `marshall-sioux-reports`; the container is
`or-series-i-volume-xiii`. No earlier registry group exists for these authors. The selections reuse
the registered Volume XIII parent `or13-illinois-ocr-v1`; this pass's byte-identical copy was not
registered again.

## Decisions and limits

- **Scope.** Marsh's ambush before the Fort Ridgely attacks, the killings across the valley,
  Sibley's march from September 19 and the later surrender at Camp Release are context only.
- **Opening strengths remain unknown.** Every figure is recorded and none adopted:
  - Fort Ridgely: the frozen force field has no figures and the live field reads 0; the frozen
    description's about 400 Sioux on August 20 and 800 on August 22 are not traced in the
    reports. Sheehan names his units (the remnant of Company B and a detachment of Company C,
    Fifth Minnesota, and the Renville Rangers) and armed refugees, without figures.
  - Wood Lake: the frozen 1,500 (the column leaving Fort Ridgely) and 700 warriors; Sibley's about
    300 attackers, 27 cavalry and Campbell's relayed 800 assembled within 2 miles, the greater part
    not engaged; Marshall's five companies.
- **Disputes preserved** (3 claims marked `disputed`):
  - Fort Ridgely casualties: frozen US 16 (Sheehan's return totals 16) against the live 26.
  - Wood Lake force figures (300, 700, 800) and casualties (frozen US 37, live 41 and 25; Sibley 4
    killed and 35–40 wounded; Campbell's 30 Dakota killed; 14 bodies buried; Marshall's 7).
- **Command roles.** The frozen commanders are First Lieutenant Sheehan, Colonel Sibley and Little
  Crow (no rank). The live pages give Sibley as brigadier general and tag Little Crow [CS]; neither
  is adopted, and Sibley's 1865 note says he was acting as colonel under the Governor. The inspected
  reports do not name Little Crow at Fort Ridgely and mention him at Wood Lake only in Campbell's
  relayed statement. No listed commander receives automatic sole credit.
- **No Dakota account was inspected.** Every statement of Dakota numbers, aims and losses comes
  from their opponents or the NPS summary; NPS's statement of grievances is recorded as NPS's.
- **Tags.** No claim is tagged `inherited`: the Fort Ridgely ravines are natural, but the
  outbuildings were destroyed on the defenders' order, and the Wood Lake rifle pits were dug.
  Outcomes are `post_outcome`.

The two null unknowns are the opening strengths. No morale/readiness score, probability, causal
effect or commander ranking is introduced. No model input, frozen baseline or admission proposal is
changed.

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
`sioux-1862-review-correction-2026-09-25`.

- **FRC-01 (accepted, applied).** The record count is corrected from 10 to 8 above, and the reuse of
  the registered Volume XIII parent is stated.
- **FRA-13 (applied).** MN002 `command-roles` now also cites Sibley's statement that Marshall "led his
  men to a charge and cleared the ravine" (p.279).
- **FRA-01 (not adopted here).** The Sibley author-group note belongs in `docs/sources.md`, which this
  pass does not edit; the proposed wording is left to the primary. The groups are unchanged.

MN001 is unchanged by the review. MN002 is revised (`sioux-1862-review-correction-2026-09-25`). No
source record is added by the correction.
