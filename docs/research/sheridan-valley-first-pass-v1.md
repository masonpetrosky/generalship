# Sheridan's Valley Campaign: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). All **eight
frozen records** in **Sheridan's Valley Campaign [August-October 1864]** now have draft dossiers:
**72 claims, 9 explicit null unknowns and 342 citation occurrences** (323 before the review correction below). All seven dimensions are
represented in each record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| VA117 — Guard Hill | 1864-08-16 | 9 | 1 | 42 | 3 |
| WV014 — Summit Point | 1864-08-21 | 9 | 1 | 40 | 3 |
| WV015 — Smithfield Crossing | 1864-08-25 to 08-29 | 9 | 2 | 32 | 3 |
| VA118 — Berryville | 1864-09-03 to 09-04 | 9 | 1 | 41 | 3 |
| VA119 — Opequon (Third Winchester) | 1864-09-19 | 9 | 1 | 52 | 3 |
| VA120 — Fisher's Hill | 1864-09-21 to 09-22 | 9 | 1 | 44 | 3 |
| VA121 — Tom's Brook | 1864-10-09 | 9 | 1 | 38 | 3 |
| VA122 — Cedar Creek | 1864-10-19 | 9 | 1 | 53 | 3 |

This pass was drafted alongside Early's Raid ([memo](early-raid-first-pass-v1.md)). At the prepared
commit the repository held **153 draft dossiers** (the 127 v1 records, the 11 Overland records and these 15). The v1 dossiers, reviews and
historical revisions are unchanged. Dossier presence is not first-pass acceptance, separate review
or model eligibility.

## Inspection and stopping record

Read all eight frozen battle, force and commander row sets and the eight retained NPS pages in
full. NPS/CWSAC and the Arnold tables are one family. Each record uses two further families.

- **Pond, *The Shenandoah Valley in 1864*** (Scribner, 1883) is the same retrospective history
  registered for Early's Raid, and it quotes the reports used below. A second selection from
  the same parent OCR covers:
  - Guard Hill (OCR pp.126–129) and Summit Point (pp.132–135);
  - the August 25–29 actions (pp.137–141) and Berryville (pp.144–145);
  - Chapter IX, the Opequon (pp.153–172; p.155 is printed twice in the scan);
  - Chapter X, Fisher's Hill (pp.173–185) and Tom's Brook (pp.201–205);
  - Sheridan's absence and Cedar Creek (pp.212–242). Page 222 is printed twice, and the p.225
    and p.226 heads read "223" and "22G".
  - Appendix B parts V–VI on strength (pp.265–266), whose tables are garbled in OCR.
- **Sheridan's** dispatches and his February 3, 1866 report (OR XLIII Part 1, No. 1) are the
  report family for VA117, WV014, WV015 and VA118.
  - Dispatches of August 17, August 22 (headed "Angust 1864" in OCR, received 2 a.m. the 23d;
    date mapped null), August 28, September 4 and September 5 (pp.19–23).
  - The 1866 report from its opening to "were suffering by the delay" (pp.40–46).
- **Early's** reports and dispatches to Lee (No. 173) are the report family for VA119, VA120,
  VA121 and VA122. It is the same family as his July 14 report selected for Early's Raid.
  - The October 9 report on Winchester and Fisher's Hill (pp.554–556; the p.555 head reads
    "655").
  - The unsigned killed-and-wounded table (p.557, garbled).
  - The Mount Jackson dispatch, whose day is lost in OCR, and the September 25 letter
    (pp.557–558).
  - The October 9 letter on Tom's Brook (pp.559–560) and the October 20 telegram (p.560).
  - A garbled New Market dispatch dated only "6" (p.560).
  - The surviving end of the Cedar Creek report (pp.563–564).

The following were read but not selected:

- Sheridan's other August 11–September 13 dispatches and his October 9 and 11 dispatches;
- the rest of his 1866 report through Cedar Creek;
- Lee's indorsements and September 27 reply;
- the Cedar Creek organization table.

Crook's, Wright's, Emory's, Torbert's, Merritt's, Custer's and the Confederate subordinate
reports, Hotchkiss's journal, the compiled Union returns (Nos. 3–7) and print pages were not
inspected. No targeted follow-up was used. Stop after this batch.

