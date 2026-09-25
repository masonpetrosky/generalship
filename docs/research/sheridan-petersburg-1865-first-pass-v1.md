# Sheridan's Expedition to Petersburg: bounded first pass

Prepared 2026-09-25 under the [cohort v2](../cohort-v2.md) research order. The single record in
**Sheridan's Expedition to Petersburg [March 1865]** now has a draft dossier: **9 claims, 1
explicit null unknown and 43 citation occurrences**. All seven dimensions are represented. The
dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| VA123 — Waynesboro | 1865-03-02 | 9 | 1 | 43 | 3 |

Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. The page
labels the campaign "Sheridan's Expedition to Petersburg" and dates it "March 1865"; neither
replaces the frozen interval. NPS/CWSAC and the Arnold tables are one family. Two further
families:

- **Pond**, *The Shenandoah Valley in 1864* (the registered parent
  `pond-shenandoah-valley-ocr-v1`, reused as `pond-waynesboro-selections-v1`, cited through its
  `metadata_only` successor `pond-waynesboro-selections-v2` after the review correction). One passage was
  read and selected: the close of Chapter XIV, from Grant's February 1865 wish to repeat the
  Staunton attempt through Waynesboro and the march to White House (OCR pp.251–254). The
  earlier part of Chapter XIV (pp.243–251, October 1864 to January 1865) was read, not selected.
  Pond was not a participant. For Waynesboro he quotes and closely follows Sheridan's report, so
  he is not independent of it; the selection's dependency note says so.
- **Sheridan's** July 16, 1865 report on the expedition from Winchester (No. 1, from the
  registered *Official Records* Series I, Volume XLVI, Part 1, parent `or46-1-illinois-ocr-v1`,
  reused). The expedition's summary of events and report list (p.474) and the report
  (pp.474–482) were read. Two passages were selected:
  - from the heading through the Waynesborough results (pp.474–476);
  - the paragraph on prisoners and losses for the whole march (pp.480–481).

  The march from Charlottesville to White House was read but not selected, and the inclosure
  of captures and destruction was read in part.

Not inspected: Custer's, Merritt's and Devin's reports (Nos. 8, 3, 4); Lee's dispatches (No. 13);
Hotchkiss's journal (No. 14); maps and print pages. The inspected report list contains no Early
report. No follow-up beyond three families was made. Stop after this record.

This pass **adds 4 source records**:

- one NPS HTML/text pair (`nps-va123-v1-html`, `nps-va123-v1`);
- one Pond selection (`pond-waynesboro-selections-v1`);
- one OR selection (`or46-1-sheridan-waynesborough-selections-v1`).

No new volume or catalog record is registered.

### Independence groups

- **Pond** stays in `pond-shenandoah-valley-1883`, with the parent and the two Valley
  selections already registered there. The v1 selection's dependency note wrongly said there was
  no earlier registry group for this author; the successor corrects it (APX-A7).
- **Sheridan** is placed in his most recent registered group, `sheridan-valley-1864-reports`,
  with his Appomattox reports added in the Appomattox pass. The dependency note says one
  author's accounts are not mutually independent corroboration.
- The OR volume is a shared container (`or-series-i-volume-xlvi`), not a witness.

## Decisions and limits

- **Scope.** The expedition's march from Winchester (February 27) to White House (March 19),
  Rosser's attack on the prisoner guard near Mount Jackson and the destruction of the railroad
  and canal are context. Sheridan's march-wide figures (about 1,600 prisoners; loss not over 100
  men) are not assigned to this record.
- **Opening strength remains unknown.** The frozen and live force fields read 4,100 (US 2,500;
  CS 1,600), with no stated date or population. Recorded, not adopted:
  - Sheridan's effective force of February 28: 503 officers and 9,484 men (9,987).
  - Pond's 10,000 sabres: Custer's 4,840 and Devin's 5,047 aggregate effective.
  - The Confederate force by formation: two infantry brigades and Rosser's cavalry (Sheridan);
    Wharton's two brigades, Nelson's six guns and Rosser's cavalry (Pond).

  The frozen Confederate 1,600 equals the prisoner count both accounts give; this is an
  observation only.
- **Disputes preserved** (3 claims marked `disputed`: strength, result and casualties):
  - NPS says the attack rolled up Early's right flank; Sheridan and Pond put the turning column
    on his left.
  - The frozen casualty text reads 1,800 total and the live field 1,630 (US 30; CS 1,600).
    NPS's description says more than 1,500 surrendered. Sheridan gives 1,600 officers and men
    at Waynesborough and about 1,600 prisoners for the whole march; Pond gives "first and last,
    about 1,600" and little if any loss on either side.
- **Command roles and ranks.** The live page gives Early as Major General against frozen
  Lieutenant General; it is not adopted. Custer, not a frozen commander, directed the attack in
  both accounts, and Early's dispositions are described only by his position. No listed
  commander receives automatic sole credit.
- **Tags.** The ridge and river predate the action, but when the breastworks were built is not
  stated, so the terrain claim stays `unresolved`. Outcomes are `post_outcome`.
- **OCR limits.** Quotes preserve OCR corruption, for example "soinecavalry", "Bosser" for Rosser,
  "Bockfish" for Rockfish and "oiDen".

The one null unknown is the opening strength. No morale/readiness score, probability, causal
effect or commander ranking is introduced. The v1 cohort, the frozen baseline and both admission
proposals are unchanged, with zero promoted rows.

## Validation

- After the review correction, `python3 -m generalship check` passes and
  `python3 -m unittest discover -s tests` passes (134 tests).
- After building, the builder's quote-miss list is empty.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed this
pass together with the Appomattox pass at commit `02dde7d` as
`appomattox-review-02dde7d-opus-high-v1` on 2026-09-25. Its outcome was "corrections required";
its three required findings (APX-R1 to APX-R3) concern Appomattox records, and one of its ten
advisories (APX-A7) concerns this record. It is an AI review within its stated scope, not human
historical adjudication, proof of source independence or feature admission.

## Review correction

- **APX-A7** (registry): the dependency note of `pond-waynesboro-selections-v1` copied two
  sentences from the earlier Pond records that are inaccurate here: that the history is not
  independent of "the Official Records families selected in this pass", and "No earlier registry
  group for this author". The `metadata_only` successor `pond-waynesboro-selections-v2`
  (superseding v1, kept unchanged; same raw bytes, parent, ranges and group) attributes the
  quoted-report sentence to the earlier Pond records and names the parent and the two earlier
  selections in `pond-shenandoah-valley-1883`. VA123's twelve Pond citations move to v2.

VA123 is revised under `sheridan-petersburg-1865-review-correction-2026-09-25` and supersedes
the byte-for-byte archive `data/evidence/history/VA123.v1.json`. The review correction adds
**one source record** (`pond-waynesboro-selections-v2`). Claims (9), unknowns (1), citations (43)
and disputed claims (3) are unchanged. No model input, cohort file, admission proposal or
baseline is changed.
