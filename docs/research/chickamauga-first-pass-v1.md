# Chickamauga Campaign: bounded first pass

Prepared 2026-09-25. All **three frozen records** in **Chickamauga Campaign
[August-September 1863]** now have draft dossiers: **27 claims, 3 explicit null unknowns
and 147 citation occurrences** after review correction. All seven dimensions are
represented in each record. Separate Claude Opus 5.5 `high` [review](../../artifacts/review-results/chickamauga-93a2694-opus-high-v1/review.md) found
eight required corrections, all applied and verified by the primary. All dossiers remain
drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| TN018 — Chattanooga | 1863-08-21 | 9 | 1 | 38 | 3 |
| GA003 — Davis' Cross Roads | 1863-09-10 to 09-11 | 9 | 1 | 49 | 3 |
| GA004 — Chickamauga | 1863-09-18 to 09-20 | 9 | 1 | 60 | 3 |

Coverage is **108/127 draft dossiers**, **19 without**, and **27/36 complete source
campaigns by dossier presence**. All 105 earlier dossiers and all historical revisions
are unchanged.

## Inspection and stopping record

Read all three frozen battle, force and commander row sets and the three retained NPS
summaries in full. NPS/CWSAC and the Arnold tables are one family. Each battle uses two
further families:

- **Cist**, *The Army of the Cumberland* (1882), reused through one new selection from the
  pinned OCR (`cist-cumberland-ocr-v1`):
  - three Chapter XI passages: the Chattanooga shelling (OCR pp.178–179), and Negley and
    Bragg in McLemore's Cove (pp.180–181 and pp.185–186);
  - nine Chapter XII passages on the battle (pp.195–229).

  Cist is an interested Union staff history. Page 206's running head reads "20'j" in OCR,
  so its locator is marked inferred.
- **One Confederate report per battle**, each a new selection from newly pinned *Official
  Records* Series I, Volume XXX, Part 2, with catalog metadata:
  - **Hill's** undated report (opening passage, pp.136–137; p.137's running head reads
    "87"), for Chattanooga;
  - **Hindman's** October 22 transmittal and October 25 report on McLemore's Cove
    (pp.292–298), for Davis' Cross Roads;
  - **Bragg's** September 24, September 29 (with the September 27 field return) and
    October 9 reports, and three passages of his December 28 narrative (pp.23–37; p.37's
    running head reads "87"), for Chickamauga.

  Orders quoted inside a report belong to that report and do not count as separate
  families. Hindman wrote after Bragg had suspended him, to defend his conduct.

No Union reports, maps, returns, Hindman's exhibits or print pages were inspected. Stop
after this batch.

Twelve new source records bring the registry to **504 entries / 488 raw paths**,
preserving the earlier **492/476**. They are:

- three NPS HTML/text pairs;
- OR XXX Part 2 catalog metadata and full OCR;
- the Hill, Hindman and Bragg selections;
- a Cist selection.

## Decisions and limits

- **Scope.**
  - The frozen Chattanooga record is August 21 only. NPS says the shelling continued
    periodically for two weeks; that later shelling and Bragg's September evacuation are
    context, not part of the record.
  - Chickamauga's frozen interval ends on September 20. The withdrawal to Rossville and
    Chattanooga is outside it.
- **Opening strengths remain unknown.** All three records have blank frozen side bounds.
  - Chickamauga: Cist gives Rosecrans at most 55,000 effective men on the field (against a
    return of 67,548 present for duty equipped) and Bragg about 70,000. Bragg's
    December 28 narrative gives Rosecrans fully 70,000 effective infantry and artillery as of
    August 20, and himself a little over 35,000 exclusive of cavalry after the last of August,
    and his September 27 return shows 38,846 effective after the battle.
  - Davis' Cross Roads: Hindman's order estimate ("4,000 or 5,000"), Mackall's ("12,000 or 15,000")
    and Cist's 30,000 Confederates differ in scope.

  None is adopted.
- **Disputes preserved.**
  - The McLemore's Cove failure: Bragg suspended Hindman for not obeying orders; Hindman
    says his council was unanimous and the delays did not affect the result.
  - Chickamauga command: Bragg blames Polk's delay; Cist blames Wood's execution of the
    order to close up on Reynolds and argues Rosecrans should have gone to the front.
  - Chickamauga casualties: frozen and live 34,624 (US 16,170; CS 18,454) against Cist's
    16,336 and 20,950 and Bragg's "nearly if not quite 18,000". Bragg's prisoner claims
    are about 7,000 in September and over 8,000 in December.
- **Command roles and ranks.** Judgments are attributed to their authors. The live
  headings disagree with the frozen ranks and are not adopted:
  - Hill is given as "Colonel Daniel Hill";
  - Hindman as Brigadier General;
  - Bragg as Major General.

  Breckinridge is a frozen Davis' Cross Roads commander, but Cist places his division south
  of La Fayette. No listed commander receives automatic sole credit.
- **Tags.** Obstructed gaps, Union breastworks and Hill's river works were made within or
  around the operations, so none is tagged `inherited`. Terrain, logistics and command
  claims stay `unresolved`.

The three null unknowns are the opening strengths. No morale/readiness score,
probability, causal effect or new commander ranking is introduced. The cohort and both
admission proposals are unchanged, with **zero promoted rows**. The baseline still uses
**23/127 engagements in 13 eligible groups**, with strength Brier **0.276882** against
**0.250000** for equal odds.

## Review correction and validation

The reviewer found eight required corrections, all verified against the retained text
(each new quote occurs once) and applied:

- **CH-R1** corrects Hill's Clayton passage: Clayton sent an officer up the river.
- **CH-R2** scopes NPS's attention effect to two weeks of shelling beyond the one-day
  record.
- **CH-R3** replaces an unsupported "by both sides" for the gap obstructions.
- **CH-R4** records Hindman's post-suspension self-defense in two rationales, with
  citations.
- **CH-R5** cites two uncited value clauses.
- **CH-R6** dates Bragg's 70,000 to August 20.
- **CH-R7** restores Cist's "to this extent" qualifier on Wood.
- **CH-R8** scopes Bragg's prisoner counts beyond September 20.

Observations O1 (an undated withdrawal in the boundary note), O3 ("during the night" without
a date) and O4 (the sources' "or" wording above) are adopted. O2 (the inherited Cist
dependency count) is deferred, and O5 needs no change. Citations rise from 135 to 147;
claims and unknowns are unchanged, and no source record changes. The originals are
retained as `data/evidence/history/*.v1.json`, linked by `supersedes`. The
[primary assessment](../../artifacts/review-results/chickamauga-93a2694-opus-high-v1/primary-assessment.md) closes all eight findings; no second
reviewer pass is claimed.

Next by frozen campaign start is **East Tennessee Campaign [September-October 1863]**:
TN019 and TN020. Do not start that group within this batch.
