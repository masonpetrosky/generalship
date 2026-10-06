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

On 2026-10-06, eleven more tables from the same commit were pinned in `data/raw/arnold-tables-v1/`
for the [v3 strength ledger](ledgers-v3.md): the CWSAC Report Updates and CWSS force tables, Bodart
(1908) and Clodfelter (2008) force tables with Arnold's concordances, and Arnold's Livermore table
for cross-checking only.

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
Separate reviews on 2026-10-06 checked the Antietam and Champion Hill drafts against
these same records, and both sets of corrections are applied; Champion Hill's were installed
once frozen ledgers replayed through the archive chain. Each still rests on this one family.

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

The per-pass record of every source added since 2026-09-20 — what was registered, from where,
under which independence group, and with what transformation — is in
[source additions](source-additions.md). `data/sources.json` remains the authority for exact
bytes, rights and dependence metadata.
