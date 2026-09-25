# Goldsboro Expedition: bounded first pass

Prepared 2026-09-24. All **three frozen records** in **Goldsboro Expedition
[December 1862]** now have draft dossiers: **28 claims, 4 explicit null unknowns and
75 citation occurrences** after review correction. All seven dimensions are
represented in each record. Separate Claude Opus 5.5 `high`
[review](../../artifacts/review-results/goldsboro-9de5b1d-opus-high-v1/review.md)
covered the complete batch; its five required corrections are fixed and verified by
the primary. All dossiers remain drafts; no features are admitted.

| Record | Date (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| NC007 — Kinston | 1862-12-14 | 9 | 1 | 31 | 3 |
| NC008 — White Hall | 1862-12-16 | 9 | 2 | 19 | 3 |
| NC009 — Goldsborough Bridge | 1862-12-17 | 10 | 1 | 25 | 3 |

Coverage is **63/127 draft dossiers**, **64 without**, and **15/36 complete source
campaigns by dossier presence**. All 60 earlier dossiers and all historical
revisions are unchanged. Coverage does not establish historical completeness,
source independence, equal research depth or model eligibility.

## Inspection and stopping record

Read all three frozen battle, force and commander row sets and the three retained
NPS summaries in full. NPS/CWSAC and the Arnold tables are one family.

No retrospective history already pinned covers this expedition (Woodbury's Ninth
Corps history ends before it). The follow-up therefore uses *The War of the
Rebellion*, Series I, Volume XVIII (Washington, 1887), from a University of
Illinois scan: catalog metadata, full OCR and two selection derivatives, following
the Eastern Kentucky pattern of one container and one family per report author.

- **Foster**, Union expedition commander: reports of December 14 (Kinston), 20
  and 27, 1862, OCR pp.53–59.
- **G. W. Smith**, Confederate department commander: reports of December 15, 16
  (letter and telegram), 18 and 29, pp.107–110.

These are interested commanders' accounts dated after the events they describe.
Their dates are section-specific and are not event times or proof of contemporary
knowledge. The OCR is poor (for example "A" for "w", ")" for "p") and quotes preserve
it exactly. Locators follow OCR running-header markers, read as: Foster p.53
(compiler header before the selected range), 54, 55 (OCR "S5"), 56, 57 (misprinted
"61"), 58 (OCR "1)8"), 59; Smith p.107 (OCR "m", before the selected range), 108, 109,
110. Pages are not checked against print. The compiler's Union casualty return (No. 2) is garbled in the OCR
and was not used, and its revised statement (p.60) was not inspected. Evans's,
Robertson's, Clingman's and subordinate reports were not selected.

Three families per battle is the protocol's ceiling; no further source was opened.
Ten new source records bring the registry to **337 entries / 334 raw paths**,
preserving the earlier **327/324**.

## Decisions and limits

- **Opening strengths remain unknown.** Foster left New Berne with about 10,000
  infantry, 40 guns and 640 cavalry; he put Evans at about 6,000 with twenty guns.
  Smith gives Evans 2,000, relayed an estimate of 30,000 for Foster on December 15,
  and wrote on December 18 that Foster had "certainly over 15,000". Each commander's
  figure for the other differs sharply from the other's own; none is adopted.
- **White Hall is contested by both reports**: Foster says his batteries silenced
  the Confederate guns and he moved on after a feint; Smith says the Federals were
  driven back with very severe loss. The frozen Inconclusive (live Indecisive) is
  retained and the claim is disputed.
- **Goldsborough Bridge**: Foster reports the railroad bridge burned and a
  Confederate counterattack repulsed; Smith says his brigades drove the Federals back
  and saved the county bridge, and that the superstructure could be replaced at once;
  the claim is disputed. The frozen Union victory is retained.
- **Casualties**: Kinston frozen and live agree at 685; White Hall **150 / 0** and
  Goldsborough Bridge **220 / 0** (frozen/live) are disputed. Foster's expedition-wide
  90 killed, 478 wounded and 9 missing, and Smith's 71, 268 and about 400 missing, are
  recorded once in NC009 and not allocated or added across records.
- The frozen and live records rank Foster Brigadier General; his OR reports are
  headed Major General. The conflict is retained. Approach delays at Kinston are
  tagged `inherited`.

The four null unknowns are three opening strengths and White Hall logistics. No
morale/readiness score, probability, causal effect or new commander ranking is
introduced. Cohort and both admission proposals remain unchanged, with **zero
promoted rows**. The baseline still uses **23/127 engagements in 13 eligible
groups**, with strength Brier **0.276882** versus **0.250000** for equal odds.

## Review correction and validation

The reviewer found five required corrections, all verified against the retained OCR
(each quote occurs once) and applied exactly: **GB-01** cites Foster's own
"Major-General, Commanding Department" signature; **GB-02** cites the 40 guns and the
cavalry figure, which the OCR reads as "G40"; **GB-03** adds Smith's claim that his
brigades drove the Federals back and saved the county bridge, cites Foster's
"disastrous failure", and marks the Goldsborough result claim `disputed`; **GB-04**
removes a repeated, uncited expedition-wide figure from Kinston; **GB-05** records the
full page-marker reading in this memo. Citations rise from 70 to 75; claims and
unknowns are unchanged. The originals are retained as
`data/evidence/history/NC007.v1.json` and `NC009.v1.json`, linked by `supersedes`. The
reviewer disclosed calling the packet function in its own worktree, with
byte-identical results. The
[primary assessment](../../artifacts/review-results/goldsboro-9de5b1d-opus-high-v1/primary-assessment.md)
closes all five findings; no second reviewer pass is claimed.

Next by frozen campaign start is **Forrest's Expedition into West Tennessee
[December 1862-January 1863]**: TN009 and TN011. Do not start that group within
this batch.
