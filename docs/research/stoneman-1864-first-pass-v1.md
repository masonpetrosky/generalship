# Stoneman's Raid into Southwest Virginia (December 1864): bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both frozen records in
**Stoneman's Raid into Southwest Virginia [December 1864]** now have draft dossiers: **18 claims, 2 explicit
null unknowns and 89 citation occurrences** (85 before the review correction below). All seven dimensions are
represented in each record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| VA081 — Marion | 1864-12-17 to 12-18 | 9 | 1 | 48 | 3 |
| VA082 — Saltville (II) | 1864-12-20 to 12-21 | 9 | 1 | 41 | 3 |

Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and both retained NPS pages in full. The VA082 page's
Description field is empty, so the frozen Arnold description stands for the NPS/CWSAC narrative there (one
family). The expedition's summary of events and list of reports (Nos. 1–16) in the registered *Official
Records* Series I, Volume XLV, Part 1 (`or45-1-illinois-ocr-v1`; catalog volume v.45:1, OCR title "SERIES I—
VOLUME XLV — IN TWO PARTS. PART I— Reports, Correspondence, etc.", 1894, checked before use) were read.

- **George Stoneman** (No. 1): the December 27 telegraphic report (pp.807–808) and the January 6, 1865 report
  (pp.808–814). The report prints his November 26 letter and Schofield's December 6 reply. The December 13
  dispatch and Thomas's December 27 congratulations were read and not selected. The p.810 running head is
  lowercase in OCR ("810 ky.").
- **John C. Breckinridge** (No. 4): the January 3, 1865 report with its postscript (pp.824–827). The
  postscript disputes Burbridge's report.

Burbridge's No. 2 and Gillem's No. 3 reports, the Confederate reports Nos. 5–16 and Steuart's letter on the
salt-works damage were not inspected. No targeted follow-up was used. Stop after this batch.

**Consequential gap.** No report of Burbridge, Gillem, Vaughn, Duke or Preston was inspected. The Union side
of the Marion fighting rests on Stoneman, who took command at the front.

## New source records

This pass adds **6 source records**: two NPS HTML/text pairs and two selections from the registered Volume XLV
Part 1 parent:

- `or45-1-stoneman-swva-selections-v1`, new group `stoneman-1864-reports`;
- `or45-1-breckinridge-swva-selections-v1`, placed in Breckinridge's existing group
  `breckinridge-baton-rouge-1862-report`, shared with the Bull's Gap selection.

## Decisions and limits

- **Scope.** The following are context and are not assigned to either record:
  - Kingsport (13th), Bristol (14th), and Marion and Wytheville against Vaughn (16th);
  - the lead-mine raid and the withdrawal on the 22nd;
  - expedition-wide captures (34 officers and 845 men by Stoneman's telegram) and destruction.
  VA081 is the engagement with Breckinridge near Marion on the 17th–18th; VA082 is the capture and
  destruction of Saltville on the 20th–21st.
- **Opening strengths remain unknown.** Both frozen force fields read "Divisions", without bounds. Figures
  recorded, none adopted:
  - Stoneman: Burbridge's force about 4,200 aggregate with four guns at Cumberland Gap on November 24, by
    Burbridge's report; Gillem about 1,500 effective;
  - Breckinridge: at the close of the 18th, three brigades and a battalion numbering fewer than 1,000,
    against not less than 6,000; a body reported as 900–1,200 in his rear proved to be some 600;
  - Saltville garrison: about 700 home guards (Stoneman) against some 400 left under Preston
    (Breckinridge).
- **Disputes preserved.**
  - Who met whom near Marion: Stoneman says he met Breckinridge in a strong position on his return.
    Breckinridge says the Union force was not met while returning but overtaken while marching up the
    valley, Witcher overtaking its rear on Saturday (the 17th).
  - Marion result: Stoneman says Breckinridge, nearly surrounded, escaped over the mountains. Breckinridge
    says his right repulsed the attacks and he withdrew by the only possible route. The recorded Union
    victory is kept.
  - Damage: Stoneman reports total destruction of the lead-works and salt-works; Breckinridge reports the
    lead-mine damage as very slight and relays the proprietor's view that no raid could stop the salt-works
    for more than a few weeks. Stoneman disputes an official report that the wells were not seriously
    damaged. This is campaign context.
  - Casualties: VA081 frozen 274 total against live zero; VA082 frozen Unknown against live zero. No
    inspected source gives either record's totals. Breckinridge's postscript excludes Vaughn's and Duke's
    commands (no report yet) and the citizens he says made up most prisoners, and says that for the rest
    not more than twenty were taken, most at Saltville. He puts the prisoners from the enemy, including
    wounded, at 200 and the horses they left at no fewer than 800 (read "8'00"). These figures are context
    and are not assigned.
- **Command roles.** Stoneman says he took immediate control of Burbridge's command at Marion and criticises
  Burbridge's vigor at Saltville. Breckinridge was absent when Saltville fell and says Preston had no
  alternative. No listed commander receives automatic sole credit.
- **Tags.** The Saltville works predate the attack, but the terrain claim also describes the assault. No
  claim is tagged `inherited`; all stay `unresolved` or `post_outcome`.

The two null unknowns are the opening strengths. No morale/readiness score, probability, causal effect or new
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

VA081 and VA082 are revised under `stoneman-1864-review-correction-2026-09-25` and supersede the
byte-for-byte archives at `data/evidence/history/<ID>.v1.json`.

- **VA081-R1 and VA082-R1** (both `casualty-records`): Breckinridge's "not more than twenty prisoners" is what
  remains after he excludes Vaughn's and Duke's commands, from which he had no report yet, and the citizens he
  says made up most prisoners. It is not the whole expedition's or all his troops' figure. Both values now
  state this scope and cite the postscript sentence (p.827).

Advisories:

- **Adopted:** A12 (VA082 `casualty-records` only, to avoid double counting): Breckinridge's "The prisoners,
  including the wounded left in our hands, will reach 200" and "at least 8'00 horses" follow his account of
  the retreat from Saltville. They are recorded as expedition context and not assigned to the record.
- **No action:** A18 (NPS Campaign fields), already noted in the NPS inspection records and not adopted.

VA081 now has 48 citations (47 before) and VA082 41 (38); claims (9 each) and unknowns (1 each) are unchanged.
The review correction adds no source records for this campaign. No model input, cohort file, admission
proposal or baseline is changed.
