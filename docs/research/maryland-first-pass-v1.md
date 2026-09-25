# Maryland Campaign: bounded first pass

Prepared 2026-09-24. The three undrafted frozen records in **Maryland Campaign
[September 1862]** now have draft dossiers: **29 claims, 4 explicit null unknowns
and 86 citation occurrences** after review correction. MD003 Antietam keeps its
existing draft, unchanged, so all four members now have dossiers. All seven
dimensions are represented in each new record. Separate Claude Opus 5.5 `high`
[review](../../artifacts/review-results/maryland-3796300-opus-high-v1/review.md)
covered the three new dossiers; its four required corrections are fixed and verified
by the primary. All dossiers remain drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| WV010 — Harpers Ferry | 1862-09-12 to 09-15 | 10 | 1 | 24 | 2 |
| MD002 — South Mountain | 1862-09-14 | 10 | 1 | 38 | 2 |
| MD003 — Antietam | 1862-09-16 to 09-18 | existing draft, unchanged | | | |
| WV016 — Shepherdstown | 1862-09-19 to 09-20 | 9 | 2 | 24 | 2 |

Coverage is **54/127 draft dossiers**, **73 without**, and **11/36 complete source
campaigns by dossier presence**. All 51 earlier dossiers and seven historical
revisions are unchanged. Coverage does not establish historical completeness,
source independence, equal research depth or model eligibility.

## Inspection and stopping record

Read the three new records' frozen battle, force and commander row sets. Retrieved
three NPS battle-detail HTML pages and read each retained summary in full.
NPS/CWSAC and the Arnold tables are one family.

