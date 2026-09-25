# Operations in the Indian Territory, 1861: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). All **three
frozen records** in **Operations in the Indian Territory [November-December 1861]** now have draft
dossiers: **27 claims, 3 explicit null unknowns and 116 citation occurrences**. All seven dimensions
are represented in each record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| OK001 — Round Mountain | 1861-11-19 | 9 | 1 | 34 | 3 |
| OK002 — Chusto-Talasah | 1861-12-09 | 9 | 1 | 42 | 3 |
| OK003 — Chustenahlah | 1861-12-26 | 9 | 1 | 40 | 3 |

It was drafted in a parallel worktree with five other 1861 western campaigns. Dossier presence is not
first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read all three frozen battle, force and commander row sets and the three retained NPS pages in full.
The OK001 live page has an empty description and a blank force field, so its frozen CWSAC description
is that family's narrative. NPS/CWSAC and the Arnold tables are one family.

| Records | Second family | Third family |
| --- | --- | --- |
| OK001, OK002 | Cooper | Britton |
| OK003 | McIntosh | Cooper |

- **Official Records, Series I, Volume VIII** (1883; University of Illinois scan
  `warofrebellion08unit`, whose title page confirms Series I Volume VIII):
  - **Cooper's** January 20, 1862 report covering all three engagements (No. 1, pp.5–14). The p.5
    running head is merged into the report heading in OCR and the locator is inferred; several lines
    are garbled.
  - **McIntosh's** January 1, 1862 report on Chustenahlah (No. 10, pp.22–25).
- **Britton**, *The Civil War on the Border*, volume I (second edition, 1891), registered with the
  Missouri 1861 pass: the title page and preface and Chapter XIII (pp.164–174), which describes Round
  Mountain without naming it and covers Chusto-Talasah and Chustenahlah.

Britton's chapter covers Chustenahlah but was not used for OK003: Cooper's report was chosen there
because the frozen force field names Cooper's brigade, and both commanders' reports address whether it
was engaged. McIntosh's January 4 transmittal, the letters found in the camp and W. C. Young's No. 11
report were read while delimiting and not selected. Not inspected: Brinson's and Young's Round
Mountain reports (Nos. 2–3), the Chusto-Talasah reports Nos. 4–9, the other Chustenahlah reports
(Nos. 12–15), Stand Watie's and Boudinot's reports, returns and maps. **No account by Opothleyahola's
side was inspected;** every figure for his force and losses is an opponent's estimate or Britton's. No
targeted follow-up was used. Stop after this batch.

This pass adds **11 source records**: three NPS HTML/text pairs; OR VIII catalog metadata and full OCR
(`ia-or8-illinois-metadata-v1`, `or8-illinois-ocr-v1`), shared with the Northeast Missouri pass; the
selections `or8-cooper-indian-territory-selections-v1` and `or8-mcintosh-chustenahlah-selections-v1`;
and `britton-border-1-indian-territory-selections-v1`. New author groups:
`cooper-indian-territory-report` and `mcintosh-chustenahlah-report`; Britton is in
`britton-civil-war-border`, and the container is `or-series-i-volume-viii`. Cooper wrote after
McIntosh and criticizes him; Britton uses the Confederate reports.

## Decisions and limits

- **Scope.** Cooper's march from the Deep Fork and return to Concharta, the December 8 dispersal of
  Drew's Cherokee regiment, Cooper's withdrawal to Fort Gibson, Stand Watie's December 27 pursuit and
  Cooper's scout toward the Kansas line are context only.
- **Opening strengths remain unknown.** All frozen bounds are blank; the live OK002 field gives CS
  1,300. Every figure is recorded and none adopted:
  - Round Mountain: Cooper's about 1,400 (the frozen description agrees) and 800–1,200 Creeks and
    Seminoles with 200–300 negroes; Britton's fourteen hundred, and fifteen hundred as the chief's own
    estimate of what he could field.
  - Chusto-Talasah: Cooper's 780, Drew's about 500 (dispersed the night before) and an engaged force
    not over 1,100; the enemy over 2,500, 4,000 by Cherokee prisoners, and 2,000 by an escaped
    prisoner; Britton's eleven hundred, five hundred and three hundred.
  - Chustenahlah: McIntosh's 1,600 at Fort Gibson and 1,380 on the march (the frozen description's
    figure), the enemy estimated at 1,700, and Stand Watie's 300 arriving at the end; Cooper's report
    that McIntosh announced some 2,000.
- **Disputes preserved** (10 claims marked `disputed`: three force-scope, three casualty, two result,
  one logistics and one command-role claim):
  - **Round Mountain.** Cooper lists a buggy, 12 wagons and provisions left in the camp; Britton says
    a few old ponies and broken wagons. Cooper says the enemy retreated under cover of darkness;
    Britton says the Union Indians first drove the attackers from the field.
  - **Chusto-Talasah.** Cooper says the enemy disappeared from his front; Britton says the
    Confederates withdrew five miles and Cooper, badly crippled, fell back to Fort Gibson. The live US
    412 equals the prisoners' figure in Cooper's report; Britton says the chief's loss was much less
    than the Confederates'.
  - **Chustenahlah.** The frozen force field names Cooper's brigade, but by both reports it did not
    reach the field. McIntosh gives 8 killed and 32 wounded in his text and "Killed, 0; wounded, 40" in
    his closing line (OCR); the basis of the live US 211 is not established in the selected passages.
  - **Command at Chustenahlah.** Cooper calls McIntosh's attack precipitate and argues the chief could
    have been captured had McIntosh waited; this is Cooper's interested judgment, not a causal finding.
- **Command roles and ranks.** The frozen commanders are Colonels Cooper and McIntosh and Opothleyahola
  (no rank; cited by name). The live pages give Cooper as Brigadier General and the chief as US; neither
  is adopted. No listed commander receives automatic sole credit.
- **Tags.** The Round Mountain creek timber and the Chustenahlah hill are tagged `inherited`; the
  Chusto-Talasah bend stays `unresolved` because its cover was strengthened with fallen logs. Outcomes
  are `post_outcome`.

The three null unknowns are the opening strengths. No morale/readiness score, probability, causal
effect or commander ranking is introduced. No model input, frozen baseline or admission proposal is
changed.

## Validation

`python3 -m generalship check` passes and `python3 -m unittest discover -s tests` passes (134 tests)
in the worktree.

## Separate review pending

No separate review has been run for this pass.
