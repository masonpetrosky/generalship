# Appomattox and Waynesboro first passes: separate AI review

**Outcome: corrections required** (3 required corrections, 10 advisories).

This is an AI review. It is not a human historical adjudication, independent corroboration,
proof of source independence, or feature admission.

## Reviewer record

- Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. Separate
  evidence-reviewer subagent, started with fresh context. The author's conversation was not an input.
- Date: 2026-09-25.
- Worktree HEAD (review bundle): `ac30b17ec86fbd7dbfc28c9020ea057d50207f80`.
- Prepared commit reviewed: `02dde7d6d5dc6b5796059efabddf4b1b47f2d474`. Previous commit:
  `e72731fca9799260e77d670d691c2d0c20e8f6d9`.
- Assignment: `assignment.md`, sha256
  `5d79d2fb15c0b0c516ab0f1d248316b17b439dbea78bcfe3ccedcb8e84eab68d`.
- Input manifest: `inputs.json`, sha256
  `4ac7a10164ba09609b8fe1c19eaa7fa4e71668249bdbb9acbcc8a090fecba90e`.
- **Input hashes:** all 75 bound paths were hashed twice, once from
  `git show 02dde7d6…:<path>` and once from the worktree file. Every hash matched the manifest,
  with **no mismatches**. `git diff 02dde7d ac30b17` touches only the two bundle files.
- **Validation:** `make check` was run offline at the worktree HEAD. `unittest` ran 134 tests: OK.
  `python3 -m generalship check` passed with `artifacts_written: false`. No build, packet or network
  command was run. The worktree was clean before this file was written.
- Writes: this file only.

## Scope actually inspected

- **Governing docs:** AGENTS.md; `docs/evidence-contract.md` (full);
  `docs/methodology.md` (research depth and coverage, and the identification/phase passage);
  `docs/cohort-v2.md` (full). I also read both memos in full:
  `appomattox-first-pass-v1.md` and `sheridan-petersburg-1865-first-pass-v1.md`.
- **Dossiers:** all 15 dossiers (VA085–VA097, VA123, VA124) were read claim by claim, covering
  every value, rationale, status, phase, boundary note and open question. I checked **all 589
  citation occurrences**: the 546 Appomattox citations plus VA123's 43. Each text quote was read
  inside its section with about 200 characters of context on each side. Each CSV citation was
  checked against its frozen row. I recomputed the claim, unknown, citation, disputed and phase
  counts, and the independence groups cited per dossier.
- **Frozen rows and live pages:** I read the frozen `cwsac_battles`, `cwsac_forces` and
  `cwsac_commanders` rows for all 15 records. I read all 15 NPS text snapshots in full. The NPS
  HTML parents were checked by hash only.
- **Source records:** I read all 40 records added to `data/sources.json`. None was modified, and
  their selection character ranges do not overlap any existing selection of the same parent. I
  compared them with the pre-existing groups: `humphreys-gettysburg-rapidan-1883`,
  `lee-richmond-petersburg-dispatches`, `sheridan-valley-1864-reports`,
  `sheridan-overland-reports`, `fitz-lee-kellys-ford-reports` and `pond-shenandoah-valley-1883`.
  I confirmed that the previous registry had no earlier group for Bushrod Johnson, Miles, Gibbon
  or Ewell.
- **Selections read:**
  - Humphreys (Appomattox) was read around every cited quote. I read these sections substantially
  in full: `appendix-l-returns`, `high-bridge-and-farmville`, and the close of `appomattox`.
  - I read the Humphreys Petersburg selection's `spring-1865-strengths` section in full.
  - The Lee, Sheridan, Johnson (including its casualty note), Miles, Gibbon, Ewell and Fitz Lee
    selections were read around every cited quote. I also read some additional passages, such as
    Fitz Lee on Deep Creek and on his burned records.
  - I read the Pond and Sheridan Waynesborough selections in full.
