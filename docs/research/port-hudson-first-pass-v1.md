# Siege of Port Hudson: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both **frozen
records** in **Siege of Port Hudson [May-July 1863]** now have draft dossiers: **18 claims, 2
explicit null unknowns and 96 citation occurrences**. All seven dimensions are represented in each
record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| LA009 — Plains Store | 1863-05-21 | 9 | 1 | 39 | 3 |
| LA010 — Port Hudson | 1863-05-21 to 07-09 | 9 | 1 | 57 | 3 |

This pass was drafted alongside the other 1862-1863 Louisiana campaigns. Existing dossiers,
reviews and historical revisions are unchanged. Dossier presence is not first-pass acceptance,
separate review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and the two retained NPS pages in full.
NPS/CWSAC and the Arnold tables are one family. Both records use the same two further families.

- **Irwin, *History of the Nineteenth Army Corps*** (Putnam's, 1892), already registered. A new
  selection (`irwin-port-hudson-selections-v1`) reuses the registered parent
  `irwin-nineteenth-corps-ocr-v1`. Irwin served on Banks's staff during the siege and was named
  a surrender commissioner, so these chapters are partly a participant's account.
  They cite Miles's report and a Confederate surgeon's partial return. Selected:
  - the end of Chapter XV from Banks's departure from New Orleans through Plains Store (OCR
    pp.159-162);
  - Chapter XVI, The Twenty-seventh of May (pp.163-184);
  - the summons, second assault and losses of June 14 (pp.193-201);
  - the besiegers' strength and conditions (pp.216-218);
  - the capitulation, captures and losses (pp.227-234).