**Consequential gap.** In this OCR, Early's Cedar Creek report begins mid-sentence on p.563. Its
heading and opening, pp.561–562, are absent. A second scan was not sought. Pond quotes part of the
report.

Nineteen new source records bring the registry from **670 entries / 649 raw paths** to **689 /
668**:

- eight NPS HTML/text pairs;
- the Pond Sheridan's Valley selection, reusing the Pond parent OCR registered for Early's Raid;
- the Sheridan selection and the Early Volume XLIII selection, reusing the Volume XLIII Part 1
  parent registered for Early's Raid.

Before both campaigns the registry held 643 / 622 (after the Overland pass).

## Decisions and limits

- **Scope.**
  - Context only: the August 11–15 advance and August 17 Winchester fight; the August 22–24
    Halltown skirmishes; Averell's September 2–3 fight at Bunker Hill; Early's September 17–18
    move to Martinsburg; Torbert's Luray Valley operations; the October 6–8 cavalry
    skirmishing; and the October 13 reconnaissance at Hupp's Hill.
  - Smithfield Crossing's frozen interval (August 25–29) also contains the August 25
    Kearneysville fight, the August 26 Halltown reconnaissance and the August 28 Leetown fight.
    The sources record them separately. They are not added to the August 29 engagement.
    WV015's logistics dimension is an explicit unknown.
- **Opening strengths remain unknown.** The frozen imported bounds are:

  | Record | US | CS | Live differences |
  | --- | ---: | ---: | --- |
  | Opequon | 39,240 | 15,200 | none |
  | Fisher's Hill | 29,444 | 9,500 | live US 38,950 |
  | Tom's Brook | 6,300 | 3,500 | none |
  | Cedar Creek | 31,945 | 21,000 | live CS 15,265 |

  No inspected passage gives their basis. The other records' bounds are blank. Every figure is
  recorded with its date and scope, and none is adopted:
  - Sheridan: effective line-of-battle strength on August 13 of about 18,000 infantry and
    3,500 cavalry; Early's force estimated at about 27,000 infantry on September 5; "but little"
    difference between the armies in early September.
  - Grant, via Pond: Early could not exceed 40,000 (read "4.0,000").
  - Pond's appendix: 17,195 without Kershaw and about 21,000 with him, reconstructed from the
    September 10 present-for-duty figures plus an assumed 1,700 for Fitz Lee taken from June–July
    inspection reports. Sheridan's September 10 field return south of the
    Potomac is 45,487 as printed and 45,509 corrected, excluding about 2,500 of Averell's
    cavalry.
  - Pond: Grover's division 6,797 effective before the Opequon (derived from an after-action
    return), and Early's October
    reinforcements nearly 5,000.
  - Early: the Union at three times, or three or four to one; about 6,000 muskets without
    Kershaw on October 9.
- **Disputes preserved.**
  - Guard Hill:
    - result: Sheridan says the enemy was badly beaten; NPS says the Confederates drove the
      Union brigades back.
    - prisoners: 24 officers and 276 men, against 300 and about 300.
    - where Merritt withdrew: Nineveh or White Post.
  - Summit Point: Union loss 275 (Sheridan, uncategorized) against 260 killed and wounded (Pond).
  - Berryville: Sheridan's 50 prisoners and over 200 Confederate killed and wounded, later
    raised, against Pond's three score prisoners and Crook's 166.
  - Opequon:
    - Early says he had defeated the Union infantry before the cavalry turned the scale.
    - Confederate loss: Early's 3,611 infantry and artillery, the memorandum's 1,707 killed and
      wounded, and Pond's 3,900–4,000, which he derives from Early's 3,611 plus an assumed
      cavalry ratio (not an independent count).
    - Union loss: Pond's 4,900–5,000 against the frozen 5,020. Pond's table for Crook's command
      includes its Fisher's Hill casualties, so it overlaps VA120 and is not added to it.
  - Fisher's Hill:
    - guns lost: 12 (Early) against 16 (Pond);
    - prisoners: at most 400–500 (Early) against 1,100 (Sheridan, via Pond). Pond's 1,300–1,400
      Confederate loss combines Early's report with Sheridan's prisoner count.
  - Tom's Brook: Early says Rosser fell back in good order and nine guns were lost; Pond says
    both divisions were routed and eleven guns taken.
  - Cedar Creek:
    - frozen 8,575 (US 5,665; CS 2,910) against live 7,682 (US 5,672; CS 2,010);
    - Pond: Union 5,764 and Confederate about 3,100;
    - Early: killed and wounded under 1,000 in one dispatch and 700–800 in another; 1,300
      prisoners taken; a net loss of twenty-three guns.