- **Locators:**
  - I mechanically checked all 432 sectioned citations against the OCR running heads. Every locator
    matched a detectable head, apart from the declared inferred cases.
  - I confirmed that pp.322, 373 and 432 have no running head. The p.354 head reads '854'.
  - Lee's p.1265 head, which reads `'285`, falls in the parent gap excluded between sections
    `lee-1865-04-02-a` and `lee-1865-04-02-b` (parent characters 4785733–4785793). The p.1264 and
    p.1265 locators are therefore consistent.
- **Not inspected:** the full parent OCR files beyond that one gap; the reports the memos list as
  deferred; and print facsimiles. I did no new research.

## Overall assessment

- **Support.** The extraction is careful. Nearly every claim says only what its quotes support in
  context.
  - Attributions are correct. Examples: Humphreys relaying Hunton, McGowan, Ayres, Gillespie,
    Wilcox, Gibbon, Ord and Sheridan, including the "only cavalry" passage, which is Sheridan's
    words quoted by Humphreys; Ewell's figures "at the time of the evacuation"; and Miles's list
    dating the Sutherland's Station captures April 1.
  - Dates are right. Johnson's bracketed "28th [29th]" is correctly read as March 29. Fitz Lee's
    Namozine passage sits within the march of April 3.
  - I found no quote that belongs to the wrong side or engagement.
- **Rules.**
  - All 15 opening strengths are null unknowns. No figure is adopted.
  - Live zeros are labelled as not measured absence in every force claim.
  - Unknowns have no citations.
  - Every record uses exactly three families, correctly grouped. NPS and Arnold are counted as one.
  - No listed commander receives automatic credit.
- **Memo figures.** The totals in both memos match the dossiers exactly:
  - Appomattox: 126 claims, 20 unknowns, 546 citations and 25 disputed claims; 6 claims tagged
    `inherited` and 1 tagged `commander_created`.
  - Waynesboro: 9 claims, 1 unknown, 43 citations and 3 disputed claims.
- **Source choices in item 4 of the assignment.** All of them are sound:
  - **Humphreys as a family where he commanded a corps.** This is sound because it is labelled.
    The boundary notes of VA087, VA089, VA090, VA093, VA094, VA095 and VA097 all identify his
    account as a participant's. His self-referential statements are attributed as his, for
    example the order to Miles, the refusal of Lee's requests, and the "Without it…" counterfactual.
  - **Reused author groups (Lee, Sheridan, Fitzhugh Lee).** These are sound, and the dependency
    notes explain that each group name reflects an earlier campaign. Sheridan already had two
    same-author groups before this pass, `sheridan-overland-reports` and
    `sheridan-valley-1864-reports`. No dossier here uses both, and the notes say one author's
    accounts are not independent.
  - **New groups for Johnson, Miles, Gibbon and Ewell.** These are correct. No prior group exists
    for any of them.
  - **The spring 1865 strengths paragraph.** It is correctly cited from
    `humphreys-petersburg-selections-v1#spring-1865-strengths`. That range, 756666–757688, lies
    between the new `chapter-xiii-opening` and `march-28-29` ranges and is not selected twice.
  - **Totals that span records.** Keeping them as context is correct:
    - VA088 keeps the 2,599 prison-record total as context and separates the 2,063 entry for
      Five Forks on April 1.
    - VA094 correctly treats Humphreys' 571 as a whole-day total spanning VA094 and VA095.
    - VA095 misstates this total; see APX-R1.
  - **Inferred page locators.** These are verified as described above.

## Required corrections

### APX-R1: VA095, `casualty-records`, April 7 figure misstated

The rationale ends "No figure is given for April 7." That is incorrect. Humphreys gives a
whole-day Second Corps loss for April 7 of 571: "The loss of the Second Corps to-day was five
hundred and seventy-one officers and men killed, wounded, and missing." This is in section
`high-bridge-and-farmville`, p.390. VA094 correctly records it as spanning VA094 and VA095. The
correction keeps the figure unassigned, but the dossier must not say that no figure exists.

- **`value`: append this sentence.** "Humphreys gives the Second Corps' loss for the whole of
  April 7 as 571 killed, wounded and missing, a day total that also covers Barlow's fight near
  Farmville and Cumberland Church (VA094)."
- **`citations`: add this citation.**
  `{"source_id": "humphreys-appomattox-selections-v1", "section": "high-bridge-and-farmville", "locator": "p.390 (OCR page markers; not checked against print)", "quote": "The loss of the Second Corps to-day was five hundred and seventy-one officers and men killed, wounded, and missing."}`
  It uses the same exact quote and locator already validated in VA094.
- **`rationale`: replace** "No figure is given for April 7." **with** "Humphreys' April 7 figure
  (571) is a whole-day Second Corps total spanning this record and VA094; it is not assigned to
  either alone, and no figure specific to the High Bridge crossing is given."

### APX-R2: VA096, `supply-trains`, phase and rationale

This is the only claim in the batch tagged `commander_created`. It mixes four things:

- pre-existing supply trains at the depot;
- Sheridan's and Custer's decisions during the action;
- the capture itself, which is part of this engagement's result;
- Humphreys' counterfactual that Lee "lost the supplies awaiting him at Appomattox Station"
  because of his detention on April 7.

That counterfactual is a campaign-contribution judgment tied to VA094. VA094's rationale already
labels it that way, but VA096 uses it here without that caveat. The current rationale, "created by
the action", describes an engagement outcome, not a condition a commander created. Other
`commander_created` tags in the registry are used for attributed decisions or features, with
contribution explicitly not estimated. The methodology says uncertain classifications stay
`unresolved`.

- **`phase`:** change `commander_created` to `unresolved`.
- **`rationale`: replace the whole rationale with:** "The counts differ (four against three), and
  NPS says the trains were burned where Sheridan says they were run back; all are preserved. The
  claim mixes pre-existing supply trains at the depot, in-action decisions by Sheridan and Custer,
  and the capture that forms part of this engagement's result, so it is not tagged as a whole.
  Humphreys' statement that Lee lost these supplies is his participant's campaign-contribution
  judgment about the April 7 detention (VA094), not a measured logistics effect. No contribution
  is estimated."

