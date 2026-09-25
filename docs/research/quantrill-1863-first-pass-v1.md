# Quantrill's Raid into Kansas: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The one
**frozen record** in **Quantrill's Raid into Kansas [August 1863]** now has a draft dossier:
**9 claims, 1 explicit null unknown and 47 citation occurrences**. All seven dimensions are
represented. The dossier remains a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| KS001 — Lawrence | 1863-08-21 | 9 | 1 | 47 | 3 |

It changes no other dossier. Dossier presence is not first-pass acceptance, separate review or
model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family. Two further families:

- **Britton, *The Civil War on the Border*, volume II** (Putnam's, 1899), from the registered
  parent, with a new selection from Chapter X, The Lawrence Massacre: from the Kansas incursions
  into Missouri and Ewing's reports of guerrilla threats through the raid, the pursuit and
  Britton's account of the failures that made it possible (OCR pp.135–145). Britton relays
  Ewing's, Lazear's, Clark's and Pike's reports, so he is not independent of the Ewing family.
- **Ewing's** August 31, 1863 report (*Official Records* Series I, Volume XXII, Part 1, No. 2,
  pp.579–585), with A. R. Banks's August 21 dispatch from Lawrence printed as its inclosure. Banks
  is a separate writer, selected as a separate section and not counted as a further family. Ewing
  wrote while detachments were still out and was at Leavenworth on the 20th and 21st.

The following were read but not selected: the rest of Britton's Chapter X (the earlier guerrilla
war, pp.127–135, and the aftermath, Order No. 11 and the Paola meeting, pp.145–148); the raid's
summary and report list (p.572); and the opening of Schofield's No. 1 transmittal. Clark's,
Lazear's, Thacher's, Coleman's, Ballinger's, Leland's and King's reports (Nos. 3–9) were located
by heading only. No targeted follow-up was used. Stop after this batch.

**Consequential gap.** No guerrilla or Confederate account of the raid was located in the
inspected volume, and no list of the Lawrence dead was inspected. The only Confederate-side
figure is the NPS/CWSAC one.

**New source records.** This pass adds **4 records**: one NPS HTML/text pair and the Britton
and Ewing selections.

## Decisions and limits

- **Scope.** The approach march of August 19–20, the pursuit through Paola to Grand River
  (August 21–22), later guerrilla deaths and Order No. 11 are context. Most of the dead were
  unarmed civilians; they are recorded as reported and are not treated as ordinary combat
  casualties.
- **Opening strengths remain unknown.** The frozen bounds are blank; the live field gives 350
  and the live description 300 to 400. Figures recorded and not adopted: Ewing's about 300 (about
  250 assembled first and about 50 joining on the 20th); Banks's about 200; Britton's three
  hundred and Pike's first report of as many as seven hundred. Ewing's 500 men Lawrence "could
  have" mustered is counterfactual. The frozen "No Union troops" is recorded; Ewing says 14
  recruits of the Fourteenth Kansas and 20 of the Second Kansas Colored were among the murdered,
  who were unarmed.
- **Disputes preserved.**
  - Losses: frozen 204 (US 164; CS 40) against live 150 (US 150; CS 0); Ewing's and Britton's
    140 killed and Ewing's about 24 wounded; Banks's same-day "about GO" (60) citizens; Ewing's
    claim that at least as many raiders had been killed since, which belongs to later actions.
  - The frozen and live "Confederate victory" labels a raid on an undefended town; this is
    recorded in the result rationale.
- **Command roles and ranks.**
  - The frozen commander is Lieutenant Colonel William C. Quantrill; no Union commander is listed.
    The live page styles Quantrill a Colonel; it is not adopted.
  - Ewing blames Pike's failure to pursue and Clark's slowness; Britton calls Pike's failure the
    first fatal blunder. Lane led a party of citizens in the pursuit.
  - No listed commander receives automatic sole credit.
- **Tags.** All claims stay `unresolved` or `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect
or new commander ranking is introduced. No model input, cohort file, admission proposal or
baseline is changed.

## Validation

`python3 -m generalship check` passes, and `python3 -m unittest discover -s tests` passes.
Every quote occurs in its cited section; the builder's miss list is empty.

## Separate review pending

No separate review has been run for this pass. Coverage, separate review and feature
admission stay distinct.
