# Demonstration on the Rapidan River: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The one frozen
record in **Demonstration on the Rapidan River [February 1864]** now has a draft dossier: **9 claims,
1 explicit null unknown and 61 citation occurrences**. All seven dimensions are represented. The
dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| VA045 — Morton's Ford | 1864-02-06 to 02-07 | 9 | 1 | 61 | 3 + follow-up |

This pass was drafted alongside the Kilpatrick-Dahlgren Raid, Crook-Averell Raid and Lynchburg
passes ([Kilpatrick-Dahlgren](kilpatrick-dahlgren-1864-first-pass-v1.md),
[Crook-Averell](crook-averell-1864-first-pass-v1.md), [Lynchburg](lynchburg-1864-first-pass-v1.md)).
Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family. The record uses two further families and one targeted follow-up:

- **Humphreys, *From Gettysburg to the Rapidan*** (Scribner, 1883), a new selection from the
  registered parent OCR (`humphreys-ocr-v2`): the winter dispositions, the February 6-7
  demonstration to aid Butler and Wistar's movement (OCR pp.71-74). It follows the parent range
  already selected for Mine Run. Humphreys was chief of staff of the Army of the Potomac, and
  Caldwell's February 6 dispatches were addressed to him.
- **Caldwell's** reports, from *Official Records* Series I, Volume XXXIII (1891 imprint), using the
  registered parent `or33-illinois-ocr-v1` (first registered for Plymouth): the 12.30 p.m. and 2.15
  p.m. dispatches of February 6 and the March 22 report of his division (No. 3, pp.119-120).
- **Targeted follow-up: Lee's** February 8 report (No. 24, p.141), for the Confederate account and
  losses, which no other inspected family gives.

The following were read but not selected:

- Warren's March 23 report with the compiled return of Second Corps casualties and Humphreys'
  February 9 letter (No. 2 and addenda, pp.114-118);
- the First Corps itinerary (No. 1) and Webb's report (No. 4);
- part of Cabell's report on the Confederate artillery (No. 25).

Hays's, Owen's and the regimental reports, the cavalry reports of Merritt and Kilpatrick at
Barnett's and Culpeper Mine Fords, maps and print pages were not inspected. The report list has no
Ewell or other Confederate Second Corps report. Humphreys' *The Virginia Campaign of '64 and '65*
mentions Morton's Ford only for the spring 1864 positions (about p.3 of the registered parent). That
passage was read during the search but not selected. Stop after this record.

This pass adds **five source records**: the NPS HTML/text pair and the Caldwell, Lee and Humphreys
selections. This pass's own copy of Volume XXXIII was byte-identical to the registered parent
`or33-illinois-ocr-v1` and was deduplicated at merge (see `docs/sources.md`).

## Decisions and limits

- **Scope.** The frozen description and live page include the First Corps crossing at Raccoon Ford
  and the cavalry at the upper fords as part of the same demonstration. The inspected passages
  describe Morton's Ford almost exclusively. Butler's simultaneous movement under Wistar toward
  Bottom's Bridge is context, not part of this record.
- **Opening strength remains unknown.** The frozen side bounds are blank and the force field reads
  "Divisions"; the live page gives zeros. Every figure is recorded with its scope, and none is
  adopted:
  - Humphreys: the Second Corps with three batteries at Morton's Ford; a small part of Caldwell's
    force crossed first, then all of Hays's division, with Webb's following.
  - Caldwell: two brigades across at 12.30 p.m. and a division by 2.15 p.m.; 30 or more men in the
    rifle-pits at the ford; prisoners' report of two brigades within 2 miles and probably ten guns.
  - Lee: the ford guard was a lieutenant and 25 men.
  - Wistar's 4,000 infantry and 2,200 cavalry (Humphreys) belong to Butler's separate movement.
- **Disputes preserved.**
  - Command: Humphreys says Caldwell crossed "through some misapprehension of the instructions";
    Caldwell says his instructions directed a demonstration and that he chose to hold rather than
    advance.
  - Result: Lee says the Union force was driven to the river; Humphreys says it was brought back at
    dark. Caldwell calls the demonstration entirely successful if its object was only to make the
    enemy mass in his front.
  - Losses: frozen 723 against live zeros; Humphreys' over 200 killed and wounded in Hays's division;
    Lee's 17 Union dead and 46 prisoners, and his own 4 killed and 20 wounded, with the ford guard
    captured; Caldwell's 26 men and 2 officers taken without loss. The compiled Second Corps return
    was read but not selected.
- **Command roles and ranks.**
  - Caldwell commanded the Second Corps only until Warren arrived between 4 and 5 p.m. Humphreys
    places the sharp fight toward sunset; read together the two suggest it followed Warren's
    arrival, but their times are not synchronized. Warren's own report (read, not selected) gives
    his arrival at the ford as about 3 p.m. Caldwell says Hays's division did all the fighting.
  - Ewell's role rests on the NPS sentence that his corps resisted the crossings.
  - Frozen and live ranks agree. No listed commander receives automatic credit.
- **Tags.** The river, ford and winter intrenchments are tagged `inherited`, on Humphreys' account
  of the winter dispositions. Caldwell's artillery dispositions are commander-created and are
  left out of that claim. All other claims stay `unresolved` or `post_outcome`.
- **Families.**
  - Humphreys' selection stays in `humphreys-gettysburg-rapidan-1883`.
  - Caldwell is a new author group, `caldwell-rapidan-1864-reports`.
  - Lee's report is placed in his latest group, `lee-richmond-petersburg-dispatches`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
new commander ranking is introduced. The cohort, admission proposals and baseline are unchanged,
with **zero promoted rows**.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the four 1864
Eastern small-operation first passes (Rapidan, Kilpatrick-Dahlgren, Crook-Averell and Lynchburg)
together at prepared commit `8642430` as `e1864-review-8642430-opus-high-v1` on 2026-09-25. Its
outcome was "corrections required": seven required findings (E1864-R1 to E1864-R7) and thirteen
advisories (E1864-A1 to E1864-A13) across the four passes. It is an AI review within its stated
scope, not human historical adjudication, proof of source independence or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the registry
record) before any change; every new quote occurs in its cited section, and the dossiers were
regenerated from the builder. After the correction, `python3 -m generalship check` passes,
`python3 -m unittest discover -s tests` passes (134 tests) and `gs.MISSES` is empty.

VA045 is revised under `rapidan-1864-review-correction-2026-09-25` and supersedes the byte-for-byte
archive at `data/evidence/history/VA045.v1.json`.

- **E1864-R1** (this memo): the Caldwell paragraph and the record count predated the merge
  deduplication of Volume XXXIII. The memo now names the registered parent `or33-illinois-ocr-v1`
  and gives five records, not seven.

Advisories:

- **Adopted:** E1864-A1 (VA045 `command-roles` and this memo): the rationale no longer synchronizes
  Caldwell's 4-5 p.m. and Humphreys' "toward sunset"; it says the two suggest the heaviest fighting
  followed Warren's arrival without a common clock. A new open question records, uncited, that
  Warren's report (read, not selected) gives his arrival at the ford as about 3 p.m. and places
  Humphreys on the field at night-fall, which bears on Humphreys' standing as a participant witness.
- **Not adopted:** E1864-A6 (the Humphreys record's note names Volume XXVII rather than XXXIII; its
  conclusion of no dependence on the printed compilation still holds): registry records are
  immutable and the advisory is optional; the finding is left to any future metadata-only revision.

The review correction adds no source records for this campaign. Claims (9), unknowns (1),
citations (61) and disputed claims are unchanged. No model input, cohort file, admission proposal
or baseline is changed.
