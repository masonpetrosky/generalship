# Wilson's Raid in Alabama and Georgia: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
frozen record in **Wilson's Raid in Alabama and Georgia [April 1865]** now has a draft dossier:
**9 claims, 1 explicit null unknown and 46 citation occurrences** (45 before the review
correction below). All seven dimensions are
represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| AL007 — Selma | 1865-04-02 | 9 | 1 | 46 | 3 |

Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family. Two further families:

- **Wilson's** reports (Official Records Series I, Volume XLIX, Part 1) are the Union report
  family.
  - Selected: the summary report of May 3, 1865 from Macon (pp.349–353) and the Selma passage
    of the detailed report (pp.359–361). The detailed report's heading and date are garbled in
    OCR, so its date is mapped null.
  - Read but not selected: the rest of the detailed report through Columbus and West Point, the
    short transmittal and part of Thomas's report.
  - The OCR is badly garbled at line starts and ends, and the detailed report's list of captures
    at Selma is largely unreadable.
  - The Volume XLIX Part 1 parent is registered once with the Mobile Campaign pass.
- **Jordan and Pryor, *The Campaigns of Lieut.-Gen. N. B. Forrest*** (1868) is a retrospective
  Confederate history written from Forrest's papers. It is already registered
  (`jordan-pryor-forrest-ocr-v1`), and a second selection from that parent was made.
  - Selected: Chapter XXIV from the night of March 31 through the fall of Selma (OCR
    pp.664–676).
  - It is not independent of Forrest, and it cites Andrews's *History of the Campaign of Mobile*.

Not inspected:

- Long's, Upton's, Minty's and Miller's reports and the Second Division casualty returns;
- Chalmers's and Armstrong's accounts;
- Andrews's chapters on Wilson's raid, a different family registered for the Mobile Campaign;
- a second scan of Volume XLIX.

The Wilson's Raid report list in this OCR is garbled. The Confederate reports that can be made out
near its end are Daniel W. Adams's (No. 39) and a Tuscaloosa post report (No. 40); neither was
inspected, and no Forrest report was found. No targeted follow-up was used. Stop after this
record.

**Consequential gap.** The legible casualty figures are fragmentary. Wilson's own figures are
largely unreadable in this OCR, and Jordan gives none for Selma.

This pass adds **4 source records**:

- the NPS HTML/text pair;
- a second Jordan and Pryor selection (existing group `jordan-pryor-forrest-1868`);
- the Wilson selection (new group `wilson-selma-1865-reports`), whose parent is the Volume XLIX
  Part 1 OCR registered with the Mobile Campaign pass (`or49-1-illinois-ocr-v1`).

Same-author groups are one witness family under the `docs/sources.md` rule: this group and
`wilson-south-side-raid-reports` (Petersburg, 1864) are both James H. Wilson's reports.

## Decisions and limits

- **Scope.** The following are context, not added:
  - the march from Chickasaw;
  - the April 1 action at Ebenezer Church;
  - Croxton's and McCook's detached operations;
  - Chalmers's attack on Long's rear;
  - the later captures of Montgomery, Columbus, West Point and Macon.
- **The opening strength remains unknown.** The frozen Confederate bound is 5,000 ("troops in
  city (approx. 5,000 men)"), and the Union bound is blank. Every figure below is recorded with
  its scope, and none is adopted:
  - NPS live: 18,500 (US 13,500; CS 5,000), with 13,500 given for the raid's start;
  - Wilson: Long's assault with 1,160 men against Armstrong's brigade of nearly 1,500;
  - Jordan: Wilson's column at least 9,000 after detaching McCook, and the defenders as
    Armstrong's brigade of about 1,400 plus some 1,700 of Roddy's men and others.
- **Disputes preserved.**
  - Strength: 5,000 against Jordan's 1,400 plus 1,700.
  - The distance charged: 500 yards in Wilson's May 3 report against 600 yards in his detailed
    report.
  - The extent of the works: a radius of nearly three miles (Wilson) against a trace of nearly
    four miles (Jordan).
  - Taylor's escape: NPS says Taylor escaped with Forrest; Jordan says Taylor left by rail at
    2 p.m., before the assault; Wilson's May 3 OCR reads that Taylor "had left at3", the time
    garbled.
  - Casualties: frozen 3,019 (US 319) against live 3,059 (US 359). Wilson's partly legible
    "46 killed" (Long's division) and a prisoner count garbled as "t’loosaod seven hundred …
    including 150", whose thousands figure is illegible, so it is not recorded as disagreeing
    with the frozen CS 2,700.
- **Command roles and ranks.** Wilson credits Long with opening the assault without waiting for
  the signal. Jordan has Forrest take command on Taylor's departure and order Roddy to fill the
  breach. The live page gives Wilson as Brigadier General and Forrest as Major General; the frozen
  ranks are kept. No listed commander receives automatic sole credit.
- **Tags.** No claim is tagged `inherited`. All stay `unresolved` or `post_outcome`.

The one null unknown is the opening strength. No morale/readiness score, probability, causal
effect or new commander ranking is introduced. The cohort, both admission proposals and the
baseline are unchanged.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed commit
`5d5bc1c` as `price-review-5d5bc1c-opus-high-v1` on 2026-09-25, together with the Price's
Missouri, Mobile Bay and Mobile passes. Its outcome was "corrections required" (four required
findings and nine advisories across the four passes). It is an AI review within its stated
scope, not human historical adjudication, proof of source independence or feature admission.

## Review correction

AL007 is revised under `wilson-raid-review-correction-2026-09-25` and supersedes the
byte-for-byte archive `data/evidence/history/AL007.v1.json`.

- **PRV-R3** (required; holds and applied): the May 3 OCR reads "t’loosaod seven hundred
  prisoners, including 150" (p.351). The dossier and this memo had dropped the legible
  "t’loosaod" and added "officers", which the OCR does not show. The `casualty-records` value now
  quotes the reading and says the thousands figure and the word after 150 are illegible; the
  memo no longer frames it as a dispute with the frozen CS 2,700.
- **PRV-A5** (adopted): Wilson's garbled "Taylor had left at3" is cited in `recorded-result` and
  noted as a third account above.
- **PRV-A4** (recorded, no registry change): the same-author link to
  `wilson-south-side-raid-reports` is noted above; the v1 Wilson selection record stays
  unchanged.

Citations rise from 45 to 46; claims (9), unknowns (1) and disputed claims (4) are unchanged.
No model input, cohort file, admission proposal or baseline is changed.
