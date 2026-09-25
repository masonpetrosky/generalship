# Operations in West Louisiana (April 1863): bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). All **three
frozen records** in **Operations in West Louisiana [April 1863]** now have draft dossiers:
**27 claims, 3 explicit null unknowns and 120 citation occurrences**. All seven dimensions are
represented in each record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| LA006 — Fort Bisland | 1863-04-12 to 04-13 | 9 | 1 | 44 | 3 |
| LA007 — Irish Bend | 1863-04-14 | 9 | 1 | 42 | 3 |
| LA008 — Vermillion Bayou | 1863-04-17 | 9 | 1 | 34 | 3 |

This pass was drafted alongside the other 1862-1863 Louisiana campaigns. Existing dossiers,
reviews and historical revisions are unchanged. Dossier presence is not first-pass acceptance,
separate review or model eligibility.

## Inspection and stopping record

Read all three frozen battle, force and commander row sets and the three retained NPS pages in
full. NPS/CWSAC and the Arnold tables are one family. Every record uses the same two further
families.

- **Irwin, *History of the Nineteenth Army Corps*** (Putnam's, 1892), already registered. A new
  selection (`irwin-west-louisiana-1863-selections-v1`) reuses the registered parent
  `irwin-nineteenth-corps-ocr-v1`. It cites Taylor's report and the Official Records nominal lists,
  so it is not independent of them. Selected:
  - Chapter IX from Banks's return to New Orleans on March 24 to its end (OCR pp.88-93);
  - Chapter X, Bisland (pp.94-103; the p.100-102 heads read "lOO", "loi" and "I02");
  - Chapter XI, Irish Bend (pp.104-120);
  - Chapter XII, Opelousas, to the rebuilding of the Vermilion bridge (pp.121-125).
- **Taylor's** report of April 23, 1863 on operations of April 9-23 (*Official Records* Series I,
  Volume XV, No. 39, pp.388-396; the p.393 head reads "893"), from the Volume XV parent pinned in
  the Baton Rouge pass.

The earlier part of Irwin's Chapter IX (pp.85-88) was read but not selected. Banks's No. 1 report
(opening only seen) and return of casualties, Weitzel's, Emory's, Grover's, Dwight's, Birge's and the
other Union reports (Nos. 2-37), Kirby Smith's No. 38 and Mouton's No. 40 reports, the naval reports
and print pages were not inspected. No targeted follow-up was used. Stop after this batch.

**Consequential gap.** No Confederate loss return exists in the inspected passages (Irwin: "never
been reported"; Taylor could not yet estimate), and Banks's return of casualties, which could check
the frozen 234 against Irwin's 224, was not inspected.

**New source records.** This pass adds **8 source records**: three NPS HTML/text pairs, the Taylor
selection and the Irwin Teche selection (reusing the registered parent). It uses the OR Volume XV
parent registered in the Baton Rouge pass.

## Decisions and limits

- **Scope.** The Berwick Bay crossing (April 9-11), Grover's landing and skirmishes of April 13,
  and the pursuit to Opelousas and Alexandria are context. Grover's return of 353 covers April 13,
  14 and 17; it is cited in LA007 and noted in LA008, and is not split or added.
- **Opening strengths remain unknown.** Every frozen bound is blank. Every figure is recorded with
  its date and scope, and none is adopted:
  - Bisland: Irwin, Banks 10,000 against Taylor's reported 4,000 with 24 or 25 guns; Banks set out
    with seven brigades and fifty-six guns. Taylor: at least 14,000 and about sixty guns in his
    front on April 13; his army less than 4,000 at the start.
  - Irish Bend: Irwin, Grover about 5,000, Birge not over 1,500 with a fighting line of perhaps
    1,200, Taylor's charge less than 1,000 (from Taylor), eighteen Union guns with four in action.
    Taylor: less than 1,000 in the charge against four regiments, a cavalry battalion and a
    battery, with a larger reserve concealed.
  - Vermilion: Irwin's three-to-one ratio on April 15; no count for the action.
- **Disputes preserved.**
  - Bisland: the Union strength (10,000 against 14,000); the result (Taylor's "gained no ground"
    against the abandoned works); losses (frozen 684 with US 234, live 674 with US 224, Irwin's
    224; no Confederate figure).
  - Irish Bend: the result (Taylor's successful charge and escape against the Union victory);
    losses (frozen US 353 and CS unknown, live 355 and CS 0, Irwin's 353 and 21 Confederate dead
    and 35 wounded left on the field).
  - Vermilion: NPS's artillery repulse against Irwin's "drove off the enemy"; losses (frozen
    Unknown, live zero, Irwin's one killed and five wounded in Dwight's brigade).
- **Command roles.**
  - Taylor blames Sibley for the failed Bisland counterattack and the loss of the Diana's crew,
    and credits Mouton and Green.
  - Banks gave discretionary assault orders at Bisland and recalled them; Grover's conduct at Irish
    Bend is described by Irwin as cautious and governed by orders based on misinformation.
  - No listed commander receives automatic sole credit.
- **Tags.** Taylor chose the Nerson's Woods ground, and the Bisland works were partly recent, so no
  claim is tagged `inherited`. All claims stay `unresolved` or `post_outcome`.
- **Families.** Irwin stays in `irwin-nineteenth-corps-1892`. Taylor's report is placed in his
  existing group `taylor-red-river-1864-reports` (from the Red River pass), because one author's
  reports are one family; the group name refers to the earlier registration.

The three null unknowns are the three opening strengths. No morale/readiness score, probability,
causal effect or new commander ranking is introduced. The cohort, both admission proposals and the
baseline are unchanged, with **zero promoted rows**. `python3 -m generalship check` passes, the unit
tests pass, and the baseline still reports **23/127 eligible engagements in 13 groups**, with
strength Brier **0.276882** against **0.250000** for equal odds.

## Separate review pending

No separate review has been run for this campaign. A Claude Opus 5.5 `high` evidence-reviewer
assignment should be prepared by the primary after commit, bound to the exact commit, dossiers
and source hashes. Coverage, separate review and feature admission stay distinct.
