# Marmaduke's First Expedition into Missouri: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both **frozen
records** in **Marmaduke's First Expedition into Missouri [January 1863]** now have draft dossiers:
**18 claims, 2 explicit null unknowns and 107 citation occurrences** (104 before the review
correction below). All seven dimensions are represented in each record. Both dossiers remain drafts;
no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| MO018 — Springfield | 1863-01-08 | 9 | 1 | 56 | 3 |
| MO019 — Hartville | 1863-01-09 to 01-11 | 9 | 1 | 51 | 3 |

Drafted with the Prairie Grove pass ([memo](prairie-grove-first-pass-v1.md)), whose Britton
volume I registration it reuses. It changes no dossier outside MO018 and MO019. Dossier
presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and both retained NPS pages in full.
NPS/CWSAC and the Arnold tables are one family. Both records use the same two further families:

- **Britton, *The Civil War on the Border*, volume I** (1891; see the Prairie Grove memo for the
  edition and dependency). Selected: Chapter XXXII, General Marmaduke's Attack on Springfield
  (OCR pp.442–457), and Chapter XXXIII, Action at Hartville (pp.458–465). Britton relays
  Brown's, Crabb's and Marmaduke's figures, so he is not independent of the report families.
- **Marmaduke's** January 18 dispatch and February 1, 1863 report (*Official Records* Series I,
  Volume XXII, Part 1, No. 8, pp.194–199), with Holmes's February 8 indorsement and the compiled
  No. 9 return of casualties (p.199, garbled in OCR). The indorsement and return are selected as
  separate sections and not counted as further families.

The following were read but not selected: the expedition's summary and report list (p.178),
Curtis's first dispatch on Springfield, and the boundaries of Burch's (No. 7) and Shelby's
(No. 10) reports. Brown's, Holland's, Crabb's, Warren's, Dunlap's, Porter's and Bennett's reports
were located by heading only. No targeted follow-up was used. Stop after this batch.

**Consequential gap.** Merrill, the frozen Union commander at Hartville, is represented only
through Britton; Warren's and Dunlap's reports (Nos. 5–6) were located and not read, and no
report by Merrill appears in the report list. Brown's report (No. 2) was also not read.

**New source records.** This pass adds **6 records**: two NPS HTML/text pairs, the Britton
volume I selection and the Marmaduke selection. Marmaduke has a new group,
`marmaduke-1863-reports`, shared by his three 1863 selections in this batch (this expedition, the
April–May expedition and Pine Bluff).

## Decisions and limits

- **Scope.** The captures of Fort Lawrence and Ozark (January 6–7), the Confederate appearance
  on the Rolla road on January 9, the Marshfield and Sand Spring burnings and the retreat to
  Batesville are context. Hartville's frozen interval (January 9–11) includes Porter's capture
  of the Hartville garrison on the 9th and the engagement of the 11th, recorded as one record.
