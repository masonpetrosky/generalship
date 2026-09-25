# Operations in North Alabama (January 1864): bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The only frozen record
in **Operations in North Alabama [January 1864]** now has a draft dossier: **9 claims, 1 explicit null
unknown and 46 citation occurrences**. All seven dimensions are represented. The dossier is a draft; no
features are admitted.

| Record | Date (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| AL002 — Athens | 1864-01-26 | 9 | 1 | 46 | 3 (Rawlins's dispatch not independent of Dodge) |

Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and the
Arnold tables are one family.

The two further families come from the registered *Official Records* Series I, Volume XXXII, Part 1
(`or32-1-illinois-ocr-v1`; the catalog volume field reads v.32:1 and the OCR title "SERIES I— VOLUME
XXXII", checked before use):

- **Grenville M. Dodge** (No. 2): the three January 26 dispatches (p.118) and the January 29 report
  (p.119). Dodge commanded at Pulaski and was not at Athens. The report's year reads "18G4" in OCR.
- **John A. Rawlins** (No. 1): the January 29 dispatch (p.117). It relays the same figures as Dodge's
  first dispatch and is not independent of him.

The "Operations in North Alabama" summary and report list (Nos. 1–8) were read. Dodge's February 1 letter
and Rawlins's February 2 dispatch were read and not selected. Woods's, Miller's, Atkins's and the
regimental reports (Nos. 3–8) were not inspected. **No Confederate report on Athens appears in the report
list**, so the Confederate side rests on Union accounts and NPS; this is the consequential gap. No
targeted follow-up was used. Stop after this record.

## New source records

This pass adds **4 source records**: the NPS HTML/text pair for AL002 and two selections from the
registered Volume XXXII Part 1 parent (`or32-1-dodge-athens-selections-v1`, new group
`dodge-1864-reports`; `or32-1-rawlins-athens-selections-v1`, new group `rawlins-1864-dispatches`). Neither
author had an earlier registry group.

## Decisions and limits

- **Scope.** Miller's January 25 fight near Florence (Shoal Creek) and the January 28–29 operations
  against Roddey are context and are not added.
- **Opening strength remains unknown.** The frozen side bounds are blank. Figures recorded, none adopted:
  - frozen description: about 600 Confederate cavalry against about 100 Union troops;
  - live NPS Forces Engaged: 800 (US 700; CS 100), which reverses the description;
  - Dodge, January 26 (first dispatch): Hannon with about 600 men and 2 guns against about 100;
  - Dodge, January 26 (second dispatch): Adam's men, 75 all told;
  - Dodge, January 29: Adam and 75 men, all the force then at the post;
  - Rawlins, January 29: 600 against a garrison of about 100.
- **Disputes preserved.**
  - Distance of Brown's Ferry from Athens: 12 miles (January 26) against 18 (January 29).
  - Whether the attackers knew the mounted force had left: "They got news some way of our move"
    (January 26) against "General Roddey did not know of this" (January 29).
  - The Confederate commander: Hannon (January 26 dispatches) against Roddey in person (January 29).
  - Line of retreat: Wood Ferry against Brown's Ferry.
  - Unit names: the frozen force field names the 1st Alabama Cavalry for the Confederates; Dodge's January
    29 report names Patterson's and Hannon's regiments. They are not reconciled.
- **Casualties.** The frozen and live 50 (US 20; CS 30) match Dodge's Union 20; the Confederate 30 has no
  inspected basis.
- **Command roles and ranks.** Hannon (Lieutenant Colonel) and Emil Adams (Captain) are the frozen and
  live commanders; Dodge spells the Union officer "Adam". No listed commander receives automatic sole
  credit.
- **Tags.** No works or ground are tagged `inherited` (the defenders had no fortifications). All claims
  stay `unresolved` or `post_outcome`.

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

AL002 is revised under `north-alabama-1864-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/AL002.v1.json`. No required finding concerns this campaign.

Advisories:

- **Adopted:** A1 (the family table now says Rawlins's dispatch is not independent of Dodge; the effective
  independent witnesses are NPS/CWSAC and Dodge) and A2 (AL002 `reported-force-scope` rationale and this memo:
  the frozen 1st Alabama Cavalry and Dodge's Patterson's and Hannon's regiments are named differently and not
  reconciled).
- **No action:** A18 (NPS Campaign fields), already noted in the NPS inspection records and not adopted.

Claims (9), unknowns (1) and citations (46) are unchanged. The review correction adds no source records for
this campaign. No model input, cohort file, admission proposal or baseline is changed.
