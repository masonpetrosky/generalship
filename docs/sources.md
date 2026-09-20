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
