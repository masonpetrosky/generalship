# Stones River Campaign: bounded first pass

Prepared 2026-09-24. Both **frozen records** in **Stones River Campaign [December
1862-January 1863]** now have draft dossiers: **20 claims, 2 explicit null unknowns
and 79 citation occurrences** after review correction. All seven dimensions are
represented in each record. Separate Claude Opus 5.5 `high`
[review](../../artifacts/review-results/stones-river-8005b6b-opus-high-v1/review.md)
covered both dossiers; its five required corrections and one advisory note are
applied and verified by the primary. All dossiers remain drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| TN008 — Hartsville | 1862-12-07 | 10 | 1 | 30 | 2 |
| TN010 — Stones River | 1862-12-31 to 1863-01-02 | 10 | 1 | 49 | 2 |

Coverage is **59/127 draft dossiers**, **68 without**, and **13/36 complete source
campaigns by dossier presence**. All 57 earlier dossiers and twelve historical
revisions are unchanged. Coverage does not establish historical completeness,
source independence, equal research depth or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets. Retrieved two NPS
battle-detail HTML pages and read each retained summary in full. NPS/CWSAC and the
Arnold tables are one family.

The targeted follow-up reuses the already pinned OCR of Henry M. Cist, *The Army
of the Cumberland* (1882), through one new selection derivative; the existing
catalog metadata and full OCR are unchanged. Inspected: title/preface and these
bounded passages with running headers, map-plate headers and signature marks:

- Hartsville and Morgan's commission, OCR pp.82–83.
- Stones River ground, dispositions and both armies' plans, pp.97–101.
- The opening of December 31 through Rosecrans's change of plan, pp.102–104.
- January 1–3, from the right's collapse through Bragg's retreat, pp.118–125.
- Results, strengths and losses, pp.127–128.

Cist is an interested retrospective history by a staff officer of Rosecrans, the
Union commander at Stones River. Quotations of Bragg, Breckinridge, Polk, Cleburne
and Withers are part of Cist, not separately inspected originals. A map-plate
header prints p.105 before p.104; the quotes on either side use explicit locators.
No maps, rosters or print pages were inspected.

No third family was opened. Stop after this batch; do not launch another
source-recovery or reconciliation cycle because disputes remain.

Five new source records bring the registry to **324 entries / 321 raw paths**,
preserving the earlier **319/316**: two NPS HTML/text pairs and one Cist selection
derivative whose parent is the existing `cist-cumberland-ocr-v1`.

## Decisions and limits

- **Both opening strengths remain unknown.** Hartsville's brigade was about two
  thousand effectives by Cist; no Confederate count is given. At Stones River, NPS
  gives about 44,000 when Rosecrans left Nashville on December 26 against more than 37,000 and the live field 45,000 Union; Cist
  gives Rosecrans 43,400 on the field and computes Bragg's effective force at 46,604
  from a December 10 return, calling Rosecrans's army slightly inferior. Which army
  was larger is disputed; no figure is adopted.
- **Hartsville's warning is disputed**: NPS says the pickets gave the alarm and held
  Morgan until the brigade formed; Cist says no warning was given. Morgan's frozen
  and live rank (Brigadier General) conflicts with Cist's statement that his
  commission was signed after Hartsville.
- **Casualty disagreements remain** (frozen/live): Hartsville **2,004 / 2,235**,
  Stones River **23,515 / 23,000**. Cist gives Morgan's loss as 125 killed and
  wounded and Moore's 150 plus the captured command; at Stones River, Bragg 10,125,
  and Rosecrans 1,553 killed, 7,245 wounded and about 2,800 captured.
- **Command roles**: Rosecrans abandoned his own attack and then chose to stay rather
  than fall back to Nashville (tagged `commander_created`; Cist is his staff
  historian). Bragg's January 2 order for Breckinridge's attack, his report calling it
  a failure, and the subordinates' notes urging retreat are attributed; Cist says Bragg
  decided at noon on January 3 "on consultation with his generals". Hartsville's
  regiment commanders' conduct is Cist's judgment. No listed commander receives
  automatic sole credit.
- Retreat timing differs: Cist has Bragg in retreat by 11 p.m. on January 3; NPS says
  he left on January 4–5. Both lie outside the frozen interval. Hartsville's guard
  mission is tagged `inherited`.

The two null unknowns are the opening strengths. Information and logistics claims
rest on retrospective summaries, not inspected message chains or returns. No
morale/readiness score, probability, causal effect or new commander ranking is
introduced. Cohort and both admission proposals remain unchanged, with **zero
promoted rows**. The baseline still uses **23/127 engagements in 13 eligible
groups**, with strength Brier **0.276882** versus **0.250000** for equal odds.

## Review correction and validation

The reviewer found five required corrections, all verified against the retained
text (each replacement quote occurs once) and applied exactly: **R1** quotes Cist's
"shortly after this engagement" for Morgan's commission; **R2** cites Bragg's order
and the subordinates' notes and attributes the retreat decision to Bragg's noon
consultation with his generals; **R3** scopes NPS's 44,000 to the December 26
departure and cites the December 10 return; **R4** removes an unsupported date for
sending for supplies and cites the 10,070 cavalry; **R5** adds eleven missing
citations. Advisory A1 is also adopted: Bragg's live heading rank (Major General)
conflicts with the frozen General and is recorded, not adopted. A2 (the copied Cist
dependency note) would need a versioned metadata revision and is not applied; A3–A5
need no change. Citations rise from 58 to 79 (77 from the required findings plus two
for A1); claims and unknowns are unchanged. The originals are retained as
`data/evidence/history/TN008.v1.json` and `TN010.v1.json`, linked by `supersedes`. The
[primary assessment](../../artifacts/review-results/stones-river-8005b6b-opus-high-v1/primary-assessment.md)
closes all five findings; no second reviewer pass is claimed.

Next by frozen campaign start is **Fredericksburg Campaign [November-December
1862]**: VA028. Do not start that group within this batch.
