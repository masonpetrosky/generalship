# Operations in Mobile Bay: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
frozen record in **Operations in Mobile Bay [August 1864]** now has a draft dossier: **9 claims,
1 explicit null unknown and 56 citation occurrences**. All seven dimensions are represented. The
dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| AL003 — Mobile Bay (Passing of Forts Morgan and Gaines) | 1864-08-02 to 08-23 | 9 | 1 | 56 | 3 |

Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family. Two further families:

- **Mahan, *The Gulf and Inland Waters*** (Scribner, 1883) is a retrospective naval history by a
  Union naval officer. It is already registered from the Project Gutenberg transcription of the
  1898 London printing (`mahan-gulf-inland-text-v1`); a second selection from that parent was
  made rather than registering an Internet Archive scan.
  - Selected: Chapter VIII from its opening through the surrender of Fort Morgan (digital page
    markers pp.218–245).
  - Read but not selected: the rest of Chapter VIII (the 1865 naval operations) and the
    chapter's footnotes.
  - The chapter compiles its table of times "From a careful comparison of the logs and reports"
    and quotes Farragut and Buchanan. It is not independent of the naval reports.
- **Page's** reports and telegrams to Maury (Official Records Series I, Volume XXXIX, Part 1,
  No. 14, pp.435–441) are the Confederate report family. Page commanded Fort Morgan and the
  outer defenses throughout the frozen interval.
  - Selected: the August 6 report, the August 8 telegram, the August 8 report on Fort Gaines,
    the August 23 note and the August 30 report on the siege.
  - The volume and part were checked against the OCR title page ("SERIES I~VOLUME XXXIX …
    PART I-REPORTS", 1892).

Also read but not selected: the Mobile Bay report list (Nos. 1–25) and Canby's No. 1 dispatches.

The following were not inspected:

- Granger's report (No. 4), named in the assignment as a candidate. The three-family ceiling
  went to Page, so the record has a Confederate primary account; Mahan covers Granger's landing,
  investment and siege.
- Buchanan's and the other naval and army reports in Volume XXXIX.
- Farragut's report in the Official Records of the Navies.

No targeted follow-up was used. Stop after this record.

**Consequential gap.** No return gives Granger's land force or the prisoner counts for Forts
Gaines and Morgan in an inspected family. Canby's dispatches, read but not selected, give prisoner
counts; they would be a fourth family.

This pass adds **6 source records**:

- the NPS HTML/text pair;
- a second Mahan selection from the registered parent (existing group
  `mahan-gulf-inland-waters`);
- the Volume XXXIX Part 1 catalog metadata and full OCR (new parent) and the Page selection (new
  group `page-mobile-bay-1864-reports`).

A parallel Franklin-Nashville worktree has also fetched Volume XXXIX Part 1
(`data/raw/franklin-nashville-v1/or39-1-full.txt`), not registered there when checked. The
primary should reconcile the two parents at merge so the volume is registered once.

## Decisions and limits

- **Scope.** The frozen interval spans several phases, all kept within the one record and not
  split:
  - the landing on Dauphin Island and investment of Fort Gaines;
  - the August 5 passage of the forts and naval battle;
  - the evacuation of Fort Powell and surrender of Fort Gaines;
  - the siege and August 23 surrender of Fort Morgan.

  The 1865 Mobile Campaign is a separate campaign.
- **The opening strength remains unknown.** The frozen side-specific bounds are blank and the
  live field reads zero. Every figure below is recorded with its scope, and none is adopted:
  - the frozen force text: 14 wooden ships and 4 monitors, against three gunboats and an
    ironclad and three garrisons;
  - NPS: eighteen ships;
  - Page: twenty-three men-of-war, four of them monitors;
  - Mahan: the order of attack in two columns and Buchanan's four vessels;
  - Mahan: Granger had "not men enough to attack both forts at once";
  - Page: some 400 effective in Fort Morgan during the siege.
- **Disputes preserved.**
  - The number of ships: 18 against 23.
  - The date of Fort Gaines's surrender: Mahan puts it the day after August 6; Page says the
    Union flag rose over Gaines at 9.30 on August 8.
  - Casualties:
    - the frozen record gives 1,822 (US 322; CS 1,500) and the live page 1,827 (US 327);
    - Mahan gives the Tennessee's loss as 2 killed and 10 wounded, the Union fleet's as 52 killed
      and 170 wounded, the Selma's as 5 killed and 10 wounded, and 21 saved from the Tecumseh;
    - Page calls his losses slight, and his lists are marked "Not found".
  - The live page files the record under "Burbridge's Raid into Southwest Virginia". This is
    recorded and not adopted.
- **Command roles and ranks.** Mahan describes Farragut and Buchanan directing in person. Page
  rejected the joint Farragut–Granger demand and condemned Anderson's surrender of Gaines. The
  live page gives Farragut as Admiral and misspells Buchanan; the frozen Rear Admiral is kept. No
  listed commander receives automatic sole credit.
- **Tags.** The forts, channel and torpedo lines predate the attack. Even so, no claim is tagged
  `inherited`; all stay `unresolved` or `post_outcome`.

The one null unknown is the opening strength. No morale/readiness score, probability, causal
effect or new commander ranking is introduced. The cohort, both admission proposals and the
baseline are unchanged.

## Separate review pending

No separate review has been run for this record. A Claude Opus 5.5 `high` evidence-reviewer
assignment should be prepared by the primary after commit, bound to the exact commit, dossier and
source hashes. Coverage, separate review and feature admission stay distinct.
