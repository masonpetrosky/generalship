# Operations on the White River (1862): bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
**frozen record** in **Operations on the White River [June 1862]** now has a draft dossier: **10
claims, 1 explicit null unknown and 62 citation occurrences**. All seven dimensions are
represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| AR002 — Saint Charles | 1862-06-17 | 10 | 1 | 62 | 3 + 1 follow-up |

Drafted alongside the [Cache River](cache-river-1862-first-pass-v1.md) and
[Boston Mountains](boston-mountains-1862-first-pass-v1.md) passes, whose *Official Records* Volume
XIII parent and Hindman selection it uses. Existing dossiers, reviews and historical revisions
are unchanged. Dossier presence is not first-pass acceptance, separate review or model
eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family. The OR Volume XIII parent (`or13-illinois-ocr-v1`) is
registered with the Boston Mountains pass. Its White River chapter (Nos. 1–4) and the appendix
Saint Charles list were read.

- **Fitch** (`fitch-white-river-1862-reports`): June 17 and June 19, 1862 reports (pp.103–105),
  read in full. His June 24 and 28 reports were read at their openings and not selected.
- **Dunnington** (`dunnington-saint-charles-1862-report`): June 21, 1862 report, printed in the
  appendix (pp.929–931), read in full. He was the senior Confederate naval officer at Saint Charles
  in Fry's absence. Williams's No. 2 report was read at its opening and not selected.
- **Targeted follow-up: Hindman's** general report dated June 19, 1863 (Saint Charles passage,
  pp.34–36, now cited from `or13-hindman-cache-river-selections-v2`, the metadata-only successor of
  v1; see TM-R3). It fills the gap left by Dunnington, who gives no count of Confederate personnel.
  Hindman was not present. He refers for particulars to an unnamed earlier detailed report, and his
  personnel figures do not appear in Dunnington's report, so their basis is unestablished; he is not
  an eyewitness and is not counted as independent corroboration. The selection sits in the author's
  existing group, `hindman-mclemores-cove-reports`.

Not inspected:

- Davis's and Shirk's naval reports and the miscellaneous correspondence (Nos. 2–4);
- Kilty's report and the *Official Records of the Union and Confederate Navies*;
- the Mound City casualty lists and maps.

No Scribner or comparable 19th-century history of this action was used. Stop after this batch.

The pass adds **4 source records**:

- one NPS HTML/text pair;
- two OR XIII selections (Fitch, Dunnington).

## Decisions and limits

- **Scope.** Fitch's later movements upriver and the Clarendon repulse are context.
- **Opening strength remains unknown.** The frozen bounds are blank and the live field reads zero.
  The frozen force text gives "fifty men and C.S. boats". The inspected figures are:
  - Fitch: infantry of unknown numbers supporting the batteries;
  - Dunnington: a list of guns, and two gunboats, a tug and two transports reported by pickets;
  - Hindman: 1,000 to 1,500 Union infantry, and a defence of 79 sailors and 35 armed infantry.

  None is adopted.
- **Disputes preserved.**
  - Losses: frozen 290 (US 135; CS 155) against live 200 (US 160; CS 40).
    - NPS: more than 125 Mound City sailors killed.
    - Fitch: no land troops killed; half or more of a Mound City crew of over a hundred dead;
      7 or 8, or 8 or 9, Confederate dead; about 30 prisoners.
    - Dunnington: about 3 Confederate losses before the retreat.
    - Hindman: 6 killed, 1 wounded, 8 missing, and 180 Union dead on the Mound City.
  - Guns captured: Fitch's 8 against the six Hindman places in battery. Dunnington names more
    pieces.
  - Firing on the Mound City's crew in the water: Fitch reports a prisoner's charge that Fry
    ordered it and Fry's denial. Dunnington says "our own men were directed" to fire and does not
    name who directed it. This is kept as a separate disputed responsibility claim and is not
    adjudicated.
- **Command roles and ranks.** The frozen rows list Fry (Captain, navy), Fitch (Colonel) and Kilty
  (Commander, navy); Fitch styles Fry colonel. Kilty chose to engage with the gunboats first, and
  Fitch signaled a cease-fire before the infantry assault. No listed commander receives automatic
  sole credit.
- **Tags.** The obstructions were placed the night before. All claims are `unresolved` or
  `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
new commander ranking is introduced. The cohort, admission proposals and baseline are unchanged,
with zero promoted rows.

## Validation

`python3 -m generalship check` passes. Every quote occurs in its cited section, and `gs.MISSES` is
empty. `python3 -m unittest discover -s tests` passes (134 tests).
After the review correction, both pass again (134 tests) in the main repository, and
`gs.MISSES` is empty.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the five 1862
Trans-Mississippi and New Mexico first passes together at prepared commit `3d36bfe` as
`tm1862-review-3d36bfe-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": six
required findings (TM-R1 to TM-R6) and eight advisories (TM-A1 to TM-A8) across the five passes.
It is an AI review within its stated scope, not human historical adjudication, proof of source
independence or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the registry
record) before any change; every new quote occurs in its cited section, and the dossiers were
regenerated from the builder.

AR002 is revised under `white-river-1862-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/AR002.v1.json`.

- **TM-R3** (AR002, the Hindman registry record and this memo): Hindman refers for particulars to
  "the detailed report of the engagement heretofore forwarded" without naming its author, and his
  79 crewmen and 35 armed men do not appear in Dunnington's report. The dependency note is corrected
  in the metadata-only successor `or13-hindman-cache-river-selections-v2` (same raw bytes, ranges
  and group), registered with the Cache River correction; AR002's 11 Hindman citations are
  repointed to it, and its last open question and this memo now use the corrected wording.

The review correction adds no source record for this campaign beyond the shared Hindman successor.
Claims (10), unknowns (1), citations (62) and disputed claims are unchanged. No model input, cohort
file, admission proposal or baseline is changed.
