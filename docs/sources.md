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
