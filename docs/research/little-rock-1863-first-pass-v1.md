# Advance on Little Rock: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both **frozen
records** in **Advance on Little Rock [September-October 1863]** now have draft dossiers: **18
claims, 2 explicit null unknowns and 92 citation occurrences** (90 before the review correction
below). All seven dimensions are represented in each record. Both dossiers remain drafts; no
features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| AR010 — Bayou Fourche (Little Rock) | 1863-09-10 | 9 | 1 | 43 | 3 |
| AR011 — Pine Bluff | 1863-10-25 | 9 | 1 | 49 | 3 |

It changes no dossier outside AR010 and AR011. Dossier presence is not first-pass acceptance,
separate review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and both retained NPS pages in full.
NPS/CWSAC and the Arnold tables are one family. A search of Britton's volume II OCR found no
treatment of these actions beyond passing mention, and no other history was searched; this is a
recorded gap. Each record instead uses two report families from *Official Records* Series I,
Volume XXII, Part 1, one per side:

- Bayou Fourche:
  - **Davidson's** September 12, 1863 report on September 10 (No. 5, pp.486–487);
  - **Price's** November 20, 1863 report on July 24–September 25 (No. 22, pp.520–522), the
    compiled Confederate casualty return printed as its addenda (p.523, marked incomplete and
    garbled in OCR), and Price's November 25 letter to Dobbin printed as addenda to Dobbin's
    report (pp.525–526). The return is a separate section, not Price's text.
- Pine Bluff:
  - **Clayton's** October 27, 1863 report (No. 2, pp.723–724), with Captain James B. Talbot's
    report on the freedmen as its inclosure (pp.724–725) and the compiled Union return (p.725,
    garbled). Talbot is a separate writer, selected as a separate section and not counted as a
    further family;
  - **Marmaduke's** October 26, 1863 report (No. 7, p.730).

The following were read but not selected:

- the advance's summary and report list (pp.468–469), the Union No. 4 return (p.482), Davidson's
  August 15 and September 1 reports and his September 13 General Orders No. 62;
- **Dobbin's** November 19 report (No. 23, pp.523–525), which covers Bayou Fourche from the
  Confederate cavalry side. It was read while locating Price's letter, so AR010 was read in four
  families; it is not cited, and this is recorded in AR010's open questions;
- the Pine Bluff report list (pp.721–722), the opening of Steele's No. 1 transmittal and the
  opening of Greene's No. 8 report.

No targeted follow-up was used. Stop after this batch.

**Consequential gap.** Marmaduke, the frozen Confederate commander at Bayou Fourche, has no report
on September 10 in the list (his No. 24 covers August 17–28); his role there is known only from
Price and Davidson. Steele's report (No. 3) was not read.

**New source records.** This pass adds **8 records**: two NPS HTML/text pairs and the Davidson,
Price, Clayton and Marmaduke selections. Price's selection is placed in his most recent registry
group, `price-missouri-1864-reports`; his Lexington, Camden and 1864 Missouri groups
(`price-lexington-report`, `price-camden-1864-report`, `price-missouri-1864-reports`) are the same
author family and not mutually independent corroboration (see the review W61-R14 note in
`docs/sources.md`). Marmaduke's Pine Bluff selection shares the new group `marmaduke-1863-reports`
with his January and May 1863 selections registered in this batch for the two Missouri expeditions.
Davidson and Clayton have new groups.

## Decisions and limits

- **Scope.** The advance from Helena and Clarendon, the Brownsville and Bayou Meto actions (August
  25–27), the Ashley's Mills skirmish (September 7), Steele's advance on the north bank, the
  evacuation and retreat to Arkadelphia, and Caldwell's pursuit after Pine Bluff are context. The
  fall of Little Rock is campaign context; AR010's tactical record is the engagement at the bayou.
