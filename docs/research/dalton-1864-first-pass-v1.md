# Demonstration on Dalton (February 1864): bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The only frozen record
in **Demonstration on Dalton [February 1864]** now has a draft dossier: **9 claims, 1 explicit null unknown
and 48 citation occurrences** (47 before the review correction below). All seven dimensions are represented.
The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| GA006 — Dalton I | 1864-02-22 to 02-27 | 9 | 1 | 48 | 3 |

Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and the Arnold
tables are one family. The report families come from the registered *Official Records* Series I, Volume
XXXII, Part 1 (`or32-1-illinois-ocr-v1`; catalog volume v.32:1, OCR title checked). The demonstration's
report list (Nos. 1–39) points to Thomas's general report for the Union side.

- **George H. Thomas** (general report No. 1): his March 10, 1864 report was read in full (pp.6–12). The
  Dalton passage is selected (pp.8–11), with two of its inclosures:
  - Inclosure No. 4, John W. Gladden's statement, submitted by James Lamon (p.13). Thomas's transmittal
    sentence, just after the selected passage, calls it "a statement of a refugee from Dalton";
  - Inclosure No. 5, the killed-and-wounded table for Buzzard Roost (p.14).
  The January operations, the veteran-regiment list and Inclosures Nos. 1–3 were read and not selected.
- **Joseph E. Johnston** (No. 28): the February 25 and 27 dispatches and the Dalton portion of his October 20,
  1864 report (pp.476–477). Stewart's No. 29 report was read at its opening and not selected.

Palmer's orders, the Union division, brigade and regimental reports, the other Confederate reports, Wheeler's
itinerary and the No. 2 Union casualty return were not inspected. No targeted follow-up was used. Stop after
this record.

## New source records

This pass adds **4 source records**: the NPS HTML/text pair for GA006 and two selections from the registered
Volume XXXII Part 1 parent:

- `or32-1-thomas-dalton-selections-v1`, placed in Thomas's existing group `thomas-mill-springs-report`;
- `or32-1-johnston-dalton-selections-v1`, placed in `johnston-atlanta-report`. The October 20, 1864 report
  is the same document whose Atlanta portion is registered as `or38-3-johnston-atlanta-selections-v1`.
  The compiler's footnote after the Dalton excerpt (outside the selection) places the omitted portion in
  Vol. XXXVIII, Part II, while the registered Atlanta selection is from Part 3; this is recorded, not
  reconciled.

Same-author groups are one witness family.

## Decisions and limits

- **Scope.** The frozen interval covers the whole demonstration: Tunnel Hill (23rd–24th), Buzzard Roost and
  Crow's Valley (24th–25th), Dug Gap (26th) and the withdrawal. The January reconnaissance and the Meridian
  Expedition are context.
- **Opening strength remains unknown.** The frozen side bounds are blank and the live field reads zero.
  Figures recorded, none adopted:
  - Thomas: four divisions, against an army he became convinced largely outnumbered them;
  - Gladden's statement: about 30,000 Confederates;
  - Johnston: effective infantry and artillery of 36,826 and cavalry of 5,613 on December 31, 1863;
    Hardee's infantry except Stevenson's division ordered to Polk on February 17;
  - NPS: the loss of two divisions.
- **Disputes preserved.**
  - Result: Johnston says his troops were successful and the enemy retired in the night of the 26th. Thomas
    calls the movement a complete success because it caused the recall of the reinforcements sent against
    Sherman. The recall is campaign contribution, not the tactical result.
  - Casualties: the frozen field is Unknown and the live field reads 429 (US 289; CS 140). The live Union 289
    matches the Buzzard Roost table (killed and wounded, February 24–25). Gladden gives 50–60 Confederate
    killed and 150 wounded. No inspected source gives the live Confederate 140.
- **Command roles and ranks.** The live page styles Johnston "Lieutenant Colonel"; the frozen rank (General)
  is kept and the live rank is not adopted. Thomas's report has Palmer directing the advance and Thomas
  deciding to withdraw. Johnston's account of the retaking of Dug Gap is passive and names no one as giving
  the order. No listed commander receives automatic sole credit.
- **Tags.** Rocky Face Ridge and its gaps were held during the operation. No claim is tagged `inherited`;
  all stay `unresolved` or `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or new
commander ranking is introduced. The cohort, both admission proposals and the baseline are unchanged.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the fifteen 1864
Western small-operation first passes (ten campaigns) together at prepared commit `4986724` as
`w1864-review-4986724-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": seven
required findings (KY010-R1, KY011-R1, TN031-R1, VA081-R1, VA082-R1, TN030-R1 and GA006-R1) and
eighteen advisories (A1 to A18) across the ten passes. It is an AI review within its stated scope, not
human historical adjudication, proof of source independence or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the frozen row,
the registry record or the pinned parent OCR) before any change; every new quote occurs in its cited
section, and the dossiers were regenerated from the builder. After the correction, `python3 -m
generalship check` passes, `python3 -m unittest discover -s tests` passes (134 tests) and
`gs.MISSES` is empty.

GA006 is revised under `dalton-1864-review-correction-2026-09-25` and supersedes the byte-for-byte
archive at `data/evidence/history/GA006.v1.json`.

- **GA006-R1** (GA006 and this memo): Inclosure No. 4 is headed "JOHN W. GLADDEN'S STATEMENT"; the word
  "refugee" is Thomas's, in his transmittal sentence outside the selected range (verified in the pinned parent
  OCR). `reported-force-scope` now names Gladden's statement, submitted by Lamon and forwarded with Thomas's
  report, and cites the inclosure heading; `transport-and-forage`, `casualty-records` and the family note say
  "Gladden's statement", the family note adding that Thomas's transmittal calls it a refugee's. The registry
  record `or32-1-thomas-dalton-selections-v1` still calls it "a refugee's statement" in its dependency note.
  The review offered a metadata-only revision only "if that is wanted"; none is made here, and the choice is
  left to the primary.

Advisories:

- **Adopted:** A4, as notes, not citations: the compiler's footnote after Johnston's Dalton excerpt lies
  outside the selection. It is recorded in GA006's family note and in this memo (Vol. XXXVIII, Part II against
  the registered Part 3 selection). The footnote to the Inclosure No. 5 total row, which was not selected, is
  listed as deferred.
- **No action:** A18 (NPS Campaign fields), already noted in the NPS inspection records and not adopted.

GA006 now has 9 claims, 1 unknown and 48 citations (47 before). The review correction adds no source records
for this campaign. No model input, cohort file, admission proposal or baseline is changed.
