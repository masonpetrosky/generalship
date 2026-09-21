# Jackson's Valley Campaign: bounded first pass

Prepared 2026-09-20. All **seven frozen records** in **Jackson's Valley Campaign
[March-June 1862]** now have draft dossiers: **68 claims, 17 explicit null unknowns
and 91 citation occurrences**. All seven dimensions are represented. Separate
campaign review is pending; no features are admitted.

| Record | Claims | Unknowns | Citations | Families |
| --- | ---: | ---: | ---: | ---: |
| VA101 — Kernstown, First | 10 | 2 | 15 | 2 |
| VA102 — McDowell | 9 | 2 | 14 | 2 |
| WV009 — Princeton Court House | 10 | 4 | 9 | 1 |
| VA103 — Front Royal | 10 | 2 | 12 | 2 |
| VA104 — Winchester, First | 9 | 2 | 14 | 2 |
| VA105 — Cross Keys | 10 | 3 | 14 | 2 |
| VA106 — Port Republic | 10 | 2 | 13 | 2 |

Coverage is **40/127 draft dossiers**, **87 without**, and **8/36 complete source
campaigns by dossier presence**. All 33 earlier dossiers and five historical
revisions are unchanged. Coverage does not establish historical completeness,
source independence, equal research depth or model eligibility.

## Inspection and stopping record

Read all seven frozen battle, force and commander row sets. Retrieved seven NPS
battle-detail HTML pages and read all six populated summaries; Princeton's response
is an empty template retained solely as a retrieval diagnostic. NPS/CWSAC and the
Arnold tables constitute one family, not independent confirmation. Campaign dates
in live page headings do not replace the frozen engagement intervals.

Reused the pinned 1880 [William Allan history](https://archive.org/details/historyofcampaig01alla)
as the single shared targeted follow-up for six battles. Inspected its retained
catalog title, creator, publisher and year, complete title/preface, and these
bounded passages with adjacent context and intervening footnotes:

- Kernstown information and field command, OCR pp.45–46.
- McDowell hill/access and senior command, pp.73–75.
- Front Royal bridge damage and pursuit, pp.95–96.
- Winchester reported information, pp.108–109.
- Cross Keys position, p.152.
- Port Republic crossing delay and sequential arrivals, p.158.

Allan identifies himself as a former Confederate staff officer. His preface praises
Jackson and says he used official reports, returns, biographies and diaries. His
account is interested retrospective history; embedded report quotations are not
separately inspected originals or extra source families. The May 1, 1880 preface
does not date each passage. Dependence between Allan and later NPS summaries is
unestablished. No maps, scans, manuscripts or whole-book inspection is claimed.

A Princeton keyword lookup in the shared OCR found no match; this is not proof
that the book contains no relevant account. No new source family was opened for
Princeton. The source-family and follow-up limits are ceilings, not quotas:
Princeton retains the frozen NPS/CWSAC account and explicit unknowns. Stop after
this batch; do not launch another source-recovery or reconciliation cycle simply
because those unknowns remain.

Fourteen new source records bring the registry to **273 entries / 270 raw paths**,
preserving the earlier **259/256**: six NPS HTML/text pairs, one empty HTML
snapshot, and one new Allan selection derivative. The existing Allan metadata,
full OCR and Hancock selections remain unchanged. The new selection contains the
title/preface and six battle sections; exact Unicode ranges and whitespace-only
normalization reproduce them. OCR errors, split words, headers and footnotes are
preserved. Source IDs, locators, parent hashes and SHA-256 hashes are in
[`data/sources.json`](../../data/sources.json). Dossiers are in
[`data/evidence`](../../data/evidence); packets are in
[`artifacts/research`](../../artifacts/research).

## Decisions and limits

- **All seven opening strengths remain unknown.** Existing numerical estimates
  remain in the frozen import without newly validating simultaneous populations.
  Kernstown's Confederate force field says **3,800**, its narrative **3,400**.
  Front Royal's live force field shows **zero**, versus frozen **4,063 total**;
  zero is not measured absence. Port Republic's crossing narrative describes
  sequential arrivals, not one unchanged army available at the initial attack.
- **Casualty disagreements remain:** McDowell's frozen **720** with parenthetical
  surgeon's **556**, versus live **756**; Cross Keys **951 / 972**; Port Republic
  **1,818 / 1,800** (frozen/live). No original return reconciliation is claimed.
  Front Royal's nearly 900 surrendered are not additional losses to add to the
  aggregate, nor an opening personnel estimate.
- **Princeton's 129 is incomplete**, with Wharton's losses unreported. The
  force-table zero missing/captured fields do not establish complete Confederate
  coverage. Its narrative also dates the later Winchester rout to **March 25**,
  whereas VA104's frozen battle date is **May 25**. Preserve the conflict and the
  May 15–17 Princeton interval; no raw correction or extra Princeton victory.
- Kernstown's reported estimate through Ashby and Banks's reported estimate at
  Winchester are attributed beliefs, not measured opposing strengths or verified
  message chains. Kimball's field role, Schenck's senior approval and Ewell/Trimble's
  separate roles do not imply equal or sole outcome credit. Live heading rank
  conflicts for Kimball and Ewell, and Frémont's garbled display name, are not adopted.
- **Cross Keys and Port Republic retain separate June 8 and June 9 intervals.**
  The same troops' movement between them does not create independent army
  observations or additive campaign credit. Princeton's later Lewisburg narrative
  likewise stays outside its own battle interval. The group label does not imply
  Jackson personally commanded all seven engagements.

The 17 null unknowns are seven opening strengths, five information states, four
logistics states and Princeton terrain. No morale/readiness score, probability,
causal effect or new commander ranking is introduced. Cohort and both admission
proposals remain unchanged, with **zero promoted rows**. The baseline still uses
**23/127 engagements in 13 eligible groups**, with strength Brier **0.276882**
versus **0.250000** for equal odds; coverage has not improved predictive results.

Next by frozen campaign start is **Confederate Heartland Offensive [June-October
1862]**: **TN005 Chattanooga, TN006 Murfreesboro, KY007 Richmond, KY008 Munfordville
and KY009 Perryville**. Do not start that group within this batch.
