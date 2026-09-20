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