- **Command roles and ranks.**
  - Anderson is frozen as Lieutenant General at Guard Hill and live as Major General. Pond says
    he declined to take command from Early.
  - At Cedar Creek, Wright commanded until Sheridan returned. The frozen commanders list both;
    the live page lists Wright only.
  - The live pages give Early as Major General.
  - No listed commander receives automatic sole credit, and live ranks are not adopted.
- **Tags.** No works or ground are tagged `inherited`. The Berryville intrenchments were dug
  during the engagement. Fisher's Hill combined Early's August line with new works. The Cedar
  Creek camps were chosen by the Union commanders. All claims stay `unresolved` or
  `post_outcome`.
- **Campaign contribution.** The following are recorded as campaign or political contribution,
  not tactical outcome:
  - the burning of the Valley;
  - the Union cavalry's later superiority;
  - the Sixth Corps' recall;
  - Cedar Creek's effect on the election.
- **Families.**
  - The Sheridan family is placed in `sheridan-valley-1864-reports`.
  - The Overland pass registered Sheridan's Volume XXXVI dispatches and May 13, 1866 report as
    `sheridan-overland-reports`; the Valley set is kept in its own group, and the two are one
    author's accounts, not mutually independent corroboration.
  - Early's two volumes share `early-valley-1864-reports`.

The nine null unknowns are the eight opening strengths and WV015's logistics. No morale/readiness
score, probability, causal effect or new commander ranking is introduced. The cohort, both admission
proposals and the baseline are unchanged, with **zero promoted rows**. The baseline still uses
**23/127 engagements in 13 eligible groups**, with strength Brier **0.276882** against **0.250000**
for equal odds.

## Separate review pending

No separate review has been run for this campaign. A Claude Opus 5.5 `high` evidence-reviewer
assignment should be prepared by the primary after commit, bound to the exact commit, dossiers
and source hashes. Coverage, separate review and feature admission stay distinct.

## Review correction

A separate Claude Opus 5.5 `high` review of this pass and Early's Raid
(`valley-review-586811f-opus-high-v1`, reviewing `586811f`) required thirteen corrections and made
ten advisories. Each finding was checked against the retained selection or parent text before any
change; every new quote occurs in its cited section, and the dossiers were regenerated from the
builder. The findings for this campaign all hold and are applied:

- **VALLEY-R04** (VA117 `reinforcement-reports`): the selection does not say Grant's message
  reported "no brigade"; that wording is in the Pond parent outside the selection. The value now
  gives Weber's and Leet's warnings of Hill and Longstreet against Grant's message, which "had been
  positive the other way"; two citations added, and the rationale notes that the OCR dates
  Weber's message "July 11th" in an August context.
- **VALLEY-R05** (WV015 `casualty-records`): Pond's 35 for Gibbs's brigade follows his account of
  both the August 28 Leetown and August 29 Smithfield actions and names no day. Value corrected;
  citation added.
- **VALLEY-R06** (VA118 and VA119 `reported-force-scope`, and this memo): Pond's 17,195 adds an
  assumed 1,700 for Fitz Lee, from the June 30 and July 10 inspection reports, to the September 10
  present-for-duty figures. It is his mixed-date reconstruction, not a return total. Values,
  rationales and the opening-strength bullet above corrected; three citations added to VA118 and
  two to VA119.