- **Opening strengths remain unknown.** Both frozen records have blank bounds and the live Forces
  Engaged fields read zero. Figures recorded and not adopted:
  - Bayou Fourche: Price's barely 8,000 against nearly or quite 20,000 (district-wide) and Dobbin's
    about 1,200 at the crossing; Davidson's three brigades and Engelmann's infantry division, and
    his identification of Marmaduke's dismounted cavalry and Tappan's brigade with two batteries.
  - Pine Bluff: Clayton's some 550 and his estimate of 2,500 Confederates with twelve guns (2,000–3,000
    from prisoners); Marmaduke's about 600 effective with seven guns for the garrison.
- **Disputes preserved.**
  - Pine Bluff's defenders: NPS calls the 300 men who rolled out the cotton bales African-American
    soldiers; Clayton and Talbot describe freedmen from the contraband camp, fifteen of whom had
    arms. The NPS wording is not adopted.
  - Bayou Fourche losses: the frozen US 72 and CS unknown against the live CS 64; Davidson's "not
    exceed ... 60 killed and wounded"; the compiled Confederate return's grand total read as 64,
    which matches the live figure but covers the whole advance from August 25 to September 10.
  - Pine Bluff losses: the frozen US 56 (CS unknown) and live CS 40; Clayton's 11 killed, 27 wounded
    and 1 missing plus 5 freedmen killed and 12 wounded (printed components summing to 56; whether
    the frozen figure includes the freedmen is not established, although the garbled compiled return
    has a legible "Freedman 5" row and a total line read as "16 39 1"); Clayton's estimate of about
    130–150 Confederate killed and wounded against Marmaduke's about 40; Clayton's charge that
    Marmaduke burned some of his own wounded, recorded as reported.
- **Command roles and ranks.**
  - The live pages list Marmaduke without a rank.
  - Price's letter records that Walker was mortally wounded in a duel with Marmaduke the morning
    after September 5, that Marmaduke was under arrest and restored to command for the operations,
    and that Dobbin came to Price under arrest by Marmaduke's order; the disruption is recorded,
    not scored. Price says Marmaduke took command of all the cavalry south of the river and handled
    the rear guard skillfully.
  - At Pine Bluff, Clayton organized the defence and Talbot the freedmen under his orders.
  - No listed commander receives automatic sole credit.
- **Tags.** The Pine Bluff cotton-bale works, built on the morning of the attack on Clayton's order,
  are tagged `commander_created`; the tag is a hypothesis about timing and agency, not a causal
  estimate. The rule applied is works constructed on an explicit order; ground selected during an
  action (such as Cabell's ambush, Shoup's ridge or Merrill's line in the other 1863 passes) stays
  `unresolved`. The agency evidence is Clayton's report and Talbot's inclosure, one report family.
  All other claims stay `unresolved` or `post_outcome`.

The two null unknowns are the opening strengths. No morale/readiness score, probability,
causal effect or new commander ranking is introduced. No model input, cohort file, admission
proposal or baseline is changed.

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

AR011 is revised under `little-rock-1863-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/AR011.v1.json`. AR010 is unchanged. No required
finding concerned this campaign.

Advisories:

- **Adopted:** A3 (this memo names Price's Lexington group as the same author family, per
  `docs/sources.md`); A4 (AR011: Marmaduke's next sentence, "The women and children I could not
  bring away", added to `water-mules-and-property` and cited; the casualty rationale notes the
  compiled return's legible "Freedman 5" row and total line, which matches Clayton's figures with the
  freedmen added, as a suggestion rather than a resolution, and cites it); A10 (the
  `commander_created` rule and the one-family agency evidence are stated here and in the AR011
  rationale).
- **Kept as is:** A11 (Dobbin's report, read in full and not cited, stays recorded in AR010's open
  questions as the first target if the record is revisited).

The review correction adds no source records for this campaign. Citations rise from 90 to 92; claims
(18), unknowns (2) and disputed claims are unchanged. No model input, cohort file, admission
proposal or baseline is changed.
