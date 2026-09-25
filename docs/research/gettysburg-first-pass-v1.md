# Gettysburg Campaign: bounded first pass

Prepared 2026-09-25. All **ten frozen records** in **Gettysburg Campaign [June-July
1863]** now have draft dossiers: **90 claims, 10 explicit null unknowns and 336
citation occurrences** after review correction. All seven dimensions are represented in
each record. Separate Claude Opus 5.5 `high` [review](../../artifacts/review-results/gettysburg-48ea563-opus-high-v1/review.md) found eleven required
corrections, all applied and verified by the primary. All dossiers remain drafts; no
features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| VA035 — Brandy Station | 1863-06-09 | 9 | 1 | 39 | 3 |
| VA107 — Winchester, Second | 1863-06-13 to 06-15 | 9 | 1 | 45 | 3 |
| VA036 — Aldie | 1863-06-17 | 9 | 1 | 28 | 3 |
| VA037 — Middleburg | 1863-06-17 to 06-19 | 9 | 1 | 37 | 3 |
| VA038 — Upperville | 1863-06-21 | 9 | 1 | 29 | 3 |
| PA001 — Hanover | 1863-06-30 | 9 | 1 | 27 | 3 |
| PA002 — Gettysburg | 1863-07-01 to 07-03 | 9 | 1 | 48 | 3 |
| MD004 — Williamsport | 1863-07-06 to 07-16 | 9 | 1 | 31 | 3 |
| MD006 — Boonsboro | 1863-07-08 | 9 | 1 | 25 | 3 |
| VA108 — Manassas Gap | 1863-07-23 | 9 | 1 | 27 | 3 |

Coverage is **101/127 draft dossiers**, **26 without**, and **24/36 complete source
campaigns by dossier presence**. All 91 earlier dossiers and all historical revisions
are unchanged.

## Inspection and stopping record

Read all ten frozen battle, force and commander row sets and the ten retained NPS
summaries in full. NPS/CWSAC and the Arnold tables are one family. Each battle uses two
further families:

- **Doubleday**, *Chancellorsville and Gettysburg* (1882), reused through a new
  selection from the pinned OCR: Brandy Station, Winchester, Aldie to Upperville,
  Hanover, the armies on July 1, the July 3 repulse, and the pursuit with campaign
  losses (OCR pp.82–210). Doubleday commanded the First Corps at Gettysburg, so his
  history is an interested participant account; he relays others' figures.
- **Humphreys**, *From Gettysburg to the Rapidan* (1883), newly pinned from a Cornell
  scan, is used for Williamsport, Boonsboro and Manassas Gap (pp.1–10). Humphreys was chief of
  staff of the Army of the Potomac in 1863–64 per his publisher's list, so his history is
  also interested; when that role began is not established in the inspected pages.
- **Lee's detailed report** (transmitted January 20, 1864; the report's own day is blank
  in OCR) for Winchester, Gettysburg, Williamsport and Manassas Gap.
- **Stuart's reports** (June 13 and August 20) for Brandy Station, Aldie, Middleburg,
  Upperville, Hanover and Boonsboro.

The two report selections come from newly pinned *Official Records* Series I, Volume
XXVII, Part 2. Stuart's Boonsboro passage is heavily garbled in OCR, so only
intelligible fragments are cited. No maps, returns, Meade's or Ewell's reports, or
print pages were inspected. Stop after this batch.

Twenty-eight new source records bring the registry to **468 entries / 458 raw paths**,
preserving the earlier **440/430**. They comprise:

- ten NPS HTML/text pairs;
- OR XXVII Part 2 catalog metadata and full OCR, and the Lee and Stuart selections;
- a Doubleday selection;
- Humphreys' catalog metadata, full OCR and selection.

## Decisions and limits

- **Overlaps.** Middleburg (June 17–19) overlaps Aldie (June 17), and Boonsboro lies
  inside Williamsport's frozen interval. Stuart's loss of 65 killed, 279 wounded and 166
  missing covers Stuart's Loudoun operations from June 17 through the June 22 pursuit and is
  not assigned to Aldie, Middleburg or Upperville. The
  Count of Paris's campaign estimates (23,186 Union, 22,728 Confederate), relayed by
  Doubleday, are not assigned to Gettysburg.