- **Opening strengths remain unknown.** The frozen Union bounds are Springfield 2,000 and
  Hartville 700, matching the live pages; no inspected passage gives their basis. Figures
  recorded and not adopted:
  - Springfield: Britton's five thousand (Brown's report of Marmaduke), five or six thousand
    (Burch's prisoners), a garrison of perhaps less than one thousand effective men before
    reinforcement, about four hundred armed convalescents and nearly two hundred citizens, and his
    unit-by-unit counts (not summed); Marmaduke's 1,000 under Shelby and 270 under MacDonald on
    leaving Lewisburg, December 31, and his claim that the Federals had 4,200.
  - Hartville: Britton's about eight hundred plus one hundred and eighty cavalry for Merrill,
    the prisoners' five thousand for Marmaduke, eight hundred muskets and Dunlap's two hundred
    and fifty; Marmaduke's 1,500 infantry and 500 cavalry (January 18) against 2,500 (February 1)
    for the enemy, and Porter's 600 against about 700.
- **Disputes preserved.**
  - Springfield's works: Britton's four unfinished forts against Marmaduke's "strongly
    fortified".
  - Springfield's result: Marmaduke's claim to hold most of the town at dark against Britton's
    account of the Confederates driven back into the college palisades.
  - Springfield losses: Britton's Union 14, 146 and 4 against the frozen US 163; Marmaduke's 20
    killed and 80 wounded (January 18) against Britton's report of his 20 and 124, and Crabb's 60
    to 80 Confederate wounded left behind; the expedition total of 33, 203 and 29 is not assigned.
  - Hartville's result: Marmaduke's account of a Union rout against Britton's of Dunlap's
    regiment holding until the Confederates retreated.
  - Hartville losses: Britton's Union 7, 64, 5 and 2 (the frozen US 78); Marmaduke's 15 and 70
    (January 18) against Britton's report of his 12, 96 and 3; the frozen CS 329 has no inspected
    basis. The Hartville garrison taken on the 9th is thirty-five militia (Britton) or some 50
    (Marmaduke).
- **Command roles and ranks.**
  - The live pages list Marmaduke without a rank. Marmaduke calls his Hartville opponent
    "General Merrill"; the frozen rank is Colonel.
  - At Springfield, Brown was wounded and handed command to Crabb, who met the last assault. At
    Hartville, Warren put Merrill in command; Dunlap's regiment held the field after the rest
    retired; Porter was wounded.
  - No listed commander receives automatic sole credit.
- **Tags.** No ground is tagged `inherited`; the Springfield works predated the attack, but
  their extent is disputed. All claims stay `unresolved` or `post_outcome`.

The two null unknowns are the opening strengths. No morale/readiness score, probability,
causal effect or new commander ranking is introduced. No model input, cohort file, admission
proposal or baseline is changed.

## Validation

`python3 -m generalship check` passes, and `python3 -m unittest discover -s tests` passes.
Every quote occurs in its cited section; the builder's miss list is empty.
After the review correction, both pass again (134 tests) in the main repository, and the
builder's miss list is empty.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the eight
Trans-Mississippi 1863–64 first passes together at prepared commit `29c2811` as
`tm1863-review-29c2811-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": four
required findings (R1 to R4) and twelve advisories (A1 to A12) across the eight passes. It is an
AI review within its stated scope, not human historical adjudication, proof of source independence
or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the registry
record) before any change; every new quote occurs in its cited section, and the dossiers were
regenerated from the builder.

MO018 and MO019 are revised under `marmaduke-1863-first-review-correction-2026-09-25` and supersede
byte-for-byte archives at `data/evidence/history/<ID>.v1.json`.

- **R1** (MO018 `reported-force-scope`): Marmaduke's 1,000 under Shelby and 270 under MacDonald
  were stated as the force that struck Springfield. His January 18 dispatch gives them as the
  columns he marched with from Lewisburg on December 31, 1862, and his February 1 report as about
  1,000 effective men, some without horses, and about 270 effective men on leaving Lewisburg. The
  value and rationale now say so, with three citations added (p.194 and two on p.196).

Advisories:

- **Adopted:** A8 (MO019 rationale: Marmaduke's "General Merrill" is recorded as differing from
  Britton's "Colonel Merrill" and the frozen rank, not as his rank error); A12 (MO018: the No. 9
  return's heading "January 2-11, 1862" is quoted with its printed year); A1 (the Britton volume I
  selection used here, `britton-border-1-marmaduke-1863-first-selections-v1`, binds to the
  registered parent `britton-border-1-ocr-v1`; its v1 dependency note's merge clause is stale and
  documented in `docs/sources.md`; no successor is registered); A2 (`docs/sources.md` (review
  W61-R14) records `britton-civil-war-border`, `britton-civil-war-border-1899` and
  `britton-civil-war-on-border-1899` as one Britton witness family).

The review correction adds no source records for this campaign. Citations rise from 104 to 107;
claims (18), unknowns (2) and disputed claims are unchanged. No model input, cohort file, admission
proposal or baseline is changed.
