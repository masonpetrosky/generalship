# Confederate Heartland Offensive: bounded first pass

Prepared 2026-09-24. All **five frozen records** in **Confederate Heartland Offensive
[June-October 1862]** now have draft dossiers: **54 claims, 6 explicit null unknowns
and 157 citation occurrences**. All seven dimensions are represented in each record.
Separate Claude Opus 5.5 `high` [review](../../artifacts/review-results/heartland-fc79026-opus-high-v1/review.md)
covered the complete batch. Its one population-scope correction in Perryville is
fixed and verified by the primary. All dossiers remain drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| TN005 — Chattanooga | 1862-06-07 to 06-08 | 10 | 1 | 26 | 2 |
| TN006 — Murfreesboro | 1862-07-13 | 12 | 1 | 30 | 2 |
| KY007 — Richmond | 1862-08-29 to 08-30 | 11 | 2 | 33 | 2 |
| KY008 — Munfordville | 1862-09-14 to 09-17 | 10 | 1 | 25 | 2 |
| KY009 — Perryville | 1862-10-08 | 11 | 1 | 43 | 2 |

Coverage is **45/127 draft dossiers**, **82 without**, and **9/36 complete source
campaigns by dossier presence**. All 40 earlier dossiers and six historical
revisions are unchanged. Coverage does not establish historical completeness,
source independence, equal research depth or model eligibility.

## Inspection and stopping record

Read all five frozen battle, force and commander row sets. Retrieved five NPS
battle-detail HTML pages and read each retained summary in full. NPS/CWSAC and the
Arnold tables are one family, not independent confirmation. The live pages' shared
campaign heading, "June-October 1862", does not replace the frozen engagement intervals.

The single shared targeted follow-up is Henry M. Cist, [*The Army of the
Cumberland*](https://archive.org/details/armyofcumber00cist) (New York: Scribner's,
1882; Campaigns of the Civil War, vol. VII per OCR signature marks, not the catalog). The pinned public catalog record,
full OCR and one selection derivative are retained. Inspected: catalog title,
creator, year, publisher and scan provenance; the title page, preface and contents;
and these bounded passages with intervening running headers:

- Negley's Chattanooga expedition and Kirby Smith's response, OCR pp.32–34.
- Forrest's Murfreesboro attack through the surrender and stores, pp.43–45.
- Nelson's arrival in Kentucky through Richmond losses, pp.53–54.
- Bragg's march to Munfordville through the surrender, pp.57–59.
- Perryville, from the start of Chapter VI to Bragg's arms quotation, pp.61–70
  (the chapter continues to p.86).

Cist's title page identifies him as a staff officer of Rosecrans and of a second
major-general whose name is garbled in the OCR (apparently Thomas). His
preface thanks Col. E. N. Scott for data furnished and credits the maps to Van
Horne's history. He is an interested retrospective Union historian, not an
inspected witness to these 1862 actions. Quotations of Duke, Bragg and Buell inside
Cist are not separately inspected originals or extra families. Dependence between
Cist and NPS summaries is unestablished. The Perryville map's OCR label text is
retained but not read as evidence. No maps, rosters, scans or whole-book
inspection is claimed.

The source-family and follow-up limits are ceilings, not quotas. No third family
was opened. The Chattanooga and Munfordville chronology questions and the
Murfreesboro result-field conflict below remain explicit. Stop after this batch;
do not launch another source-recovery or reconciliation cycle simply because
those disputes remain.

Thirteen new source records bring the registry to **286 entries / 283 raw paths**,
preserving the earlier **273/270**: five NPS HTML/text pairs, the Cist catalog
metadata, the full Cist OCR and one selection derivative. The selection contains
the title/preface and five battle sections; exact half-open Unicode ranges and
whitespace-only normalization reproduce them. OCR errors, split words, headers and
map-label text are preserved. Source IDs, locators, parent hashes and SHA-256 hashes
are in [`data/sources.json`](../../data/sources.json). Dossiers are in
[`data/evidence`](../../data/evidence); packets are in
[`artifacts/research`](../../artifacts/research).

## Decisions and limits

- **All five opening strengths remain unknown.** Only Murfreesboro has frozen
  numerical force fields: **approx. 1,400 CS / 900 US**. Cist gives about **2,000**
  Confederates and **1,700 surrendered** Union troops. Richmond's Cist estimates of
  some **7,000 / 12,000** cover whole commands, and NPS says troops joined both
  sides during the day. At Perryville, NPS gives nearly **55,000** on October 7.
  Cist reports Buell's pre-battle **58,000 effective**, less than half engaged, and
  Hardee's attacking divisions at some **16,000**. Live zeros at Chattanooga,
  Richmond and Munfordville are not measured absence.
