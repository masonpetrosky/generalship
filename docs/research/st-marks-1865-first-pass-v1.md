# Operations near St. Marks, 1865: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
frozen record in **Operations near Saint Mark's [March 1865]** now has a draft dossier: **9
claims, 1 explicit null unknown and 49 citation occurrences** (47 before the review correction
below). All seven dimensions are represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| FL006 — Natural Bridge | 1865-03-06 | 9 | 1 | 49 | 2 |

This pass was drafted in one batch with eight other Atlantic-coast campaigns. Dossier presence
is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC
and the Arnold tables are one family. One further family from *Official Records* Series I,
Volume XLIX, Part 1 (1897 imprint; the already registered `or49-1-illinois-ocr-v1`, deduplicated
at merge):

- **Newton's** papers (pp.57–67): the March 15 preliminary report, the April 17 covering letter
  and postscript, the March 19 detailed report, the April 6 letter (to its inclosure), the April
  19 letter and the casualty report dated March 19.

Read but not selected: the operations' summary and report list, the inclosed Special Orders No.
49 of Sam Jones, the newspaper extract, Gibson's March 21 letter, and Weeks's March 9 report on
the East River and Newport bridges. No Confederate report is printed with these operations, and
no history covering Natural Bridge was found (Samuel Jones's *Siege of Charleston* ends in
1863). Two families were inspected (below the three-family ceiling); the naval reports in the
already pinned *Official Records of the Navies* volume 17 were deferred. No targeted follow-up
was used. Stop after this record.

## New source records

This campaign adds **3 records**: the FL006 NPS HTML/text pair and the Newton selection, whose
parent is the already registered Volume XLIX Part 1 OCR (`or49-1-illinois-ocr-v1`); this pass's
byte-identical copy and catalog record were deduplicated at merge.

## Decisions and limits

- **Scope.** The March 4–5 skirmishes at the East River and Newport bridges and the naval
  operations off St. Marks are context.
- **Opening strength remains unknown.** The frozen CS bound is 1,000 and the US bound is blank;
  the live force field reads zero. The frozen CS text appears to follow Newton's April 17
  postscript, which lists the Confederate units named in a Tallahassee newspaper (the frozen
  units occur there in the same order, with three more) and adds over 1,000 Georgia
  reinforcements; the frozen text's basis is not stated. Newton's own figures, recorded with
  date and scope and none adopted: his force 900 to 1,000 (March 15) or 893 enlisted men (March
  19), only 500 in line when the Georgia troops arrived (April 6); the enemy's local force
  expected at 600 to 700 and increased with pressed men to about 1,000 before the Georgia troops
  arrived (April 6), which the frozen text, tying its 1,000 to the Georgia reinforcements, does
  not distinguish; the enemy 1,500 to 2,000 by report and by a prisoner, over 2,000 in all
  (April 6), over 1,000 at first and reinforced by 1,000 (April 19), and not over 700 available
  when the expedition started (April 19).
- **Disputes preserved.** Result: NPS says the Union troops, unable to take the bridge,
  retreated to the fleet; Newton claims the complete repulse of two charges and a withdrawal in
  order because the navy failed. Casualties: frozen 174 (US 148; CS 26) against live 173 (US 148;
  CS 25); Newton's 150 (March 15) against 148, of whom 35 missing (March 19 and the casualty
  table); no Confederate figure is inspected.
- **Command roles and ranks.** The frozen commanders are Major General John Newton (US) and Major
  General Sam Jones (CS). Newton signs these reports as brigadier general; the live page gives
  Samuel Jones without rank; Newton names Generals Jones and Miller. Newton's blame of the naval
  command change is his own. No listed commander receives automatic sole credit.
- **Tags.** All claims stay `unresolved` or `post_outcome`.

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

FL006 is revised under `st-marks-1865-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/FL006.v1.json`.

- **R11** (this memo): the Volume XLIX Part 1 paragraph and the record count predated the merge
  deduplication. The memo now names the registered parent and gives 3 records, not 5.

Advisories:

- **Adopted:** A9 (this memo: two families were inspected, below the three-family ceiling, and the
  naval reports in ORN 17 were deferred) and A11 (`reported-force-scope`: Newton's April 6 statement
  that the local force he expected at 600 to 700 was increased with pressed men to about 1,000
  before the Georgia troops arrived is added and cited, p.64, and the rationale notes that the
  frozen text ties its 1,000 to the Georgia reinforcements alone).
- **Not adopted:** A12 (the casualty table's section date). The table's section is mapped to
  1865-03-19, but the dateline ("Key West, Fla., March 19, 1865") lies just after the selection's
  end offset in the parent, so the date is not visible in the snapshot. The mapping is correct
  against the parent; the fact is recorded here, and no metadata-only successor of
  `or49-1-newton-natural-bridge-selections-v1` was registered for it.

The review correction adds no source records. Citations rise from 47 to 49; claims (9), unknowns
(1) and disputed claims (3) are unchanged. No model input, cohort file, admission proposal or
baseline is changed.

After the review correction, `python3 -m generalship check` and `python3 -m unittest discover -s
tests` pass (134 tests) in the main repository, and `gs.MISSES` is empty.
