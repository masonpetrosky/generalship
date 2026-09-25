# Morgan's Raid into Kentucky (June 1864): bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The only frozen record
in **Morgan's Raid into Kentucky [June 1864]** now has a draft dossier: **9 claims, 1 explicit null unknown
and 53 citation occurrences** (50 before the review correction below). All seven dimensions are represented.
The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| KY011 — Cynthiana | 1864-06-11 to 06-12 | 9 | 1 | 53 | 3 |

Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and the Arnold
tables are one family. The raid's summary of events and list of reports (Nos. 1–14) in the registered
*Official Records* Series I, Volume XXXIX, Part 1 (`or39-1-illinois-ocr-v1`; catalog volume v.39:1, OCR title
checked) were read.

- **Stephen G. Burbridge** (No. 1): all his reports were read (pp.19–27). Selected are the two June 13
  dispatches (p.20) and the August 1 report with its casualty list (pp.22–27). The June 10 dispatch, the
  undated June letter and the June 23 letter on Hobson's surrender and the addenda were read and not selected.
- **John H. Morgan** (No. 14): all of No. 14 was read (pp.64–84). Selected are the June 11 letter from
  Cynthiana (p.66) and the July 20 report (pp.67–70). The following were read and not selected: the May 31
  letter, the indorsements and Inclosures A–E, and the addenda (Morgan's August 21 letter, Giltner's and
  Alston's complaints of plunder, the court-of-inquiry orders and charges, and Norris's memorandum).

Hobson's No. 5 report on Keller's Bridge, the brigade reports and Garis's and Asper's reports were not
inspected. Basil W. Duke's registered *History of Morgan's Cavalry* is a separate family but not independent of
Morgan's command; it was not used under the three-family ceiling. No targeted follow-up was used. Stop after
this record.

## New source records

This pass adds **4 source records**: the NPS HTML/text pair for KY011 and two selections from the registered
Volume XXXIX Part 1 parent:

- `or39-1-burbridge-cynthiana-selections-v1`, new group `burbridge-1864-reports`, shared with the Saltville
  pass's Burbridge selection;
- `or39-1-morgan-kentucky-selections-v1`, new group `jh-morgan-1864-reports`.

## Decisions and limits

- **Scope.** The frozen interval covers the capture of Cynthiana and the action at Keller's Bridge on the 11th
  and Burbridge's attack on the 12th. The following are context and are not added to this record:
  - Mount Sterling (8th–9th), Lexington and Frankfort;
  - the retreat to Abingdon;
  - raid-wide losses and captures.
- **Opening strength remains unknown.** The frozen side bounds are blank and the live field reads zero.
  Figures recorded, none adopted:
  - NPS: Morgan 1,200; Garis about 300 and Hobson about 750 on the 11th; Burbridge 2,400 on the 12th;
  - Burbridge: about 2,400 in his column; Morgan's raiders nearly 3,000 on entering Kentucky, earlier
    reported at 5,000;
  - Morgan: about 400 surrendered in town; Hobson's brigade 2,000 (June 11 letter) or 1,500 (report);
    attacked on the 12th by 5,200, his own force engaged not over 1,200.
- **Disputes preserved.**
  - Hobson's command: Morgan's two figures, 2,000 and 1,500.
  - Losses: frozen and live 2,092 (US 1,092; CS 1,000). Burbridge claimed 300 killed, as many wounded and
    nearly 400 captured at Cynthiana, for about 150 of his own. His casualty list, the total of the brigade
    reports for the loss of his immediate command, gives 53, 156 and 205 for the raid, and its footnote says
    many of the missing had since returned. Morgan gives about 80 killed, 125 wounded and 150 captured or
    missing for the raid and 2,500 paroled prisoners. NPS says Morgan held about 1,300 Union prisoners
    overnight after the 11th. NPS's 1,300 and Morgan's 400 and 1,500 (or 2,000) surrendered bear on the frozen
    Union 1,092, but no inspected source states its basis.
- **Command roles and ranks.** Both listed commanders are Brigadier Generals in the frozen and live records.
  Morgan took Cassell's battalion into Hobson's rear in person on the 11th and ordered the withdrawal on the
  12th. Burbridge directed the attack and Garrard's pursuit. No listed commander receives automatic sole
  credit.
- **Tags.** No claim is tagged `inherited`. All stay `unresolved` or `post_outcome`.
- **Campaign contribution.** Morgan counts the diversion of the forces moving on the Southwest Virginia
  salt-works as the raid's first result. This is campaign context, not this record's tactical result.

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

KY011 is revised under `morgan-kentucky-1864-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/KY011.v1.json`.

- **KY011-R1** (KY011 `casualty-records` and this memo): the NPS Description's about 1,300 Union prisoners
  camping with Morgan overnight after the 11th is now recorded and cited. The unsupported inference that the
  frozen Union 1,092 "presumably includes" the men captured on the 11th is replaced: NPS's 1,300 and Morgan's
  400 and 1,500 (or 2,000) bear on the 1,092, but no inspected source states its basis.

Advisories:

- **Adopted:** A10 (KY011 `casualty-records` and this memo): Burbridge's list is "the loss of my immediate
  command", the total of the brigade reports, and its footnote says many of the missing had since returned to
  their regiments; both are now quoted and cited (pp.26–27).
- **No action:** A18 (NPS Campaign fields), already noted in the NPS inspection records and not adopted.

KY011 now has 9 claims, 1 unknown and 53 citations (50 before). The review correction adds no source records
for this campaign. No model input, cohort file, admission proposal or baseline is changed.
