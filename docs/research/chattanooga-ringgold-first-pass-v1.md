# Chattanooga-Ringgold Campaign: bounded first pass

Prepared 2026-09-25. Both **frozen records** in **Chattanooga-Ringgold Campaign
[November 1863]** now have draft dossiers: **18 claims, 2 explicit null unknowns and 84
citation occurrences** after review correction. All seven dimensions are represented in
each record. Separate Claude Opus 5.5 `high` [review](../../artifacts/review-results/chattanooga-ringgold-450a5ba-opus-high-v1/review.md) found five required
corrections, all applied and verified by the primary. All dossiers remain drafts; no
features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| TN024 — Chattanooga | 1863-11-23 to 11-25 | 9 | 1 | 50 | 3 |
| GA005 — Ringgold Gap | 1863-11-27 | 9 | 1 | 34 | 3 |

Coverage is **123/127 draft dossiers**, **4 without**, and **34/36 complete source
campaigns by dossier presence**. All 121 earlier dossiers and all historical revisions
are unchanged.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and the two retained NPS summaries
in full. NPS/CWSAC and the Arnold tables are one family. Each battle uses two further
families.

**Cist**, *The Army of the Cumberland* (1882), Chapter XIV, is reused through a new
selection from the pinned OCR. Five passages are used:

- the plan and Orchard Knob (OCR pp.243–248);
- Missionary Ridge (pp.253–256);
- the pursuit and Ringgold (pp.256–257);
- losses and captures (p.258);
- Cist's critique of Grant's plan (pp.259–262; p.261's running head reads "201").

The Lookout Mountain narrative (pp.248–253) was not inspected. Cist is an interested Union
staff history.

**One Confederate report per battle** comes from newly pinned *Official Records* Series I,
Volume XXXI, Part 2, with catalog metadata:

- **Bragg's** November 30 report and November 20 dispatch to Davis (pp.664–667), for
  Chattanooga.
- **Cleburne's** December 9 Ringgold Gap report (pp.753–758; heads for p.757 and p.758
  read "1T&7" and "15 8"), for Ringgold Gap.

This OCR's title page has no imprint line, so no publication year is recorded. No Union
reports, maps, returns or print pages were inspected. Stop after this batch.

Nine new source records bring the registry to **564 entries / 544 raw paths**, preserving
the earlier **555/535**. They are:

- two NPS HTML/text pairs;
- OR XXXI Part 2 catalog metadata and full OCR;
- the Bragg and Cleburne selections;
- a Cist selection.

## Decisions and limits

- **Scope.** Chattanooga covers Orchard Knob, Lookout Mountain and Missionary Ridge. The
  frozen and live descriptions place the first two on November 23–24 and the ridge assault
  on the 25th, within the frozen interval; the live other names list only Missionary Ridge
  and Lookout Mountain, and the frozen other-names cell is blank. The November 26 pursuit and Ringgold Gap are kept
  separate.
- **Opening strengths remain unknown.** Bragg says the enemy was at least double his
  strength. Cist gives only part-force figures: Sherman's 8,000 and Hooker's fewer than
  10,000. Cleburne's 4,157 bayonets are his own engaged infantry. None is adopted.
- **Disputes preserved.**
  - Chattanooga responsibility: Bragg blames Stevenson and "shameful" troops; Cist says
    the soldiers charged without orders and argues Grant's plan favored Sherman.
  - Cist's aggregate of 3,951 as read in the unverified OCR for Thomas's losses against components that sum to
    2,951 (a computation here).
  - Ringgold Gap: NPS says the Federals failed after five hours; Cist says the Confederates
    were driven from the pass after over an hour.
  - Casualties in both records. Cleburne's 221 equals the live Confederate figure.
- **Command roles and ranks.** Judgments are attributed to their authors. Live headings
  rank Grant Lieutenant General and Bragg Major General; the live ranks are not adopted,
  and no listed commander receives automatic sole credit.
- **Tags.** The Missionary Ridge works and slope, which Cist says were originally in place
  before the first line fell on November 23, are tagged `inherited`. Other terrain, logistics and command claims stay
  `unresolved`.

The two null unknowns are the opening strengths. No morale/readiness score, probability,
causal effect or new commander ranking is introduced. The cohort and both admission
proposals are unchanged, with **zero promoted rows**. The baseline still uses **23/127
engagements in 13 eligible groups**, with strength Brier **0.276882** against
**0.250000** for equal odds.

## Review correction and validation

The reviewer found five required corrections. Each was verified against the retained
text (every new quote occurs once) and applied:

- **R1** reads Cist's 3,951 as an OCR reading, not a verified print figure. In the same
  paragraph Sheridan's 1,256 sits against components summing to 1,286 (a computation).
- **R2** gives TN024's scope basis: the frozen interval and descriptions. The frozen
  other-names cell is blank.
- **R3** cites Bragg's Stevenson and Cleburne passages.
- **R4** bounds the `inherited` ridge-works tag at the record's November 23 opening and
  treats Bragg's statements as post-assault judgments.
- **R5** labels the p.243 locator as inferred, since the chapter's opening page has no
  running head.

Advisories A1 (Brent signs the order; the GA005 rationales say so), A2 (Bragg's Cleburne
and Gist passage, added to GA005's open questions with the OCR reading "Binggold") and A3
(Howard's command in both Cist figures) are adopted. A4 (the stale Cist dependency note)
and A5 (the live title and date) need no change in this batch.

Citations rise from 82 to 84 (TN024 50, GA005 34); claims and unknowns are unchanged,
and no source record changes. The originals are retained as
`data/evidence/history/TN024.v1.json` and `GA005.v1.json`, linked by `supersedes`. The
[primary assessment](../../artifacts/review-results/chattanooga-ringgold-450a5ba-opus-high-v1/primary-assessment.md) closes all five findings; no second
reviewer pass is claimed.

Next by frozen campaign start is **Mine Run Campaign [November-December 1863]**: VA044.
Do not start that group within this batch.
