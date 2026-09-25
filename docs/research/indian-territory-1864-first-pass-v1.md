# Operations in the Indian Territory, February 1864: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The one
**frozen record** in **Operations in the Indian Territory [February 1864]** now has a draft dossier:
**9 claims, 2 explicit null unknowns and 40 citation occurrences** (35 before the review correction
below). All seven dimensions are represented. The dossier remains a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| OK005 — Middle Boggy Depot | 1864-02-13 | 9 | 2 | 40 | 3 |

It changes no other dossier. Dossier presence is not first-pass acceptance, separate review or
model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. The live NPS
page has an empty description; only its summary fields are usable, and its campaign ("Red River
Campaign") and dates ("March-April 1864") do not match the frozen record. NPS/CWSAC and the Arnold
tables are one family. Two further families:

- **Britton, *The Civil War on the Border*, volume II** (Putnam's, 1899), from the registered
  parent, with a new selection: the opening of Chapter XVI on Maxey's command and Phillips's
  February expedition, including Middle Boggy (OCR pp.237–239). Britton relays Phillips's report.
- **Phillips's** February 1864 papers (*Official Records* Series I, Volume XXXIV, Part 1, No. 1,
  pp.106–111, and No. 2, pp.111–112), from the registered parent `or34-1-illinois-ocr-v1`: his
  February 16 and February 24 reports; Thayer's February 22 dispatch quoting Phillips's February 14
  report from Middle Boggy; Inclosure No. 3, his February 15 letter to John Jumper; and the Indian
  Brigade itinerary (No. 2, compiled, unstated authorship). Thayer's dispatch is a relay of
  Phillips and the itinerary a compiled record; neither is counted as a further family.

The following were read but not selected: the rest of Britton's Chapter XVI to the Quantrill
paragraph on p.241; Inclosures Nos. 1 and 2 (to Governor Colbert and the Choctaw council); and the
opening of Wright's No. 3 report. No targeted follow-up was used. Stop after this batch.

**Consequential gap.** No Confederate report on Middle Boggy was located in the inspected pages,
and Willette, the frozen Union commander, left no inspected report; the engagement is known only
from Phillips's relayed report, the itinerary, Britton and the frozen description.

**New source records.** This pass adds **4 records**: one NPS HTML/text pair and the Britton and
Phillips selections.

## Decisions and limits

- **Scope.** Phillips's February 1–29 expedition (the Canadian River skirmishes of February 5–8,
  the march to near Fort Arbuckle and the return) is context. The live Red River Campaign label and
  March–April dates are not adopted.
- **Opening strengths remain unknown.** The frozen bounds are blank and the live Forces Engaged
  field reads 0 total with blank side figures. Figures recorded and not adopted: Britton's about one
  thousand for Phillips's whole command on February 1 and Phillips's 450 mounted men and one
  howitzer taken farthest south. Neither is a count of Willette's advance engaged at Middle Boggy:
  Britton's thousand includes Willetts's battalion of the Fourteenth Kansas, while Phillips's
  February 24 report says the Fourteenth Kansas "was not sent", which the inspected passages do not
  reconcile. No Confederate figure was inspected.
- **Terrain is an explicit unknown.** No inspected passage describes the ground at Middle Boggy;
  the heavy roads and rain are expedition-wide.
- **Disputes preserved.**
  - Losses: the frozen casualty text reads Unknown while the frozen description gives 47
    Confederates killed; the live field gives 47. Phillips's relayed report gives 47 killed with
    wounded unknown; the itinerary and Britton give 49 dead left on the field. Phillips's expedition
    total of about 250 killed and 4 wounded is not assigned.
  - The frozen description's return to Fort Gibson for fear of fresh Confederate forces is the
    expedition's end, not the engagement's result.
- **Command roles and ranks.**
  - The frozen commanders are Lieutenant Colonel John Jumper and Major Charles Willette; the reports
    spell the Union major "Willetts". Phillips's relayed report says the attack was made by his
    advance under Willetts; his letter to Jumper refers to Jumper's defeat in the late engagement.
    The frozen description names the expedition's commander "Col. John F. Phillips"; the inspected
    reports are headed Col. William A. Phillips.
  - No listed commander receives automatic sole credit.
- **Tags.** All claims stay `unresolved` or `post_outcome`.

The two null unknowns are the opening strength and the terrain. No morale/readiness score,
probability, causal effect or new commander ranking is introduced. No model input, cohort file,
admission proposal or baseline is changed.

## Validation

`python3 -m generalship check` passes, and `python3 -m unittest discover -s tests` passes.
Every quote occurs in its cited section; the builder's miss list is empty.
After the review correction, both pass again (134 tests) in the main repository, and the
builder's miss list is empty.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the eight
Trans-Mississippi 1863–64 first passes together at prepared commit `29c2811` as
`tm1863-review-29c2811-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": four
required findings (R1 to R4) and twelve advisories (A1 to A12) across the eight passes. It is an
AI review within its stated scope, not human historical adjudication, proof of source independence
or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the registry
record) before any change; every new quote occurs in its cited section, and the dossiers were
regenerated from the builder.

OK005 is revised under `indian-territory-1864-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/OK005.v1.json`. No required finding concerned this
campaign.

Advisories:

- **Adopted:** A5 (OK005: the live Forces field is recorded as "0 total (US ; CS ;)", not blank;
  Phillips's "The Fourteenth Kansas ... was not sent" is recorded against the Fourteenth Kansas
  battalion under Willetts named by Britton and the itinerary, unreconciled; the frozen
  description's "Col. John F. Phillips" is recorded against the reports' heading "Col. William A.
  Phillips" as a name discrepancy in the frozen text; five citations added; this memo's ambiguous
  "Neither counts Willette's advance" is reworded).

The review correction adds no source records for this campaign. Citations rise from 35 to 40; claims
(9), unknowns (2) and disputed claims are unchanged. No model input, cohort file, admission proposal
or baseline is changed.
