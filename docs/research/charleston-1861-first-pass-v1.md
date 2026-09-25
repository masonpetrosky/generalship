# Operations in Charleston Harbor, 1861: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
frozen record in **Operations in Charleston Harbor [April 1861]** now has a draft dossier: **9
claims, 1 explicit null unknown and 59 citation occurrences** after the review correction (53
before). All seven dimensions are represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| SC001 — Fort Sumter | 1861-04-12 to 04-14 | 9 | 1 | 59 | 3 |

This pass was drafted with five other 1861 eastern campaigns (Chesapeake, Western Virginia,
Manassas, Carolina coast and McClellan's northern Virginia operations), which share its Nicolay
source record. Dossier presence is not first-pass acceptance, separate review or model
eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC
and the Arnold tables are one family. Two further families:

- **Nicolay, *The Outbreak of Rebellion*** (Scribner, 1881; Campaigns of the Civil War, I;
  Illinois scan `outbreakofrebell00nico`). Selected: the title page and preface, and Chapter V,
  Sumter (pp.56–68; the p.66 head reads "GG" in OCR). The book is registered here once and
  reused by the Western Virginia and Manassas passes. By its preface it rests largely on the
  Official Records for 1861; it quotes Anderson's correspondence.
- **Anderson's** April 18 telegram and April 19, 1861 report (No. 6, *Official Records* Series I,
  Volume I, pp.12–13). The volume is the University of California scan
  `warofrebellion01secrrich`: the Illinois identifiers `warofrebellion01unit` and
  `warofrebellion01unit_0` are Series III and Series II volumes and were not used.

Read but not selected: the inclosed Beauregard–Anderson correspondence of April 11–15 and
Cameron's April 20 letter. Not inspected: Beauregard's reports (No. 8), Foster's engineer journal
(No. 7), Fox's report (No. 5), the South Carolina subordinate reports (Nos. 9–28) and print
pages. No targeted follow-up was used. Stop after this record.

The pass adds **8 source records**:

- the NPS HTML/text pair;
- OR Volume I catalog metadata and full OCR (`ia-or1-ucal-metadata-v1`, `or1-ucal-ocr-v1`);
- Nicolay catalog metadata and full OCR (`ia-nicolay-outbreak-metadata-v1`,
  `nicolay-outbreak-ocr-v1`);
- `or1-anderson-sumter-selections-v1` and `nicolay-sumter-selections-v1`.

New groups: `nicolay-outbreak-of-rebellion-1881`, `anderson-sumter-1861-reports` and the
container group `or-series-i-volume-i`.

## Decisions and limits

- **Scope.** The December 1860–April 1861 occupation and siege, the Star of the West firing and
  both relief expeditions are context.
- **Opening strength remains unknown.** The frozen bounds (US 80; CS 500) have no inspected
  basis. Nicolay counts 9 officers, 68 enlisted men, 8 musicians and 43 workmen, 128 in all,
  against 4,000–6,000 Confederates supporting the batteries; he gives 48 guns in the fort and 47
  in the besieging works. None is adopted.
- **Disputes preserved.**
  - Result: frozen Confederate victory against live "Indecisive".
  - The demand for evacuation: April 10 in NPS, April 11 in Nicolay and Anderson.
  - Duration and timing: thirty-four hours (Anderson) against thirty-six (Nicolay); evacuation
    on the afternoon (Anderson) or at noon (Nicolay) of April 14; NPS gives the surrender at
    2:30 p.m. on April 13.
  - Losses: frozen "None"; live 15 (US 11; CS 4). The salute accident after the surrender cost
    one killed and three wounded in NPS, one killed and five wounded in Anderson. Both, and
    Nicolay, record no life lost (Anderson: no one seriously injured) to the bombardment.
- **Command roles.** Beauregard and Anderson are listed with matching frozen and live ranks.
  Nicolay attributes the withdrawal from the barbette guns to Anderson and the first shot to
  Doubleday. No listed commander receives automatic sole credit.
- **Tags.** No claim is tagged `inherited`; all stay `unresolved` or `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect
or new commander ranking is introduced. Nothing in this pass changes a model input.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed this pass
together with the other five 1861 Eastern passes at commit `c298447` as
`e1861-review-c298447-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": eight
required findings (E1861-R1 to E1861-R8) and fifteen advisories (E1861-A1 to E1861-A15). None
changes a model input. It is an AI review within its stated scope, not human historical
adjudication, proof of source independence or feature admission.

## Review correction

Each finding was checked against the retained selection text or the registry before any change;
every new quote occurs in its section, and the dossiers were regenerated from the builder. SC001 is
revised under `charleston-1861-review-correction-2026-09-25` and supersedes a byte-for-byte archive
at `data/evidence/history/<ID>.v1.json`. No required finding concerns this pass.

- **Adopted:** A1 (the brick work on an artificial island now has its own quote, p.62) and A2
  (Nicolay's fifty barrels taken from the magazine, all but five rolled into the sea by Anderson's
  order, added to the logistics claim; Anderson's offer to evacuate by noon on April 15 and the 3:20
  a.m. one-hour notice added to the information claim; five citations).
- **Recorded, no change:** A13 (the Nicolay preface date stays null; it could be filled after a
  print check). A3–A12, A14 and A15 concern other 1861 passes.

Shared finding:

- **E1861-R8** (`docs/sources.md`): the 1861 section's "thirty report selections" should read
  twenty-seven report selections (thirty selections with Nicolay's three); the 78 records are
  correct. That document belongs to the primary and is not edited here. This pass's own record count
  is unchanged.

The review correction adds **no source records**. Citations rise from 53 to 59; claims (9), the
unknown (1) and the disputed claims are unchanged. No model input, cohort file, admission proposal
or baseline is changed.

After the review correction, `python3 -m generalship check` passes and
`python3 -m unittest discover -s tests` passes (134 tests).
