# Occupation of Indian Territory North of the Arkansas River: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The one
**frozen record** in **Occupation of Indian Territory North of the Arkansas River [October 1863]**
now has a draft dossier: **9 claims, 1 explicit null unknown and 59 citation occurrences** (56
before the review correction below). All seven dimensions are represented. The dossier remains a
draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| KS002 — Baxter Springs | 1863-10-06 | 9 | 1 | 59 | 3 |

It changes no other dossier. Dossier presence is not first-pass acceptance, separate review or
model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family. Two further families:

- **Britton, *The Civil War on the Border*, volume II** (Putnam's, 1899), from the registered
  parent, with a new selection from Chapter XIV, The Baxter Springs Massacre: from the
  establishment of the post to Blunt's return to Fort Scott (OCR pp.212–225; several running heads
  are misread and the p.215 head carries no number, noted in the locators). Britton relays Pond's
  and Blunt's reports.
- **Quantrill's** October 13, 1863 report to Price, with postscript (*Official Records* Series I,
  Volume XXII, Part 1, No. 5, pp.700–701); an interested guerrilla account.

The following were read but not selected: the chapter's opening on Fort Scott and Order No. 11
(pp.209–212), the Baxter Springs report list, the opening of Blunt's No. 1 report, and **Pond's**
No. 4 report (pp.698–700), read in full while locating Quantrill's. Pond is a frozen commander, so
the record was read in four families; his report is not cited, to keep the evidence within three
families, and this is recorded in the open questions. Blair's and Henning's reports were located
by heading only. No targeted follow-up was used. Stop after this batch.

**Consequential gap.** Blunt, a frozen commander, is represented through Britton and Quantrill;
his October 19 report was read only at its opening. Pond's report, read and not cited, is the
first candidate if this record is revisited.

**New source records.** This pass adds **4 records**: one NPS HTML/text pair and the Britton and
Quantrill selections.

## Decisions and limits

- **Scope.** Quantrill's march south from Lafayette County and the killing of captives on the way to
  the Canadian are context. The killing of surrendered soldiers, bandsmen and civilians is recorded
  as reported, not as ordinary combat casualties.
- **Opening strengths remain unknown.** The frozen Confederate bound of 400 matches the live page;
  no inspected passage gives its basis. Figures recorded and not adopted: Britton's between three
  and four hundred for Quantrill, Blunt's escort of about one hundred, about 150 raiders forming on
  the escort's flank, the escort's impression of not less than six hundred, and less than a company
  of colored infantry at the post; Quantrill's 150 men in three companies, an escort of 125 and his
  250 in the charge.
- **Disputes preserved.**
  - Losses: frozen and live 106 (US 103; CS 3). Britton gives three officers, sixty-seven enlisted
    men and ten citizens killed and eighteen wounded, and relays Pond's eleven raiders left dead.
    Quantrill gives his own loss as 3 killed and 3 wounded (matching the frozen CS 3) and claims
    about 80 of the escort and 16 at the fort killed, naming Blunt, Henning and Tough among the dead
    although Britton places all three alive.
  - Killings: Britton says men were shot after surrendering and the bandsmen murdered; Quantrill
    says he left only about 40 of the escort alive and that of about 150 Union Indians and Black
    men caught on the march south "We brought none of them through". These are recorded as
    reported.
  - The result label covers two fights with opposite local outcomes: the post held and refused a
    summons, while the escort was destroyed.
- **Command roles and ranks.**
  - The frozen commanders are Lieutenant Colonel William C. Quantrill, Lieutenant James B. Pond and
    Major General James G. Blunt. The live page lists Pond without a rank and Quantrill as Colonel
    and omits Blunt; live ranks are not adopted.
  - Britton credits Pond's howitzer with driving the raiders from the camp and says Blunt and Curtis
    tried to rally the escort; Quantrill and Britton agree that he led the charge on the camp.
  - No listed commander receives automatic sole credit.
- **Tags.** The post's breastworks predate the attack, but their extension was under way; no claim
  is tagged `inherited`. All claims stay `unresolved` or `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect
or new commander ranking is introduced. No model input, cohort file, admission proposal or
baseline is changed.

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

KS002 is revised under `indian-territory-north-1863-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/KS002.v1.json`.

- **R4(a)** (KS002 `casualty-records`): Britton's statements that the fourteen bandsmen, the driver
  and O'Neal were murdered, and that Henning and Tough returned to the prairie and Blunt followed the
  raiders after the fight, are now cited within the claim (p.220, p.221 and p.224 citations added;
  the value is unchanged).

Advisories:

- **Kept as is:** A11 (Pond's report, read in full and not cited, stays recorded in the open
  questions as the first target if the record is revisited).

The review correction adds no source records for this campaign. Citations rise from 56 to 59; claims
(9), unknowns (1) and disputed claims are unchanged. No model input, cohort file, admission proposal
or baseline is changed.