The single shared targeted follow-up is Francis Winthrop Palfrey, [*The Antietam
and Fredericksburg*](https://archive.org/details/antietamfrederic5950palf) (New
York: Scribner's, 1882; Campaigns of the Civil War, V). The pinned public catalog
record, full OCR and one selection derivative are retained. Inspected: catalog
title, creator, year, publisher and digitization provenance; the title page,
preface and contents; and these bounded passages with running headers and footnotes:

- The Harpers Ferry garrison, Lee's expectation and Halleck's telegram, OCR pp.18–20.
- The investment and surrender of Harpers Ferry, pp.23–26.
- South Mountain, from McClellan's letter to Franklin through the result, pp.27–41.
- Shepherdstown, September 19–20, pp.128–129.

Palfrey's title page describes him as formerly colonel of the 20th Massachusetts;
his service in this campaign is not shown in the inspected text. His preface says he
used his own recollection, memoranda and correspondence, many other volumes,
and advance sheets of the Official Records supplied by Col. Robert N. Scott. The
book is therefore not independent of the Official Records compilation; it is still
a different family from the NPS/CWSAC summaries. Quotations of McClellan, Halleck,
Lee and D. H. and A. P. Hill are part of Palfrey, not separately inspected originals.
Several running-header page numbers are misread or missing: p.24 prints "21" and
p.34 prints "31". Locators follow the corrected marker sequence. No Antietam chapter,
maps, rosters or print pages were inspected.

No third family was opened; MD003 was not revisited. Stop after this batch; do not
launch another source-recovery or reconciliation cycle because disputes remain.

Nine new source records bring the registry to **310 entries / 307 raw paths**,
preserving the earlier **301/298**: three NPS HTML/text pairs, the Palfrey catalog
metadata, full OCR and one selection derivative. The selection holds the
title/preface and four bounded passages; exact half-open Unicode ranges and
whitespace-only normalization reproduce them.

## Decisions and limits

- **All three opening strengths remain unknown.** Palfrey puts 9,000 men at
  Harpers Ferry under Miles plus 2,500 from Martinsburg, and says White surrendered
  11,000. NPS says Miles surrendered more than 12,000. At South Mountain, Palfrey
  quotes McClellan's 30,000 a side, caps the two engaged corps' present-for-duty
  aggregate at 35,155, and counts brigades at Turner's Gap. None is adopted.
- **South Mountain's live NPS result field reads "Indecisive"** against the frozen
  **Union victory**. Palfrey calls the actions tactical Confederate defeats but
  strategic Confederate victories. The frozen value is retained and the conflict is
  recorded as disputed.
- **Who surrendered Harpers Ferry is disputed**: Miles (NPS) or White after Miles's
  mortal wound (Palfrey). Halleck's order holding the garrison in place is tagged
  `inherited` for the field commanders.
- **Casualty disagreements remain** (frozen/live): Harpers Ferry **12,922 / 13,005**,
  South Mountain **4,500 / 4,625**, Shepherdstown **625 / 654**. Palfrey's South
  Mountain figures cover separate gaps and are not summed. At Shepherdstown the 118th
  Pennsylvania lost 269 (NPS) or 282 of 800 (Palfrey); A. P. Hill's reported claim
  of 3,000 killed and drowned is quoted and rejected by Palfrey, not adopted.
  Captured guns on September 19 are four (NPS) or five (Palfrey).
- **Command roles changed within intervals**: Cox commanded as senior until Reno
  came up, Reno and Garland were killed, and Franklin carried Crampton's Gap
  separately from Turner's Gap. Pendleton commanded the September 19 rearguard and
  A. P. Hill the September 20 counterattack. McClellan's decision not to march on
  the night of the 13th is tagged `commander_created`; Palfrey's claims that a night
  march would have let Franklin pass Crampton's substantially unopposed and given
  McClellan both passes early on the 14th are attributed counterfactuals.
- South Mountain's lost-order receipt time is not established; Palfrey reports that it
  has been said the hour does not appear and gives the 6.20 p.m. date of the letter to
  Franklin. The
  Harpers Ferry, South Mountain and Antietam intervals overlap in troops; no
  additive campaign credit is implied.

The four null unknowns are three opening strengths and Shepherdstown logistics.
Information and logistics claims elsewhere rest on retrospective summaries, not
inspected message chains or returns. No morale/readiness score, probability, causal
effect or new commander ranking is introduced. Cohort and both admission proposals
remain unchanged, with **zero promoted rows**. The baseline still uses **23/127
engagements in 13 eligible groups**, with strength Brier **0.276882** versus
**0.250000** for equal odds. Coverage has not improved predictive results.

## Review correction and validation

The reviewer found four required corrections. **R1**: the new-record count is 9,
not 12; the memo and `docs/sources.md` are corrected. **R2**: Palfrey attributes the
unknown lost-order hour to others ("It has been said") and gives the 6.20 p.m. letter
date; the MD002 claim, citations and memo now say so, with the McLaws clause cited
and the "seems" hedge on Stuart restored. **R3**: the no-night-march claim now keeps
Palfrey's "possible exception of Couch" and limits "substantially unopposed" to
Franklin's pass. **R4**: citations are added for the 2,500 from Martinsburg, Reno's
death "at about dark", Franklin gaining Crampton's crest, Cox's notification to
Pleasonton and the four volunteer regiments at Shepherdstown. The primary checked
every replacement quote against the selection (each occurs once) and applied them
exactly; citations rise from 79 to 86, with claims and unknowns unchanged.

Of three advisory notes, A3 is adopted in the dossiers' shared note and this memo:
the inspected text shows Palfrey was formerly colonel of the 20th Massachusetts, not
that he served in this campaign. The registered source record's dependency note is
unchanged and would need a versioned metadata revision. A1 and A2 are not applied.
The originals are retained as `data/evidence/history/WV010.v1.json`, `MD002.v1.json`
and `WV016.v1.json`, linked by `supersedes`. The
[primary assessment](../../artifacts/review-results/maryland-3796300-opus-high-v1/primary-assessment.md)
closes all four findings; no second reviewer pass is claimed.

Next by frozen campaign start is **Iuka and Corinth Operations [September-October
1862]**: MS001, MS002 and TN007. Do not start that group within this batch.
