# Marmaduke's Second Expedition into Missouri: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both **frozen
records** in **Marmaduke's Second Expedition into Missouri [April-May 1863]** now have draft
dossiers: **18 claims, 2 explicit null unknowns and 86 citation occurrences** (84 before the review
correction below). All seven dimensions are represented in each record. Both dossiers remain drafts;
no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| MO020 — Cape Girardeau | 1863-04-26 | 9 | 1 | 43 | 3 |
| AR007 — Chalk Bluff | 1863-05-01 to 05-02 | 9 | 1 | 43 | 3 |

It changes no dossier outside MO020 and AR007. Dossier presence is not first-pass acceptance,
separate review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and both retained NPS pages in full.
NPS/CWSAC and the Arnold tables are one family. A search of Britton's volume II OCR found no
treatment of these actions, and no other history was searched; this is a recorded gap. Each
record instead uses two report families, one per side:

- **Marmaduke's** May 20, 1863 report (*Official Records* Series I, Volume XXII, Part 1, No. 13,
  pp.285–288), with Kirby Smith's June 4 indorsement and the compiled addenda return (p.288,
  garbled in OCR), for both records. The indorsement and return are separate sections and not
  counted as further families.
- **McNeil's** two April 26 dispatches from Cape Girardeau (No. 3, p.255), for MO020.
- **Vandever's** April 30, May 2 and two May 4 dispatches (No. 11, pp.275–278), for AR007.

The following were read but not selected:

- the expedition's summary and report list (pp.251–252) and Curtis's No. 1 dispatches and
  addenda return (pp.252–253);
- the rest of McNeil's No. 3 papers (April 28 and May 1 dispatches, the May 10 letter and the May
  12 report on the pursuit to Chalk Bluff, pp.256–260);
- Vandever's April 23–29 dispatches, Davidson's indorsement, the addenda orders and the Second
  Division itinerary (pp.271–283).

McNeil's May 12 report covers Chalk Bluff, so AR007 was read in four families; it is not cited
there, to keep the record's evidence within three families, and this is recorded in AR007's open
questions. Curtis's return was read while locating reports. No targeted follow-up was used. Stop
after this batch.

**Consequential gap.** McNeil's own report of the Cape Girardeau action is not in the volume's
selected papers (his May 10 letter says it would follow); the two April 26 dispatches are his
only inspected account of the action. The Union brigade and battery reports (Nos. 4, 9–10) were
not read.

**New source records.** This pass adds **7 records**: two NPS HTML/text pairs and the McNeil,
Vandever and Marmaduke selections. The McNeil selection reuses by name the group
`mcneil-kirksville-1862-reports` that the parallel Trans-Mississippi 1862 pass gives the same author;
Vandever has a new group; Marmaduke's selection is in the new `marmaduke-1863-reports` group shared
with his January 1863 and Pine Bluff selections.

## Decisions and limits

- **Scope.** The Patterson and Fredericktown skirmishes (April 20–22), Vandever's night attack
  near Jackson (April 26) and the rear-guard fighting to Bloomfield (April 27–30) are context. At
  Chalk Bluff the May 1 fighting on the road and the May 2 crossing are one record.
- **Opening strengths remain unknown.** Both frozen records have blank bounds; the live Cape
  Girardeau page gives 2000 (US 2000; CS 0) and the Chalk Bluff page zero. Figures recorded and
  not adopted:
  - McNeil's 8,000 for the attackers; Marmaduke's own 5,000 with ten guns, of whom 1,200 were
    unarmed and 900 dismounted, his estimate of McNeil's 2,000 at Bloomfield and of 3,000 in the
    Cape Girardeau works; NPS's 2,000, apparently for McNeil.
  - Chalk Bluff: Vandever's 7,000 or 8,000 for the enemy; Marmaduke's effective 3,500 against an
    estimated 8,000 with fifteen guns.
- **Disputes preserved.**
  - Cape Girardeau's character: McNeil's repulsed attack against Marmaduke's demonstration that
    "amounted almost to an attack".
  - Cape Girardeau losses: the frozen and live 337 (CS 325) have no inspected basis; Marmaduke's
    some 30 killed, 60 wounded (read "GO") and 120 missing cover the whole expedition and are not
    assigned.
  - Chalk Bluff result: the frozen Confederate tactical victory with a Union strategic gloss;
    Marmaduke's safe crossing against Vandever's heavy loss inflicted. The strategic gloss is
    campaign contribution.
  - Chalk Bluff losses: the frozen Unknown and live zero; Vandever's "will not exceed 50" (scope
    possibly the whole pursuit), one officer killed by a Union shell, and 19 enemy dead after one
    charge (place unstated).
- **Command roles and ranks.**
  - The live pages list Marmaduke and Vandever without ranks. NPS calls Shelby "John S. Shelby".
  - Vandever says he gave McNeil the advance throughout the pursuit; Marmaduke says he ordered
    Shelby's demonstration and brought Carter's column in support.
  - No listed commander receives automatic sole credit.
- **Tags.** All claims stay `unresolved` or `post_outcome`.

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

MO020 and AR007 are revised under `marmaduke-1863-second-review-correction-2026-09-25` and supersede
byte-for-byte archives at `data/evidence/history/<ID>.v1.json`.

- **R3** (AR007 `casualty-records`): Vandever's May 4 dispatch does not say where Glover's charge
  left 19 enemy dead, and calls the Chalk Bluff engagement of the 2d "also" disastrous. The value
  now gives the place as unnamed and the rationale says the figure may belong to the earlier
  pursuit; two p.278 citations are added.

Advisories:

- **Adopted:** A6 (MO020: NPS "appears to" give McNeil's combined force as about 2,000, since its
  "his" does not name the antecedent; the live US 2000 is noted).

The review correction adds no source records for this campaign. Citations rise from 84 to 86; claims
(18), unknowns (2) and disputed claims are unchanged. No model input, cohort file, admission
proposal or baseline is changed.
