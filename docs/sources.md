# Sources and provenance

Inspected on 2026-09-20. The checked-in manifest is the authority for exact bytes.

## Pilot tables

Jeffrey B. Arnold's [American Civil War Battle Data](https://github.com/jrnold/acw_battle_data)
provides structured versions of the U.S. National Park Service's CWSAC summaries.
We pin commit `3a6020dbfcbcfc650a268b10a9f155588472432b` and retain four CSVs verbatim:

| Table | Grain | Rows | Role |
|---|---|---:|---|
| `cwsac_battles.csv` | Source battle ID | 384 | Sampling frame, dates, recorded outcomes, descriptions |
| `cwsac_forces.csv` | Battle × belligerent | 768 | Force bounds, missingness, population descriptions |
| `cwsac_commanders.csv` | Battle × belligerent × listed name | 891 | Candidate command identities; no credit allocation |
| `cwsac_campaigns.csv` | Campaign label | 119 | Source grouping and theater |

The [pinned package metadata](https://github.com/jrnold/acw_battle_data/blob/3a6020dbfcbcfc650a268b10a9f155588472432b/rawdata/metadata/datapackage.yaml)
identifies **version 11.0.0 and CC-BY-4.0**. The hosted Read the Docs site currently
shows older version 8.0.0 and ODC-BY. Use the pinned package's metadata for this
snapshot; do not silently mix the documentation's schema or license label into it.
For example, the current CSV has fewer force columns than the older published schema.

These are historical government summaries digitized by a third party, not original
wartime reports. Source row locators establish where a claim came from, not whether
the underlying account is correct. Original NPS URLs in the tables may have moved;
the pinned CSV remains inspectable even when an old URL fails.

## Live NPS evidence snapshots

Two [Shiloh](https://www.nps.gov/civilwar/search-battles-detail.htm?battleCode=tn003)
and [Antietam](https://www.nps.gov/civilwar/search-battles-detail.htm?battleCode=md003)
pages were retrieved directly and converted to normalized text. The manifest
records the transformation and hashes. Preserve them alongside the older records:
a later live page does not automatically supersede an archived estimate.

- Antietam's displayed force table contains zeros, while its narrative describes
  opposing armies and a numerical imbalance. The dossier flags this conflict;
  zeros are not used as measured force counts.
- Shiloh's narrative describes Buell's arrival and the Johnston-to-Beauregard
  transfer. Whole-battle force totals cannot simply become opening-state inputs.
- The current pages' date and commander-summary fields need independent scrutiny;
  narrative detail does not validate every structured field.

NPS text and the CWSAC-derived tables share an `independence_group`. Agreement
between them is not independent historical corroboration. The third dossier,
Champion Hill, uses exact cells in the archived CWSAC table and remains a draft.

## Audit of the original project

Reference: Ethan Arsht's [published notebook at commit d2d77e8](https://github.com/ethanarsht/military_rankings/blob/d2d77e89c054b2eae45320c0e5c69f0821f85ffa/battle_project.ipynb).
The notebook was inspected; its code and dataset are not vendored here.

The executed modeling path constructs normalized own-minus-opponent force
differences, fills missing feature entries with zero, and fits scikit-learn
`LogisticRegression` (zero-based cells 159–166). It drops artillery and removes
the final feature before fitting. Commander scoring (cell 196) uses complementary
win-probability residuals, special handling for unavailable strength, and 0.5
for some inconclusive outcomes. Cell 167 scores the fitted training data.

Thus “linear model” in a high-level description should not be read as ordinary
least squares: the implementation uses logistic regression. The inspected path
does not establish campaign-held-out evaluation. Version 0.1 here is an independently
implemented, reduced **original-style baseline**, not a reproduction of Arsht's
published rankings: different cohort, total personnel rather than force categories,
explicit missingness exclusions, fixed regularization, and held-out campaigns.
An exact numerical reproduction remains a separate milestone.

## Source additions

**Author groups across campaigns (cohort v2).** Full-war passes may register one author's reports
from different campaigns under separate independence groups (for example
`sheridan-overland-reports` and `sheridan-valley-1864-reports`). Groups by the same author are one
witness family: they never count as independent corroboration of each other, whatever their group
names.

### 1861 Eastern first passes (cohort v2), 2026-09-25

The first passes for six 1861 campaigns add **78 records**: Charleston Harbor, the Chesapeake,
Western Virginia, Manassas, the Carolina coast and McClellan's Northern Virginia operations (memos
`docs/research/{charleston,chesapeake,western-virginia,manassas,carolina-coast,northern-virginia}-1861-first-pass-v1.md`).
The records are:

- seventeen NPS HTML/text pairs;
- Nicolay, *The Outbreak of Rebellion* (1881): catalog metadata, full OCR and selections;
- Official Records Series I, Volumes I and II (University of California scans; the Illinois
  identifiers are Series II and III volumes) and Volume V: catalog metadata and full OCR;
- Official Records of the Navies, Series I, Volumes 4–6: catalog metadata and full OCR;
- thirty report selections.

No model inputs are changed.

### Plymouth and Fort Fisher first passes (cohort v2), 2026-09-25

The first passes for Plymouth (1864), the December 1864 Fort Fisher expedition and Fort Fisher and
Wilmington (1865) add **23 records**:

- five NPS HTML/text pairs;
- Official Records Series I, Volume XXXIII: catalog metadata and full OCR;
- Official Records of the Union and Confederate Navies, Series I, Volume 9: catalog metadata and
  full OCR;
- nine report selections, four of them from the registered Volumes XLII and XLVI Part 1.

Navies Volume 11 was found not to cover Plymouth; Volume 9 does. This pass's Volume XLVII Part 1
parent was deduplicated to the Carolinas registration, whose OCR is byte-identical. No model inputs
are changed.

### Appomattox and Waynesboro first passes (cohort v2), 2026-09-25

The first passes for the [Appomattox Campaign](research/appomattox-first-pass-v1.md) and
[Sheridan's Expedition to Petersburg](research/sheridan-petersburg-1865-first-pass-v1.md) add
**40 records**:

- fifteen NPS HTML/text pairs;
- new selections from the registered Humphreys and Pond OCR;
- eight report selections from the registered Volume XLVI Part 1 OCR.

No new volume or catalog record was registered, and no model inputs are changed.

### 1861 Western and Trans-Mississippi first passes (cohort v2), 2026-09-25

The first passes for six 1861 campaigns add **78 records**: Missouri, Eastern Kentucky, the Gulf
Blockading Squadron, Belmont, the Indian Territory and Northeast Missouri (memos
`docs/research/*-1861-first-pass-v1.md`). The records are:

- eighteen NPS HTML/text pairs and one empty template;
- Snead, *The Fight for Missouri* (1886), and Britton, *The Civil War on the Border*, volume I
  (1891 second edition): catalog metadata, full OCR and selections;
- Official Records Series I, Volumes III, IV, VI and VIII: catalog metadata and full OCR;
- twenty-five report selections, two of them from the registered Volume VII Cornell OCR.

The Illinois scans labelled Volumes III and IV are Series II and III volumes. The University of
California scans `warofrebellion03secrrich` and `warofrebellion04secrrich` were used instead,
confirmed from their title pages. No model inputs are changed.

### Carolinas Campaign first pass (cohort v2), 2026-09-25

The [first pass](research/carolinas-first-pass-v1.md) adds **23 records**:

- five NPS HTML/text pairs;
- Official Records Series I, Volume XLVII Part 1 (`warofrebellion471unit`): catalog metadata and
  full OCR; the imprint year is illegible in OCR and left null;
- ten report and return selections, including the compiled Union casualty return, used as the
  single targeted follow-up for three records;
- one new Cox selection, reusing the registered *March to the Sea* OCR.

No model inputs are changed.

### Price's Missouri Expedition, Mobile Bay, Mobile and Wilson's Raid first passes (cohort v2), 2026-09-25

The first passes for [Price's Missouri Expedition](research/price-missouri-first-pass-v1.md),
[Mobile Bay](research/mobile-bay-first-pass-v1.md), [Mobile](research/mobile-first-pass-v1.md) and
[Wilson's Raid](research/wilson-raid-first-pass-v1.md) add **44 records**:

- fifteen NPS records (Glasgow's page is an empty template);
- Andrews, *History of the Campaign of Mobile* (1867): catalog metadata, full OCR and one
  selection;
- new selections from the registered Britton volume II, Mahan and Jordan and Pryor texts;
- Official Records Series I, Volumes XLI Part 1 and XLIX Part 1: catalog metadata and full OCR;
- five report selections.

**Merge deduplication.** This pass was drafted in parallel with the Camden and Franklin-Nashville
passes. It had fetched its own copies of Britton volume II and OR XXXIX Part 1. The OCR files were
byte-identical to the registered parents (`britton-civil-war-border-2-ocr-v1`,
`or39-1-illinois-ocr-v1`), so they were not registered again. This pass's selections point to
those parents, and its duplicate catalog-metadata records were dropped. The memos still name the
IDs used during drafting. No model inputs are changed.

### Bermuda Hundred and Richmond-Petersburg first passes (cohort v2), 2026-09-25

The first passes for [Bermuda Hundred](research/bermuda-hundred-first-pass-v1.md) and
[Richmond-Petersburg](research/petersburg-first-pass-v1.md) add **70 records**:

- twenty-four NPS HTML/text pairs;
- two Humphreys selections, reusing the registered *Virginia Campaign* OCR;
- Official Records Series I, Volumes XL, XLII and XLVI, Part 1 of each: catalog metadata and full
  OCR;
- fourteen report selections from Volumes XXXVI (Part 2), XL, XLII and XLVI.

Meade's November 1, 1864 report stays in its Overland group. Lee's dispatches across three
volumes share one group. No model inputs are changed.

### Red River and Camden first passes (cohort v2), 2026-09-25

The first passes for the [Red River Campaign](research/red-river-first-pass-v1.md) and the
[Camden Expedition](research/camden-first-pass-v1.md) add **34 records**:

- twelve NPS HTML/text pairs;
- Irwin, *History of the Nineteenth Army Corps* (1892), and Britton, *The Civil War on the Border*,
  volume II (1899): catalog metadata, full OCR and one selection each;
- Official Records Series I, Volume XXXIV Part 1: catalog metadata, full OCR, and Taylor's and
  Price's report selections.

No Scribner volume covers either campaign. No model inputs are changed.

### Franklin-Nashville and Savannah first passes (cohort v2), 2026-09-25

The first passes for [Franklin-Nashville](research/franklin-nashville-first-pass-v1.md) and
[Savannah](research/savannah-first-pass-v1.md) add **51 records**:

- thirteen NPS HTML/text pairs;
- Cox, *The March to the Sea; Franklin and Nashville* (1882): catalog metadata, full OCR and two
  selections;
- Official Records Series I, Volumes XXXIX Part 1, XLIV and XLV Part 1: catalog metadata and full
  OCR for each;
- fifteen report selections.

No model inputs are changed.

### Atlanta Campaign first pass (cohort v2), 2026-09-25

The [first pass](research/atlanta-first-pass-v1.md) adds **47 records**:

- sixteen NPS HTML/text pairs;
- Cox, *Atlanta* (1882): catalog metadata, full OCR and one selection;
- Official Records Series I, Volume XXXVIII, Parts 2 and 3: catalog metadata and full OCR for
  each;
- eight report selections: Johnston, Hood, Cleburne, Logan, Hardee, Schofield, Steedman and
  Kilpatrick.

The registry is now **736 entries / 715 raw paths**, preserving the previous **689/668**. No model
inputs are changed.

### Early's Raid and Sheridan's Valley first passes (cohort v2), 2026-09-25

The first passes for [Early's Raid](research/early-raid-first-pass-v1.md) and
[Sheridan's Valley Campaign](research/sheridan-valley-first-pass-v1.md) add **46 records**:

- fifteen NPS HTML/text pairs;
- Pond, *The Shenandoah Valley in 1864* (1883): catalog metadata, full OCR and two selections;
- Official Records Series I, Volume XXXVII Part 1 and Volume XLIII Part 1: catalog metadata and
  full OCR for each;
- eight report selections.

The Volume XLIII scan used is `warofrebellion431unit_0`; the identifier without the suffix is
Volume XLVII Part 2. The registry is now **689 entries / 668 raw paths**, preserving the previous
**643/622**. No model inputs are changed.

### Overland Campaign first pass (cohort v2), 2026-09-25

The [first pass](research/overland-first-pass-v1.md) adds **34 records**:

- eleven NPS HTML/text pairs;
- Humphreys, *The Virginia Campaign of '64 and '65* (1883): catalog metadata, full OCR and one
  selection;
- Official Records Series I, Volume XXXVI, Parts 1 and 2: catalog metadata and full OCR for each;
- five report selections: Meade, Sheridan and Hampton from Part 1, and Butler and Wild from Part 2.

The registry is now **643 entries / 622 raw paths**, preserving the previous **609/588**. No model
inputs are changed.

### Best-estimate ledger, 2026-09-25

One record is added: `livermore-transcription-v1`, a manual transcription of the Livermore
entry lines and derivation notes, made from the 25 registered page images, one section per
printed page. It is the text cited for Livermore figures, because the OCR merges note markers
into numbers. The registry is now **609 entries / 588 raw paths**, preserving the previous
**608/587**. No model inputs are changed.

### Reported-strength scoping, 2026-09-25

The [scoping memo](research/reported-strength-scoping-v1.md) adds **27 records**: Livermore's
*Numbers and Losses* (1901) catalog metadata, full OCR and 25 downscaled page images of
printed pp.78–107 (Internet Archive `numberslosses00liverich`). Figures were read from the
images because the OCR merges note markers into numbers. The registry is now **608 entries /
587 raw paths**, preserving the previous **581/560**. No model inputs are changed.

### Operations about Dandridge review correction, 2026-09-25

One `metadata_only` revision (DAN-R4) supersedes `or32-1-longstreet-dandridge-selections-v1`
with `-v2`, removing Lawton's indorsement from its author and dependency note because the
selected range ends before it. Raw files, hashes and ranges are unchanged; the registry
is now **581 entries / 560 raw paths**.

### Operations about Dandridge first pass, 2026-09-25

The [three-record memo](research/dandridge-first-pass-v1.md) adds **12 records**, bringing
the registry to **580 entries / 560 raw paths**, preserving the previous **568/548**. Three
NPS battle HTML/text pairs remain in the NPS/CWSAC family. Official Records Series I
Volume XXXII Part 1 (Internet Archive `warofrebellion321unit`) is pinned with catalog
metadata, full OCR and Sturgis and Longstreet selections; new Sturgis and Martin
selections reuse `or31-1-illinois-ocr-v1`. Character ranges and whitespace-only
normalization reproduce all sections. No model inputs are changed.

### Mine Run Campaign first pass, 2026-09-25

The [one-record memo](research/mine-run-first-pass-v1.md) adds **4 records**, bringing the
registry to **568 entries / 548 raw paths**, preserving the previous **564/544**. One NPS
battle HTML/text pair remains in the NPS/CWSAC family. A new Humphreys Chapter III
selection reuses `humphreys-ocr-v2`, and a new Lee selection reuses
`or29-1-illinois-ocr-v1`. Character ranges and whitespace-only normalization reproduce
all sections. No model inputs are changed.

### Chattanooga-Ringgold Campaign first pass, 2026-09-25

The [two-record memo](research/chattanooga-ringgold-first-pass-v1.md) adds **9 records**,
bringing the registry to **564 entries / 544 raw paths**, preserving the previous
**555/535**. Two NPS battle HTML/text pairs remain in the NPS/CWSAC family. Official
Records Series I Volume XXXI Part 2 (Internet Archive `warofrebellion312unit`) is pinned
with catalog metadata, full OCR and Bragg and Cleburne selections; a new Cist selection
reuses `cist-cumberland-ocr-v1`. Character ranges and whitespace-only normalization
reproduce all sections. No model inputs are changed.

### Knoxville Campaign first pass, 2026-09-25

The [three-record memo](research/knoxville-first-pass-v1.md) adds **9 records**, bringing
the registry to **555 entries / 535 raw paths**, preserving the previous **546/526**. Three
NPS battle HTML/text pairs remain in the NPS/CWSAC family. Burnside, Longstreet and Parke
selections reuse `or31-1-illinois-ocr-v1`. Character ranges and whitespace-only
normalization reproduce all sections. No model inputs are changed.

### Memphis & Charleston Railroad review correction, 2026-09-25

One `metadata_only` revision (MC-04) supersedes `or31-1-chalmers-collierville-selections-v1`
with `-v2`, correcting its inspection note about McCulloch's and Slemons's reports. Raw
files, hashes and ranges are unchanged; the registry is now **546 entries / 526 raw
paths**.

### Averell's Raid first pass, 2026-09-25

The [one-record memo](research/averell-raid-first-pass-v1.md) adds **4 records**, bringing
the registry to **545 entries / 526 raw paths**, preserving the previous **541/522**. One
NPS battle HTML/text pair remains in the NPS/CWSAC family. Averell and Echols selections
reuse `or29-1-illinois-ocr-v1`. Character ranges and whitespace-only normalization
reproduce all sections. No model inputs are changed.

### Memphis & Charleston Railroad first pass, 2026-09-25

The [one-record memo](research/memphis-charleston-first-pass-v1.md) adds **4 records**,
bringing the registry to **541 entries / 522 raw paths**, preserving the previous
**537/518**. One NPS battle HTML/text pair remains in the NPS/CWSAC family. Hatch and
Chalmers selections reuse `or31-1-illinois-ocr-v1`. Character ranges and whitespace-only
normalization reproduce all sections. No model inputs are changed.

### Reopening the Tennessee River first pass, 2026-09-25

The [one-record memo](research/reopening-tennessee-first-pass-v1.md) adds **6 records**,
bringing the registry to **537 entries / 518 raw paths**, preserving the previous
**531/512**. One NPS battle HTML/text pair remains in the NPS/CWSAC family. Official
Records Series I Volume XXXI Part 1 (Internet Archive `warofrebellion311unit`) is pinned
with catalog metadata, full OCR and a Bratton selection; a new Cist selection reuses
`cist-cumberland-ocr-v1`. Character ranges and whitespace-only normalization reproduce
all sections. No model inputs are changed.

### Bristoe Campaign first pass, 2026-09-25

The [five-record memo](research/bristoe-first-pass-v1.md) adds **16 records**, bringing
the registry to **531 entries / 512 raw paths**, preserving the previous **515/496**. Five
NPS battle HTML/text pairs remain in the NPS/CWSAC family. Official Records Series I
Volume XXIX Part 1 (Internet Archive `warofrebellion291unit`) is pinned with catalog
metadata, full OCR and Stuart, Hill and Lee selections; a new Humphreys selection reuses
`humphreys-ocr-v2`. Character ranges and whitespace-only normalization reproduce all
sections. No model inputs are changed.

### Morgan's Raid review correction, 2026-09-25

Three `metadata_only` revisions supersede `or23-1-burnside-morgan-raid-selections-v1`,
`or23-1-hobson-morgan-raid-selections-v1` and `or23-1-shackelford-morgan-raid-selections-v1`
with `-v2`, carrying the TL-R7 imprint correction and reparenting them to
`or23-1-illinois-ocr-v2`. Raw files, hashes and ranges are unchanged; the registry is now
**515 entries / 496 raw paths**.

### East Tennessee Campaign first pass, 2026-09-25

The [two-record memo](research/east-tennessee-first-pass-v1.md) adds **8 records**, bringing
the registry to **512 entries / 496 raw paths**, preserving the previous **504/488**. Two
NPS battle HTML/text pairs remain in the NPS/CWSAC family. Foster, Samuel Jones, Burnside
and Williams selections reuse `or30-2-illinois-ocr-v1`. Character ranges and
whitespace-only normalization reproduce all sections. No model inputs are changed.

### Chickamauga Campaign first pass, 2026-09-25

The [three-record memo](research/chickamauga-first-pass-v1.md) adds **12 records**, bringing
the registry to **504 entries / 488 raw paths**, preserving the previous **492/476**. Three
NPS battle HTML/text pairs remain in the NPS/CWSAC family. Official Records Series I
Volume XXX Part 2 (Internet Archive `warofrebellion302unit`) is pinned with catalog
metadata, full OCR and Hill, Hindman and Bragg selections; a new Cist selection reuses
`cist-cumberland-ocr-v1`. Character ranges and whitespace-only normalization reproduce
all sections. No model inputs are changed.

### Gettysburg review correction, 2026-09-25

Three `metadata_only` revisions (GB-R11) supersede `ia-humphreys-metadata-v1`,
`humphreys-ocr-v1` and `humphreys-gettysburg-rapidan-selections-v1` with `-v2`,
replacing an unsupported chief-of-staff start date and an anachronistic dependence on the
printed Official Records. Raw files, hashes and ranges are unchanged; the registry is now
**492 entries / 476 raw paths**.

### Tullahoma review correction, 2026-09-25

Three `metadata_only` revisions (TL-R7) supersede `ia-or23-1-illinois-metadata-v1`,
`or23-1-illinois-ocr-v1` and `or23-1-bate-hoovers-gap-selections-v1` with `-v2`,
recording the OCR imprint year 1889. Raw files, hashes and ranges are unchanged; the
registry is now **489 entries / 476 raw paths**. The three Morgan's Raid OR selections
still carry the v1 edition text pending that campaign's review.

### Morgan's Raid first pass, 2026-09-25

The [three-record memo](research/morgans-raid-first-pass-v1.md) adds **12 records**, bringing
the registry to **486 entries / 476 raw paths**, preserving the previous **474/464**. Three
NPS battle HTML/text pairs remain in the NPS/CWSAC family. Duke's *History of Morgan's
Cavalry* (Internet Archive `historyofmorgans00duke`) is pinned with catalog metadata, full
OCR and a selection; Burnside, Hobson and Shackelford selections reuse
`or23-1-illinois-ocr-v1`. Character ranges and whitespace-only normalization reproduce
all sections. No model inputs are changed.

### Tullahoma Campaign first pass, 2026-09-25

The [one-record memo](research/tullahoma-first-pass-v1.md) adds **6 records**, bringing
the registry to **474 entries / 464 raw paths**, preserving the previous **468/458**. One
NPS battle HTML/text pair remains in the NPS/CWSAC family. Official Records Series I
Volume XXIII Part 1 (Internet Archive `warofrebellion231unit`) is pinned with catalog
metadata, full OCR and a Bate selection; a new Cist selection reuses
`cist-cumberland-ocr-v1`. Character ranges and whitespace-only normalization reproduce
all sections. No model inputs are changed.

### Gettysburg Campaign first pass, 2026-09-25

The [ten-record memo](research/gettysburg-first-pass-v1.md) adds **28 records**,
bringing the registry to **468 entries / 458 raw paths**, preserving the previous
**440/430**. Ten NPS battle HTML/text pairs remain in the NPS/CWSAC family. Official
Records Series I Volume XXVII Part 2 (Internet Archive `warofrebellion272unit`) is pinned
with catalog metadata, full OCR, and Lee and Stuart selections, each its own independence
group. Humphreys' *From Gettysburg to the Rapidan* (`cu31924030917177`) is pinned with
metadata, OCR and one selection, and a new Doubleday selection reuses `doubleday-ocr-v1`.
Character ranges and whitespace-only normalization reproduce all sections. No model
inputs are changed.

### Chancellorsville review correction, 2026-09-25

One `metadata_only` revision (CV-R1/R2) supersedes `doubleday-chancellorsville-selections-v1`
with `-v2`, correcting its inspection note's page statements. Raw files, hashes and
ranges are unchanged; the registry is now **440 entries / 430 raw paths**.

### Grant's Operations Against Vicksburg review correction, 2026-09-25

Six `metadata_only` revisions (VB63-R9) supersede `ia-or24-2-illinois-metadata-v1`,
`or24-2-illinois-ocr-v1` and the Dennis, McCulloch, Reid and Walker selections with
`-v2` records whose edition quotes the garbled imprint in full ("1 SS  9.", outside
the selected title ranges). Raw files, hashes and ranges are unchanged; the registry
is now **439 entries / 430 raw paths**.

### Streight's Raid first pass, 2026-09-25

The [one-record memo](research/streights-raid-first-pass-v1.md) adds **4 records**,
bringing the registry to **433 entries / 430 raw paths**, preserving the previous
**429/426**. One NPS battle HTML/text pair remains in the NPS/CWSAC family. Two new
selections reuse pinned parents: Cist (`cist-cumberland-ocr-v1`) and Jordan and Pryor
Chapter IX (`jordan-pryor-forrest-ocr-v1`). Character ranges and whitespace-only
normalization reproduce all sections. No model inputs are changed.

### Chancellorsville Campaign first pass, 2026-09-25

The [three-record memo](research/chancellorsville-first-pass-v1.md) adds **12 records**,
bringing the registry to **429 entries / 426 raw paths**, preserving the previous
**417/414**. Three NPS battle HTML/text pairs remain in the NPS/CWSAC family. Doubleday's
*Chancellorsville and Gettysburg* (Internet Archive `chancellorsville00doubuoft`) is
pinned with catalog metadata, full OCR and one selection. Three report selections (Lee,
Sedgwick, Early) reuse the pinned `or25-1-illinois-ocr-v1`, each its own independence
group. Character ranges and whitespace-only normalization reproduce all sections. No
model inputs are changed.

### Grant's Operations Against Vicksburg (1863) first pass, 2026-09-25

The [ten-record memo](research/vicksburg-1863-first-pass-v1.md) adds **38 records**,
bringing the registry to **417 entries / 414 raw paths**, preserving the previous
**379/376**. Ten NPS battle HTML/text pairs remain in the NPS/CWSAC family. Catalog
metadata and full OCR are pinned for Official Records Series I Volume XXIV Parts 1 and 2
and Volume XXII Part 1 (Internet Archive `warofrebellion241unit`, `242unit`, `221unit`);
the Part 2 imprint year is garbled in OCR and not substituted. Eleven report selections
(Bowen, Sherman, Forney/Hébert, Gregg, Johnston, Pemberton, Dennis, McCulloch, Reid,
Walker, Holmes), each its own independence group, and one Greene selection reusing
`greene-mississippi-ocr-v1` complete the additions. Character ranges and
whitespace-only normalization reproduce all sections. No model inputs are changed.

### Cavalry Operations along the Rappahannock first pass, 2026-09-25

The [one-record memo](research/rappahannock-cavalry-first-pass-v1.md) adds **6 records**,
bringing the registry to **379 entries / 376 raw paths**, preserving the previous
**373/370**. One NPS battle HTML/text pair remains in the NPS/CWSAC family. The Official
Records Series I Volume XXV Part 1 catalog metadata and full OCR
(`or25-1-illinois-ocr-v1`, Internet Archive `warofrebellion251unit`) are pinned as a
shared container, with two selections: Averell's report and Fitz Lee's report, letter
and orders, each its own independence group. Character ranges and whitespace-only
normalization reproduce all sections. No model inputs are changed.

### Longstreet's Tidewater Operations first pass, 2026-09-25

The [four-record memo](research/tidewater-first-pass-v1.md) adds **12 records**,
bringing the registry to **373 entries / 370 raw paths**, preserving the previous
**361/358**. Four NPS battle HTML/text pairs remain in the NPS/CWSAC family. Four new
selections reuse the pinned `or18-illinois-ocr-v1` parent, one per reporting commander
(Foster, D. H. Hill, Peck and French with Longstreet's indorsement), each its own
independence group. Character ranges and whitespace-only normalization reproduce all
sections. No model inputs are changed.

### Middle Tennessee first pass, 2026-09-25

The [five-record memo](research/middle-tennessee-first-pass-v1.md) adds **12 records**,
bringing the registry to **361 entries / 358 raw paths**, preserving the previous
**349/346**. Five NPS battle HTML/text pairs remain in the NPS/CWSAC family. Two new
selections reuse pinned parents: Cist Chapter IX (`cist-cumberland-ocr-v1`) and Jordan
and Pryor Chapter VIII (`jordan-pryor-forrest-ocr-v1`). Character ranges and
whitespace-only normalization reproduce all sections. No model inputs are changed.

### Operations Against Vicksburg (1862–63) first pass, 2026-09-24

The [two-record memo](research/vicksburg-1862-first-pass-v1.md) adds **5 records**,
bringing the registry to **349 entries / 346 raw paths**, preserving the previous
**344/341**. Two NPS battle HTML/text pairs remain in the NPS/CWSAC family. One new
Greene selection reuses the pinned `greene-mississippi-ocr-v1` parent and holds the
title/preface and two Chapter III passages. Character ranges and whitespace-only
normalization reproduce all sections. No model inputs are changed.

### Forrest West Tennessee first pass, 2026-09-24

The [two-record memo](research/forrest-west-tennessee-first-pass-v1.md) adds **7 records**,
bringing the registry to **344 entries / 341 raw paths**, preserving the previous
**337/334**. Two NPS battle HTML/text pairs remain in the NPS/CWSAC family. Jordan and
Pryor's 1868 *Campaigns of Lieut.-Gen. N. B. Forrest* adds a `jordan-pryor-forrest-1868`
family: public catalog metadata, full OCR (Google-digitized Harvard copy) and one
selection holding the title/preface and three Chapter VII passages. Forrest's prefatory
note accepts responsibility for most of the narrative, so the family is not
independent of him. Character ranges and whitespace-only normalization reproduce all
sections. No model inputs are changed.

### Goldsboro first pass, 2026-09-24

The [three-record memo](research/goldsboro-first-pass-v1.md) adds **10 records**,
bringing the registry to **337 entries / 334 raw paths**, preserving the previous
**327/324**. Three NPS battle HTML/text pairs remain in the NPS/CWSAC family. Official
Records Series I, Volume XVIII (Illinois scan) adds catalog metadata and full OCR in
an `or-series-i-volume-xviii` container, and two sectioned report selections:
Foster's three reports (`foster-goldsborough-reports`) and G. W. Smith's five
(`gw-smith-goldsborough-reports`), with section-specific document dates. OCR errors
are retained exactly; the garbled compiler casualty return was not used. No model
inputs are changed.

### Fredericksburg first pass, 2026-09-24

The [one-record memo](research/fredericksburg-first-pass-v1.md) adds **3 records**, bringing
the registry to **327 entries / 324 raw paths**, preserving the previous **324/321**.
One NPS battle HTML/text pair remains in the NPS/CWSAC family. One new Palfrey
selection derivative reuses the pinned `palfrey-antietam-ocr-v1` parent and holds the
title/preface and seven bounded Chapter IV passages; its dependency note omits the
unsupported claim that Palfrey served in the campaign. Character ranges and
whitespace-only normalization reproduce all sections. No model inputs are changed.

### Stones River first pass, 2026-09-24

The [two-record memo](research/stones-river-first-pass-v1.md) adds **5 records**, bringing
the registry to **324 entries / 321 raw paths**, preserving the previous **319/316**.
Two NPS battle HTML/text pairs remain in the NPS/CWSAC family. One new Cist selection
derivative reuses the pinned `cist-cumberland-ocr-v1` parent; its metadata and OCR
are unchanged, and it holds the title/preface and five bounded passages. Character
ranges and whitespace-only normalization reproduce all sections. Cist is an
interested retrospective history by Rosecrans's staff officer; quoted reports are
not separately inspected originals. No model inputs are changed.

### Iuka and Corinth first pass, 2026-09-24

The [three-record memo](research/iuka-corinth-first-pass-v1.md) adds **9 records**,
bringing the registry to **319 entries / 316 raw paths**, preserving the previous
**310/307**. Three NPS battle HTML/text pairs remain in the NPS/CWSAC family. Francis
Vinton Greene's 1882 *The Mississippi* adds a `greene-mississippi-1882` family: public
catalog metadata, full OCR and one selection derivative holding the title/preface
and two bounded Chapter II passages. Character ranges and whitespace-only
normalization reproduce all sections. Greene was not a participant and founded the
book on the Official Records; quoted reports are not separately inspected
originals. No model inputs are changed.

### Maryland first pass, 2026-09-24

The [campaign memo](research/maryland-first-pass-v1.md) adds **9 records**, bringing
the registry to **310 entries / 307 raw paths**, preserving the previous **301/298**.
Three NPS battle HTML/text pairs remain in the NPS/CWSAC family. Francis Winthrop
Palfrey's 1882 *The Antietam and Fredericksburg* adds a
`palfrey-antietam-fredericksburg-1882` family: public catalog metadata, full OCR and
one selection derivative holding the title/preface and four bounded passages.
Character ranges and whitespace-only normalization reproduce all sections; OCR
errors, misread page markers and footnotes are retained. All selections were read,
without print, map, roster or whole-book verification. Palfrey was a Union
participant who used advance sheets of the Official Records; quoted reports are not
separately inspected originals. The dependency note's claim that Palfrey served in this campaign
is not shown in the inspected text (review advisory A3); the record itself is unchanged. MD003's
existing sources are unchanged. No model
inputs are changed.

### Northern Virginia first pass, 2026-09-24

The [six-record memo](research/northern-virginia-first-pass-v1.md) adds **15 records**,
bringing the registry to **301 entries / 298 raw paths**, preserving the previous
**286/283**. Six NPS battle HTML/text pairs remain in the NPS/CWSAC family. John
Codman Ropes's 1881 *The Army under Pope* adds a `ropes-army-under-pope-1881` family:
public catalog metadata, full OCR and one selection derivative holding the
title/preface, ten bounded battle passages and Appendix D. Character ranges and
whitespace-only normalization reproduce all sections; OCR errors, running headers,
one garbled page and map-label text are retained. All selections were read, without
print, map, roster or whole-book verification. Ropes is a retrospective history
written from the Federal standpoint; quoted reports are not separately inspected
originals. Casualty, result-label and knowledge disputes remain visible. No model
inputs are changed.

### Heartland Offensive first pass, 2026-09-24

The [five-record memo](research/heartland-first-pass-v1.md) adds **13 records**, bringing
the registry to **286 entries / 283 raw paths**, preserving the previous **273/270**.
Five NPS battle HTML/text pairs remain in the NPS/CWSAC family. Henry M. Cist's
1882 *The Army of the Cumberland* adds a new `cist-cumberland-1882` family: public
catalog metadata, full OCR and one selection derivative. That derivative holds the
title/preface and five bounded battle passages. Character ranges and whitespace-only
normalization reproduce all sections; OCR errors, running headers and map-label text
are retained. All selections were read, without claiming print, map, roster or
whole-book verification. Cist is an interested retrospective Union history; quoted
reports and participant accounts are not separately inspected originals. Result-field,
casualty, chronology and rank conflicts remain visible. No model inputs are changed.

### Valley first pass, 2026-09-20

The [seven-record memo](research/valley-first-pass-v1.md) adds **14 records**, bringing
the registry to **273 entries / 270 raw paths**, preserving the previous **259/256**.
Six NPS battle HTML/text pairs and the empty Princeton HTML diagnostic remain in
the NPS/CWSAC family. One new selection derivative reuses the pinned Allan 1880
OCR for six battles: title/preface plus six bounded passages. Previous metadata,
OCR and Hancock selections stay unchanged. Character ranges and whitespace-only
normalization reproduce all sections; OCR errors and footnotes are retained.
All selections were read, without claiming print, map or whole-book verification.
Allan's interested retrospective history and embedded reports are one family,
not separately inspected originals. Princeton retains only frozen NPS/CWSAC
evidence; the empty page and unsuccessful shared-book keyword lookup establish
no historical facts. Source disputes, incomplete casualties, reported beliefs
and changing populations remain visible. No model inputs are changed.

### Peninsula first pass, 2026-09-20

The [16-record memo](research/peninsula-first-pass-v1.md) adds **36 source records**,
bringing the registry to **259 entries / 256 raw paths**, preserving all previous
**223/220**. Fifteen NPS battle HTML/text pairs, the empty VA020 HTML diagnostic,
and one Drewry's Bluff park-history HTML/text pair stay in the NPS/CWSAC family.
VA020A has no live narrative. Webb's 1881 *The Peninsula* contributes catalog, full
OCR and thirteen sectioned selections (title/preface and twelve battle/context
passages), serving fourteen land records. His participant recollections and
collation of reports are retrospective; original documents and maps were not
inspected. The November 1881 preface does not date individual passages.

All retained selections were read; exact character ranges and whitespace-only
normalization preserve the OCR without claiming print fidelity. No new maps or
images were inspected. Hampton Roads' naval follow-up could not be downloaded
(NHHC certificate/404 and NOAA 403); search snippets supply no evidence. Both
naval records retain one family, the land records two, with independence
unestablished. Source conflicts, hospital/vessel populations and June 30 overlap
remain explicit. No frozen cohort, source, model or admission input is replaced.

### New Madrid/Memphis first pass, 2026-09-20

The [two-battle memo](research/mississippi-joint-first-pass-v1.md) adds seven
records, bringing the registry to **223 entries / 220 raw paths**, preserving all
previous **216/213**. The live MO012 HTML is an empty-template retrieval diagnostic;
it supplies no battle evidence. Memphis has a complete NPS HTML/text pair.
Mahan's *The Gulf and Inland Waters* adds a Gutenberg catalog, full HTML and
normalized text, and selected text with exact parent offsets. Read title/preface,
two Island No. 10 passages and the Memphis passage including its letter reference.
Each battle uses two families and one targeted shared-history follow-up.

The edition is **1898**, with 1883 copyright and a June 1883 preface, not a
contemporary battle document. Gutenberg provides a corrected digital transcription;
our transforms preserve its characters apart from whitespace normalization.
Original reports/letters, maps and print were not inspected. Section dates stay
null; later NPS dependence is unestablished. The memo preserves surrender-date
differences, missing personnel/casualty definitions, separate command roles and
vessels versus crews. All earlier source records remain unchanged; no feature
is admitted.

### Burnside campaign first pass, 2026-09-20

The [five-battle memo](research/burnside-first-pass-v1.md) records all frozen
members of Burnside's North Carolina Expedition. Thirteen new artifacts bring
the registry to **216 entries / 213 raw paths**, preserving all previous
**203/200**: five NPS HTML/text pairs, Woodbury catalog metadata and full OCR,
and one sectioned text selection. Read every summary, the catalog/title/preface,
and six selected battle-context passages. Each battle uses two retained families;
Woodbury is one interested, non-eyewitness author across the campaign, and NPS
summaries/table copies share a family. His source documents were not inspected.
No facsimile or map was checked. Character ranges replay whitespace-only
selection; OCR errors and source disagreements remain visible. Reported dates,
strength populations, outcomes and casualty differences are not silently resolved.
The shared history served the one targeted follow-up per battle; additional
original orders, returns and historical adjudication remain deferred. No source
is overwritten and no model feature is admitted.

### Eastern Kentucky first pass, 2026-09-20

The [campaign memo](research/eastern-kentucky-first-pass-v1.md) records Middle
Creek and Mill Springs together. Ten new source records bring the registry to
**203 entries / 200 raw paths**, preserving all previous **193/190**: NPS
HTML/text pairs for both battles and the Crittenden article, Cornell/Internet
Archive catalog and full Official Records VII OCR, and Garfield/Thomas selections.
Each battle uses NPS/CWSAC plus its Union commander's report family; reprints and
the shared compilation are not additional witnesses. Read all retained selections;
no print facsimile, casualty-table layout, original manuscript or cited modern
book was inspected. Report dates are section-specific. Exact character ranges
replay whitespace-only extraction; OCR errors remain. The OCR imprint is 1882,
while the catalog's 1880 is a collection date. Original Confederate evidence,
matched strengths, source disputes and exact clocks remain deferred after one
targeted report-recovery follow-up per battle. Drafts admit no model features.

### Hancock first pass, 2026-09-20

The [bounded pass](research/hancock-first-pass-v1.md) adds five records: NPS
MD001 HTML/text, Internet Archive catalog metadata for Allan's 1880 history, its
complete OCR parent and two selected sections in one text file. The registry is
**193 entries / 190 raw paths**, preserving all previous **188/185**. NPS remains
in `nps-cwsac`; Allan's three artifacts form one `allan-valley-1880` family.
Independence between the two families is unestablished. Both selected book sections
and the full NPS summary were read, but no original report, map or facsimile was
inspected. OCR errors are preserved; selection ranges and hashes reproduce the
text without claiming print fidelity. The original-report follow-up was inaccessible.
The draft retains the January 4/5 approach discrepancy, 25-versus-zero casualties,
and unknown opening personnel/information. No existing source or model input changes.
Separate Astra `xhigh` [review](../artifacts/review-results/hancock-86abaf3-astra-xhigh-v1/review.md)
accepted all 11 claims with no required corrections; this is digital text/OCR review,
not print verification or historical adjudication.

### Cockpit Point first pass, 2026-09-20

The [bounded pass](research/cockpit-point-first-pass-v1.md) adds two NPS HTML
snapshots and two extracted text selections: the VA100 battle detail and the
Potomac Heritage Cockpit Point narrative. All share `nps-cwsac` with the pinned
tables; this pass retains **one source family**, with no independent confirmation.
The registry is **188 entries / 185 raw paths**, preserving all earlier records.
Both selected texts were fully inspected and replayed from their HTML parents;
no image, map, original report or facsimile was inspected. The attempted Navy
follow-up was not retained as evidence. Unknown opening personnel, combat supply
and information stay explicit, and January's nondecisive outcome is separate
from the later March evacuation. No raw evidence or model input is replaced.
Separate Astra `xhigh` [review](../artifacts/review-results/cockpit-point-1d96e40-astra-xhigh-v1/review.md)
accepted all 10 claims with no required corrections; it remains digital-text review
of one source family, not historical adjudication.

### Bounded river-campaign first pass, 2026-09-20

The [campaign memo](research/river-campaign-first-pass-v1.md) adds eight source
records: a complete Grant memoir HTML download with its license, one selected
paragraph transcript, and HTML/text pairs for NPS Fort Henry, Fort Donelson and
Corinth I. The registry now contains **184 entries / 181 raw paths**. All previous
records and raw inputs remain unchanged. Grant's selections and the three NPS
summaries were inspected as digital text; no print facsimile was checked.

Each new dossier uses **two source families**: NPS/CWSAC and Grant. The NPS
snapshots share `nps-cwsac` with the pinned table. The memoir shares `or-grant`
with Grant's existing report to avoid treating one author's later narrative as
an independent witness. Chapters and formats add no families. Independence
between the two families is not established by this bookkeeping. The memoir is
an interested retrospective account; original reports cited inside it were not
thereby inspected. Document dates remain null; the preface date does not date
the chapters. Full paragraphs preserve context, not endorsement of every claim.

The three new schema-v1 dossiers add prose observations, not typed/admitted
strengths. Proposed expeditions, late forces, prisoners and retrospective enemy
estimates remain separate. Live zeros, campaign-like date fields, casualty
mismatches and the unexplained Corinth raid wording remain unresolved; the
frozen tables and cohort are not migrated or overwritten. Separate Astra `xhigh`
[review](../artifacts/review-results/river-campaign-0cc3b1b-astra-xhigh-v1/review.md) accepted all 33 new
claims with no required corrections; its extraction replay remains digital-only.


### Shiloh contact and location packet, 2026-09-20

The [versioned packet](research/shiloh-contact-location-v1.md) adds 32 source
entries: nine selected participant-report transcriptions, one Reed excerpt file,
16 full-page facsimiles, two LOC map JPEGs, two verbatim catalog JSON responses
and two selected map-label transcriptions. The preparation registry has 85 entries and
82 distinct raw paths. Earlier 53 entries and their raw inputs are unchanged.
Full participant reports were read as OCR context across 16 OR pages; the visual
check covers selected opening passages on 12 of those pages and four Reed pages.
The contextual OCR is retained separately from the manually checked excerpts.
See the packet for exact inspection coverage, dated/undated report distinctions,
parent hashes, map locators, dependence limits and the offline reference audit.

The maps are attributed to the US Army Department of the Tennessee and to
Frémaux with Beauregard's endorsement. Catalog year 1862 does not establish
pre-contact creation or knowledge. One map distinguishes morning/night and the
other covers April 6–7 without a clock-specific legend; neither proves a B0
perimeter or full population. Map/catalog/transcription records remain in the
associated army reporting dependence group. No source is counted as independent
because it has a second image, catalog record or transcription.

The [separate review and literal correction addendum](research/shiloh-contact-location-corrections-v1.md)
add `or-prentiss-opening-v2` and `loc-85690890-readings-v2`, preserving their v1
records and images. Only `commander` → `commandant` and `Hornets` → `Hornet`
change. The registry at that correction has **87 entries / 84 raw paths**; the two versions
do not add witnesses, change dates or alter any historical assertion.

The [precontact-segmentation packet](research/shiloh-precontact-segmentation-v1.md)
adds nine selected text records and 15 page images, preserving all prior entries.
The prepared registry had **111 entries / 108 raw paths**. Ten attributed assertions
have 24 exact passage anchors; selected passages/context were visually inspected
on 19 pages, reusing four scans. Hardee’s retrospective report is dated February 7,
1863; Ricker’s uncertain printed date remains null. Contemporary orders, report
claims and later editorial headings remain distinct. The working precursor rule
is a research recommendation; the Saturday Howell link is unresolved.
The [literal correction addendum](research/shiloh-precontact-segmentation-corrections-v1.md)
adds `or-april4-march-orders-v2` for two image-confirmed Jordan wording corrections.
All 111 prior entries are preserved; the registry at that correction has **112 entries /
109 raw paths**. One PS05 quote has an explicit correction overlay; all 24 anchors
replay with unchanged document dates and historical interpretation.

The [Howell trace](research/shiloh-howell-trace-v1.md) adds seven selected text
sources, 11 page images and three exact HTML snapshots, preserving all 112 prior
entries. That packet's registry has **133 entries / 130 raw paths**. Four new book
transcriptions cover Medkirk's 1886 letter, Worthington's disputed testimony
selections and undated Abstract, and Reed's GPO 1903 printing. Three modern web
sources preserve one NPS plaque transcription and two NARA archival guides.
Seven assertions have 14 anchors; 12 retained pages were visually inspected.
No direct participant-to-Reed link or Saturday-to-Sunday continuity is established.

The [regimental and post comparison](research/shiloh-regimental-posts-v1.md) adds
five selected text sources (17 historical sections) and 13 whole-page facsimiles,
preserving all 133 prior entries. Its prepared registry has **151 entries / 148 raw
paths**. Seven assertions bind 21 anchors / 19 source-section pairs; 16 retained
pages were visually inspected including three reused pages. Reid's 1868 compilation,
Lemmon's speech delivered in 1875, Worthington's undated appended trial allegations
and additional 1872 excerpts, and Buell's retrospective map remain distinct source
families with explicit dependencies. New excerpts from the same publication are
not new witnesses. The overnight lead has no established Howell post match; no
historical feature is admitted.
The [review correction](research/shiloh-regimental-posts-corrections-v1.md) adds one
map text version restoring three literal occurrences in two sections. All 151
prepared entries remain intact. The registry at that stage has **152 entries / 149 raw
paths**; two explicit quote overlays replay the 21 anchors without changing dates
or interpretations. A corrected version is not another historical witness.

The [Reid provenance trace](research/shiloh-reid-provenance-v1.md) identifies the publisher collection process and Miller's general editorial role, but no original 46th Ohio witness. Lindsey supplies a later wording parallel with independence unestablished. Five assertions bind 11 anchors / 10 source-locator pairs, ten retained page images and one text-only LOC catalog snapshot. All earlier evidence is preserved; the registry at that stage has 164 entries / 161 raw paths and zero feature admission. Separate Astra `xhigh` [review and primary assessment](../artifacts/review-results/shiloh-reid-1c498e0-astra-xhigh-v1/primary-assessment.md) accept all five bounded assertions with two nonblocking catalog clarifications: use the retained Agate letters label and provider page/line locators; material format and printed pagination remain unverified.

The twelve records added by the Reid provenance trace comprise two selected book transcriptions (six sections),
nine whole-page images and one LOC extraction JSON. The catalog PDF was not
downloaded; its parent hash is null. Its raw hash binds only retained text.

The [Agate comparison](research/shiloh-agate-comparison-v1.md) locates two historical reprints with 1864 title imprints, supporting a Reid/Agate account dated April 9, 1862. Its inspected opening reports Saturday skirmishing but does not supply the later B/K overnight narrative or identify its witness/post. The original Gazette issue remains uninspected. Five assertions bind 16 anchors / 12 source-section pairs across 11 inspected images; the registry now has 176 entries / 173 raw paths, with zero feature admission. Separate Astra `xhigh` [review and primary assessment](../artifacts/review-results/shiloh-agate-73e26d4-astra-xhigh-v1/primary-assessment.md) accept all five bounded historical assertions; the sole documentation inventory finding is corrected and closed by primary verification. The original issue, overnight witness and continuity remain unresolved.

The Agate comparison adds twelve records: two selected book transcriptions
containing eleven historical sections and ten whole-page images. One reused Reid
page brings the inspected-image total to eleven.

Prioritize original reports, contemporary orders and correspondence, then
independently authored scholarship. Record competing estimates and account
dependencies. Do not treat search snippets, model recollection, or an unsourced
online ranking as a historical source. The [research prompt](../prompts/research-dossier.md)
sets the extraction rules; the [evidence contract](evidence-contract.md) defines review.

### Shiloh enrichment, 2026-09-20

Eight sectioned text sources and two facsimiles were added without changing any
earlier raw input. See the [research memo](research/shiloh.md) for findings and open
questions, and the registry for exact URLs, parent hashes and transformations.

| Source family | Inspected material retained | Use and dependency |
|---|---|---|
| [Official Records I.X.1](https://archive.org/details/1warofrebellion10secrrich) | Grant, Buell and Beauregard report excerpts; Union p.112 and Confederate p.396 return transcriptions and scans | Contemporary reports compiled/published in 1884; commanders' reports are interested participant accounts |
| [Official Records I.X.2](https://archive.org/details/2warofrebellion10secrrich) | Halleck to Grant, March 20 (pp.50–51) and April 5 (p.94) | Issued orders; receipt and later modifications require separate evidence |
| [M. F. Force, *From Fort Henry to Corinth*](https://www.gutenberg.org/ebooks/24438) | Preface and pp.178–180 including correction in footnote 3 | Original 1881 history; author explicitly relies on official reports and other accounts |
| [Gudmens and Staff Ride Team, *Staff Ride Handbook for the Battle of Shiloh*](https://archive.org/details/DTIC_ADA445681) | Selected government narrative pp.84–85, 100, 113 and appendix heading p.137 | Army teaching history drawing on Official Records and later histories; overlapping evidence |

The Army report documentation gives 2004, while its library catalog data uses
2005. Both labels are retained in metadata rather than silently harmonized.
Force's original work dates to 1881; the accessible ebook derives from a later
facsimile. No modern facsimile foreword was copied. Accounts quoted by Force or
the handbook are secondhand unless separately registered and inspected.

The two large Official Records volumes and the Army PDF were downloaded for local
inspection but are not vendored. Parent-file hashes identify the exact downloads
used. Report excerpts use pypdf-extracted OCR with whitespace collapsed, preserving
OCR misspellings. Tables and Halleck's orders were transcribed from rendered pages;
their transformations are explicit. The two full table-page PNGs allow review of
headings and omissions, and have their own source hashes. They are not additional
independent testimony. Snapshots can be restored from Git; `fetch` does not silently
regenerate them from mutable book downloads.

The p.112 abstract, p.396 return, and Halleck orders are not clean numeric rows by
themselves. Dates, column meanings, omissions and disagreement notes are retained
with the extracted quantities. Source IDs and section IDs are validated together:
a quote on another page in the same file cannot satisfy a declared citation.
Manual transcription and exact passage matching still require an independent
entailment/error audit. This pass has not completed that review.

### Confederate return follow-up, 2026-09-20

Reports Nos.136 and 137 in Official Records I.X.1, printed pp.398–399 (PDF
pp.422–423), were visually inspected in the same checksum-verified parent volume.
Two versioned selected-column transcriptions and two entire-page facsimiles were
added. All previous raw inputs, IDs and hashes remain unchanged. See the
[comparison and migration record](research/shiloh-confederate-returns.md).

Both returns are signed by Bragg with a bracketed June 30 submission/forwarding
date; their headings respectively describe the April 3 march and an April 10
after-battle return. These dates and population columns remain distinct. Report
136 notes Hill's Monday arrival, and report 137 describes losses and arrivals of
Carroll's brigade and previously detached cavalry. Neither supplies a numerical
reconciliation with p.396. Report 137's infantry effective and enlisted-for-duty
subtotals also disagree with the printed corps rows; both readings are retained.

The new sources keep `or-beauregard` as their independence group because they
belong to the same army reporting chain. Bragg's signature and the additional
scans do not establish independent corroboration. The scans were rendered with
pypdfium2 and rotated for reading; that optional local research tool is not a
runtime or test dependency. The NPS 44,968 total remains untraced, and no
independent historical review is claimed.

### Union availability follow-up, 2026-09-20

Eight new sectioned text snapshots and four Reed table facsimiles preserve the
inspected evidence without replacing any of the earlier 21 source records or
files. The [unit-by-phase audit](research/shiloh-union-availability.md) gives exact
locators, parent hashes, findings and migration. The new return-detail snapshot
adds Sixth Division component rows from the already pinned OR p.112 scan.

New participant excerpts cover Wallace (April 12), Prentiss (November 17 after
captivity), Chambers (April 24), Reid (date unstated in inspected heading), and
Rousseau (April 12). Dates of reports are separate from dates of events. Shared
reporting environments remain visible in independence groups; a different author
does not establish independent evidence. Selected prose is manually transcribed
from rendered pages, with whitespace normalized and line-wrap hyphens removed.

Reed's *The Battle of Shiloh and the Organizations Engaged*, revised 1909, is a
later government compilation explicitly based on Official Records. Its table
asterisks, mixed dates and stated present-for-duty-as-engaged convention remain
visible. A detachment note bridges 7,564 to 5,837, but does not explain Force's
6,500 or prove the Army handbook's 5,800 derivation. Reed's Fifteenth Michigan
narrative conflicts with his April 6 recapitulation; this is not adjudicated away.
The table scans preserve pp.93 and 96-98, rendered with pypdfium2 and rotated for
reading. The rendering library is only a research tool, not a runtime dependency.

Michigan's report **for 1862**, dated December 24, was published in **1863**.
Its p.41 supports a reported April 5 arrival of the Fifteenth Infantry and losses
over the two-day battle. It does not validate Force's Sunday-only casualty
allocation. The inspected scan, rather than a modern AI transcription or a search
snippet, is the evidence. Its underlying regimental returns have not been traced.
No new independent review record or canonical opening-strength estimate is claimed.

### Army of the Ohio reinforcement follow-up, 2026-09-20

Twelve sectioned text snapshots and five full-page facsimiles extend the registry
from 33 to 50 sources. All earlier records and raw files remain unchanged. The
[crossing and strength audit](research/shiloh-ohio-reinforcements.md) records exact
locators, parent hashes, phase distinctions and the archived dossier migration.
Participant reports cover Nelson, Ammen, Grose, Anderson, Jones, both Edward and
Alexander McCook, Crittenden, Wood, Garfield and a supplement to Buell. Ammen's
separately printed diary has event dates but no established composition date in
the inspected passages; the April 10 report dateline is not assigned to the diary.

Manual transcriptions retain the conflicting crossing clocks and preserve each
author's distinction between landing, formation and action. Nelson's action
table and the compiler's March return have different periods and populations.
Their full OR pp.326-327 facsimiles retain headings, component rows and exclusions.
Reports within Nelson's command share `or-nelson`; other Ohio army reports retain
`or-buell`. These dependence flags do not certify independent corroboration
between groups or between authors.

Reed's pp.100-102 facsimiles preserve mixed return dates, missing brigade reports,
approximation marks and Wagner's estimated late-arrival strength. McCook is
7,553 in the detail table but 7,552 in the recap; the latter produces the printed
17,918 army total. Neither reading is silently corrected or treated as a dawn
census. Reed's note j quotes an undated Buell letter that has not been separately
inspected; that secondhand lead has no new typed troop observation. The existing
Force estimate and the handbook's untraced 600-person Sunday contingent remain
visible. No independent historical review or enriched model input is claimed.

### Reviewed metadata corrections, 2026-09-20

The [bounded correction pass](research/shiloh-review-corrections.md) implements
four findings from the recorded separate AI review. All 50 earlier source entries
and raw files are preserved. Three metadata-only revisions reuse existing files:
`or-ammen-crossing-v2`, `or-nelson-reinforcements-v2` and
`or-union-return-detail-v3`. The registry therefore has 53 records and 50 distinct
raw paths; these versions add no witnesses or independent corroboration.

The first two replace an overly broad report date with section-specific dates,
retaining null diary/compiler dates. The third links the shared OR p.112 image
and aligns the same-return dependence group. Each new entry binds its predecessor's
full metadata hash. Current citations select the corrected IDs; archived dossiers
and the frozen review bundle keep the old records. Dossier schema v3 separately
records source estimation qualifiers while preserving every numerical observation.