- **VALLEY-R07** (VA119 `casualty-records`): Pond's Confederate 3,900–4,000 is derived from
  Early's 3,611 and an assumed cavalry ratio, and his Union table for Crook's command includes
  Fisher's Hill losses (overlapping VA120). Value and rationale corrected; three citations added
  (the reviewer's two plus Pond's reference to Early's 3,611).
- **VALLEY-R08** (VA120 `casualty-records`): Pond's 1,300–1,400 derives 1,340 by ascribing the
  105 difference between Sheridan's 1,100 prisoners and Early's 995 missing to the cavalry. Value
  and rationale corrected; citation added.
- **VALLEY-R09** (VA122 `command-roles`): Wright's order moving the cavalry to the left is
  Torbert's report as quoted by Pond. Value and rationale corrected; the order is cited in full
  with Pond's "says Torbert" attribution.
- **VALLEY-R11** (registry and this memo): `or36-1-sheridan-overland-selections-v1` was already
  registered in `sheridan-overland-reports` at `586811f`, so the v1 dependency note was false. A
  `metadata_only` successor, `or43-1-sheridan-valley-selections-v2`, supersedes v1 and binds its
  metadata hash. Its dependency note names the Overland record and says the two groups are one
  author's accounts and not mutually independent corroboration. The Valley set stays in
  `sheridan-valley-1864-reports`, so the reviewer's default is followed. **Merging it with
  `sheridan-overland-reports` would also be defensible; the primary decides.** The Families
  bullet above is corrected, and all Sheridan citations in VA117, WV014, WV015 and VA118 move
  to v2.
- **VALLEY-R12** (registry): nothing in the inspected OCR dates the Cedar Creek report October 21,
  and the Mount Jackson dispatch's day is lost. Two further `metadata_only` successors are
  registered:
  - `or43-1-early-valley-selections-v2`: its dependency note reads September 25–October 20, plus
    two dispatches whose day is lost in OCR and the undated Cedar Creek report fragment;
  - `or43-1-illinois-ocr-v2`: its inspection note calls the report "Early's Cedar Creek report,
    whose heading and date are not in this OCR".

  Both selection successors name `or43-1-illinois-ocr-v2` as parent (same bytes and hash). All
  Early citations in VA119–VA122 move to v2. The builder's family note and VA122's open question
  no longer say "October 21". The section-date maps were already correct and are unchanged.
- **VALLEY-R13** (this memo): the counts were stale. At `586811f` the repository held 153 draft
  dossiers, and this pass took the registry from 670/649 to 689/668. Corrected above.

The Early's Raid findings (R01–R03, R10) are recorded in [its memo](early-raid-first-pass-v1.md).

Advisories:

- **Adopted:**
  - A02 (WV014): the "August 22" dispatch's basis (headed "Angust 1864", day lost, received
    2 a.m. on the 23d) is stated where the dossier uses it, with the heading cited. The
    casualty rationale notes that Sheridan's 275 has no category.
  - A03 (VA119): the rationale notes the tension between "without field-works" and Early's old
    rifle-pits. Grover's 6,797 is labelled as derived (4,890 after action plus 1,907 losses),
    with two citations added.
  - A04 (VA119): Pond's wording is used: Averell sent word that he had been attacked by two
    infantry divisions.
  - A05 (VA122): the Kershaw passage is labelled as apparently from Early's memoir, which Pond
    cites in the adjoining footnote; two citations added.
  - A10: the v2 records' `document_date_note` says the section IDs `early-1864-09-23` and
    `sheridan-1864-08-22` name inferred dates mapped null. The raw transcription notes are
    immutable and unchanged.
- **Not adopted here: A09** (grouping consistency). Early's two 1864 volumes share one group,
  while Sheridan's Overland and Valley sets and Averell's 1863 and 1864 reports are split. The
  reviewer suggests recording once, in `docs/sources.md`, that same-author groups are never
  independent corroboration. This reconciliation may not edit `docs/sources.md`, so the rule is
  left to the primary. The new Sheridan v2 dependency note states it for that author.

Citations rise from 323 to 342; claims (72), unknowns (9) and disputed claims (19) are unchanged.
All eight dossiers changed: seven have wording or citation changes, and VA121 changes only in its
Early family note and the source ID of its Early citations. Their reviewed versions are retained as `data/evidence/history/*.v1.json`,
byte-identical to `586811f`, and linked by `supersedes` under revision
`sheridan-valley-review-correction-2026-09-25`. The three metadata-only successors add three
registry entries and no raw paths (registered when the registry held 736/715; the registry diff of
`e03c87e` carries them). The reviewer's unresolved historical disputes remain open, including the
missing pp.561–562. No second
reviewer pass is claimed.
