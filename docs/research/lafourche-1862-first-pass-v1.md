# Operations in LaFourche District: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
**frozen record** in **Operations in LaFourche District [October 1862]** now has a draft dossier:
**9 claims, 1 explicit null unknown and 47 citation occurrences**. All seven dimensions are
represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| LA005 — Georgia Landing | 1862-10-27 | 9 | 1 | 47 | 3 |

This pass was drafted alongside the other 1862-1863 Louisiana campaigns. Existing dossiers,
reviews and historical revisions are unchanged. Dossier presence is not first-pass acceptance,
separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family. The record uses two further families:

- **Irwin, *History of the Nineteenth Army Corps*** (Putnam's, 1892), already registered. A new
  selection (`irwin-lafourche-1862-selections-v1`) reuses the registered parent
  `irwin-nineteenth-corps-ocr-v1`: Chapter IV from the formation of Weitzel's Reserve Brigade to the
  Union casualty total (OCR pp.45-48). Irwin gives Mouton's strength and loss figures from Mouton's
  report, so it is not independent of it.
- **Mouton's** report of November 4, 1862 (*Official Records* Series I, Volume XV, No. 5,
  pp.176-180), from the Volume XV parent pinned in the Baton Rouge pass. The report also covers the
  Berwick Bay and Cotton actions of November 1-3.

Taylor's No. 4 transmittal of November 9 (pp.174-176) and the rest of Irwin's Chapter IV were read
but not selected. Butler's No. 1 (opening only seen) and Weitzel's No. 2 reports, Vance's No. 3, the
Union nominal lists, the naval reports and print pages were not inspected. No targeted follow-up
was used. Stop after this batch.

**Consequential gap.** No Union strength return was inspected; the 4,000 in the live field and NPS
has no basis in the inspected passages, and Mouton's figures for the enemy are estimates.

**New source records.** This pass adds **4 source records**: one NPS HTML/text pair, the Mouton
selection and the Irwin Georgia Landing selection (reusing the registered parent). It uses the OR
Volume XV parent registered in the Baton Rouge pass.

## Decisions and limits

- **Scope.** The landing at Donaldsonville on October 25-26, the evacuation to Berwick Bay by
  October 30 and the gunboat actions of November 1-5 are context. The live campaign label reads
  Operations in Lafourche District.
- **Opening strength remains unknown.** The frozen Confederate bound is 1,392 and the Union bound
  blank. Every figure is recorded with its date and scope, and none is adopted:
  - Mouton's return-based table: 1,392 on both banks (the 33d Regiment 594, the 2d Louisiana
    Cavalry 150); Irwin repeats the total.
  - Mouton's estimates of the enemy: 2,500-3,000 infantry, 250 cavalry and two batteries (from
    Vincent); 1,500-1,800 on each bank; about 2,000 infantry, 100 cavalry and a battery at the
    close of the day against his own barely 1,000.
  - NPS and the live field: a brigade of about 4,000 (US 4000; CS 1392).
  - Irwin: the outlying La Fourche regiment of 500 and 300 of the 33d.
- **Disputes preserved.** The Union strength (NPS 4,000 against Mouton's estimates). Losses: the
  frozen and live 315 (US 86; CS 229) against Mouton's 199 (5 killed, 8 wounded, 186 missing) and his
  estimate of 250-300 Union, and Weitzel's claims reported by Irwin (208 prisoners; 18 killed, 74
  wounded and 5 missing, 97 in all). The manner of the right-bank withdrawal: Mouton says "they"
  fell back in some confusion owing to the loss of their commander after Ralston's battery was
  disabled (Ralston, commanding the battery, was wounded and captured), and that Armant, who
  commanded the troops, fell back in perfect order; whose withdrawal was confused is not clear.
- **Command roles.** Mouton says Colonel Armant of the Eighteenth, which was on the right bank,
  "commanded the troops"; Weitzel pursued. No listed
  commander receives automatic sole credit.
- **Tags.** All claims stay `unresolved` or `post_outcome`.
- **Families.** Irwin stays in `irwin-nineteenth-corps-1892`. Mouton is placed in
  `mouton-la-fourche-1862-report`; he had no earlier registry group.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
new commander ranking is introduced. The cohort, both admission proposals and the baseline are
unchanged, with **zero promoted rows**. `python3 -m generalship check` passes, the unit tests pass,
and the baseline still reports **23/127 eligible engagements in 13 groups**, with strength Brier
**0.276882** against **0.250000** for equal odds.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the six
Gulf and Louisiana 1862-63 passes together at commit `be711a9` as
`gulf-review-be711a9-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": four
required findings (R1 to R4) and ten advisories (A1 to A10). It is an AI review within its stated
scope, not human historical adjudication, proof of source independence or feature admission.

## Review correction

Each finding was checked against the retained selection text or the registry before any change;
every new quote occurs in its section, and the dossiers were regenerated from the builder.
LA005 is revised under `lafourche-1862-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/LA005.v1.json`.

- **R1** (LA005 `recorded-result` and this memo): accepted. Mouton's p.177 "they were compelled to
  fall back, which was done in some confusion, owing to the loss of their commander" follows the
  disabling of Ralston's battery, and p.178 reports Ralston wounded and captured and Armant
  "falling back in perfect order". The value now keeps both statements as written; the rationale
  says whose withdrawal was confused is not clear. Three citations added (the review's two and the
  p.177 battery clause).
- **R2-R4** apply to other passes.

Advisories affecting this pass:

- **A8 adopted** (LA005 `open_questions`): Irwin is described as styled on the OCR title page
  assistant adjutant-general, not as the corps' "later" one.
- The other advisories apply to other passes.

The review correction adds no source record for this pass. Citations rise from 44 to 47; claims
(9) and unknowns (1) are unchanged. No model input, cohort file, admission proposal or baseline is
changed.
