# Forrest's Expedition into West Tennessee: bounded first pass

Prepared 2026-09-24. Both **frozen records** in **Forrest's Expedition into West
Tennessee [December 1862-January 1863]** now have draft dossiers: **18 claims, 2
explicit null unknowns and 72 citation occurrences** after review correction. All
seven dimensions are represented in each record. Separate Claude Opus 5.5 `high`
[review](../../artifacts/review-results/forrest-west-tennessee-e67e54b-opus-high-v1/review.md)
covered both dossiers; its three required corrections are fixed and verified by the
primary. All dossiers remain drafts; no features are admitted.

| Record | Date (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| TN009 — Jackson | 1862-12-19 | 9 | 1 | 34 | 2 |
| TN011 — Parker's Cross Roads | 1862-12-31 | 9 | 1 | 38 | 2 |

Coverage is **65/127 draft dossiers**, **62 without**, and **16/36 complete source
campaigns by dossier presence**. All 63 earlier dossiers and all historical
revisions are unchanged.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and both retained NPS
summaries in full. NPS/CWSAC and the Arnold tables are one family.

The follow-up is Thomas Jordan and J. P. Pryor, [*The Campaigns of Lieut.-Gen. N. B.
Forrest*](https://archive.org/details/campaignslieutg00jordgoog) (1868), from a
Google-digitized Harvard copy (a University of Michigan scan returned server
errors). The pinned catalog record, full OCR and one selection are retained.
Inspected: title page, preface and Forrest's prefatory note, and three Chapter VII
passages: the expedition's outset (OCR pp.193–194), the operations around Jackson
(pp.196–200) and Parker's Cross Roads (pp.209–216).

The book is not independent of Forrest. The authors worked from his papers, records
and notes "taken down from his lips", and his prefatory note says "For the greater
part of the statements of the narrative I am responsible." It is an interested
Confederate history of the listed Confederate commander. Dunham's report, the
Rebellion Record and the Chicago Tribune appear only as cited inside it. The scan
crops some line starts; quotes preserve the OCR exactly and avoid cropped lines where
possible. Page locators use an explicit marker map, because footnote cross-references
("p. 209") would confuse pattern matching. No maps or print pages were inspected.

Seven new source records bring the registry to **344 entries / 341 raw paths**,
preserving the earlier **337/334**.

## Decisions and limits

- **Opening strengths remain unknown.** Jackson's frozen Confederate force is a
  detachment of approx. 400 (structured 400/400); NPS gives Forrest's whole brigade as
  2,100 and Jordan and Pryor about 1,800 at the outset. At Parker's Cross Roads the
  frozen text gives two Union brigades of approx. 3,000 (structured 3,000/3,000);
  Jordan and Pryor say the Confederates never exceeded 1,200 against at least 1,800
  Federals; they total figures attributed to Dunham's report as 1,554 and use a
  newspaper's two regimental figures to reach a printed 1,824, which the OCR
  components do not reproduce (1,704). None is adopted.
- **Both results are contested in the sources.** At Jackson, NPS says Englemann's
  regiments repulsed a mounted attack; Jordan and Pryor say the Federals were driven
  to their entrenchments. At Parker's Cross Roads both sides claimed victory. The
  frozen Confederate victories are retained and the result claims are disputed.
- **Casualties**: Jackson's frozen "Total unknown (US 6; CS unknown)" becomes a live
  CS zero, which is not measured absence; Jordan and Pryor's thirty Federal casualties
  and five hundred prisoners span several actions. Parker's Cross Roads frozen and live
  agree at 737 (US 237; CS 500); the history's own figures differ and are not adopted.
- **Command and information**: Forrest's deception of numbers at Jackson is tagged
  `commander_created`, from a history he endorsed. At Parker's Cross Roads, Napier's
  charge without orders, Forrest's surrender-demand ruse, the unwarned arrival of
  Fuller's brigade and Dunham's reported pre-battle information at Clarksburg of 8,000 Confederates are attributed.
  The live headings rank Forrest Major General against the frozen Brigadier General.
- Jackson's works are tagged `inherited`; the armament claim combines the outset
  shortfall with arms captured by Forrest-ordered night raids and stays `unresolved`
  while boundaries are unset.

The two null unknowns are the opening strengths. No morale/readiness score,
probability, causal effect or new commander ranking is introduced. Cohort and both
admission proposals remain unchanged, with **zero promoted rows**. The baseline still
uses **23/127 engagements in 13 eligible groups**, with strength Brier **0.276882**
versus **0.250000** for equal odds.

## Review correction and validation

The reviewer found three required corrections, all verified against the retained OCR
and NPS text and applied: **FWT-R1** restates Parker's Cross Roads force figures as the
book's own arithmetic (1,554; a printed 1,824 that the components do not reproduce),
records Dunham's 8,000 as pre-battle information, notes the book's two arriving
brigades against NPS's Fuller brigade, and cites Carroll's warning; **FWT-R2** records
that NPS makes the rail raids concurrent with the Jackson fight while Jordan and Pryor
place them the night before; **FWT-R3** changes the armament claim from `inherited` to
`unresolved`. Citations rise from 61 to 72 (the review counted 71; its R2 instruction
to replace and also keep the "two mounted columns" quote was applied by keeping it
beside the new one). Claims and unknowns are unchanged. The originals are retained as
`data/evidence/history/TN009.v1.json` and `TN011.v1.json`, linked by `supersedes`. The
[primary assessment](../../artifacts/review-results/forrest-west-tennessee-e67e54b-opus-high-v1/primary-assessment.md)
closes all three findings; no second reviewer pass is claimed.

Next by frozen campaign start is **Operations Against Vicksburg [December
1862-January 1863]**: MS003 and AR006. Do not start that group within this batch.
