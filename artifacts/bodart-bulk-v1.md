# Bodart: a direct table across 1618–1905

**1,682 candidate entries across all 552 battle-description pages (pp. 49–600).** This expands directly from Gaston Bodart’s 1908 compilation. No Arsht dataset, code or ranking supplies the table.

[Download the complete CSV](bodart-bulk-v1.csv) · [Extraction counts and checks](bodart-bulk-v1.json)

## What is ready

- 708 entries reuse our image-checked Napoleonic-period transcription, including entries outside the French land cohort. Frozen cohorts and model inputs stay unchanged.
- 974 additional entries come from layout-aware OCR. 34 have scoped image checks and corrections; 940 remain machine readings. Commander names and identities are provisional throughout the new section.
- 1040 entries have two numerical personnel readings; 1381 have two printed commander strings. Unknown values stay blank. A printed string is not a resolved identity or an allocation of credit.
- 121 naval entries remain visible, with naval/personnel distinctions. 70 year readings remain unresolved rather than silently corrected.

## What the figures mean

This is a source extraction table, not a new ratings run. No model was fitted and no predictor admitted. Counts describe detected entries, not complete historical coverage. Bodart selects consequential or high-loss engagements, says he excludes colonial wars from this section, rounds figures, includes available forces beyond those actually engaged, and assigns a winner even to some indecisive battles. His table convention puts that winner on the left ([explanatory notes, pp. 45–47](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n46/mode/1up)). These conventions limit future modelling.

The selection is not all wars or all engagements. Overseas engagements within the listed European wars still occur, such as Cuddalore. Multiple commanders, overlapping operations, indecisive results and no-combat capitulations require explicit treatment before any fit.

The OCR’s word positions keep opposing columns separate. Only an explicitly printed personnel total is selected; components, guns, ships, casualties and survivors are not mechanically turned into a whole-side force. OCR errors remain possible even at high recognition confidence. New OCR rows retain their candidate status and are not automatically eligible for a model.

## Check against existing work

The detector recovers all 708 existing entry starts with the same counts per printed page. This is a development check: the detector vocabulary was adjusted using these pages. It is not an independent review or proof of recall elsewhere.

| Personnel field comparison | Fields |
| --- | ---: |
| agree | 831 |
| disagree | 74 |
| missing | 266 |
| not_comparable | 245 |

The final table uses the checked transcription on these pages, not the OCR values. The JSON retains every agreement, disagreement and missing reading. Matching an OCR number to a checked transcription does not establish that Bodart’s historical figure is correct.

## Small page-image check

The primary inspected 34 entry headers and personnel fields on 11 fixed pages outside the existing transcription. This is a small spread across the volume used to check and refine extraction, not a blind accuracy estimate. The original OCR, initial readings, current parser differences, image hashes and scoped corrections remain visible in the [check record](../data/bodart/image-checks-v1.json) and JSON.

| Personnel comparison before scoped image corrections | Fields |
| --- | ---: |
| agree | 43 |
| disagree | 2 |
| missing | 15 |
| not_comparable | 8 |

Lagoulin (p. 595) illustrates the risk: the scan prints **20,000 / 24,000**, while OCR reads **90,000 / 84,000**. The sampled table fields use the scan readings, with explicit field provenance. This does not verify every field in those rows or the remaining OCR rows.

The CSV keeps the original strength literal alongside the corrected numerical field. `image_checked_fields`, `image_check_id` and the image source ID/hash identify the exact override; the check record supplies its reading and locator. Other fields retain OCR status.

## Coverage by century

| Century | Entries |
| --- | ---: |
| 17 | 208 |
| 18 | 756 |
| 19 | 631 |
| 20 | 17 |
| unknown | 70 |

## A few entries to inspect

| Page | Year reading | Place | Winner personnel | Loser personnel | Source status |
| ---: | --- | --- | ---: | ---: | --- |
| 49 | 1619 | [Groß-Zablat](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n50/mode/1up) | 5000 | 3000 | ocr_candidate_with_checked_fields |
| 124 | 1701 | [Carpi](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n125/mode/1up) | 15000 | unknown | ocr_candidate_with_checked_fields |
| 359 | 1801 | [Abukir](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n360/mode/1up) | 5500 | 2000 | existing_image_checked_transcription |
| 591 | 1904 | [Chemulpo](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n592/mode/1up) | 8800 | 900 | ocr_candidate_not_image_verified |

## Reproduce

`python3 -m generalship.bodart_bulk --write` rebuilds the CSV, metadata and this report offline. With no flag it checks them. `--inspect ID` prints a structured record with its quoted source text. Every row retains source ID, SHA-256, printed pages, scan link and XML line IDs or transcription locator. Source quotes normalize OCR whitespace; they are not facsimile transcriptions unless explicitly labelled as checked.

The new XML snapshot is the original Internet Archive OCR layout, checked against the SHA-1 in our previously pinned item metadata, then gzip-compressed losslessly with a fixed timestamp. It is one source family with the existing Bodart scan and transcription. Frozen Napoleonic development/final reservations and all old model records remain intact.
