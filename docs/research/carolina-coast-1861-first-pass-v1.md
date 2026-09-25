# Blockade of the Carolina Coast, 1861: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
frozen record in **Blockade of the Carolina Coast [August 1861]** now has a draft dossier: **9
claims, 1 explicit null unknown and 50 citation occurrences**, unchanged by the review correction.
All seven dimensions are represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| NC001 — Hatteras Inlet Batteries | 1861-08-28 to 08-29 | 9 | 1 | 50 | 3 |

This pass was drafted with five other 1861 eastern campaigns. Dossier presence is not first-pass
acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family. On the primary's instruction, Army *Official Records* Series I,
Volume IV (which holds Butler's reports, pp.579–594 by the Navy compilers' footnote) was **not
fetched or registered**: another pass registers it. The two further families come from the
***Official Records of the Union and Confederate Navies*** Series I, Volume 6 (1897; Trent
University scan `officialrecordso0006unse`):

- **Stringham's** reports as commander of the Atlantic Blockading Squadron:
  - the August 30 transmittal with the articles of capitulation, signed jointly by Stringham,
    Butler, Barron, Martin and Andrews (pp.119–120);
  - the September 2 detailed report (pp.120–123);
  - the September 2 prisoner letter and September 3 letter (pp.124–125), with the compilers'
    footnote that the omitted list held 670 names.
- **William F. Martin's** August 31 report (pp.140–142), which the compilers say was copied from
  a newspaper clipping.

Read but not selected:

- Stringham's August 7 report on the batteries;
- Gillis's enclosure and report, and Mercer's report; Stellwagen's report in part;
- the Confederate telegrams of August 27–30 and Davis's August 31 letter;
- Barron's August 31 report and the opening of Andrews's September 1 report.

Martin's enclosed returns are not printed. No Scribner history narrates the engagement; Nicolay
mentions the Hatteras victory only in passing, in his concluding chapter. No targeted
follow-up was used. Stop after this record.

The pass adds **6 source records**:

- the NPS HTML/text pair;
- Navy Volume 6 catalog metadata and full OCR (`ia-orn6-trent-metadata-v1`,
  `orn6-trent-ocr-v1`);
- `orn6-stringham-hatteras-selections-v1` and `orn6-martin-hatteras-selections-v1`.

New groups: `stringham-hatteras-reports`, `martin-hatteras-report` (distinguished from William T.
Martin's registered group) and the container `orn-series-i-volume-6`.

## Decisions and limits

- **Scope.** The August 26 departure, the Confederate reinforcement attempts from the sound and
  the later occupation of the inlet are context.
- **Opening strength remains unknown.**
  - The frozen bounds are US 2,000 (marked an estimate) and CS 900; the live page gives US 2,000
    and CS 0.
  - Martin says he had about 350 men when the fleet appeared, with at least 225 needed to work
    the guns, and was reinforced by 247 men with their officers on the evening of the 28th.
  - The 670 surrendered on the 29th are a later population.

  None is adopted.
- **Disputes preserved.** Losses are frozen at 773 (US 3; CS 770) and live at 673 (US 3; CS 670).
  - NPS says the Federals lost one man; Stringham records no accident to any officer or man.
  - Martin reports one or two killed on the 28th and doubts his captains' returns.
  - Stringham could not get the enemy's killed and wounded.
- **Command roles.**
  - Butler and Martin are listed with matching frozen and live ranks.
  - The naval attack was under Stringham, who is not listed.
  - Martin and Andrews gave command of the defenses to Barron on the evening of the 28th, so the
    listed Confederate commander did not command at the capitulation. NPS says Martin surrendered
    the garrison.
  - Butler's own account is in the deferred Army Volume IV.
  - No listed commander receives automatic sole credit.
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

Once Army Volume IV is registered, Butler's reports are the natural bounded follow-up for the Union
command role.

## Review correction

Each finding was checked against the retained selection text or the registry before any change;
every new quote occurs in its section, and the dossiers were regenerated from the builder. NC001 is
revised under `carolina-coast-1861-review-correction-2026-09-25` and supersedes a byte-for-byte
archive at `data/evidence/history/<ID>.v1.json`.

- **E1861-R7** (NC001 `casualty-records`): the rationale no longer says prisoners are counted in the
  frozen and live Confederate totals. It now says the live Confederate 670 equals the compilers'
  count of Stringham's prisoner list, so it appears to be a prisoner count; the basis of the frozen
  770 is not established; prisoners are not added to any other loss figure.

Advisories:

- **Adopted:** A11 (NC001 open questions record Martin's statement that Barron and Andrews's report
  "contains all that is material", which was read but not selected, so the Confederate side of the
  capitulation rests on the articles and Martin's clipping-copied report).
- **Recorded, no change:** A13 (Stringham's two-date section stays null). The other advisories
  concern other 1861 passes.

Shared finding:

- **E1861-R8** (`docs/sources.md`): the 1861 section's "thirty report selections" should read
  twenty-seven report selections (thirty selections with Nicolay's three); the 78 records are
  correct. That document belongs to the primary and is not edited here. This pass's own record count
  is unchanged.

The review correction adds **no source records**. Citations (50), claims (9), the unknown (1) and
the disputed claims are unchanged. No model input, cohort file, admission proposal or baseline is
changed.

After the review correction, `python3 -m generalship check` passes and
`python3 -m unittest discover -s tests` passes (134 tests).
