# Mobile Campaign: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both frozen
records in the **Mobile Campaign [March-April 1865]** now have draft dossiers: **18 claims, 2
explicit null unknowns and 93 citation occurrences**. All seven dimensions are represented in
each record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| AL005 — Spanish Fort | 1865-03-27 to 04-08 | 9 | 1 | 46 | 3 |
| AL006 — Fort Blakely | 1865-04-02 to 04-09 | 9 | 1 | 47 | 3 |

Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and both retained NPS pages in full.
NPS/CWSAC and the Arnold tables are one family.

- **Canby's** report of June 7, 1865 (Official Records Series I, Volume XLIX, Part 1, No. 1,
  pp.91–100) is the Union report family for both records. It is selected together with the
  unsigned comparative casualty statement printed in its addenda (p.102). That statement is
  garbled in OCR, and the compiler marks it "But see revised statement, p. 115", which was not
  inspected. The addenda (pp.100–105) were read, and the rest was not selected. The volume and
  part were checked against the OCR title page ("SERIES I— VOLUME XLIX … PART I— REPORTS,
  CORRESPONDENCE, ETC.", 1897).
- **Gibson's** report of April 16, 1865 from Meridian (No. 97, pp.313–318) is the Confederate
  family for Spanish Fort. The OCR is badly garbled at line starts and ends, and his estimate of
  the Union muskets is unreadable.
- **Andrews, *History of the Campaign of Mobile*** (Van Nostrand, 1867) is the history family
  for Fort Blakely. The author commanded the Second Division, Thirteenth Corps, in the assault,
  so this is an interested participant account. It quotes Liddell's dispatches and Pile's report
  and shares the Union chain of command with Canby. Selected:
  - the title page;
  - Chapter XV, the investment (OCR pp.121–129);
  - Chapter XXIII, the last day and assault (pp.189–222);
  - Chapter XXIV, observations (pp.223–226).

  The running heads for pp.211, 214 and 221 are misread.

Not inspected:

- the organization and casualty returns (Nos. 2–3);
- Granger's, A. J. Smith's, Steele's and all division, brigade and naval reports, including
  Andrews's own report (No. 27);
- Andrews's Spanish Fort chapters and Blakely Chapters XXI–XXII.

No Liddell or Maury report appears in the inspected report list. No targeted follow-up was used.
Stop after this batch.

**Consequential gap.** Neither record has a Confederate return. Blakely has no Confederate
report in an inspected family, and its garrison strength comes from NPS and Andrews. Spanish Fort
uses Gibson in place of Andrews under the three-family ceiling.

This pass adds **11 source records**:

- two NPS HTML/text pairs;
- Andrews's catalog metadata, full OCR and selection (new group `andrews-mobile-1867`);
- the Volume XLIX Part 1 catalog metadata and full OCR (new parent; the Wilson's Raid pass also
  selects from it);
- the Canby selection (new group `canby-mobile-1865-reports`) and the Gibson selection (new
  group `gibson-spanish-fort-report`).

## Decisions and limits

- **Scope.** The frozen intervals overlap (March 27–April 8 and April 2–9). Each record keeps its
  own engagement. The following are context, not added:
  - Steele's march from Pensacola;
  - the Batteries Huger and Tracy operations;
  - the occupation of Mobile;
  - Canby's campaign-wide casualty and prisoner totals (including 4,924 prisoners accounted
    for).
- **Opening strengths remain unknown.** The frozen side-specific bounds are blank. Every figure
  below is recorded with its scope, and none is adopted:
  - Spanish Fort:
    - Canby: 32,200 at Mobile Point and Dauphin Island in mid-March;
    - Gibson: Thomas's reserves about 950 muskets, Patton's artillery 360 and his brigade 500
      rifles;
    - Gibson: "less than 2,000 men" against two corps and a fleet with over seventy-five guns
      on land.
  - Blakely:
    - NPS live figures: 20,000 (US 16,000; CS 4,000);
    - Andrews: a garrison of about 3,500, and "fully sixteen thousand troops" in the assault,
      with fifteen or twenty thousand more come up from Spanish Fort;
    - Canby: Steele's column 13,200 in mid-March.
- **Disputes preserved.**
  - Blakely's garrison: 3,500 against 4,000.
  - Blakely's works: Andrews says the line was nearly three miles long; Canby says two and a
    half miles.
  - Spanish Fort casualties:
    - frozen 1,401 (US 657; CS 744) against live 1,398 (CS 741);
    - Canby: more than 600 prisoners;
    - Gibson: 73 killed, 350 wounded and about six missing before the evacuation, and about 20
      killed, 45 wounded and 250 captured that night;
    - Gibson's guess of 2,500 Union losses.
  - Blakely casualties:
    - frozen 4,475, with April 9 alone 3,529 (US 629; CS 2,900); the frozen side rows give 798
      and 3,677;
    - live 4,475 (US 775; CS 3,700);
    - Canby: 3,700 prisoners;
    - Andrews: 654 Union killed and wounded in the assault and 3,423 prisoners.
  - The garbled comparative-statement figures are quoted as read, and their columns are not
    assigned.
- **Command roles and ranks.**
  - Canby says he set the Spanish Fort bombardment time on A. J. Smith's suggestion and credits
    Geddes, Carr and Smith with the lodgment.
  - Gibson says he decided to withdraw under Maury's standing orders.
  - At Blakely, Canby instructed Steele; Andrews says Steele fixed the hour.
  - The live pages give Canby and Liddell as Brigadier General; the frozen ranks are kept. No
    listed commander receives automatic sole credit.
- **Tags.** No claim is tagged `inherited`. All stay `unresolved` or `post_outcome`.

The two null unknowns are the opening strengths. No morale/readiness score, probability, causal
effect or new commander ranking is introduced. The cohort, both admission proposals and the
baseline are unchanged.

## Separate review pending

No separate review has been run for this campaign. A Claude Opus 5.5 `high` evidence-reviewer
assignment should be prepared by the primary after commit, bound to the exact commit, dossiers
and source hashes. Coverage, separate review and feature admission stay distinct.
