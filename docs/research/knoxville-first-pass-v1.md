# Longstreet's Knoxville Campaign: bounded first pass

Prepared 2026-09-25. All **three frozen records** in **Longstreet's Knoxville Campaign
[November-December 1863]** now have draft dossiers: **27 claims, 3 explicit null unknowns
and 130 citation occurrences** after review correction. All seven dimensions are
represented in each record. Separate Claude Opus 5.5 `high` [review](../../artifacts/review-results/knoxville-5acbded-opus-high-v1/review.md) found
eight required corrections, all applied and verified by the primary. All dossiers remain
drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| TN023 — Campbell's Station | 1863-11-16 | 9 | 1 | 43 | 3 |
| TN025 — Fort Sanders | 1863-11-29 | 9 | 1 | 49 | 3 |
| TN026 — Bean's Station | 1863-12-14 | 9 | 1 | 38 | 3 |

Coverage is **121/127 draft dossiers**, **6 without**, and **33/36 complete source
campaigns by dossier presence**. All 118 earlier dossiers and all historical revisions
are unchanged.

## Inspection and stopping record

Read all three frozen battle, force and commander row sets and the three retained NPS
pages in full. NPS/CWSAC and the Arnold tables are one family. Bean's Station's live page
has no description, so its frozen description is cited instead.

Each report family is a new selection from the already pinned *Official Records* Series I,
Volume XXXI, Part 1 (`or31-1-illinois-ocr-v1`), with its own author group:

- **Burnside's** November 17 and 30 dispatches, plus the Campbell's Station, siege and Fort
  Sanders passages of his November 1865 report (pp.268–278). Used for Campbell's Station
  and Fort Sanders.
- **Longstreet's** January 1864 report: plan, strength estimate, Campbell's Station, the
  approach to Knoxville, Fort Sanders and Bean's Station (cited passages pp.455–465; the
  No. 58 heading is on p.454). Used for all three. The p.456 head reads "45f)" in OCR.
- **Parke's** December 10 and 14 dispatches (pp.326–327). Used for Bean's Station.
  Shackelford's reports stop before the fight. Parke's heading is on p.325; the next two
  heads read "320" and "827" in OCR and are inferred as 326 and 327.

No maps, Poe's, Benjamin's, McLaws's, Jenkins's or Shackelford's selected reports,
returns, the McLaws court-martial or print pages were inspected. Stop after this batch.

Nine new source records bring the registry to **555 entries / 535 raw paths**, preserving
the earlier **546/526**: three NPS HTML/text pairs and three OR selections.

## Decisions and limits

- **Scope.** The Huff's Ferry and Lenoir's actions, the siege, the November 23–25
  actions, the December 15 fighting and the pursuit are outside the frozen records.
- **Opening strengths remain unknown.** Each commander assigns the larger number to the
  other side, and none of these figures is adopted:
  - Burnside: little over 5,000 against at least double at Campbell's Station; about
    12,000 against an estimated 20,000–23,000 at Knoxville.
  - Longstreet: a planned 20,000, and Stevenson's 23,000 for Burnside.
- **Disputes preserved.**
  - Campbell's Station: Longstreet's blame of Jenkins and Law, and his counterfactual.
  - Fort Sanders: Burnside's two sets of Confederate losses (about 500 killed and wounded
    plus about 300 prisoners in 1863; about 500 surrendered "in all" and over 1,000 lost
    in 1865) and his own losses (about 20; 13).
  - Bean's Station: the frozen description's 2 a.m. picket skirmishing and day-long
    battle against Parke's 2 p.m. attack (possibly different phases), Longstreet's surprise
    against the pickets' warning, and frozen 1,600 against live 337 casualties.
  - Longstreet's judgments on his subordinates, including the pursuit abandoned after
    the frozen date.
- **Command roles and ranks.** Live headings rank Longstreet Major General against the
  frozen Lieutenant General; the live rank is not adopted. No listed commander receives
  automatic sole credit.
- **Tags.** Fort Sanders' works, ditch and entanglements existed before the assault and
  are tagged `inherited` relative to the November 29 start; under a campaign boundary the
  siege-built works may be commander-created. Other terrain, logistics and command claims
  stay `unresolved`.

The three null unknowns are the opening strengths. No morale/readiness score,
probability, causal effect or new commander ranking is introduced. The cohort and both
admission proposals are unchanged, with **zero promoted rows**. The baseline still uses
**23/127 engagements in 13 eligible groups**, with strength Brier **0.276882** against
**0.250000** for equal odds.

## Review correction and validation

The reviewer found eight required corrections. Each was verified against the retained
text (every new quote occurs once) and applied:

- **KX-01** removes an unsupported date from the guides' failure and cites Longstreet's
  Lenoir's Station passage for the abandoned wagons.
- **KX-02** adds Burnside's 1865 "in all, about 500" and says Ruff was killed at the
  ditch while McElroy's and Thomas's bodies were found in it.
- **KX-03** keeps the qualifier on Burnside's 12,000: exclusive of new Tennessee
  recruits.
- **KX-04** drops the Chattanooga rumors, which lie outside the selected passage.
- **KX-05** says Jenkins was ordered to advance a brigade, with a citation.
- **KX-06** reports the OCR reading "Grade’s" instead of silently correcting it.
- **KX-07** gives Longstreet's actual reasons and timing for abandoning the pursuit,
  with three added citations on Law's march and the enemy's retreat.
- **KX-08** treats the 2 a.m. and 2 p.m. clocks as possibly different phases.

Notes N2 (the campaign-boundary tag caveat), N3 (Parke's full "unless further orders or
developments" wording), N4 (the p.454 heading) and N6 (the picket wording) are adopted.
N1 (Burnside's 11 against 12 o'clock), N5 (Shackelford's unselected December 14
dispatch) and N7 (Blain's Cross Roads against Longstreet's 3 miles below the station)
remain deferred leads.

Citations rise from 123 to 130: the reviewer's three additions (KX-01, KX-02, KX-05) plus
four by the primary, one for Ruff's death at the ditch and three for KX-07. Claims and unknowns are unchanged,
and no source record changes. The originals are retained as
`data/evidence/history/TN023.v1.json`, `TN025.v1.json` and `TN026.v1.json`, linked by
`supersedes`. The [primary assessment](../../artifacts/review-results/knoxville-5acbded-opus-high-v1/primary-assessment.md) closes all eight
findings; no second reviewer pass is claimed.

Next by frozen campaign start is **Chattanooga-Ringgold Campaign [November 1863]**:
TN024 and GA005. Do not start that group within this batch.