- **Miles's** report of May 22 on Plains Store and field reports of May 27, June 14, July 6 and
  July 7, 1863 (*Official Records* Series I, Volume XXVI, Part 1, No. 46, pp.167-177). Volume XXVI
  Part 1 is newly pinned from the University of Illinois scan `warofrebellion261unit` with catalog
  metadata and full OCR. Before use, the catalog volume ("v.26:1") and the OCR title ("SERIES I—
  VOLUME XXVI— IN TWO PARTS. PART I.", 1889 imprint) were checked. Miles commanded a legion and
  later the right wing, not the garrison.

The following were read but not selected:

- the rest of Irwin's Chapter XV and pp.205-208 of Chapter XVII; other pages of Chapters XVII-XVIII
  were seen only as search hits;
- Miles's other field reports of May 24-June 24.

Banks's No. 1 siege reports (opening only seen), the Union returns (No. 2), Dudley's No. 17 report
on Plains Store, the signal and brigade reports (Nos. 3-31), Jackson's No. 33 report and the No. 34
Confederate returns (headings seen only as search hits), Beall's and the other Confederate reports
(Nos. 35-48), any Gardner report (none in the inspected list), the naval reports, Irwin's appendix
loss tables and print pages were not inspected. No targeted follow-up was used. Stop after this
batch.

**Consequential gap.** No Confederate garrison return for the opening of the siege was inspected;
Irwin's "about seven thousand" has no stated source, and his footnote says the Union May and June
returns merely carry March forward. The Confederate returns (No. 34) and Jackson's report (No. 33)
are the obvious follow-up.

**New source records.** This pass adds **8 source records**:

- two NPS HTML/text pairs;
- the OR Volume XXVI Part 1 catalog metadata and full OCR (shared with the Taylor 1863 pass);
- the Miles selection;
- the Irwin Port Hudson selection (reusing the registered parent).

## Decisions and limits

- **Scope.** Plains Store shares the siege's start date and is recorded only in LA009; its losses
  are excluded from LA010, as Irwin's surgeon's return also excludes them. The investment of
  May 22-25, the Clinton expedition, Logan's raids and Springfield Landing are context.
- **Opening strengths remain unknown.** Every frozen bound is blank. Every figure is recorded with
  its date and scope, and none is adopted:
  - Plains Store: Miles's 400 infantry and a battery; prisoners' report of fifteen regiments; no
    Union count.
  - Garrison: 16,287 present for duty at the end of March; about seven thousand when the siege
    began after the Vicksburg detachments; 6,340 prisoners at the surrender; Miles's less than 400
    muskets for his wing on July 6.
  - Besiegers: more than two to one on May 26; effective strength never above 17,000, less than
    12,000 available for siege duty, hardly 8,000 at the end outside the cavalry.
- **Disputes preserved.**
  - Plains Store losses: the frozen and live 250 (US 150; CS 100) against Irwin's Union 102 and
    Miles's 89 (8 killed and 23 wounded known), the enemy's report of 40 Confederate dead buried,
    and the surgeon's 12 killed and 36 wounded.
  - Siege losses: the frozen 12,208 (US 5,000; CS 7,208) and live 17,500 (US 10,000; CS 7,500)
    against Irwin's Union 1,995 (May 27), 1,805 (June 14) and 4,363 (the siege), the surgeon's
    partial Confederate 623, Jackson's 200 killed, 300-400 wounded and 200 dead of sickness, and
    Beall's 358 to June 1. The basis of the frozen and live totals is not stated; that they
    include the surrendered garrison is only an inference from their size. Sick are not battle casualties.
  - Colonel Powers's initials (Irwin "S. P."; the frozen and live records "Frank P.").
- **Command roles.**
  - Banks ordered the May 27 assault after an unminuted council, put Weitzel over the right wing
    and resolved to replace T. W. Sherman; Grover and Weitzel agreed to wait.
  - Gardner was ordered by Pemberton to hold and by Johnston, too late, to evacuate; he declined
    Banks's June summons and surrendered after the Vicksburg news.
  - Augur, Grierson, Dudley and Chapin at Plains Store; Miles withdrew under Boone's fire.
  - No listed commander receives automatic sole credit.
- **Tags.** The works and felled timber predate the assaults, but their state on each day is not
  established. All claims stay `unresolved` or `post_outcome`.
- **Families.** Irwin stays in `irwin-nineteenth-corps-1892`. Miles is placed in
  `miles-port-hudson-1863-reports`; he had no earlier registry group. The OR parent is in
  `or-series-i-volume-xxvi`.

The two null unknowns are the two opening strengths. No morale/readiness score, probability,
causal effect or new commander ranking is introduced. The cohort, both admission proposals and the
baseline are unchanged, with **zero promoted rows**. `python3 -m generalship check` passes, the unit
tests pass, and the baseline still reports **23/127 eligible engagements in 13 groups**, with
strength Brier **0.276882** against **0.250000** for equal odds.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the six
Gulf and Louisiana 1862-63 passes together at commit `be711a9` as
`gulf-review-be711a9-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": four
required findings (R1 to R4) and ten advisories (A1 to A10). It is an AI review within its stated
scope, not human historical adjudication, proof of source independence or feature admission.

## Review correction

Each finding was checked against the retained selection text or the registry before any change;
every new quote occurs in its section, and the dossiers were regenerated from the builder.
LA010 is revised under `port-hudson-review-correction-2026-09-25` and supersedes the
byte-for-byte archive at `data/evidence/history/LA010.v1.json`. LA009 is unchanged.

- No required finding applies to this pass (R1-R4 apply to other passes).

Advisories affecting this pass:

- **A6 adopted** (LA010 and this memo): `reported-force-scope` now says Irwin's footnote concerns
  the Union monthly and tri-monthly returns; `command-roles` drops the "July 7" date of Gardner's
  council, which the selected surrender section gives only as "That evening"; the
  `casualty-records` rationale says that the totals include the surrendered garrison is an
  inference, not a stated fact.
- The other advisories apply to other passes.

The review correction adds no source record for this pass. Citations (96), claims (18) and
unknowns (2) are unchanged. No model input, cohort file, admission proposal or baseline is changed.