- **Opening strengths remain unknown.** Winchester and Gettysburg have imported
  structured bounds, which are unchanged. At Gettysburg the frozen text's 158,300 differs
  from its own components' sum of 158,343 (a computation here), which the live field
  gives. Other records have unit-level frozen text only. Brandy Station's figures
  (Pleasonton's 12,000, McClellan's 9,335 on paper, Gregg's 9,000) are relayed by
  Doubleday with his warning that commanders overstate enemy numbers.
- **Disputes preserved**:
  - Brandy Station: Pleasonton's claimed reconnaissance success against NPS's statement
    that he found no infantry.
  - Middleburg: NPS's regiment against Doubleday's division.
  - Hanover: who held the town at the end.
  - Casualties: every record where frozen and live counts differ. Boonsboro's live 1,078
    stands against the frozen 100, and Williamsport's live 654 against the frozen 1,730.
- **Command roles**: Lee's and Stuart's judgments of subordinates, Doubleday's account of
  Pickett's retreat and Humphreys' defense of Meade are attributed. Stuart's Sabbath
  decision before Upperville is recorded as his stated reason. The compiler notes that Lee
  marked a Stuart sentence "Omit, if published". Live headings give Lee Major General,
  Hampton Lieutenant General and Stuart no rank; none is adopted, and no listed commander
  receives automatic sole credit.
- Winchester's forts are tagged `inherited`; other terrain, logistics and command claims
  stay `unresolved`.

The ten null unknowns are the opening strengths. No morale/readiness score, probability,
causal effect or new commander ranking is introduced. Cohort and both admission
proposals remain unchanged, with **zero promoted rows**. The baseline still uses
**23/127 engagements in 13 eligible groups**, with strength Brier **0.276882** versus
**0.250000** for equal odds.

## Review correction and validation

The reviewer found eleven required corrections, all verified against the retained text
(each new quote occurs once) and applied:

- **GB-R1** extends Stuart's Loudoun loss scope to the June 22 pursuit in all ten boundary
  notes and three casualty rationales.
- **GB-R2** names Middleburg's two worn brigades on June 19 and moves the rain to June 20,
  outside the frozen interval.
- **GB-R3** quotes Boonsboro's garbled OCR ("successfulfy with", "heavily re-",
  "Tunkstown") instead of silently reconstructing it.
- **GB-R4** reports "numerous skirmishers", cites the 200 wagons and Custer's arrival, and
  corrects the "Omit, if published." locator to p.695.
- **GB-R5** attributes the Stevensburg detachment to Doubleday, gives Stuart's nine and
  seven infantry regiments, and restores Stuart's words on Robertson.
- **GB-R6** restores Early's 108 officers and 3,250 men and Doubleday's full reasons for
  clearing the valley.
- **GB-R7** moves Lee's "rendered the others untenable" from the `inherited` terrain claim
  to the Winchester result.
- **GB-R8** scopes Lee's superior-numbers statements to Heth's two brigades and to his
  stated risk.
- **GB-R9** restores "partially".
- **GB-R10** corrects Longstreet's crossing.
- **GB-R11** records three `metadata_only` Humphreys revisions: neither the July 1863 start
  of his chief-of-staff role nor dependence on the printed Official Records is established.
  The raw bytes and ranges are unchanged, and the dossiers cite the v2 selection. The
  shared open question and MD004's rationale now use his publisher's list.

No advisory findings were raised. Citations rise from 320 to 336; claims and unknowns
are unchanged. The originals are retained as `data/evidence/history/*.v1.json` for all ten
dossiers, linked by `supersedes`, and the registry is now **492 entries / 476 raw paths**.
The [primary assessment](../../artifacts/review-results/gettysburg-48ea563-opus-high-v1/primary-assessment.md) closes all eleven findings; no second
reviewer pass is claimed.

Next by frozen campaign start is **Tullahoma or Middle Tennessee Campaign [June
1863]**: TN017. Do not start that group within this batch.
