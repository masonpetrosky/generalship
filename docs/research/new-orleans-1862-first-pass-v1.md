# Expedition to, and Capture of, New Orleans: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both **frozen
records** in **Expedition to, and Capture of, New Orleans [April-May 1862]** now have draft
dossiers: **18 claims, 2 explicit null unknowns and 106 citation occurrences**. All seven
dimensions are represented in each record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| LA001 — Forts Jackson and St. Philip | 1862-04-16 to 04-28 | 9 | 1 | 60 | 3 |
| LA002 — New Orleans | 1862-04-25 to 05-01 | 9 | 1 | 46 | 3 |

This pass was drafted alongside the other 1862-1863 Louisiana campaigns (Baton Rouge, La Fourche
1862, West Louisiana, Port Hudson and Taylor's 1863 operations). Existing dossiers, reviews and
historical revisions are unchanged. Dossier presence is not first-pass acceptance, separate review
or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and the two retained NPS pages in full.
NPS/CWSAC and the Arnold tables are one family. Both records use Mahan; each uses one report
family.

- **Mahan, *The Gulf and Inland Waters*** (Scribner's, copyright 1883; the Project Gutenberg
  text of the 1898 London issue), already registered for the Mississippi pass. A new selection
  (`mahan-new-orleans-selections-v1`) reuses the registered parent `mahan-gulf-inland-text-v1`.
  Mahan was a U.S. Navy officer and relies chiefly on the official reports, so this is an
  interested Union naval history and not independent of the Confederate reports. Selected
  (digital page markers):
  - the title page;
  - the mortar flotilla and its steamers (pp.53-56);
  - the forts, obstructions, bombardment and passage to the anchorage at quarantine (pp.57-85);
  - the ascent to New Orleans, the surrender of the city and the forts, and the garrison's loss
    (pp.85-89).
- **Duncan's** report of April 30, 1862 (*Official Records* Series I, Volume VI, No. 4,
  pp.521-534), for LA001. Volume VI is newly pinned from the University of Illinois scan
  `warofrebellion06unit` with catalog metadata and full OCR. Before use, the catalog volume
  ("v.6") and the OCR title ("SERIES I— VOLUME VI.", 1882 imprint) were checked.
- **Lovell's** reports of April 26 (pp.510-511) and May 22, 1862 (pp.512-518) (Volume VI, No. 3),
  for LA002.

The following were read but not selected:

- the opening of Chapter III of Mahan (pp.52-53), including the fleet's ammunition and coal
  shortage, and its footnotes;
- Lovell's May 27 transmittal and the opening of his June 18, 1863 correction letter;
- the opening of Duncan's May 13 addendum.

Farragut's and Porter's naval reports (Official Records of the Navies, Series I, Volume 18),
Butler's No. 1 (opening only seen) and Phelps's No. 2 reports, Higgins's and Squires's reports
(Nos. 5-6), M. L. Smith's report on the Chalmette lines (No. 7), Lovell's inclosures A-D, Duncan's
attached documents A-W, the Confederate Court of Inquiry (No. 8) and print pages were not
inspected. Irwin's *History of the Nineteenth Army Corps*, whose Chapter I covers New Orleans, was
not used, to keep within three families per record. No targeted follow-up was used. Stop after
this batch.

**Consequential gap.** No garrison return for the forts was inspected, and the frozen Confederate
casualty total (782) has no stated basis; Mahan's 14 killed and 39 wounded is the only garrison
loss figure found. The Union fleet's own casualty return was not inspected.

**New source records.** This pass adds **9 source records**:

- two NPS HTML/text pairs;
- the OR Volume VI catalog metadata and full OCR;
- the Duncan and Lovell selections;
- the Mahan New Orleans selection (reusing the registered parent).

## Decisions and limits

- **Scope.** The passage of the forts on April 24 lies inside LA001's frozen interval; the
  fleet's fight at the Chalmette and McGehee batteries on April 25 and the city's surrender belong
  to LA002. The forts' surrender on April 28 falls inside both intervals and is recorded in LA001
  only. The live date fields read April-May 1862 and do not replace the frozen dates.
- **Opening strengths remain unknown.** Every frozen bound is blank. Every figure is recorded
  with its date and scope, and none is adopted:
  - NPS: 24 vessels and 19 mortar schooners.
  - Mahan: seventeen vessels with 154 guns, twenty mortar-schooners and six gunboats; 109 guns in
    the two forts; four Confederate navy, two State and six River Defence vessels.
  - Duncan: thirteen of twenty-three vessels passed; twenty-one mortar schooners; about 125
    sharpshooters, about 500 in the Chalmette Regiment and 150 men lent to the Louisiana.
  - Lovell: about 3,000 ninety-day troops in the city, about 1,200 with muskets, against more than
    100 guns afloat; thirteen ships engaged the lower batteries.
  - Mahan: the Chalmette and McGehee batteries of five and nine guns; 250 marines landed on
    April 29.
- **Disputes preserved.**
  - The vessel and mortar-schooner counts (NPS, Mahan and Duncan differ).
  - Whether the passage was planned (Mahan's orders of April 23) or, as Duncan judged, improvised
    when the river was left dark.
  - LA001 losses: the frozen and live 1,011 (US 229; CS 782) against Mahan's garrison 14 killed
    and 39 wounded and his ship figures.
  - LA002: the food on hand (Mahan "a few days"; Lovell eighteen days); the city's surrender
    (NPS April 28; Mahan's account of the mayor's submission and the flag hauled down; Lovell's
    advice not to surrender).
- **Command roles and ranks.**
  - Duncan commanded the exterior works and Higgins the forts; everything afloat was put under
    Mitchell on April 22, and the River Defence Fleet refused his orders.
  - The live pages give Farragut as Admiral; the frozen rows give Flag Officer. Neither page lists
    Mitchell (LA001) or Butler (LA002).
  - No listed commander receives automatic sole credit, and live ranks are not adopted.
- **Tags.** The forts, the flood and the city's position predate the fighting, but the
  obstruction was placed and repaired by the defenders. All claims stay `unresolved` or
  `post_outcome`.
- **Families.** Mahan stays in `mahan-gulf-inland-waters`. Duncan is placed in
  `duncan-forts-1862-report` and Lovell in `lovell-new-orleans-1862-reports`; neither author had an
  earlier registry group. The OR parent is in `or-series-i-volume-vi`. The assignment noted that
  another pass may register Volume VI in parallel; the primary should deduplicate.

The two null unknowns are the two opening strengths. No morale/readiness score, probability,
causal effect or new commander ranking is introduced. The cohort, both admission proposals and the
baseline are unchanged, with **zero promoted rows**. `python3 -m generalship check` passes, the
unit tests pass, and the baseline still reports **23/127 eligible engagements in 13 groups**, with
strength Brier **0.276882** against **0.250000** for equal odds.

## Separate review pending

No separate review has been run for this campaign. A Claude Opus 5.5 `high` evidence-reviewer
assignment should be prepared by the primary after commit, bound to the exact commit, dossiers
and source hashes. Coverage, separate review and feature admission stay distinct.
