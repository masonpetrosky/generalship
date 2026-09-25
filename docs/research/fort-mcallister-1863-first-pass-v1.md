# Naval Attacks on Fort McAllister, March 1863: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
frozen record in **Naval Attacks on Fort McAllister [March 1863]** now has a draft dossier: **9
claims, 1 explicit null unknown and 47 citation occurrences** (42 before the review correction
below). All seven dimensions are represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| GA002 — Fort McAllister I | 1863-03-03 | 9 | 1 | 47 | 3 |

This pass was drafted in one batch with eight other Atlantic-coast campaigns. Dossier presence
is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full.
NPS/CWSAC and the Arnold tables are one family. Two further families from newly pinned
*Official Records of the Navies* Series I, Volume 13 (1901 imprint; Thomas J. Bata Library,
Trent University copy digitized 2019; `orn13-trent-ocr-v1`):

- **Drayton's** detailed report to Du Pont (pp.717–719), headed "March 1863" with the day lost
  in OCR (date mapped null), and his March 8 report to the Bureau of Ordnance (pp.725–728).
- **McCrady's** report and two tables (pp.730–734), by the Confederate chief engineer of
  Georgia, founded by its own statement on Assistant Engineer McAlpin's notes and the fort
  officers' statements. Its heading's day reads "March <§" (date mapped null), and its text
  dates the attack "Tuesday, March 8" in OCR, while its tables in the same section date it March
  3, 1863.

Read but not selected: Du Pont's March 6 transmittal and March 7 papers, Miller's report of the
Passaic's injuries, Stimers's telegram and Harris's March 9 covering letter (pp.716–730). In
*Official Records* Series I, Volume XIV, the March 3 report list and Beauregard's March 3–4
dispatches were read but not selected. Ammen's and Downes's reports, the abstract logs and
Samuel Jones's chapter IX were not inspected. No targeted follow-up was used. Stop after this
record.

## New source records

This campaign adds **6 records**: the GA002 NPS HTML/text pair, the Navies volume 13 catalog
metadata and full OCR (also the parent of the Rhind selection for Simmon's Bluff), and the
Drayton and McCrady selections.

## Decisions and limits

- **Scope.** The January 27, February 1 and February 28 attacks and the mortar fire of the night
  of March 3–4 are context.
- **Opening strength remains unknown.** The frozen bounds are blank and the live force field
  reads zero. Only vessel and gun counts exist: three monitors in action with mortar schooners
  and gunboats in support (Drayton), a fourth monitor not engaged (McCrady), and the fort's
  seven guns and a mortar (Drayton), the guns McCrady names, or "a small three-gun earthwork
  battery" (NPS). No personnel figure; none is adopted.
- **Disputes preserved.**
  - Range: about 1,200 yards (Drayton's calculation), a thousand (the pilot), 1,400 to 1,900
    (McCrady).
  - Armament: seven guns and a mortar (Drayton), at least six named pieces (McCrady) and three
    guns (NPS); the force claim is now `disputed`.
  - Casualties: frozen Unknown, live CS 1, McCrady's two men slightly wounded; McCrady also
    reports that riflemen in the marsh shot an officer stepping out of monitor No. 1's turret;
    Drayton's selected reports list damage to the Passaic but no casualties.
  - McCrady identifies the monitor under fire as the Montauk; the compiler's footnote says the
    Montauk was not in action. McCrady's report text reads "Tuesday, March 8" in OCR, but his
    tables in the same section and Drayton's ordnance report date the action March 3, matching
    the frozen date.
- **Command roles and ranks.** The frozen commanders are Captain P. Drayton (US navy) and Captain
  George A. Anderson (CS); McCrady's text gives Captain [G. W.] Anderson with the compiler's
  bracketed initials, and the live page Major George Anderson. The live rank is not adopted. No
  listed commander receives automatic sole credit.
- **Objectives.** NPS says the attack was to test the ironclads and give gunnery practice; Du
  Pont's own statement of that aim was read but not selected, so the aim is cited from NPS and
  Drayton's reports.
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

GA002 is revised under `fort-mcallister-1863-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/GA002.v1.json`.

- **R3** (`reported-force-scope`): NPS calls the fort "then a small three-gun earthwork battery",
  against Drayton's seven guns and a mortar and McCrady's named pieces. The NPS phrase is cited and
  added to the value, and the claim is now `disputed`.
- **R4** (`recorded-result` and this memo): McCrady's tables (p.734) and Drayton's March 8 ordnance
  report (p.725) date the action March 3; both are cited, and the value's last sentence and the
  memo's date item now say so.
- **R5** (`observation-and-identification`): the passage identifying monitor No. 1 ("No. 1 is
  supposed to be the Montauk", p.732) is now cited beside the turret-flag passage.
- **R6** (`casualty-records`): McCrady's report that riflemen shot an officer stepping out of monitor
  No. 1's turret is added and cited (p.732) against the live US 0.

Advisories:

- **Not adopted:** A7 (a metadata-only revision of the McCrady record's dependency note to add the
  tables' March 3 dating). The note is accurate as far as it goes and the record is immutable; the
  dossier and this memo now carry the tables' date, and the section date stays null.

The review correction adds no source records. Citations rise from 42 to 47; claims (9) and
unknowns (1) are unchanged; disputed claims rise from 2 to 3. No model input, cohort file,
admission proposal or baseline is changed.

After the review correction, `python3 -m generalship check` and `python3 -m unittest discover -s
tests` pass (134 tests) in the main repository, and `gs.MISSES` is empty.
