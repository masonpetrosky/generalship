# Expedition to St. John's Bluff: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The
single frozen record in **Expedition to St. John's Bluff [September-October 1862]** now has a
draft dossier: **9 claims, 1 explicit null unknown and 40 citation occurrences**. All seven
dimensions are represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| FL003 — St. John's Bluff | 1862-10-01 to 10-03 | 9 | 1 | 40 | 3 |

This pass was drafted in one batch with eight other Atlantic-coast campaigns. Dossier presence
is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full.
NPS/CWSAC and the Arnold tables are one family. Two further families from *Official Records*
Series I, Volume XIV (registered with Charleston 1862):

- **Brannan's** October 4 and October 13, 1862 reports (No. 1, pp.127–132), by the Union
  expedition commander.
- **Hopkins's** October 8 report and December 24 letter (No. 7, pp.138–142), by the
  Confederate post commander who abandoned the bluff.

Read but not selected: the expedition's summary and report list; Finegan's October 2–3
dispatches and his indorsement blaming Hopkins (No. 6), which is printed between Hopkins's two
papers and is answered in the December 24 letter; and part of the court-of-inquiry inclosures.
Good's, the signal officers', Bacon's and Steedman's naval reports and Samuel Jones's chapter
VII (located by contents only) were not inspected. No targeted follow-up was used. Stop after
this record.

## New source records

This campaign adds **4 records**: the FL003 NPS HTML/text pair and the Brannan and Hopkins
selections.

## Decisions and limits

- **Scope.** The expedition's later occupation of Jacksonville and capture of the Governor
  Milton (October 5–9) are context.
- **Opening strength remains unknown.** The frozen US bound is 1,573; Brannan's October 13 report
  gives effective strengths of 825, 647, 41 and 60, printed "Total 1 573", at the start of the
  expedition, and NPS says about 1,500 infantry. The Confederate side is only "small" in the
  frozen text. Mutual estimates during the action are preserved: Brannan's local reports of
  1,200 Confederate infantry and cavalry and his 300 reinforcements from Fernandina (arriving
  on the 4th); Hopkins's own force of not more than 500 in rear of the batteries, about 110
  dismounted cavalry, and enemy landings of 3,000 (a civilian's report), 2,500 in the main
  column (Chambers) and at least 1,000 more (his own reckoning). None is adopted.
- **Disputes preserved.** Hopkins's decision to abandon the bluff: he says he reconnoitred with a
  glass, held conferences that were unanimous, and did not spike the guns because he had nothing
  to do it with; he quotes Finegan's charge that he failed to reconnoitre. Frozen casualties read
  Unknown and the live field zero; Brannan says the guerrillas did his force no injury.
- **Command roles and ranks.** The frozen commanders are Brigadier General John M. Brannan and
  Lieutenant Colonel Charles F. Hopkins. Brannan ordered Colonel Good forward with the infantry
  and credits Steedman's gunboats. No listed commander receives automatic sole credit.
- **Tags.** All claims stay `unresolved` or `post_outcome`; the Confederate works predate the
  action but are not tagged `inherited`.

The one null unknown is the opening strength. No morale/readiness score, probability, causal
effect or new commander ranking is introduced. The cohort, the admission proposals and the
baseline are unchanged, with zero promoted rows.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the nine
Atlantic-coast first passes (15 dossiers) together at prepared commit `0e6063c` as
`atlantic-review-0e6063c-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": eleven
required findings (R1 to R11) and thirteen advisories (A1 to A13) across the nine passes. It is
an AI review within its stated scope, not human historical adjudication, proof of source
independence or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the registry
record) before any change; every new quote occurs in its cited section, and the dossiers were
regenerated from the builder.

FL003 is revised under `st-johns-bluff-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/FL003.v1.json`.

- **R9** (`command-roles` value): Hopkins's December 24 letter quotes Finegan's charge only on
  reconnaissance; his remarks on the unspiked guns answer the commanding general's
  communication. The value now says he answered Finegan's charge that he had failed to
  reconnoitre, and explained why he had not spiked the guns. This memo's disputes item already
  used that attribution.

Advisories:

- **Not adopted:** A10 (select Finegan's already-read indorsement as the targeted follow-up). It
  would add a new selection and source record; the dispute is visible through Hopkins's reply,
  which quotes the charge, and the indorsement stays recorded as read, not selected.

The review correction adds no source records. Claims (9), unknowns (1), citations (40) and
disputed claims (2) are unchanged. No model input, cohort file, admission proposal or baseline
is changed.

After the review correction, `python3 -m generalship check` and `python3 -m unittest discover -s
tests` pass (134 tests) in the main repository, and `gs.MISSES` is empty.
