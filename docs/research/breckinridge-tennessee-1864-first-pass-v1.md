# Breckinridge's Advance into East Tennessee (November 1864): bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The only frozen record
in **Breckenridge's Advance into East Tennessee [November 1864]** (frozen spelling) now has a draft dossier:
**9 claims, 1 explicit null unknown and 51 citation occurrences** (48 before the review correction below). All
seven dimensions are represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| TN033 — Bull's Gap | 1864-11-11 to 11-13 | 9 | 1 | 51 | 3 |

Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. Its Description field is
empty, so the frozen Arnold description stands for the NPS/CWSAC narrative (one family). The summary of events
and list of reports (Nos. 1–8) in the registered *Official Records* Series I, Volume XXXIX, Part 1
(`or39-1-illinois-ocr-v1`; catalog volume v.39:1, OCR title checked) were read.

- **Alvan C. Gillem** (No. 3): his November 16 report to Governor Johnson (pp.888–892).
- **John C. Breckinridge** (No. 4): the November 17 dispatch from Strawberry Plains (context only) and the
  November 29 report (pp.892–893).

Thomas's No. 1 relay of Gillem's November 15 telegram and Ammen's No. 2 dispatches were read and not selected.
Vaughn's, Duke's, Palmer's and Tool's reports (Nos. 5–8) were not inspected. No targeted follow-up was used.
Stop after this record.

## New source records

This pass adds **4 source records**: the NPS HTML/text pair for TN033 and two selections from the registered
Volume XXXIX Part 1 parent:

- `or39-1-gillem-bulls-gap-selections-v1`, new group `gillem-1864-reports`;
- `or39-1-breckinridge-bulls-gap-selections-v1`, placed in Breckinridge's existing group
  `breckinridge-baton-rouge-1862-report` (registered in the main repository by another pass).

The Stoneman pass's Breckinridge selection is placed in the same group.

## Decisions and limits

- **Scope.** The frozen interval covers the attacks of the 11th and 12th and the firing of the 13th. The
  following are context, and their losses and captures are not assigned to this record:
  - the Union evacuation on the night of the 13th;
  - the night attack and rout near Russellville and Morristown on the 14th;
  - Strawberry Plains (16th–17th).
- **Opening strength remains unknown.** The frozen Confederate bound is 2,400; the frozen Union bound is blank;
  the live field reads "0 total (US ; CS ;)". Figures recorded, none adopted:
  - Breckinridge: about 1,800 men and six howitzers, later joined by Palmer's some 600 (read "GOO"), against
    about 2,500 with six guns;
  - Gillem: Breckinridge's force much superior to his; Ammen's belief that only 1,200 were advancing; about
    2,500–3,000 at Morristown on the 14th.
  Gillem gives no count of his own brigade in the selected report.
- **Disputes preserved.**
  - The 11th: Gillem says the morning attack was repulsed by 11 a.m. Breckinridge says that on the evening of
    the 11th the Union rearguard was driven into the gap after a short engagement. That date conflicts with
    Gillem's arrival at the gap at 7 a.m. on the 10th and the attack on the morning of the 11th (printed "10th
    [11th]"); it is kept and not reconciled.
  - The 12th: Breckinridge says his mountain force carried a line of works but the assault as a whole
    failed. Gillem says the attackers left 27 dead before his lines.
  - Withdrawal date: the frozen description dates the Union withdrawal "after midnight on the 4th", which
    does not fit the frozen dates; it is not adopted.
  - Casualties: the frozen "Total unknown (US 241; CS unknown)" against the live 424 (US 324; CS 100). No
    inspected source gives either. Gillem's retreat losses of the 14th (6 guns, 61 wagons read "G1", 71
    ambulances, about 300 horses, probably about 150 men) are context and are not added.
- **Command roles and ranks.** The live page styles Gillem Major General against the frozen Brigadier General;
  the live rank is not adopted. Gillem's blame of Ammen for want of supplies and support is recorded as his
  statement. Breckinridge's report says passively that an attack for the next morning "was arranged", with
  himself to lead the force on the mountain. No listed commander receives automatic sole credit.
- **Tags.** Gillem's works were thrown up on the 10th. No claim is tagged `inherited`; all stay `unresolved`
  or `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or new
commander ranking is introduced. The cohort, both admission proposals and the baseline are unchanged.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the fifteen 1864
Western small-operation first passes (ten campaigns) together at prepared commit `4986724` as
`w1864-review-4986724-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": seven
required findings (KY010-R1, KY011-R1, TN031-R1, VA081-R1, VA082-R1, TN030-R1 and GA006-R1) and
eighteen advisories (A1 to A18) across the ten passes. It is an AI review within its stated scope, not
human historical adjudication, proof of source independence or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the frozen row,
the registry record or the pinned parent OCR) before any change; every new quote occurs in its cited
section, and the dossiers were regenerated from the builder. After the correction, `python3 -m
generalship check` passes, `python3 -m unittest discover -s tests` passes (134 tests) and
`gs.MISSES` is empty.

TN033 is revised under `breckinridge-tennessee-1864-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/TN033.v1.json`. No required finding concerns this campaign.

Advisories:

- **Adopted:** A16 (TN033 `recorded-result`, `command-roles` and this memo). The rationale now states that
  Breckinridge's "evening of the 11th" conflicts with Gillem's arrival on the 10th and the attack on the
  morning of the 11th, and cites both passages; the date is kept and not reconciled. `command-roles` now
  follows the report's passive "An attack for the next morning was arranged" rather than "Breckinridge says he
  arranged".
- **No action:** A18 (NPS Campaign fields), already noted in the NPS inspection records and not adopted.

TN033 now has 9 claims, 1 unknown and 51 citations (48 before). The review correction adds no source records
for this campaign. No model input, cohort file, admission proposal or baseline is changed.