The memo's "Tags" bullet then needs to change. The Appomattox batch would have no
`commander_created` claims, and the capture of the trains moves to the list of `unresolved` claims.

### APX-R3: VA096, `casualty-records`, NPS statement contradicts the cited field

The value quotes the live NPS field "1,048 (US 48; CS 1,000)". It then says "Humphreys and NPS give
no loss figures." NPS is the source of that field.

- **`value`: replace** "Humphreys and NPS give no loss figures." **with** "Humphreys gives no loss
  figures, and the NPS description adds none beyond the live casualty field."

## Advisories (not required)

1. **VA087 `casualty-records` rationale.** Johnson's casualty note gives 187 for the White Oak road
   without stating its unit. VA085 treats the note's unit as garbled ('Muse') and its population as
   unclear. The note later names Moody's brigade separately, which suggests its earlier lines
   describe one brigade, not the division.
   - Suggested addition: "The note's unit is garbled in OCR ('Muse' in its first entry) and its
     population is unclear; its 187 is not compared with or added to Johnson's division-wide
     800."
2. **VA088 `reported-force-scope`.** The phrase "on reporting on March 27" dates Sheridan's 9,000
   more precisely than the passage does. Sheridan's text says Crook's division reported on
   March 27. It then says "The effective force of these three divisions of cavalry was as follows"
   without a date, and the force moved out on the 29th.
   - Suggested wording: "Sheridan gives the effective force of his three cavalry divisions, as
     assembled when Crook's division reported on March 27 (the figure is not itself dated), as
     9,000 …"
   - The memo's "Sheridan's 9,000 effective cavalry on March 27" should be softened the same way.
3. **VA094 `reported-force-scope` rationale.** "His contemporary estimate" should read: "the
   estimate Humphreys says he sent Meade that afternoon, as retold in his 1883 history (the
   dispatch itself was not inspected)."
4. **Live Confederate zeros in VA092 and VA094.** The memo says the live Confederate casualty
   zeros at Rice's Station and Cumberland Church are not measured absence. Only VA124 and VA091
   say so in their `casualty-records` rationale.
   - Suggested addition to the VA092 and VA094 `casualty-records` rationales: "The live
     Confederate zero is not measured absence."
   - Alternatively, narrow the memo sentence to the records that state it.
5. **"Cited once."** The VA085 boundary note and the memo say the spring 1865 army-wide returns are
   cited once, in VA085. VA086 also cites the same paragraph's sentence on Sheridan's cavalry
   (13,000 present for duty). Nothing is summed, so there is no double counting, but the wording
   should acknowledge VA086's use.
6. **NPS commander conflation.** The NPS descriptions of VA086 and VA087 read "Maj. Gen. W.H.
   Fitzhugh Lee's cavalry", which conflates W. H. F. Lee and Fitzhugh Lee. Neither dossier uses
   that phrase for attribution. A note in each `command-roles` rationale would make the
   conflation visible.
7. **`pond-waynesboro-selections-v1` dependency note.** It copies two parent sentences that are
   inaccurate for this record:
   - "not independent of the Official Records families selected in this pass";
   - "No earlier registry group for this author". The group `pond-shenandoah-valley-1883`
     already held three records.

   The grouping itself is correct. `humphreys-appomattox-selections-v1` similarly repeats the
   parent's Overland-specific sentences about Volume XXXVI, which are stale but harmless. If
   either note is changed, follow the contract's `metadata_only` revision rule: a new source ID
   with `supersedes`. Do not edit the recorded source entry in place.
8. **`or46-1-johnson-appomattox-selections-v1` dependency note.** It could add that Humphreys
   relays Johnson's account of his April 6 losses ("General Bushrod Johnson … says that his loss
   was small", section `sailors-creek-and-rices-station`, p.384). The two are therefore not
   independent for Sailor's Creek. The pass does not pair them there.
9. **VA093 `casualty-records`.** This is an optional completeness point. Humphreys' separate
   estimate for Gordon at Perkinson's mill, "their total loss could not have been less than
   2,000" (p.381), could be recorded. It is currently subsumed in the "not less than 8,000" day
   total.
10. **VA095 boundary note.** The note could state, as VA094's does, that Humphreys is a frozen
    commander of this record as well as a participant historian.

## Unresolved and not adjudicated

The following remain source disputes, preserved as the dossiers record them:

- Five Forks prisoners and guns;
- Sailor's Creek strengths;
- Read's party of 580, against the 780 and 800 prisoners reported;
- the Appomattox parole counts;
- the NPS flank at Waynesboro;
- the frozen and live casualty and result differences.

This review does not resolve them. It does not change phase hypotheses beyond APX-R2, admit
features, or alter the v1 cohort, the baseline or admission artifacts.
