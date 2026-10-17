# Source additions

Per-pass record of the sources registered in `data/sources.json`, moved verbatim from
`docs/sources.md` on 2026-10-06. Entries are kept as originally written. The rules for using
sources are in [sources and provenance](sources.md); the registry is the authority for exact
bytes, rights and dependence metadata.

## Trans-Mississippi 1862 first passes (cohort v2), 2026-09-25

The first passes for Sibley's New Mexico campaign, Pea Ridge, the White River, Cache River and the
operations north of the Boston Mountains add **46 records**:

- eleven NPS HTML/text pairs;
- Official Records Series I, Volumes IX and XIII: catalog metadata and full OCR;
- nineteen report selections, including compiled casualty returns labelled as the compiler's work;
- a Britton volume I selection.

This pass's Volume VIII and Britton volume I parents were deduplicated to the 1861 West
registrations (`or8-illinois-ocr-v1`, `britton-border-1-ocr-v1`), whose OCR is byte-identical. No
model inputs are changed.

**Review correction (TM-R2, TM-R3).** Two metadata-only successors correct dependency notes and
groups: `or13-cooper-newtonia-old-fort-wayne-selections-v2` (group `cooper-indian-territory-report`)
and `or13-hindman-cache-river-selections-v2` (Hindman names no author for "the detailed report").
Citations moved to them. The Trans-Mississippi 1863 Cooper record stays in
`cooper-indian-territory-1862-reports`, the same author family. The Britton volume I selection stays
in `britton-civil-war-on-border-1899` (TM-R1; see the W61-R14 note).

## Gulf and Louisiana 1862–63 first passes (cohort v2), 2026-09-25

The first passes for six campaigns add **50 records**: New Orleans, Baton Rouge, La Fourche (1862),
West Louisiana, Port Hudson and Taylor's 1863 operations. The records are:

- fourteen NPS HTML/text pairs;
- Official Records Series I, Volumes XV and XXVI Part 1, and Navies Volume 19: catalog metadata and
  full OCR;
- ten report selections;
- six selections from the registered Mahan and Irwin OCR.

This pass's Volume VI parent was deduplicated to the 1861 West registration, whose OCR is
byte-identical. No model inputs are changed.

## 1861 Eastern first passes (cohort v2), 2026-09-25

The first passes for six 1861 campaigns add **78 records**: Charleston Harbor, the Chesapeake,
Western Virginia, Manassas, the Carolina coast and McClellan's Northern Virginia operations (memos
`docs/research/{charleston,chesapeake,western-virginia,manassas,carolina-coast,northern-virginia}-1861-first-pass-v1.md`).
The records are:

- seventeen NPS HTML/text pairs;
- Nicolay, *The Outbreak of Rebellion* (1881): catalog metadata, full OCR and selections;
- Official Records Series I, Volumes I and II (University of California scans; the Illinois
  identifiers are Series II and III volumes) and Volume V: catalog metadata and full OCR;