- **Murfreesboro's live NPS result field reads "Union Victory"**, against the frozen
  **Confederate victory**. Its own narrative says all Union units surrendered to
  Forrest. The frozen value is retained and the conflict is recorded as disputed,
  not silently corrected.
- **Casualty disagreements remain** (frozen/live): Chattanooga **88 / 3**;
  Murfreesboro **1,040 / 1,350**; Richmond **5,650 / 6,223**; Munfordville
  **4,862 / 4,433**; Perryville **7,407 / 7,607**. At Perryville, Cist prints
  Buell's reported loss as **4,348**, but its OCR components sum to **4,048**. The
  printed page was not checked. Richmond's roughly **4,000** captured (NPS) versus
  **over 2,000** (Cist) is also retained. No original return reconciliation is claimed.
- **Command roles changed within intervals.** Kirby Smith arrived at Chattanooga on
  the 8th and Leadbetter commanded the place; Crittenden's command at Murfreesboro
  is disputed, arriving July 11 or 12. At Richmond, Manson and Cleburne led until
  Nelson and Smith arrived. Munfordville command passed from Wilder to Dunham and
  back to Wilder. At Perryville, Polk had immediate command, and Bragg's two
  reports as quoted by Cist conflict about his own role. No listed commander
  receives automatic sole credit, and no exact transfer clock is adopted.
- **Chronology and rank conflicts are preserved.** Cist dates Wilder's first
  surrender demand to the 13th, while NPS dates the refusal to the 14th.
  Murfreesboro's attack is timed 4:15–4:30 am (NPS) versus about 5:00 (Cist). Live
  headings rank Negley and Forrest as Major General, Kirby Smith as Lieutenant
  General and Bragg as Major General, against different frozen ranks. The headings
  are not adopted.
- Attributed judgments stay attributed. These include Duke's view that only the
  river prevented Chattanooga's capture, Cist's inference about Bragg's Louisville
  intent, and NPS's statement that Buell would have sent reserves. Wilder's
  reported count of 25,000 is also attributed. None is a causal estimate or a
  measured strength.
- Chattanooga's earlier Jasper action and Perryville's October 7 Peters Hill fight
  stay outside or at the edge of their frozen intervals and are not added. Buell's
  later pursuit is also excluded. Munfordville's delay benefit to Buell is campaign
  contribution, not a tactical result. The group label does not imply one commander
  directed all five engagements.

The six null unknowns are five opening strengths and Richmond logistics.
Information and logistics claims elsewhere rest on retrospective summaries, not
inspected message chains or returns. No morale/readiness score, probability, causal
effect or new commander ranking is introduced. Cohort and both admission proposals
remain unchanged, with **zero promoted rows**. The baseline still uses **23/127
engagements in 13 eligible groups**, with strength Brier **0.276882** versus
**0.250000** for equal odds. Coverage has not improved predictive results.

## Review correction and validation

The reviewer found **HO-R1**: Perryville's `union-unengaged-forces` rationale called
Crittenden's corps "the idle corps". The same Cist p.68 passage says Wagner's
brigade of Wood's division was engaged and only "the rest" of the corps was not.
The primary reread the passage and applied the exact proposed value, rationale and
two added citations. KY009 rises from 41 to 43 citations; claims, unknowns and every
other dossier are unchanged. The original dossier is retained as
`data/evidence/history/KY009.v1.json`, and the current draft records its hash in
`supersedes`. The original KY009 packet remains available at commit `fc79026`; the
current packet is regenerated.

Five nonblocking notes need no claim change. The memo now qualifies the garbled
second staff name (HO-N1), the source of the volume number (HO-N2) and the partial
Perryville chapter (HO-N3); the registered source records are unchanged. The KY008
quote-span note (HO-N4) and Cist's internal Munfordville day-count tension (HO-N5)
stay in the deferred chronology question. The
[primary assessment](../../artifacts/review-results/heartland-fc79026-opus-high-v1/primary-assessment.md)
closes R1 after direct verification; no second reviewer pass is claimed.

Next by frozen campaign start is **Northern Virginia Campaign [August 1862]**:
**VA022–VA027**, six records. Do not start that group within this batch.
