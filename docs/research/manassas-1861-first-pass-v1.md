# Manassas Campaign, 1861: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). All **three
frozen records** in **Manassas Campaign [July 1861]** now have draft dossiers: **27 claims, 3
explicit null unknowns and 157 citation occurrences**. All seven dimensions are represented in
each record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| WV002 — Hoke's Run | 1861-07-02 | 9 | 1 | 45 | 3 |
| VA004 — Blackburn's Ford | 1861-07-18 | 9 | 1 | 51 | 3 |
| VA005 — Manassas, First | 1861-07-21 | 9 | 1 | 61 | 3 |

This pass was drafted with five other 1861 eastern campaigns and adds no parent source: it reuses
the Nicolay parent registered by the Charleston pass and the Official Records Volume II parent
registered by the Chesapeake pass. Dossier presence is not first-pass acceptance, separate review
or model eligibility.

## Inspection and stopping record

Read all three frozen battle, force and commander row sets and the three retained NPS pages in
full. NPS/CWSAC and the Arnold tables are one family.

| Record | Second family | Third family |
| --- | --- | --- |
| WV002 | Patterson (OR II) | T. J. Jackson (OR II) |
| VA004 | Nicolay | Beauregard (OR II) |
| VA005 | Nicolay | McDowell (OR II) |

- **Nicolay, *The Outbreak of Rebellion*** (1881). Four passages from Chapters XIV–XVII:
  - the two armies' numbers (pp.173–176);
  - Blackburn's Ford (pp.177–180);
  - Chapter XV, Bull Run (pp.181–196);
  - Chapter XVI, The Retreat, with the opening of Chapter XVII on losses (pp.197–206).

  In OCR the p.190 head reads "100", p.198 "103" and p.202 "C02". Nicolay's Chapter XIII was
  read; it mentions the Falling Waters skirmish in a single clause, so Hoke's Run uses two report
  families instead.
- ***Official Records* Series I, Volume II** (University of California scan):
  - Patterson's July 3 telegram, July 4 letter and July 4 telegram (pp.157–158);
  - T. J. Jackson's July 3 report, which quotes Harper and Stuart (pp.185–186);
  - Beauregard's July 17 telegram (p.439; the p.440 head reads "4-iO") and his report on
    Blackburn's Ford, dated "August — , 18G1" with the day blank (pp.440–447);
  - McDowell's July 21 and 22 telegrams and his report headed "August 4," with no year in OCR
    (pp.316–325).

Read but not selected:

- Hoke's Run: the Simpson, Thomas, Perkins, Keim, Abercrombie, Starkweather, Jarrett and Hudson
  reports, Johnston's transmittal and the June 28–30 returns (the Confederate abstract is
  garbled);
- Blackburn's Ford: Beauregard's Special Orders No. 100 and indorsement;
- First Manassas: McDowell's appendices B and C, in part.

Not inspected: Tyler's, Richardson's and McDowell's July 16–20 reports on Blackburn's Ford;
Beauregard's and Johnston's July 21 reports; the division and brigade reports; the consolidated
returns; maps and print pages. No targeted follow-up was used. Stop after this batch.

The pass adds **11 source records**:

- three NPS HTML/text pairs;
- five selections: `nicolay-manassas-selections-v1`,
  `or2-patterson-falling-waters-selections-v1`, `or2-tjjackson-falling-waters-selections-v1`,
  `or2-beauregard-blackburns-ford-selections-v1` and `or2-mcdowell-bull-run-selections-v1`.

Beauregard's new group, `beauregard-bull-run-1861-reports`, is the same author family as the
registered Shiloh group `or-beauregard`; the dependency note says so.

## Decisions and limits

- **Scope.** Patterson's movements after July 2, Johnston's move from the Valley, the Mitchell's
  Ford demonstration of July 18, the McLean's Ford attack of July 21 and the retreat to
  Washington are context.
- **Opening strengths remain unknown.**
  - Hoke's Run and Blackburn's Ford have blank frozen bounds. Blackburn's Ford's live 57,000 (US
    35,000; CS 22,000) repeats the NPS description's whole-army figures.
  - First Manassas is frozen at US 28,450 and CS 32,230; the live page reads CS 3,230.
  - Recorded, not adopted:
    - Nicolay: McDowell's command of 34,320, a moving column of 28,568 with 49 guns and the
      Confederates' 32,073 with 57 guns;
    - McDowell: about 18,000 who crossed Bull Run;
    - Beauregard: over 3,000 attackers against 1,200 bayonets at Blackburn's Ford;
    - Patterson: 3,500 scattered at Hoke's Run;
    - Jackson: one regiment (380 men) and one gun engaged.
- **Disputes preserved.**
  - Hoke's Run: losses (frozen 114 against live 98).
  - Blackburn's Ford:
    - Nicolay calls it undecisive, with equal loss and demoralization, against the recorded
      Confederate victory;
    - Confederate losses are 68 (Beauregard) against 63 (Nicolay);
    - Longstreet's regiments number three (Beauregard) or five (Nicolay).
  - First Manassas losses:
    - frozen 4,700 against live 4,878;
    - McDowell's 481 killed and 1,011 wounded, with an inaccurate missing return;
    - Nicolay's Union 481/1,011/1,460 and Confederate 387/1,582;
    - an admitted 1,800 relayed by McDowell.

    Jones's McLean's Ford loss is kept separate.
  - NPS and the frozen description date the Union march "16 July, 1862"; the sources give 1861.
- **Command roles and ranks.**
  - Live ranks differ from frozen: McDowell (Major General live), T. J. Jackson (Major General
    live; he signs as colonel), and Johnston ("Lieutenant Colonel" live). They are not adopted.
  - At Blackburn's Ford neither listed commander directed the fighting in the inspected
    passages: Longstreet, Early and Tyler did.
  - At First Manassas, Nicolay has Johnston assuming command as ranking officer and Beauregard
    commanding the line on the plateau.
  - No listed commander receives automatic sole credit.
- **Campaign contribution.** NPS's statements that Patterson's retrograde freed Johnston and that
  First Manassas led to McDowell's replacement are campaign or political contribution, not
  tactical outcome.
- **Tags.** No claim is tagged `inherited`; all stay `unresolved` or `post_outcome`.

The three null unknowns are the opening strengths. No morale/readiness score, probability,
causal effect or new commander ranking is introduced. Nothing in this pass changes a model input.

## Separate review pending

No separate review has been run for this campaign. A Claude Opus 5.5 `high` evidence-reviewer
assignment should be prepared by the primary after commit, bound to the exact commit, dossiers
and source hashes. Coverage, separate review and feature admission stay distinct.