- Official Records of the Navies, Series I, Volumes 4–6: catalog metadata and full OCR;
- twenty-seven report selections (thirty selections in all, with Nicolay's three).

No model inputs are changed.

## Plymouth and Fort Fisher first passes (cohort v2), 2026-09-25

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

## Appomattox and Waynesboro first passes (cohort v2), 2026-09-25

The first passes for the [Appomattox Campaign](research/appomattox-first-pass-v1.md) and
[Sheridan's Expedition to Petersburg](research/sheridan-petersburg-1865-first-pass-v1.md) add
**40 records**:

- fifteen NPS HTML/text pairs;
- new selections from the registered Humphreys and Pond OCR;
- eight report selections from the registered Volume XLVI Part 1 OCR.

No new volume or catalog record was registered, and no model inputs are changed.

## 1861 Western and Trans-Mississippi first passes (cohort v2), 2026-09-25

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

**Author groups (review W61-R14).** Britton volume I (`britton-civil-war-border`) and volume II
(`britton-civil-war-border-1899`) are one witness family. Price's Lexington report
(`price-lexington-report`) is the same family as `price-camden-1864-report` and
`price-missouri-1864-reports`. The volume I and Price dependency notes that ask for reconciliation
at merge predate the merge; the records are left unchanged. The Trans-Mississippi 1862 pass
registered a third Britton volume I group name, `britton-civil-war-on-border-1899`; it is the same
family.

## Atlantic coast 1862–65 first passes (cohort v2), 2026-09-25

The first passes for nine Atlantic coast campaigns add **65 records**: Fort Pulaski, Charleston
1862, Tampa 1862, St. John's Bluff, Fort McAllister 1863, Charleston 1863, Hillsboro 1863,
Florida 1864 and St. Marks 1865 (memos `docs/research/<slug>-first-pass-v1.md`). The records are:

- fifteen NPS HTML/text pairs;
- Official Records Series I, Volumes XIV, XXVIII Part 1 and XXXV Part 1 (Illinois scans): catalog
  metadata and full OCR;
- Official Records of the Navies, Volumes 13, 14 and 17 (Trent University scans): catalog metadata
  and full OCR;
- Samuel Jones, *The Siege of Charleston*: catalog metadata, full OCR and three selections;
- eighteen report selections.

Each volume's number and part was checked against the catalog metadata and the OCR title page.

**Merge deduplication.** This pass fetched its own copies of Volumes VI and XLIX Part 1. The OCR
files were byte-identical to the registered parents (`or6-illinois-ocr-v1`,
`or49-1-illinois-ocr-v1`), so they were not registered again, and the duplicate catalog records
were dropped.

**Author groups.** Gillmore reuses `gillmore-petersburg-june-9-report` and Beauregard reuses
`beauregard-drewrys-bluff-report` (the older `or-beauregard` and `beauregard-bull-run-1861-reports` groups are the same family). Jones's book
reuses `samuel-jones-east-tennessee-reports`, the same person. No model inputs are changed.

## Trans-Mississippi 1863 first passes (cohort v2), 2026-09-25

The first passes for eight Trans-Mississippi campaigns of 1862–64 add **50 records**: Prairie
Grove, Marmaduke's first and second 1863 expeditions, the Indian Territory 1863, Quantrill's 1863
raid, Little Rock 1863, the northern Indian Territory 1863 and the Indian Territory 1864 (memos
`docs/research/<slug>-first-pass-v1.md`). The records are:

- fourteen NPS HTML/text pairs (the Middle Boggy Depot live page has an empty description and the
  wrong campaign and dates);
- six new selections from the registered Britton volumes I and II;
- fifteen selections from the registered Official Records Volume XXII Part 1 and one from Volume
  XXXIV Part 1.

**Merge deduplication.** This pass registered Britton volume I from a copy of the Trans-Mississippi
1862 drafting files, as `ia-britton-civil-war-border-1-metadata-v1` and
`britton-civil-war-border-1-ocr-v1`. The OCR was byte-identical to the registered parent
`britton-border-1-ocr-v1`, so it was not registered again; its selections point to that parent and
the duplicate catalog record was dropped. The Prairie Grove memo still names the drafting IDs.

**Author groups.** McNeil and Cooper reuse the Trans-Mississippi 1862 pass's groups; the older
`cooper-indian-territory-report` group is the same author. Hindman reuses
`hindman-mclemores-cove-reports`, Price reuses `price-missouri-1864-reports` (see the W61-R14 note)
and Marmaduke has one new group, `marmaduke-1863-reports`. `williams-cabin-creek-1863-report`
(James M. Williams) and `williams-east-tennessee-reports` (John S. Williams) are different authors. No model
inputs are changed.

## 1864 Eastern small operations first passes (cohort v2), 2026-09-25

The first passes for four 1864 Virginia campaigns add **30 records**: the Rapidan (Morton's Ford),
the Kilpatrick–Dahlgren raid (Walkerton), Crook and Averell's raid (Cloyd's Mountain, Cove
Mountain) and Lynchburg (New Market, Piedmont, Lynchburg) (memos
`docs/research/<slug>-first-pass-v1.md`). The records are:

- seven NPS HTML/text pairs;
- four selections from Official Records Series I, Volume XXXIII, and eight from the registered
  Volume XXXVII Part 1;
- four selections from the registered Humphreys (*From Gettysburg to the Rapidan*, `humphreys-ocr-v2`)
  and Pond texts.

**Merge deduplication.** This pass fetched its own copy of Volume XXXIII. The OCR was
byte-identical to the registered parent `or33-illinois-ocr-v1`, so it was not registered again, and
the duplicate catalog record was dropped.

**Author groups.** Sigel's 1864 dispatches reuse `sigel-carthage-report` and Breckinridge's reuse
`breckinridge-baton-rouge-1862-report`; Crook, Averell, Early, Kilpatrick, Lee, Humphreys and Pond
reuse their existing groups. Walkerton is scoped to the March 2 ambush; the raid is context. No
model inputs are changed.

## Frontier and Texas coast first passes (cohort v2), 2026-09-25

The first passes for nine campaigns add **66 records**: the Sioux uprising of 1862, the Texas
coast 1862, Galveston 1863, Cache Valley 1863, the Sioux (Dakota) 1863 expeditions, the Texas
coast 1863, Sully's 1864 expedition, Sand Creek 1864 and Brazos Santiago 1865 (memos
`docs/research/<slug>-first-pass-v1.md`). The records are:

- fourteen NPS HTML/text pairs;
- Official Records Series I, Volumes XLVIII Part 1 and L Part 1: catalog metadata and full OCR;
- Bancroft, *History of Utah* (1889), and the Joint Committee's *Massacre of Cheyenne Indians*
  (1865): catalog metadata and full OCR;
- thirty selections, some from the registered Volumes XXII Part 1 and XLI Part 1.

**Merge deduplication.** This pass fetched its own copies of Volumes XIII, XV and XXVI Part 1 and
Navies Volume 19. The OCR files were byte-identical to the registered parents
(`or13-illinois-ocr-v1`, `or15-illinois-ocr-v1`, `or26-1-illinois-ocr-v1`, `orn19-trent-ocr-v1`), so
they were not registered again, and the duplicate catalog records were dropped.

**Author groups.** Magruder reuses `magruder-big-bethel-reports`. Sibley, Sully and Crocker each
have one group across campaigns. `sibley-sioux-reports` and `sibley-new-mexico-1862-reports` both
carry the author string "Henry H. Sibley" but are separate groups: the reports come from opposite
sides of different campaigns. Neither the author strings nor the frozen commander table separates
the two: the table gives the identical full name "Henry Hastings Sibley" to the Confederate NM001
commander and to the Union MN002 and ND001–ND003 commander. The groups are kept apart on the
reports' content; whether the NM001 name is a frozen-table error is not resolved. The committee
report and Smith's testimony, printed in one volume, are treated as separate families. No Dakota,
Shoshone, Cheyenne or Arapaho account was obtained; no Confederate account of Palmito Ranch was
found in the inspected report list. No model inputs are changed.

**Review correction (frontier review), 2026-09-25.** Six metadata-only successors supersede
`or15-davis-galveston-selections-v1` and `or15-magruder-galveston-selections-v1` (FRC-01, stale
parent-registration note); `ia-bancroft-utah-metadata-v1`, `bancroft-utah-ocr-v1` and
`bancroft-utah-bear-river-selections-v1` (FRC-07, unsupported "First edition"; the selection is
reparented to `bancroft-utah-ocr-v2`); and `joint-committee-sand-creek-report-selections-v1`
(FRC-14, the report's dependence on Smith's testimony). Each successor is the `-v2` of its record.
Raw files, hashes and ranges are unchanged.

## 1864 Western small operations first passes (cohort v2), 2026-09-25

The first passes for ten 1864 campaigns add **58 records**: North Alabama (Athens), Meridian,
Dalton, Forrest's West Tennessee and Mississippi operations, Morgan's Kentucky raid, Burbridge's
and Stoneman's raids into Southwest Virginia, Breckinridge in East Tennessee and the Lake Village
expedition (memos `docs/research/<slug>-first-pass-v1.md`). The records are:

- fifteen NPS HTML/text pairs;
- twenty-seven report selections from the registered Official Records Volumes XXXII Part 1,
  XXXIV Part 1, XXXIX Part 1 and XLV Part 1;
- one selection from the registered Jordan and Pryor OCR (`jordan-memphis-selections-v1`).

No new parent volumes were needed. **Author groups.** Forrest, Sturgis, Sherman, Thomas, Johnston,
Jordan and Pryor, and Breckinridge reuse existing groups; Johnston's October 20, 1864 report is the
same document as the registered Atlanta selection. Seventeen authors have new groups, Burbridge
with one group for both his selections. The Fort Pillow and Saltville killings are recorded as each
source's statement; no characterization or count is adopted. No model inputs are changed.

## Livermore v2 transcription (v2 strength ledger), 2026-09-25

Under the owner's v2 source decision
([record](../data/estimates/owner-decision-v2-sources-2026-09-25.json)), **33 records** add
Livermore's *Numbers and Losses* entries that match cohort-v2 decisive engagements:

- 32 page images, `livermore-p{N}-image-v1` for printed pp. 77, 101, 104, 109, 110 and 113–139
  (Internet Archive page index n(N+11), checked against the item's page-number map and each image
  header; downscaled with `sips -Z 1600`, as in v1);
- `livermore-transcription-v2`, which reproduces every section of `livermore-transcription-v1`
  byte for byte and adds one section per new page. Wilson's Creek, Pea Ridge and Prairie Grove
  are printed on pages that already had v1 sections without those entries, so they are added as
  `p78-supplement`, `p79-supplement` and `p95-supplement`.

34 entries match 44 engagements; the match table is recorded with the v2 strength ledger. Figures
are transcribed as printed, including fractions whose arithmetic does not agree with the totals
(Deep Bottom, Fort Wagner). Summary Tables A and B (pp.140–142) are not registered, as in v1. The
v1 transcription and ledger are unchanged.

## Carolinas Campaign first pass (cohort v2), 2026-09-25

The [first pass](research/carolinas-first-pass-v1.md) adds **23 records**:

- five NPS HTML/text pairs;
- Official Records Series I, Volume XLVII Part 1 (`warofrebellion471unit`): catalog metadata and
  full OCR; the imprint year is illegible in OCR and left null;
- ten report and return selections, including the compiled Union casualty return, used as the
  single targeted follow-up for three records;
- one new Cox selection, reusing the registered *March to the Sea* OCR.

No model inputs are changed.

## Price's Missouri Expedition, Mobile Bay, Mobile and Wilson's Raid first passes (cohort v2), 2026-09-25

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

## Bermuda Hundred and Richmond-Petersburg first passes (cohort v2), 2026-09-25

The first passes for [Bermuda Hundred](research/bermuda-hundred-first-pass-v1.md) and
[Richmond-Petersburg](research/petersburg-first-pass-v1.md) add **70 records**:

- twenty-four NPS HTML/text pairs;
- two Humphreys selections, reusing the registered *Virginia Campaign* OCR;
- Official Records Series I, Volumes XL, XLII and XLVI, Part 1 of each: catalog metadata and full
  OCR;
- fourteen report selections from Volumes XXXVI (Part 2), XL, XLII and XLVI.

Meade's November 1, 1864 report stays in its Overland group. Lee's dispatches across three
volumes share one group. No model inputs are changed.

## Red River and Camden first passes (cohort v2), 2026-09-25

The first passes for the [Red River Campaign](research/red-river-first-pass-v1.md) and the
[Camden Expedition](research/camden-first-pass-v1.md) add **34 records**:

- twelve NPS HTML/text pairs;
- Irwin, *History of the Nineteenth Army Corps* (1892), and Britton, *The Civil War on the Border*,
  volume II (1899): catalog metadata, full OCR and one selection each;
- Official Records Series I, Volume XXXIV Part 1: catalog metadata, full OCR, and Taylor's and
  Price's report selections.

No Scribner volume covers either campaign. No model inputs are changed.

## Franklin-Nashville and Savannah first passes (cohort v2), 2026-09-25

The first passes for [Franklin-Nashville](research/franklin-nashville-first-pass-v1.md) and
[Savannah](research/savannah-first-pass-v1.md) add **51 records**:

- thirteen NPS HTML/text pairs;
- Cox, *The March to the Sea; Franklin and Nashville* (1882): catalog metadata, full OCR and two
  selections;
- Official Records Series I, Volumes XXXIX Part 1, XLIV and XLV Part 1: catalog metadata and full
  OCR for each;
- fifteen report selections.

No model inputs are changed.

## Atlanta Campaign first pass (cohort v2), 2026-09-25

The [first pass](research/atlanta-first-pass-v1.md) adds **47 records**:

- sixteen NPS HTML/text pairs;
- Cox, *Atlanta* (1882): catalog metadata, full OCR and one selection;
- Official Records Series I, Volume XXXVIII, Parts 2 and 3: catalog metadata and full OCR for
  each;
- eight report selections: Johnston, Hood, Cleburne, Logan, Hardee, Schofield, Steedman and
  Kilpatrick.

The registry is now **736 entries / 715 raw paths**, preserving the previous **689/668**. No model
inputs are changed.

## Early's Raid and Sheridan's Valley first passes (cohort v2), 2026-09-25

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

## Overland Campaign first pass (cohort v2), 2026-09-25

The [first pass](research/overland-first-pass-v1.md) adds **34 records**:

- eleven NPS HTML/text pairs;
- Humphreys, *The Virginia Campaign of '64 and '65* (1883): catalog metadata, full OCR and one
  selection;
- Official Records Series I, Volume XXXVI, Parts 1 and 2: catalog metadata and full OCR for each;
- five report selections: Meade, Sheridan and Hampton from Part 1, and Butler and Wild from Part 2.

The registry is now **643 entries / 622 raw paths**, preserving the previous **609/588**. No model
inputs are changed.

## Best-estimate ledger, 2026-09-25

One record is added: `livermore-transcription-v1`, a manual transcription of the Livermore
entry lines and derivation notes, made from the 25 registered page images, one section per
printed page. It is the text cited for Livermore figures, because the OCR merges note markers
into numbers. The registry is now **609 entries / 588 raw paths**, preserving the previous
**608/587**. No model inputs are changed.

## Reported-strength scoping, 2026-09-25

The [scoping memo](research/reported-strength-scoping-v1.md) adds **27 records**: Livermore's
*Numbers and Losses* (1901) catalog metadata, full OCR and 25 downscaled page images of
printed pp.78–107 (Internet Archive `numberslosses00liverich`). Figures were read from the
images because the OCR merges note markers into numbers. The registry is now **608 entries /
587 raw paths**, preserving the previous **581/560**. No model inputs are changed.

## Operations about Dandridge review correction, 2026-09-25

One `metadata_only` revision (DAN-R4) supersedes `or32-1-longstreet-dandridge-selections-v1`
with `-v2`, removing Lawton's indorsement from its author and dependency note because the
selected range ends before it. Raw files, hashes and ranges are unchanged; the registry
is now **581 entries / 560 raw paths**.

## Operations about Dandridge first pass, 2026-09-25

The [three-record memo](research/dandridge-first-pass-v1.md) adds **12 records**, bringing
the registry to **580 entries / 560 raw paths**, preserving the previous **568/548**. Three
NPS battle HTML/text pairs remain in the NPS/CWSAC family. Official Records Series I
Volume XXXII Part 1 (Internet Archive `warofrebellion321unit`) is pinned with catalog
metadata, full OCR and Sturgis and Longstreet selections; new Sturgis and Martin
selections reuse `or31-1-illinois-ocr-v1`. Character ranges and whitespace-only
normalization reproduce all sections. No model inputs are changed.

## Mine Run Campaign first pass, 2026-09-25

The [one-record memo](research/mine-run-first-pass-v1.md) adds **4 records**, bringing the
registry to **568 entries / 548 raw paths**, preserving the previous **564/544**. One NPS
battle HTML/text pair remains in the NPS/CWSAC family. A new Humphreys Chapter III
selection reuses `humphreys-ocr-v2`, and a new Lee selection reuses
`or29-1-illinois-ocr-v1`. Character ranges and whitespace-only normalization reproduce
all sections. No model inputs are changed.

## Chattanooga-Ringgold Campaign first pass, 2026-09-25

The [two-record memo](research/chattanooga-ringgold-first-pass-v1.md) adds **9 records**,
bringing the registry to **564 entries / 544 raw paths**, preserving the previous
**555/535**. Two NPS battle HTML/text pairs remain in the NPS/CWSAC family. Official
Records Series I Volume XXXI Part 2 (Internet Archive `warofrebellion312unit`) is pinned
with catalog metadata, full OCR and Bragg and Cleburne selections; a new Cist selection
reuses `cist-cumberland-ocr-v1`. Character ranges and whitespace-only normalization
reproduce all sections. No model inputs are changed.

## Knoxville Campaign first pass, 2026-09-25

The [three-record memo](research/knoxville-first-pass-v1.md) adds **9 records**, bringing
the registry to **555 entries / 535 raw paths**, preserving the previous **546/526**. Three
NPS battle HTML/text pairs remain in the NPS/CWSAC family. Burnside, Longstreet and Parke
selections reuse `or31-1-illinois-ocr-v1`. Character ranges and whitespace-only
normalization reproduce all sections. No model inputs are changed.

## Memphis & Charleston Railroad review correction, 2026-09-25

One `metadata_only` revision (MC-04) supersedes `or31-1-chalmers-collierville-selections-v1`
with `-v2`, correcting its inspection note about McCulloch's and Slemons's reports. Raw
files, hashes and ranges are unchanged; the registry is now **546 entries / 526 raw
paths**.

## Averell's Raid first pass, 2026-09-25

The [one-record memo](research/averell-raid-first-pass-v1.md) adds **4 records**, bringing
the registry to **545 entries / 526 raw paths**, preserving the previous **541/522**. One
NPS battle HTML/text pair remains in the NPS/CWSAC family. Averell and Echols selections
reuse `or29-1-illinois-ocr-v1`. Character ranges and whitespace-only normalization
reproduce all sections. No model inputs are changed.

## Memphis & Charleston Railroad first pass, 2026-09-25

The [one-record memo](research/memphis-charleston-first-pass-v1.md) adds **4 records**,
bringing the registry to **541 entries / 522 raw paths**, preserving the previous
**537/518**. One NPS battle HTML/text pair remains in the NPS/CWSAC family. Hatch and
Chalmers selections reuse `or31-1-illinois-ocr-v1`. Character ranges and whitespace-only
normalization reproduce all sections. No model inputs are changed.

## Reopening the Tennessee River first pass, 2026-09-25

The [one-record memo](research/reopening-tennessee-first-pass-v1.md) adds **6 records**,
bringing the registry to **537 entries / 518 raw paths**, preserving the previous
**531/512**. One NPS battle HTML/text pair remains in the NPS/CWSAC family. Official
Records Series I Volume XXXI Part 1 (Internet Archive `warofrebellion311unit`) is pinned
with catalog metadata, full OCR and a Bratton selection; a new Cist selection reuses
`cist-cumberland-ocr-v1`. Character ranges and whitespace-only normalization reproduce
all sections. No model inputs are changed.

## Bristoe Campaign first pass, 2026-09-25

The [five-record memo](research/bristoe-first-pass-v1.md) adds **16 records**, bringing
the registry to **531 entries / 512 raw paths**, preserving the previous **515/496**. Five
NPS battle HTML/text pairs remain in the NPS/CWSAC family. Official Records Series I
Volume XXIX Part 1 (Internet Archive `warofrebellion291unit`) is pinned with catalog
metadata, full OCR and Stuart, Hill and Lee selections; a new Humphreys selection reuses
`humphreys-ocr-v2`. Character ranges and whitespace-only normalization reproduce all
sections. No model inputs are changed.

## Morgan's Raid review correction, 2026-09-25

Three `metadata_only` revisions supersede `or23-1-burnside-morgan-raid-selections-v1`,
`or23-1-hobson-morgan-raid-selections-v1` and `or23-1-shackelford-morgan-raid-selections-v1`
with `-v2`, carrying the TL-R7 imprint correction and reparenting them to
`or23-1-illinois-ocr-v2`. Raw files, hashes and ranges are unchanged; the registry is now
**515 entries / 496 raw paths**.

## East Tennessee Campaign first pass, 2026-09-25

The [two-record memo](research/east-tennessee-first-pass-v1.md) adds **8 records**, bringing
the registry to **512 entries / 496 raw paths**, preserving the previous **504/488**. Two
NPS battle HTML/text pairs remain in the NPS/CWSAC family. Foster, Samuel Jones, Burnside
and Williams selections reuse `or30-2-illinois-ocr-v1`. Character ranges and
whitespace-only normalization reproduce all sections. No model inputs are changed.

## Chickamauga Campaign first pass, 2026-09-25

The [three-record memo](research/chickamauga-first-pass-v1.md) adds **12 records**, bringing
the registry to **504 entries / 488 raw paths**, preserving the previous **492/476**. Three
NPS battle HTML/text pairs remain in the NPS/CWSAC family. Official Records Series I
Volume XXX Part 2 (Internet Archive `warofrebellion302unit`) is pinned with catalog
metadata, full OCR and Hill, Hindman and Bragg selections; a new Cist selection reuses
`cist-cumberland-ocr-v1`. Character ranges and whitespace-only normalization reproduce
all sections. No model inputs are changed.

## Gettysburg review correction, 2026-09-25

Three `metadata_only` revisions (GB-R11) supersede `ia-humphreys-metadata-v1`,
`humphreys-ocr-v1` and `humphreys-gettysburg-rapidan-selections-v1` with `-v2`,
replacing an unsupported chief-of-staff start date and an anachronistic dependence on the
printed Official Records. Raw files, hashes and ranges are unchanged; the registry is now
**492 entries / 476 raw paths**.

## Tullahoma review correction, 2026-09-25

Three `metadata_only` revisions (TL-R7) supersede `ia-or23-1-illinois-metadata-v1`,
`or23-1-illinois-ocr-v1` and `or23-1-bate-hoovers-gap-selections-v1` with `-v2`,
recording the OCR imprint year 1889. Raw files, hashes and ranges are unchanged; the
registry is now **489 entries / 476 raw paths**. The three Morgan's Raid OR selections
still carry the v1 edition text pending that campaign's review.

## Morgan's Raid first pass, 2026-09-25

The [three-record memo](research/morgans-raid-first-pass-v1.md) adds **12 records**, bringing
the registry to **486 entries / 476 raw paths**, preserving the previous **474/464**. Three
NPS battle HTML/text pairs remain in the NPS/CWSAC family. Duke's *History of Morgan's
Cavalry* (Internet Archive `historyofmorgans00duke`) is pinned with catalog metadata, full
OCR and a selection; Burnside, Hobson and Shackelford selections reuse
`or23-1-illinois-ocr-v1`. Character ranges and whitespace-only normalization reproduce
all sections. No model inputs are changed.

## Tullahoma Campaign first pass, 2026-09-25

The [one-record memo](research/tullahoma-first-pass-v1.md) adds **6 records**, bringing
the registry to **474 entries / 464 raw paths**, preserving the previous **468/458**. One
NPS battle HTML/text pair remains in the NPS/CWSAC family. Official Records Series I
Volume XXIII Part 1 (Internet Archive `warofrebellion231unit`) is pinned with catalog
metadata, full OCR and a Bate selection; a new Cist selection reuses
`cist-cumberland-ocr-v1`. Character ranges and whitespace-only normalization reproduce
all sections. No model inputs are changed.

## Gettysburg Campaign first pass, 2026-09-25

The [ten-record memo](research/gettysburg-first-pass-v1.md) adds **28 records**,
bringing the registry to **468 entries / 458 raw paths**, preserving the previous
**440/430**. Ten NPS battle HTML/text pairs remain in the NPS/CWSAC family. Official
Records Series I Volume XXVII Part 2 (Internet Archive `warofrebellion272unit`) is pinned
with catalog metadata, full OCR, and Lee and Stuart selections, each its own independence
group. Humphreys' *From Gettysburg to the Rapidan* (`cu31924030917177`) is pinned with
metadata, OCR and one selection, and a new Doubleday selection reuses `doubleday-ocr-v1`.
Character ranges and whitespace-only normalization reproduce all sections. No model
inputs are changed.

## Chancellorsville review correction, 2026-09-25

One `metadata_only` revision (CV-R1/R2) supersedes `doubleday-chancellorsville-selections-v1`
with `-v2`, correcting its inspection note's page statements. Raw files, hashes and
ranges are unchanged; the registry is now **440 entries / 430 raw paths**.

## Grant's Operations Against Vicksburg review correction, 2026-09-25

Six `metadata_only` revisions (VB63-R9) supersede `ia-or24-2-illinois-metadata-v1`,
`or24-2-illinois-ocr-v1` and the Dennis, McCulloch, Reid and Walker selections with
`-v2` records whose edition quotes the garbled imprint in full ("1 SS  9.", outside
the selected title ranges). Raw files, hashes and ranges are unchanged; the registry
is now **439 entries / 430 raw paths**.

## Streight's Raid first pass, 2026-09-25

The [one-record memo](research/streights-raid-first-pass-v1.md) adds **4 records**,
bringing the registry to **433 entries / 430 raw paths**, preserving the previous
**429/426**. One NPS battle HTML/text pair remains in the NPS/CWSAC family. Two new
selections reuse pinned parents: Cist (`cist-cumberland-ocr-v1`) and Jordan and Pryor
Chapter IX (`jordan-pryor-forrest-ocr-v1`). Character ranges and whitespace-only
normalization reproduce all sections. No model inputs are changed.

## Chancellorsville Campaign first pass, 2026-09-25

The [three-record memo](research/chancellorsville-first-pass-v1.md) adds **12 records**,
bringing the registry to **429 entries / 426 raw paths**, preserving the previous
**417/414**. Three NPS battle HTML/text pairs remain in the NPS/CWSAC family. Doubleday's
*Chancellorsville and Gettysburg* (Internet Archive `chancellorsville00doubuoft`) is
pinned with catalog metadata, full OCR and one selection. Three report selections (Lee,
Sedgwick, Early) reuse the pinned `or25-1-illinois-ocr-v1`, each its own independence
group. Character ranges and whitespace-only normalization reproduce all sections. No
model inputs are changed.

## Grant's Operations Against Vicksburg (1863) first pass, 2026-09-25

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

## Cavalry Operations along the Rappahannock first pass, 2026-09-25

The [one-record memo](research/rappahannock-cavalry-first-pass-v1.md) adds **6 records**,
bringing the registry to **379 entries / 376 raw paths**, preserving the previous
**373/370**. One NPS battle HTML/text pair remains in the NPS/CWSAC family. The Official
Records Series I Volume XXV Part 1 catalog metadata and full OCR
(`or25-1-illinois-ocr-v1`, Internet Archive `warofrebellion251unit`) are pinned as a
shared container, with two selections: Averell's report and Fitz Lee's report, letter
and orders, each its own independence group. Character ranges and whitespace-only
normalization reproduce all sections. No model inputs are changed.

## Longstreet's Tidewater Operations first pass, 2026-09-25

The [four-record memo](research/tidewater-first-pass-v1.md) adds **12 records**,
bringing the registry to **373 entries / 370 raw paths**, preserving the previous
**361/358**. Four NPS battle HTML/text pairs remain in the NPS/CWSAC family. Four new
selections reuse the pinned `or18-illinois-ocr-v1` parent, one per reporting commander
(Foster, D. H. Hill, Peck and French with Longstreet's indorsement), each its own
independence group. Character ranges and whitespace-only normalization reproduce all
sections. No model inputs are changed.

## Middle Tennessee first pass, 2026-09-25

The [five-record memo](research/middle-tennessee-first-pass-v1.md) adds **12 records**,
bringing the registry to **361 entries / 358 raw paths**, preserving the previous
**349/346**. Five NPS battle HTML/text pairs remain in the NPS/CWSAC family. Two new
selections reuse pinned parents: Cist Chapter IX (`cist-cumberland-ocr-v1`) and Jordan
and Pryor Chapter VIII (`jordan-pryor-forrest-ocr-v1`). Character ranges and
whitespace-only normalization reproduce all sections. No model inputs are changed.

## Operations Against Vicksburg (1862–63) first pass, 2026-09-24

The [two-record memo](research/vicksburg-1862-first-pass-v1.md) adds **5 records**,
bringing the registry to **349 entries / 346 raw paths**, preserving the previous
**344/341**. Two NPS battle HTML/text pairs remain in the NPS/CWSAC family. One new
Greene selection reuses the pinned `greene-mississippi-ocr-v1` parent and holds the
title/preface and two Chapter III passages. Character ranges and whitespace-only
normalization reproduce all sections. No model inputs are changed.

## Forrest West Tennessee first pass, 2026-09-24

The [two-record memo](research/forrest-west-tennessee-first-pass-v1.md) adds **7 records**,
bringing the registry to **344 entries / 341 raw paths**, preserving the previous
**337/334**. Two NPS battle HTML/text pairs remain in the NPS/CWSAC family. Jordan and
Pryor's 1868 *Campaigns of Lieut.-Gen. N. B. Forrest* adds a `jordan-pryor-forrest-1868`
family: public catalog metadata, full OCR (Google-digitized Harvard copy) and one
selection holding the title/preface and three Chapter VII passages. Forrest's prefatory
note accepts responsibility for most of the narrative, so the family is not
independent of him. Character ranges and whitespace-only normalization reproduce all
sections. No model inputs are changed.

## Goldsboro first pass, 2026-09-24

The [three-record memo](research/goldsboro-first-pass-v1.md) adds **10 records**,
bringing the registry to **337 entries / 334 raw paths**, preserving the previous
**327/324**. Three NPS battle HTML/text pairs remain in the NPS/CWSAC family. Official
Records Series I, Volume XVIII (Illinois scan) adds catalog metadata and full OCR in
an `or-series-i-volume-xviii` container, and two sectioned report selections:
Foster's three reports (`foster-goldsborough-reports`) and G. W. Smith's five
(`gw-smith-goldsborough-reports`), with section-specific document dates. OCR errors
are retained exactly; the garbled compiler casualty return was not used. No model
inputs are changed.

## Fredericksburg first pass, 2026-09-24

The [one-record memo](research/fredericksburg-first-pass-v1.md) adds **3 records**, bringing
the registry to **327 entries / 324 raw paths**, preserving the previous **324/321**.
One NPS battle HTML/text pair remains in the NPS/CWSAC family. One new Palfrey
selection derivative reuses the pinned `palfrey-antietam-ocr-v1` parent and holds the
title/preface and seven bounded Chapter IV passages; its dependency note omits the
unsupported claim that Palfrey served in the campaign. Character ranges and
whitespace-only normalization reproduce all sections. No model inputs are changed.

## Stones River first pass, 2026-09-24

The [two-record memo](research/stones-river-first-pass-v1.md) adds **5 records**, bringing
the registry to **324 entries / 321 raw paths**, preserving the previous **319/316**.
Two NPS battle HTML/text pairs remain in the NPS/CWSAC family. One new Cist selection
derivative reuses the pinned `cist-cumberland-ocr-v1` parent; its metadata and OCR
are unchanged, and it holds the title/preface and five bounded passages. Character
ranges and whitespace-only normalization reproduce all sections. Cist is an
interested retrospective history by Rosecrans's staff officer; quoted reports are
not separately inspected originals. No model inputs are changed.

## Iuka and Corinth first pass, 2026-09-24

The [three-record memo](research/iuka-corinth-first-pass-v1.md) adds **9 records**,
bringing the registry to **319 entries / 316 raw paths**, preserving the previous
**310/307**. Three NPS battle HTML/text pairs remain in the NPS/CWSAC family. Francis
Vinton Greene's 1882 *The Mississippi* adds a `greene-mississippi-1882` family: public
catalog metadata, full OCR and one selection derivative holding the title/preface
and two bounded Chapter II passages. Character ranges and whitespace-only
normalization reproduce all sections. Greene was not a participant and founded the
book on the Official Records; quoted reports are not separately inspected
originals. No model inputs are changed.

## Maryland first pass, 2026-09-24

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

## Northern Virginia first pass, 2026-09-24

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

## Heartland Offensive first pass, 2026-09-24

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

## Valley first pass, 2026-09-20

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

## Peninsula first pass, 2026-09-20

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

## New Madrid/Memphis first pass, 2026-09-20

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

## Burnside campaign first pass, 2026-09-20

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

## Eastern Kentucky first pass, 2026-09-20

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

## Hancock first pass, 2026-09-20

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

## Cockpit Point first pass, 2026-09-20

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

## Bounded river-campaign first pass, 2026-09-20

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


## Shiloh contact and location packet, 2026-09-20

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

## Shiloh enrichment, 2026-09-20

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

## Confederate return follow-up, 2026-09-20

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

## Union availability follow-up, 2026-09-20

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

## Army of the Ohio reinforcement follow-up, 2026-09-20

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

## Reviewed metadata corrections, 2026-09-20

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

## Upstream force tables for strength ledger v3, 2026-10-06

Eleven files from Arnold's *American Civil War Battle Data* at the already-pinned commit `3a6020d`
were fetched explicitly and pinned unmodified in `data/raw/arnold-tables-v1/`, with SHA-256 in
`data/sources.json` (license CC-BY-4.0 per the pinned package metadata):

- force tables:
  - `arnold-cws2-forces` and `arnold-cwss-forces`, in the `nps-cwsac` group;
  - `arnold-bodart1908-forces` and `-battles`, in `bodart-kriegs-lexikon-1908`;
  - `arnold-clodfelter-forces` and `-battles`, in `clodfelter-warfare-armed-conflicts-2008`;
  - `arnold-livermore-forces` and `-battles`, in `livermore-numbers-losses`, used only to cross-check
    the project's Livermore transcription;
- Arnold's concordances, registered as JSON: `arnold-bodart1908-to-cwsac`,
  `arnold-clodfelter-to-cwsac` and `arnold-livermore-to-cwsac`.

Each registry entry records the upstream schema's population definition and the dependence caveat
(CWS2 is NPS's own update of the CWSAC report; Clodfelter likely draws on Livermore and NPS). Use is
limited to the v3 ledger's grade D fill ([addendum](ledgers-v3.md)).

## Bodart's Kriegs-Lexikon for the Napoleonic frame, 2026-10-06

237 records pinned in `data/raw/bodart-1908-v1/`, all in the `bodart-kriegs-lexikon-1908` group:

- from Internet Archive item `bub_gb_A0kNAAAAYAAJ`:
  - the ABBYY OCR text (`bodart-1908-ocr-v1`) and item metadata (`bodart-1908-ia-metadata-v1`);
  - the page-number map (`bodart-1908-page-numbers-v1`);
  - IA's OCR page index and search text, gzip-compressed (`bodart-1908-ocr-pageindex-v1`,
    `bodart-1908-ocr-searchtext-v1`);
  - 228 page images, `bodart-1908-p{NNN}-image-v1`, for pp. 45–48 and 267–490, downscaled to 1600 px;
- three page images of the second copy `bub_gb_Eo4DAAAAYAAJ`, pp. 337–339
  (`bodart-1908-eo4d-p{337,338,339}-image-v1`), where the first scan hides an edge;
- the sectioned manual transcription `bodart-1908-transcription-v1`. It has one section per printed
  page and an editorial `transcription-note` section. Its sections have no document dates, as the work
  is a 1908 compilation.

Rights: the Internet Archive marks both items with the Public Domain Mark 1.0. Use: the frozen
[Napoleonic frame](napoleonic-frame.md). Arnold's machine-readable Bodart table, registered for
ledger v3, is a separate derived file and is not used for the frame. No model inputs are changed.


## Alombert and Colin and Krauss for the 1805 first pass, 2026-10-17

73 records pinned in `data/raw/napoleonic-third-coalition-1805-v1/` for batch 1a of the
`third-coalition 1805` first pass (Wertingen, Günzburg and Haslach):

- **Alombert and Colin**, *La campagne de 1805 en Allemagne* (Section historique de l'État-major
  de l'armée, 1902–1908), group `alombert-colin-1805`. The French official history, which prints
  French returns, orders, reports and journals.
  - The Internet Archive OCR of t. II (`alombert-colin-t2-ocr-v1`, item
    `alombert-la-campagne-de-1805-en-allemagne-v-2`) and of t. III vol. 1
    (`alombert-colin-t3a-ocr-v1`, item `alombert-la-campagne-de-1805-en-allemagne-v-3-pt-1`).
  - The sectioned selection `alombert-colin-t3a-selections-v1`, with ten sections:
    `wertingen-intro`, `gunzburg-intro`, `haslach-intro`, `austrian-command`, `orders-8-oct`,
    `murat-report-8-oct`, `belliard-and-klein-8-oct`, `orders-9-oct`, `malher-report-10-oct` and
    `haslach-documents`.
  - 22 page images, each with a transcription of its figures: t. II pp. 162, 163, 165 and 166 (the
    corps returns at the crossing of the Rhine), and t. III vol. 1 pp. 29, 33–35, 47, 49, 50, 52–54,
    313, 318, 329, 507, 510, 511, 515 and 516.
- **Krauss**, *1805. Der Feldzug von Ulm* (Vienna, 1912), group `krauss-feldzug-ulm-1912`. An
  Austrian general's history from the Kriegsarchiv files, which draws on Alombert and Colin for
  French orders and movements.
  - The OCR (`krauss-1912-ocr-v1`, item `1805ieachtzehnhu00krau`).
  - The selection `krauss-1912-selections-v1`, with seven sections: `austrian-command`,
    `wertingen-combat`, `wertingen-strength-and-mission`, `gunzburg-austrians-9-oct`,
    `gunzburg-combat`, `austrians-10-11-oct` and `haslach-combat`.
  - 12 page images with figure transcriptions: pp. 341, 342, 366, 368, 369, 371, 377, 387, 402,
    404, 405 and 409.

The page images are single pages downscaled to 1600 px. Each transcription holds only the
sentences that carry figures, read from the image rather than the OCR. Each selection records its
parent's character ranges, and the source check rebuilds it from them. The OCR of t. III vol. 2
was fetched but is not registered, as it has not yet been read.

Rights: the Internet Archive marks the Alombert and Colin items with the Public Domain Mark 1.0.
Krauss was published in 1912; the catalogue gives the author's dates as 1862–1938. Use: the drafts
for B363a–c. No model inputs are changed.


## Alombert and Colin t. III vol. 2 and Krauss for the Ulm phase of 1805, 2026-10-17

100 records pinned in `data/raw/napoleonic-third-coalition-1805-v1/` for batch 1b of the
`third-coalition 1805` first pass (the Ulm phase, Parsdorf to Eschenau):

- **Alombert and Colin**, group `alombert-colin-1805` (see the entry above).
  - The Internet Archive OCR of t. III vol. 2 (`alombert-colin-t3b-ocr-v1`, item
    `alombert-la-campagne-de-1805-en-allemagne-v-3-pt-2`), fetched in batch 1a and held back until
    read. It prints the reports and journals of the Ulm phase and of Murat's pursuit.
  - The sectioned selection `alombert-colin-t3b-selections-v1`, with nine sections:
    `parsdorf-12-oct`, `elchingen-loison-report`, `elchingen-hermann-note`, `memmingen-soult`,
    `ulm-capitulation`, `herbrechtingen-16-oct`, `neresheim-17-oct`, `trochtelfingen-18-oct` and
    `eschenau-20-oct`.
  - The selection `alombert-colin-t3a-ulm-selections-v1` from the t. III vol. 1 OCR, with seven
    sections: `parsdorf-intro`, `elchingen-intro`, `memmingen-intro`, `ulm-investment-intro`,
    `pursuit-intro`, `ulm-council-intro` and `ulm-prisoners-intro`.
  - 30 page images, each with a transcription of its figures: t. II p. 161 (the 4th corps'
    return at the crossing of the Rhine); t. III vol. 1 pp. 67, 68, 75, 80, 83, 89, 95, 97, 102,
    103, 217 and 229; t. III vol. 2 pp. 661–663, 730, 750, 771, 773, 774, 1199, 1201, 1214, 1217,
    1218, 1222, 1224, 1253 and 1255.
- **Krauss**, group `krauss-feldzug-ulm-1912` (see the entry above).
  - The selection `krauss-1912-ulm-selections-v1` from the registered OCR, with seven sections:
    `kienmayer-12-oct`, `munich-12-oct`, `parsdorf-memmingen-13-oct`, `memmingen-elchingen`,
    `ulm-capitulation`, `werneck-pursuit` and `ulm-surrender`.
  - 18 page images with figure transcriptions: pp. 449, 454–457, 461, 470, 473, 475, 483, 484,
    486–488, 492, 495, 498 and 499.

The Internet Archive serves the t. II and t. III vol. 2 page images at 794 × 1123 pixels, so
resizing them to 1600 px on the longest side enlarged them; this adds no detail. The t. III vol. 1
and Krauss images were served larger and downscaled. Each image record's `snapshot_transform` says
which, and the `rights` text of the t. III vol. 2 records and of the t. II p. 161 pair says the
same. As in batch 1a, each transcription holds the passages that carry figures (and, where its
note says so, a few sentences without them), read from the image rather than the OCR; p. 161's
holds the whole return. Each selection records its parent's character ranges.

**Erratum to the batch 1a entry.** The four t. II page images registered in batch 1a
(`alombert-colin-t2-p162-image-v1`, `-p163-`, `-p165-` and `-p166-`) were also served at
794 × 1123 pixels and enlarged, not downscaled. Their `snapshot_transform`, the `rights` text they
share with `alombert-colin-t2-ocr-v1` and the entry's sentence "The page images are single pages
downscaled to 1600 px" are wrong on this point. The committed records stay as pinned; the files,
hashes and transcriptions are unaffected.

Rights: as in the entry above. Use: the drafts for B364a–d, B365a, B365b, B365d and B366a. No
model inputs are changed.


## Koch and Angeli for the Italian engagements of 1805, 2026-10-17

62 records pinned in `data/raw/napoleonic-third-coalition-1805-v1/` for batch 1c of the
`third-coalition 1805` first pass (Verona, Caldiero, Pojano and Castelfranco):

- **Koch**, *Mémoires de Masséna*, t. V (Paris, 1850), group `koch-memoires-massena`. A French
  history of Masséna's campaigns, written by its title page from the papers he left and from the
  Dépôt de la guerre and the Dépôt des fortifications. It prints French documents as pièces
  justificatives.
  - The Internet Archive OCR (`koch-massena-t5-ocr-v1`, item `mmoiresdemassen00massgoog`), of a New
    York Public Library copy digitised by Google.
  - The sectioned selection `koch-massena-t5-selections-v1`, with six sections: `verona-18-oct`,
    `caldiero-prelude`, `caldiero-29-oct`, `caldiero-30-oct-to-2-nov`, `castelfranco` and `errata`.
  - 18 page images, each with a transcription: pp. 80, 83, 84, 89, 94, 97, 103–105, 108, 109, 129
    and 130 of the narrative; pp. 368–370, pièce justificative VI, the army's order of battle of
    18 October 1805; and pp. 375 and 376, pièce justificative VII, General Duhesme's report.
- **Angeli**, *Erzherzog Carl von Österreich als Feldherr und Heeresorganisator*, Bd. III (Vienna and
  Leipzig, 1897), group `angeli-erzherzog-carl-1897`. An Austrian history written from the
  Kriegsarchiv files on commission from the Archduke's sons and grandsons; its numbered source notes
  cite the files.
  - The OCR (`angeli-1897-bd3-ocr-v1`, item `erzherzogcarlvo02angegoog`), of a University of Michigan
    copy digitised by Google.
  - The selection `angeli-1897-bd3-selections-v1`, with nine sections: `verona-18-oct`,
    `caldiero-position`, `caldiero-29-oct`, `caldiero-30-oct`, `caldiero-31-oct`,
    `retreat-and-pojano`, `rohan-march`, `source-notes-52-76` and `source-note-95`.
  - 11 page images with transcriptions: pp. 73, 74 (the first part of the table of the Austrian
    army's positions on 13 October), 88, 92, 93, 115, 134, 135, 149, 150 and 183.

**Dependence.** Angeli's source notes for all four actions cite pages of Koch's t. V (notes 52, 62,
63, 65, 66, 68, 76 and 95; page numbers read in the OCR), and for Castelfranco Koch is the only
source he cites in the passages read. Angeli is therefore not independent of Koch for these actions,
and each parent's `dependency_note` says so. Bodart's figures match or round Angeli's at Caldiero and
Pojano and are not treated as independent of them there; the Angeli record lists the figures of
Bodart's that are not Angeli's.

The page images are single pages, served larger than 1600 px and downscaled. Unlike batches 1a and
1b, each transcription holds the whole page or a continuous passage of it, less any sentences its
note names, read from the image rather than the OCR; tables are transcribed row by row. Each
selection records its parent's character ranges. Both OCRs keep Google's front-matter notice, which
asks for non-commercial use and for the attribution watermark to be kept; each record's `rights`
text says so. The Internet Archive holds another copy of Angeli's Bd. III
(`erzherzogcarlvo03carlgoog`, the item named in the pass's plan), which was not used.

Rights: Koch was published in 1850, and Angeli in 1897 (the catalogue gives his dates as
1829–1904); the Internet Archive marks both items NOT_IN_COPYRIGHT. Use: the drafts for B365c,
B367a, B367b and B369b. No model inputs are changed. The registry now holds 2,084 records.


## Moriggl and Victoires et conquêtes for the Tyrol and Vorarlberg, 2026-10-17

52 records pinned in `data/raw/napoleonic-third-coalition-1805-v1/` for batch 1d of the
`third-coalition 1805` first pass (Scharnitz and Dornbirn):

- **Moriggl**, *Der Feldzug des Jahres 1805 und seine Folgen für Oesterreich überhaupt und für
  Tirol insbesonders* (Innsbruck, 1861), group `moriggl-feldzug-1805-tirol`. The Tyrolean account
  by Alois Moriggl, early-mass priest at Zirl, begun as a monograph on the French invasion at the
  Leutasch and Scharnitz. His preface lists unprinted sources, among them Swinburne's papers, the
  Seefeld diary, Dipauli's notes and statements of surviving defenders, and printed ones, among
  them the *Oesterreichische militärische Zeitschrift* and the *Sammler*.
  - The Internet Archive OCR (`moriggl-1861-ocr-v1`, item `bub_gb_mz5BAAAAYAAJ`), of a Harvard
    College Library copy digitised by Google that binds Bände I–III with continuous pagination.
    The Fraktur OCR garbles many letters and page numbers.
  - The sectioned selection `moriggl-1861-selections-v1`, with nine sections: `source-list`,
    `scharnitz-orders-3-nov`, `archduke-orders-4-nov`, `scharnitz-2-3-nov`,
    `scharnitz-reinforcement-3-nov`, `scharnitz-assault-4-nov`, `leutasch-4-nov`, `seefeld-5-nov`
    and `vorarlberg-capitulation`. Within `leutasch-4-nov` the parent repeats pp. 348–349 once in
    a second, more garbled OCR; both copies are kept, and no quote is taken from the second.
  - 21 page images, each with a transcription: pp. 89, 92 and 93, from his order of battle of the
    Grande Armée at its crossing of the Rhine; pp. 300, 330, 331, 334–336, 339, 340, 347, 348 and
    363–365, for Scharnitz, the Leutasch and Seefeld; and pp. 434–438, for the Vorarlberg.
- ***Victoires, conquêtes, désastres, revers et guerres civiles des Français***, t. XV (Paris,
  1819), group `victoires-conquetes-1817`. The French compilation "by a society of soldiers and men
  of letters"; it names no sources in the passages read.
  - The OCR (`victoires-conquetes-t15-ocr-v1`, item `bub_gb_UNgLhuBKzUAC`), of a National Library
    of Naples copy digitised by Google.
  - The selection `victoires-conquetes-t15-selections-v1`, with two sections, `tyrol` and
    `vorarlberg`.
  - 3 page images with transcriptions: pp. 215, 216 and 219.

**Dependence.** The two are the sides' own accounts and share no source named in the passages
read. Moriggl quotes unnamed French reports for French losses, and *Victoires et conquêtes* may
draw on the bulletins of the Grande Armée, which was not checked. Bodart's 16 battalions, 4
squadrons and 15,000 men for Augereau's corps at Dornbirn match the total of Moriggl's order of
battle at the Rhine crossing, 16 battalions, 4 squadrons and 14,907 men; the passages read do not
show whether Bodart drew on Moriggl or on a common source.

The page images are single pages, served larger than 1600 px and downscaled. As in batch 1c, each
transcription holds the whole page or the passages its note names, read from the image; the order
of battle is transcribed one table row to a line. Each selection records its parent's character
ranges. Neither OCR keeps Google's front-matter notice, only the scanner's stamps. Before these
two were chosen, the planned families were checked: Angeli's Bd. III and Schönhals only summarise
the two actions, Alombert and Colin's t. IV gives Scharnitz one sentence, and the bulletins in the
*Correspondance* t. XI say too little; Ney's memoirs end at Ulm, and Mathieu Dumas's volumes for
1805 are not on the Internet Archive. Another Moriggl item (`bub_gb_8HpBAAAAcAAJ`), whose OCR has
none of the engagement names, was not used.

Rights: Moriggl was published in 1860–1861 and *Victoires et conquêtes* t. XV in 1819; the
Internet Archive marks both items with the Public Domain Mark 1.0. Use: the drafts for B368a and
B368d. No model inputs are changed. The registry now holds 2,136 records.


## Alombert and Colin t. IV and Schönhals for the Danube, 2026-10-17

46 records pinned in `data/raw/napoleonic-third-coalition-1805-v1/` for batch 1e of the
`third-coalition 1805` first pass (Mariazell and Dürnstein):

- **Alombert and Colin**, *La campagne de 1805 en Allemagne*, t. IV, "Saint-Pœlten et Krems"
  (Paris, 1908), group `alombert-colin-1805`, the family of tomes II and III already registered.
  The French General Staff's history of 25 October to 11 November 1805: an introduction that
  narrates each day, the documents of each day, and an appendix of situations.
  - The Internet Archive OCR (`alombert-colin-t4-ocr-v1`, item
    `alombert-la-campagne-de-1805-en-allemagne-v-4`), made with Tesseract 5.0.0 from a Princeton
    University copy digitised by Google.
  - The sectioned selection `alombert-colin-t4-selections-v1`, with six sections:
    `mariazell-7-nov`, `mariazell-8-nov`, `durnstein-10-nov`, `durnstein-11-nov`,
    `mariazell-3rd-corps-journal` and `mariazell-davout-report`.
  - 12 page images, each with a transcription: pp. 125, 142, 143, 154, 162 and 166 of the
    introduction; pp. 650 and 651, Davout's report of 9 November; pp. 711, 723 and 724, the list
    of the Grande Armée at 6 brumaire an XIV (28 October); and p. 769, the 6th corps' return of
    4 brumaire (26 October).
- **Schönhals**, *Der Krieg 1805 in Deutschland, nach österreichischen Originalquellen* (Vienna,
  1873), group `schoenhals-krieg-1805`. The Austrian account by Carl von Schönhals, written for an
  archive in 1831 by the editors' note (the OCR of the preface's signature reads 1821) and
  published from his manuscript by the editors of the *Österreichische militärische Zeitschrift*.
  - The OCR (`schoenhals-1873-ocr-v1`, item `derkriegindeuts00schgoog`), of a University of
    California copy digitised by Google.
  - The selection `schoenhals-1873-danube-selections-v1`, with two sections, `mariazell` and
    `durnstein`.
  - 9 page images with transcriptions: pp. 127–132, for Merveldt's march and Mariazell, and
    pp. 135–137, for Dürrenstein.

**Dependence.**

- t. IV cites Schönhals once, in a footnote on Austrian movements at the end of October. Its
  account of Merveldt's march to Neuhaus follows Schönhals's closely without citing him, so for
  Austrian-side statements at Mariazell the two may not be independent.
- For Dürrenstein, t. IV names its sources. On the French side they are a regimental colonel's
  letter, General Graindorge's report, the journal of Dupont's division and the officers' service
  notes, three of them cited to pages of Alombert's book on the combat (1897, not registered). On
  the allied side they are two partial Austrian eyewitness relations in the Vienna war archives
  and Danilewski's Russian relation. It also uses, with precautions, Colonel Talandier's narrative
  and the accounts derived from it, and Rozat's fragment. It identifies the account in *Victoires
  et conquêtes*, t. XV, registered in batch 1d, as Talandier's or written from his notes, so that
  account is not independent of t. IV's Talandier material here. It sets Kotzebue's account of
  1807 aside for the fighting.
- By its own footnote, Schönhals takes some details of Dürrenstein from Kotzebue. Its evening
  narrative follows, nearly sentence for sentence, the Austrian relation that t. IV quotes in
  translation on pp. 161–162, so the two are not independent for the evening. Its preface says
  that everything it has on the French army's operations comes from that army's bulletins.
- At Dürnstein, Bodart's 25,000 for side B equals Schönhals's 32,000 less the sixth column's 7000
  (our arithmetic). The passages read do not show that he reckoned so.

The page images are single pages, enlarged to 1600 pixels on the longest side. The Internet
Archive serves them at 794 x 1123 pixels (t. IV) and 804 x 1292 pixels (Schönhals). As in batches
1c and 1d, each transcription holds the whole page or the passages its note names, read from the
image, and tables are transcribed one row to a line. t. IV's OCR misreads many figures (on p. 166,
'488' for 155 and '4,600' for 1,600), so no figure is taken from it. Each selection records its
parent's character ranges. Schönhals's OCR keeps Google's front-matter notice; t. IV's keeps only
the scanner's stamps.

Rights: t. IV was published in 1908, and the Internet Archive marks it with the Public Domain
Mark 1.0. Schönhals was published in 1873; he died in 1857. The Internet Archive marks his book
NOT_IN_COPYRIGHT. Use: the drafts for B368b and B368c. No model inputs are changed. The registry
now holds 2,182 records.

## Völderndorff, and *Victoires et conquêtes* and Schönhals for Moravia, 2026-10-17

55 records pinned in `data/raw/napoleonic-third-coalition-1805-v1/` for batch 1f of the
`third-coalition 1805` first pass (Ober-Hollabrunn, Austerlitz and Steken):

- **Völderndorff**, *Kriegsgeschichte von Bayern unter König Maximilian Joseph I.*, erster Band
  (Munich, 1826), group `voelderndorff-kriegsgeschichte-bayern`, a new family. The history of the
  Bavarian army's wars by Eduard von Völderndorff und Waradein, a major of the Bavarian
  General-Quartiermeisterstab, who by his preface took up the work on higher orders. The preface
  names its sources: the archives; the commanders' official reports and their written and oral
  accounts, above all the Bavarian commanders', first among them the communications of Prince
  Eugène and of Field Marshal Prince Wrede; the published works of all the nations of Europe; and
  the author's own experience of the campaigns.
  - The OCR (`voelderndorff-1826-ocr-v1`, item `11748199bsb`), made with Tesseract 5.3.0 and
    German and Fraktur models from a Staatsbibliothek Bamberg copy digitised by the Bayerische
    Staatsbibliothek (`bsb11748199`). The title page was read on the page image n4, which is not
    registered.
  - The selection `voelderndorff-1826-selections-v1`, with two sections, `preface-sources` and
    `stecken`.
  - 6 page images with transcriptions: pp. 287, 292, 296, 297, 299 and 301, for the Bavarian corps
    from 27 November to the action of 5 December and its losses.
  - Other copies were found and not used: `bub_gb_r-hBAAAAcAAJ`, a Google scan whose OCR has no
    hit for Stecken or Iglau, and three other digitisations by the Bayerische Staatsbibliothek, of
    which only the metadata were read.
- ***Victoires et conquêtes***, t. XV (1819), group `victoires-conquetes-1817`, registered in
  batch 1d.
  - The selection `victoires-conquetes-t15-moravia-selections-v1`, with two sections,
    `hollabrunn` and `austerlitz`.
  - 10 page images with transcriptions: pp. 213 and 214, for Hollabrunn, and pp. 226, 227, 238,
    239, 266, 267, 268 and 271, for Austerlitz. A second transcription of p. 215, whose image batch
    1d registered, covers the end of the Hollabrunn pursuit at the top of the page.
- **Schönhals**, *Der Krieg 1805 in Deutschland* (1873), group `schoenhals-krieg-1805`, registered
  in batch 1e.
  - The selection `schoenhals-1873-moravia-selections-v1`, with four sections: `hollabrunn`,
    `archduke-ferdinand`, `austerlitz` and `stoecken`.
  - 9 page images with transcriptions: p. 138, for Hollabrunn; pp. 148, 156 and 169, for
    Austerlitz; pp. 177 and 178, the order of battle of the allied army at Austerlitz, which the
    table of contents lists as an appendix; and pp. 145, 174 and 175, for Archduke Ferdinand's
    corps and Stöcken. The two order-of-battle transcriptions hold the table's title, the 3rd
    column's rows and the recapitulation with its note, one row to a line.

**Dependence.**

- Völderndorff's preface names Wrede's communications among its sources, and the passages read on
  Stecken name no source. It is side A's own account at Steken, an official and interested one.
  Austrian strengths and losses in it are second-hand: it gives the Austrian loss by the enemy's
  admission. Bodart's 17 battalions, 2,000 horse and 40 guns for side B are its figures. No
  passage read shows dependence between it and Schönhals.
- *Victoires et conquêtes* cites the official bulletin by name in its Hollabrunn section (in a
  footnote, OCR) and Savary's report once in its Austerlitz account. It says that the French loss
  at Austerlitz was estimated at the time from the corps' reports, and it quotes Napoleon's
  proclamations. How far its narrative depends on the bulletins was not checked.
- By its preface Schönhals draws what it says of the French army's operations from that army's
  bulletins, so for side A it and *Victoires et conquêtes* may share them. For the French strength
  and loss at Austerlitz it cites Dumas's *Précis*. For Archduke Ferdinand's corps it cites the
  Archduke's report and two enclosures (Beilagen 35 and 37), and on p. 156 an enclosure for the
  strength of the Austrian troops. None of these was inspected.

The page images are single pages. *Victoires et conquêtes* and Völderndorff were downscaled to
1600 pixels on the longest side. The Internet Archive serves Schönhals at 804 x 1292 pixels, and
those pages were enlarged to 1600 pixels. t. XV's leaf numbers shift by two between pp. 226 and
227 (leaves n255 and n258), so each image's printed page was checked on the image. As before, each
transcription holds the whole page or the passages its note names, read from the image. The OCR
misreads figures that the images print: Schönhals's '16.000' for 15.000 on p. 169, and in
Völderndorff '30 Kanonen' for 40 (p. 296), '50,000' for 30,000 (p. 299), and '291 Mann' for 791
and '750 Mann' for 756 (p. 301). Schönhals's order of battle is garbled in the OCR. No figure is
taken from the OCR. Each selection records its parent's character ranges.

Rights: Völderndorff was published in 1826. Its Internet Archive item has no licence or
copyright-status field, and the library's own rights statement was not checked. The volume is
retained as the full OCR text with six downscaled page images. *Victoires et conquêtes* and
Schönhals are as recorded for batches 1d and 1e. Use: the drafts for B369a, B369c and B370a. No
model inputs are changed. The registry now holds 2,237 records.

## Koch, Damas, Bunbury and Colletta for Naples in 1806, 2026-10-17

127 records pinned in `data/raw/napoleonic-third-coalition-1806-v1/` for the
`third-coalition 1806` first pass (Campo Tenese, Maida, Gaëta and Amantea):

- **Koch**, *Mémoires de Masséna*, t. V (1850), group `koch-memoires-massena`, whose OCR parent
  was registered for 1805 batch 1c.
  - The selection `koch-massena-t5-naples-selections-v1`, with 24 sections from chapters I to III
    of the campaign of 1806 and the pièces justificatives: `army-reorganisation`,
    `gaeta-blockade-orders`, `calabria-expedition`, `palermo-plan`, `capri-and-garrisons`, `maida`,
    fifteen sections on Gaëta from `gaeta-blockade` to `gaeta-capitulation`, `amantea`, and
    `pj-ix-siege-troops` and `pj-x-capitulation`, the state of the troops employed at the blockade
    and siege of Gaëta and the articles of its capitulation.
  - 30 page images with transcriptions: pp. 169 and 173–176, for Campo Tenese; pp. 188–190, for
    Maida; pp. 187, 196, 202, 203, 205, 211, 212, 218, 223, 229, 231, 233, 236 and 248–250, and
    pièces IX and X on pp. 419, 420 and 422, for Gaëta; and pp. 280–282, for Amantea.
- **Damas**, *Memoirs of the Comte Roger de Damas (1787–1806)* (London, 1913), edited by Jacques
  Rambaud and translated by Mrs. Rodolph Stawell, group `damas-memoirs`, a new family. The memoirs
  of the commander of the Neapolitan corps beaten at Campo Tenese, written by the edition's account
  of the manuscripts in Sicily before he left for Vienna, with the editor's notes.
  - The OCR (`damas-memoirs-1913-ocr-v1`, item `memoirsofcomtero00damauoft`), of a University of
    Toronto copy.
  - The selection `damas-memoirs-1913-selections-v1`, with six sections: `intro-campo-tenese`,
    `intro-compiling`, `manuscripts`, `author-note`, `calabria-1806` and `notes-chapter-19`.
  - 9 page images with transcriptions: pp. 390, 391, 393, 395–397 and 399 of the narrative, and pp.
    484 and 485, the editor's notes to chapter XIX.
- **Bunbury**, *Narratives of some passages in the great war with France, from 1799 to 1810*
  (London, 1854), group `bunbury-narratives`, a new family. The narrative of the British army's
  Quartermaster-General in the Mediterranean, who rode the field at Maida. By its preface it was
  written many years after the events and privately printed in 1849 and 1851.
  - The OCR (`bunbury-1854-ocr-v1`, item `cu31924024332912`), of a Cornell University Library copy.
  - The selection `bunbury-1854-selections-v1`, with five sections: `preface`, `expedition-plan`,
    `landing`, `battle` and `aftermath`.
  - 15 page images with transcriptions: pp. 233, 235–246, 253 and 254, for the expedition, the
    landing, the battle and the losses.
- **Colletta**, *Storia del Reame di Napoli dal 1734 sino al 1825*, vol. II (Florence, 1856, third
  edition), group `colletta-storia-napoli`, a new family. The history of the kingdom by a Neapolitan
  officer, whose own entry in the volume's index lists his service.
  - The OCR (`colletta-1856-v2-ocr-v1`, item `storiadelreamedi02colluoft`), of a University of
    Toronto copy.
  - The selection `colletta-1856-v2-selections-v1`, with six sections: `fortresses-1806`,
    `gaeta-reinforced`, `gaeta-siege-slow`, `gaeta-siege`, `amantea` and `index-author`.
  - 6 page images with transcriptions: pp. 28–33, for the council's decision on Gaëta, its siege,
    surrender and losses, and the siege of Amantea.

**Dependence.**

- Koch is second-hand for side B throughout.
- Bodart's 4,800 for side B at Maida is Bunbury's 4795 rank and file rounded up. His 4,700 at
  Amantea equals Koch's three columns (our arithmetic), and his 3,000, 12,000 and 7,000 at Gaëta
  match figures in Koch, but the passages read do not show what he used.
- Damas's editor cites Duhesme, P. L. Courier, Marulli and Duthilt in his notes, none of them
  inspected.
- Colletta names no source in the passages read and gives himself no part at Gaëta or Amantea.
- No passage read shows dependence between Koch and Damas, Bunbury or Colletta.

The page images are single pages, served larger than 1600 px and downscaled. Bunbury's leaf numbers
shift at two plates (n = printed + 35, + 37 and + 39), so each image's printed page was checked on
the image. Each transcription holds the whole page or the passages its note names, read from the
image. Koch's p. 282 is heavily inked, and its transcription reads the first figure of '22' and of
'48' by their shapes. No figure is taken from the OCR. Each selection records its parent's character
ranges. The Koch selection's transcription note was corrected before registration was committed: it
had dated Maida 4 July and counted fourteen passages on Gaëta, where the selection holds fifteen.

Rights: Damas (1913) and Colletta (1856) are marked NOT_IN_COPYRIGHT by the Internet Archive.
Bunbury (1854) has no copyright-status field; its OCR front matter carries Cornell University
Library's notice that there are no known copyright restrictions on the text in the United States.
Koch is as recorded for batch 1c. Use: the drafts for B370c, B370d, B371a and B379c. No model
inputs are changed. The registry now holds 2,364 records.
