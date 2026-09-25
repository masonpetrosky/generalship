# Expedition from Camp Douglas to Cache Valley, 1863: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
**frozen record** in **Expedition from Camp Douglas, Utah, to Cache Valley, Idaho [January 1863]**
now has a draft dossier: **9 claims, 1 explicit null unknown and 52 citation occurrences** (50
before the review correction below). All seven dimensions are represented. The dossier is a draft;
no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| ID001 — Bear River | 1863-01-29 | 9 | 1 | 52 | 3 |

It was drafted in a parallel worktree with eight other frontier and Texas-coast campaigns. Dossier
presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family.

- **Official Records, Series I, Volume L, Part 1** (1897; University of Illinois scan
  `warofrebellion501unit`, whose OCR title reads Series I Volume L, Part I): **Connor's** February 6,
  1863 report, with the February 20 transmittal by the department commander George Wright, which
  summarizes it and gives casualty figures from Connor's unprinted list (pp.184–187). Wright's
  transmittal depends on Connor's report and is not counted as a separate family.
- **Hubert Howe Bancroft, *History of Utah, 1540–1886*** (San Francisco: The History Company, 1889;
  Brigham Young University scan `historyofutah15401banc`): the title page and the passage on Indian
  outbreaks and the battle of Bear River with its footnotes (pp.630–632). Bancroft uses Connor's
  despatch as printed by Tullidge and summarizes two local accounts; it is not independent of Connor
  for the figures it takes from him.

Read, not selected: Halleck's and Stanton's indorsements and Halleck's March 29 telegram. Not
inspected: Connor's list of killed and wounded (not printed), any Shoshone account, Tullidge's
*History of Salt Lake City* and the local accounts Bancroft cites, and maps. No targeted follow-up was
used. Stop after this record.

This pass adds **8 source records**: one NPS HTML/text pair; OR L part 1 catalog metadata and full
OCR (`ia-or50-1-illinois-metadata-v1`, `or50-1-illinois-ocr-v1`); Bancroft catalog metadata and full
OCR (`ia-bancroft-utah-metadata-v1`, `bancroft-utah-ocr-v1`); and the selections
`or50-1-connor-bear-river-selections-v1` and `bancroft-utah-bear-river-selections-v1`. New author
groups: `connor-bear-river-report` and `bancroft-history-utah-1889`; the container is
`or-series-i-volume-l`.

## Decisions and limits

- **Scope.** The march from Camp Douglas from January 22 is context only.
- **Opening strength remains unknown.** The frozen force field names the District of Utah and the
  Shoshoni without figures, and the live field reads 0. Every figure is recorded and none adopted:
  220 cavalry leaving Camp Douglas on January 24 with an infantry company and two howitzers; no more
  than 200 engaged and about 300 warriors by Connor's estimate (Wright repeats 200; the frozen
  description gives about 300 warriors); Bancroft's some three hundred Shoshones and Bannacks and 300
  volunteers, of whom not more than two-thirds were engaged.
- **Disputes preserved** (2 claims marked `disputed`):
  - **Characterization.** The frozen result reads "Union victory (massacre)" and the frozen other
    name "Massacre at Boa Ogoi"; the live result reads Union Victory; Wright calls the victory
    complete; NPS says the troops killed most of the warriors and a number of women, children and old
    men; Bancroft says the band was almost annihilated and that, had the Indians done it, the deed
    would pass into history as a butchery or a massacre. The characterizations are the sources' own
    and none is adopted.
  - **Casualties.** Frozen 451 (US 67; I 384); live 315 (US 65; CS 250). Connor found 224 bodies and
    did not examine the field; Wright's 14 killed and 4 officers and 49 men wounded equal the frozen
    US 67; Bancroft summarizes local accounts of 200 killed and of 368 dead counted by an eyewitness
    from Franklin, about 90 of them women and children. The number of captive women and children
    Connor left on the field reads "ICO" in OCR and is not decoded.
- **No Shoshone account was inspected.** Connor's attributions of guilt for earlier killings are
  recorded as his statements, not findings. Bancroft dates the approach "the 28th", against Connor
  and the frozen January 29; not resolved.
- **Command roles.** The frozen commanders are Colonel Connor and Bear Hunter (no rank); the live
  page tags Bear Hunter [CS], not adopted. Connor says Major McGarry had engaged before he arrived;
  NPS says an early frontal attack was repulsed before Connor took over. No listed commander
  receives automatic sole credit.
- **Tags.** No claim is tagged `inherited`: the ravine was improved by its defenders with steps and
  willow covers. Outcomes are `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
commander ranking is introduced. No model input, frozen baseline or admission proposal is changed.

## Validation

`python3 -m generalship check` passes and `python3 -m unittest discover -s tests` passes (134 tests)
in the worktree. After the review correction, both pass again (134 tests) in the main repository,
and `gs.MISSES` is empty.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the nine frontier
and Texas-coast first passes together at prepared commit `d57de7e` as
`frontier-review-d57de7e-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": fifteen
required findings (FRC-01 to FRC-15) and fourteen advisories (FRA-01 to FRA-14) across the nine
passes. It is an AI review within its stated scope, not human historical adjudication, proof of
source independence or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the registry
record) before any change; every new quote occurs in its cited section, and the dossiers were
regenerated from the builder. Each changed dossier's reviewed version is archived byte-for-byte as
`data/evidence/history/<ID>.v1.json` and linked by `supersedes` under the revision
`cache-valley-1863-review-correction-2026-09-25`.

- **FRC-06 (accepted, applied).** (a) ID001 `casualty-records` now cites Bancroft's summary of the Logan
  branch record's 200 killed (p.632). (b) `stated-aims` no longer says the marshal held warrants: Connor
  says Chief Justice Kinney made a requisition for troops to arrest Bear Hunter, San Pitch and Sagwich,
  and that he told the marshal he did not intend to take any prisoners (p.187).
- **FRC-07 (accepted, applied).** The Bancroft records' edition said "First edition", which neither the
  retained catalog (no edition field; "Also published separately, 1890") nor the title page supports.
  `metadata_only` successors `ia-bancroft-utah-metadata-v2`, `bancroft-utah-ocr-v2` and
  `bancroft-utah-bear-river-selections-v2` (reparented to `bancroft-utah-ocr-v2`) read "Printed as Works
  vol. XXVI (1889); the catalog notes the work was 'Also published separately, 1890'; edition priority
  is not established", and ID001 cites the selection successor. Raw bytes and ranges are unchanged.

The Bear River characterizations are unchanged: the result stays `disputed`, with the frozen, NPS,
Wright and Bancroft wording quoted and none adopted. ID001 is revised
(`cache-valley-1863-review-correction-2026-09-25`). The correction adds three `metadata_only` source
records.
