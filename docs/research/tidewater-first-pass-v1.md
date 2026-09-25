# Longstreet's Tidewater Operations: bounded first pass

Prepared 2026-09-25. All **four frozen records** in **Longstreet's Tidewater Operations
[March-April 1863]** now have draft dossiers: **39 claims, 4 explicit null unknowns
and 194 citation occurrences** after review correction. All seven dimensions are
represented in each record. Separate Claude Opus 5.5 `high` [review](../../artifacts/review-results/tidewater-885bd3f-opus-high-v1/review.md)
covered all four dossiers; its five required corrections are applied and verified by
the primary. All dossiers remain drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| NC010 — Fort Anderson | 1863-03-13 to 03-15 | 9 | 1 | 51 | 3 |
| NC011 — Washington | 1863-03-30 to 04-20 | 9 | 1 | 48 | 3 |
| VA031 — Suffolk (Fort Huger; Hill's Point) | 1863-04-11 to 05-04 | 12 | 1 | 62 | 3 |
| VA030 — Suffolk (Norfleet House Battery) | 1863-04-13 to 04-15 | 9 | 1 | 33 | 3 |

Coverage is **76/127 draft dossiers**, **51 without**, and **19/36 complete source
campaigns by dossier presence**. All 72 earlier dossiers and all historical revisions
are unchanged.

## Inspection and stopping record

Read all four frozen battle, force and commander row sets and the four retained NPS
summaries in full. NPS/CWSAC and the Arnold tables are one family.

The follow-up reuses the already pinned OCR of *Official Records*, Series I, Volume
XVIII (`or18-illinois-ocr-v1`, from the Goldsboro pass) through four new selections,
one per reporting commander. The volume is a shared container, not a witness:

- **Foster** (Union department commander): two New Berne reports of March 15 (OCR
  pp.183–184), the compiler's footnote on the 92nd New York's losses (p.184), and
  Washington reports of April 5, April 23 and April 30 (pp.211–216).
- **D. H. Hill** (Confederate expedition commander): his March 16 report to
  Longstreet, relaying Pettigrew (pp.188–189), and his April 20 letter to
  Beauregard (p.1007). No Hill report appears in the Washington report list.
- **Peck** (Union commander at Suffolk): his May 5 report (pp.274–280).
- **French** (Confederate Department of Southern Virginia): his April 22 report on
  the loss of Stribling's battery (pp.324–326), with Longstreet's April 25
  indorsement (pp.326–327), whose opening is garbled in OCR.

So each battle uses three families: NPS/CWSAC, one Union report and one Confederate
report. The compiler's footnote is counted with Foster's selection, and Longstreet's
indorsement with French's, for the effort ceiling; neither is treated as independent
corroboration. The OCR is heavily garbled in places (French's pp.324–326 especially);
quotes keep OCR spellings. Page locators use explicit marker maps. No maps, compiled
casualty returns, navy reports or print pages were inspected.

No further family was opened. Stop after this batch.

Twelve new source records bring the registry to **373 entries / 370 raw paths**,
preserving the earlier **361/358**: four NPS HTML/text pairs and four selections.

## Decisions and limits

- **VA030 lies inside VA031.** The frozen Norfleet House interval (April 13–15) is
  within the frozen Fort Huger interval (April 11–May 4), both carry the battle-level
  "Divisions (45,000 total)", and both casualty texts point to one 1,160 siege total.
  Their quantities must not be added; VA030 has no engagement-specific casualty count
  in any inspected source.
- **Opening strengths remain unknown.** All frozen side-specific bounds are blank.
  NPS gives Hill about 12,000 for New Berne and Suffolk 25,000 Union against
  Longstreet's 20,000. Foster puts the New Berne attackers at 13,000–14,000 from
  deserters and Pettigrew's column at 7,000, and the Washington garrison at 1,200 on his
  arrival. Peck reports a captured mail's 40,000–60,000 and says the Union works were
  defended by one-half Longstreet's own force. None is adopted.
- **Disputes preserved**: Corcoran's April 24 reconnaissance was "easily repulsed"
  (NPS) or drove the enemy "in confusion" to his main line (Peck). NPS (VA030) says a
  battery was constructed on Hill's Point on April 13, while French's sequence places
  Stribling's guns in a river work built when the Confederates held Suffolk; these may
  conflict, but whether they describe the same work is not established. The Peck paragraph on the Battery Huger capture
  has the OCR date "10th" between entries for the 18th and 20th; NPS dates it April 19.
- **Casualties** (frozen/live): Fort Anderson **7 / 0**, Washington **100 / 0**, Suffolk
  VA031 **152 (1,160 siege) / 0** and VA030 **(1,160 siege) / 0**. Live zeros are not
  measured absence. Foster reports 2 killed and 4 wounded (OCR 'I 4') at New Berne; Peck gives 260
  Union siege losses (footnoted to a revised statement) and estimates at least 1,500
  Confederate.
- **Command roles**: Hill blames Whiting's refusal, Robertson and Garnett; Foster
  attributes Hill's retreat "in all probability" to the Kinston and Swift Creek movements
  together with Hill's information of Heckman's reinforcement and his failure to gain an
  advantage; French judges the Hill's Point garrison negligent if surprised and
  insufficiently resistant if not; Longstreet's indorsement judges it completely
  surprised, while Longstreet
  says no officer deserves particular censure and that the work could have been retaken
  for 75 men (a counterfactual, not adopted). Frozen and live ranks give Foster and Peck
  Brigadier General against the Major-General signatures of their reports; live
  headings rank Hill Colonel and Longstreet Major General. None is adopted, and no
  listed commander receives automatic sole credit.
- Peck's Union works existing before April 11 are tagged `inherited` (they may be
  commander-created under a campaign boundary); the Confederate siege works he
  describes are a separate `unresolved` claim. Other terrain, logistics and
  command claims stay `unresolved`.

The four null unknowns are the opening strengths. No morale/readiness score,
probability, causal effect or new commander ranking is introduced. Cohort and both
admission proposals remain unchanged, with **zero promoted rows**. The baseline still
uses **23/127 engagements in 13 eligible groups**, with strength Brier **0.276882**
versus **0.250000** for equal odds.

## Review correction and validation

The reviewer found five required corrections, all verified against the retained text
(each new quote occurs once) and applied: **TW-R1** restores all three grounds of Foster's
"in all probability" judgment; **TW-R2** records French's surprise judgment as
conditional and only Longstreet's as a finding; **TW-R3** splits VA031's works claim so
that only pre-April 11 Union works carry `inherited`, adding `confederate-siege-works`
(`unresolved`); **TW-R4** cites the sequence linking French's old river work to Hill's
Point and states the NPS difference as unestablished; **TW-R5** reports Foster's OCR
"I 4" and the scope of his and the compiler's loss figures. Optional notes TW-N1 (the
"0 officers" OCR reading) and TW-N4 (the ambiguous "under French") are adopted as
wording; TW-N2 and TW-N3 are deferred. Claims rise from 38 to 39 and citations from
187 to 194; unknowns are unchanged. The originals are retained as
`data/evidence/history/NC010.v1.json`, `NC011.v1.json`, `VA030.v1.json` and
`VA031.v1.json`, linked by `supersedes`. The [primary assessment](../../artifacts/review-results/tidewater-885bd3f-opus-high-v1/primary-assessment.md)
closes all five findings; no second reviewer pass is claimed.

Next by frozen campaign start is **Cavalry Operations along the Rappahannock [March
1863]**: VA029. Do not start that group within this batch.
