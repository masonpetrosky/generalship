# Bermuda Hundred and Richmond-Petersburg first passes: separate review (Opus 5.5, high)

**Outcome: corrections required.** Required findings: PB-R1 to PB-R8. Advisories: PB-A1 to PB-A16.

This is an AI review, a separate analysis. It is not human historical adjudication. It does not
establish that any source is independent, and it does not admit any feature. A source-backed claim
can still be historically wrong.

## Record

| Field | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. Fresh-context subagent; the author's conversation was not an input. |
| Date | 2026-09-25 |
| Prepared commit reviewed | `40748efdb258cc0382675ebb0bb77f75ad5c2d4a` |
| Previous commit | `f22b0495c91ba5be06684e9d3a0cc47395caa8e6` |
| Bundle commit (worktree HEAD) | `b8d19758f70f04d12cf6c22a5bc4d569af78af03` |
| `assignment.md` sha256 | `bdde73d2ae462ab77831970e73f0c01eab4338b03cb14896cffba0d1211b4c90` (verified) |
| `inputs.json` sha256 | `108aa60983d3638ca1c9e555d385347fe1a996de4f31884844f25ac5b3e7801e` (verified) |
| Input hashes | All 114 paths in `inputs.json` match both `git show 40748ef:<path>` and the worktree file. No mismatch. |
| `make check` (offline) | Passed at the bundle commit: `Ran 134 tests … OK`. `python3 -m generalship check` exited 0 and reported 218 draft dossiers and 0 promoted admission rows. No build, packet or network command was run. |

## Scope actually inspected

- **Documents.**
  - Read in full: AGENTS.md, `docs/evidence-contract.md`, `docs/cohort-v2.md`, both memos
    (`bermuda-hundred-first-pass-v1.md`, `petersburg-first-pass-v1.md`) and the `docs/sources.md`
    diff from `f22b049`.
  - Read in part: `docs/methodology.md` (the research-depth and coverage section).
  - Not re-read: README and roadmap.
- **Dossiers.** All 24 (VA047, VA050, VA051, VA053, VA054, VA098, VA063, VA065, VA113, VA067, VA068,
  VA069, VA070, VA071, VA072, VA073, VA075, VA074, VA077, VA078, VA079, VA080, VA083, VA084). For
  each I read every claim's value, status, phase and rationale, the boundary note and the open
  questions.
  - **Text citations.** Every one was printed with about 170–300 characters of context on each
    side. Where attribution, date or scope needed it, I read wider passages, for example:
    - Hagood's May 9 paragraph;
    - Beauregard's 10 a.m. passage and his June 14 letter;
    - the Humphreys Globe Tavern page break (pp.277–278);
    - the Boydton footnote that spills into the `fair-oaks` section (pp.303–304);
    - Humphreys pp.213–215 (Johnson's division, Lee's June 16 telegrams);
    - Humphreys pp.280–283 (Reams's Station) and pp.320–321 (Fort Stedman).
  - **CSV and NPS citations.** Checked against the frozen battle, force and commander rows for all
    24 records and against all 24 live NPS text snapshots, which I read in full.
- **Selections.**
  - Read in full: Butler, Hagood, Barton, Beauregard, Gillmore, Meade, Hancock (selected part),
    Hampton, Stannard, and all three Lee selections.
  - Read at every cited passage plus surrounding context, not end to end: Humphreys (both
    selections, about 235 KB), Burnside and Wilson.
  - Selection integrity: I re-derived all 94 non-editorial sections of the 16 new selection files
    from their parent OCR, using the recorded character ranges and whitespace collapse. All 94
    match exactly. I also read the unselected gap between Barton's two sections.
- **Registry.** I compared `data/sources.json` with `f22b049`: 71 records added and none changed or
  removed. The 71 are the 70 of this pass plus `cox-atlanta-selections-v2`, an Atlanta successor
  outside this assignment. I read the full records for:
  - the 14 report selections and both Humphreys selections;
  - the three volume metadata/OCR pairs;
  - one NPS HTML/text pair.

  All 70 raw hashes and parent hashes match. For context I also checked the earlier groups
  `meade-overland-report` (`or36-1-meade-overland-selections-v1`) and the earlier `lee-*` groups.
- **Mechanical checks.**
  - I recounted claims, unknowns, citations, `disputed` counts and phase tags per dossier. Both
    memo tables are correct: 45/8/175 and 172/24/681 claims/unknowns/citations; 14 and 37
    `disputed`; 19 `inherited` terrain claims and 1 `commander_created`.
  - Cited independence groups per dossier: every record uses exactly three families, counting
    NPS/CWSAC as one. The family assignments match the memo tables.
  - A script listed numbers that appear in a claim value but in none of that claim's quotes. I
    checked each hit by hand.
- **Not done.**
  - No new research.
  - No other source families opened.
  - No check against print or page images; page locators rely on OCR running heads.
  - The NPS HTML to text normalization was not re-derived.

## Required corrections

### PB-R1 — VA065 `casualty-records`: Lee's June 24 loss has the wrong scope

Lee's dispatch of June 25, 9 p.m. gives "Our entire loss yesterday morning was 97 killed and wounded
and 209 missing." His June 24 dispatch describes that morning separately from Mahone's June 22–23
fights: "This morning the enemy was felt on both flanks, and a part of one of General Hoke’s brigades
entered his works." The dossier presents 97/209 as Lee's loss in this record without that scope. The
passage does not tie it to the Jerusalem Plank Road fighting.

- **`value`.** Replace "…about 600 prisoners on June 23, and his own loss on June 24 as 97 killed and
  wounded and 209 missing." with:

  > …about 600 prisoners on June 23, and, separately, his entire loss on the morning of June 24 as 97
  > killed and wounded and 209 missing, the morning on which he reports that part of one of Hoke's
  > brigades entered the enemy's works; the inspected passages do not tie that action to Mahone's
  > fights or establish that it belongs to this record.

- **Add citation.**
  - Source: `or40-1-lee-petersburg-selections-v1`
  - Section: `lee-1864-06-24`
  - Locator: `p.750 (OCR page markers; not checked against print)`
  - Quote: `This morning the enemy was felt on both flanks, and a part of one of General Hoke’s brigades entered his works.`
- **`rationale`.** Append:

  > Lee's June 24 morning loss belongs to the Hoke attack he reports that day; it is not assigned to
  > this record or added to its totals.

### PB-R2 — Barton selection: Ransom's undated indorsement sits in a section dated May 12

`or36-2-barton-chester-station-selections-v1` maps section `barton-1864-05-12` to `1864-05-12`.
That section's range (parent characters 726675–737172) ends with a separate document:

> [Indorsement.] Headquarters Department of Richmond, … In my report of Barton s case it will be
> remarked upon. R. RANSOM, Jr., Major- General.

The indorsement is by another author and has no legible date. The transcription note says such
papers are "separately headed where their author differs". As mapped, `source_document_date` would
give Ransom's indorsement Barton's May 12 date. The contract forbids borrowing a neighbouring
document's date.

The record's `inspection` is also inaccurate. It says the covering letter's "indorsements" were
selected. The three indorsements that follow the May 16 letter lie in the unselected gap (parent
725729–726675) and are not in the snapshot:

- Cooper, May 16;
- Davis;
- Cooper, May 20.

Correction. The snapshot bytes change, so this is a new raw artifact, not a `metadata_only`
revision. Keep v1 and its file unchanged.

1. Add `or36-2-barton-chester-station-selections-v2`, with a new file
   `data/raw/bermuda-hundred-v1/barton-selections-v2.txt`, the same parent and the same
   transform. Its ranges are:
   - `title` 1750–2315;
   - `barton-1864-05-16` 724688–725729;
   - `barton-1864-05-12` 726675–736975;
   - `ransom-indorsement` 736975–737172.

   Its `document_dates_by_section` gives `ransom-indorsement` null and keeps the other dates.
2. Set its `inspection` to say the May 16 letter, the May 12 report and Ransom's undated
   indorsement were selected, and that the letter's three indorsements (Cooper May 16, Davis,
   Cooper May 20) were read but not selected.
3. In VA051 `command-roles`, re-point the Ransom citation:
   - Source: `or36-2-barton-chester-station-selections-v2`
   - Section: `ransom-indorsement`
   - Locator: `p.217 (OCR page markers; not checked against print)`
   - Quote: unchanged (`In my report of Barton s case it will be remarked upon.`)
4. Re-pointing VA051's other Barton citations to v2 is optional. Their section names and text are
   unchanged.

### PB-R3 — Statements Lee relays from subordinates are attributed to Lee himself

Several values say "Lee says". The cited sentences are in dispatches that explicitly relay a
subordinate's report, so the attribution should say so.

- **VA113 `recorded-result`, `value`.**
  - Replace: "Lee says the enemy was signally repulsed at the bridge and retreated;"
  - With: "Lee relays W. H. F. Lee's statement that the enemy was signally repulsed at the bridge
    and retreated;"
  - Add citation:
    - Source: `or40-1-lee-petersburg-selections-v1`
    - Section: `lee-1864-06-26`
    - Locator: `p.751 (OCR page markers; not checked against print)`
    - Quote: `He also states that the enemy was signally repulsed at the bridge the same evening`
- **VA113 `casualty-records`, `value`.**
  - Replace: "Lee reports about thirty enemy dead left on the field;"
  - With: "Lee relays W. H. F. Lee's report of about thirty enemy dead left on the field;"
- **VA068 `recorded-result`, `value`.**
  - Replace: "Lee says the enemy was completely routed with guns, prisoners, wagons and ambulances
    captured;"
  - With: "Lee's June 29 dispatch, which opens by relaying Hampton's report, says the enemy was
    completely routed with guns, prisoners, wagons and ambulances captured (the dispatch does not
    separate Hampton's report from Lee's own words);"
  - Add citation:
    - Source: `or40-1-lee-petersburg-selections-v1`
    - Section: `lee-1864-06-29`
    - Locator: `p.752 (OCR page markers; not checked against print)`
    - Quote: `General Hampton reports that he attacked the enemy’s cavalry yesterday afternoon`
- **VA068 `command-roles`, `value`.**
  - Replace: "Lee reports Mahone's attack in front and Fitzhugh Lee's turning of the flank."
  - With: "Lee's dispatch relaying Hampton's report describes Mahone's attack in front and Fitzhugh
    Lee's turning of the flank."
- **VA079 `recorded-result`, `value`.**
  - Replace: "Lee says the enemy retired during the night leaving his wounded and more than 250
    dead."
  - With: "Lee relays Hill's report that the enemy retired during the night leaving his wounded and
    more than 250 dead."
  - Add citation:
    - Source: `or42-1-lee-petersburg-selections-v1`
    - Section: `lee-1864-10-28`
    - Locator: `p.853 (OCR page markers; not checked against print)`
    - Quote: `General Hill reports that the attack of General Heth upon the enemy on the Boydtou plank road,`

### PB-R4 — VA084: Humphreys' first-person role at Fort Stedman is not flagged

The dossier cites Humphreys for the Second Corps' picket-line capture, its loss of 690 and its
prisoners. In that passage Humphreys writes as the corps commander (p.320): "I at once got the
Second Corps under arms ready to move, ordered the division commanders to make strong
reconnoissances". The memo flags his participant role only for VA079 and VA083, and no VA084
rationale mentions it.

- **VA084 `recorded-result` and `casualty-records`, `rationale`.** Append to each:

  > Humphreys commanded the Second Corps on March 25 and narrates its picket-line attack in the
  > first person; his account of that attack and of the Second Corps' losses and prisoners is a
  > participant's account.

- **Add citation to VA084 `recorded-result`.**
  - Source: `humphreys-petersburg-selections-v1`
  - Section: `fort-stedman`
  - Locator: `p.320 (OCR page markers; not checked against print)`
  - Quote: `I at once got the Second Corps under arms ready to move, ordered the division commanders to make strong reconnoissances`

### PB-R5 — Qualifiers or attributions the cited passage does not contain

- **VA047 `reported-force-scope`, `value`.**
  - Replace: "…82 guns and Kautz's 97 officers and 2,804 men of cavalry present for duty, and says
    Beauregard's arriving brigades gave about 19,000 effective infantry. Hagood reports an aggregate
    of about 1,500 men engaged on May 7…"
  - With: "…and 82 guns (built from corps figures he gives as present for duty), and Kautz's cavalry
    as 97 officers and 2,804 enlisted men, and says Beauregard's arriving brigades gave an effective
    infantry force (enlisted men present for duty) of 19,000. Hagood reports an aggregate of 1,500
    men (OCR 'ihadanaggre eate of 1 500') engaged on May 7…"
  - Why:
    - Hagood's quoted figure and Humphreys' 19,000 carry no "about".
    - Humphreys' "present for duty" qualifies the corps figures, not Kautz's line.
    - The contract forbids inferring estimation from roundness.
- **VA047 `command-roles`, `value`.**
  - Replace: "Humphreys says Butler sent a brigade out to the railroad on May 6 and some force from
    his two corps on May 7,"
  - With: "Humphreys says a brigade was sent out to the railroad and pike on May 6 (the passage does
    not name who sent it) and that on May 7 General Butler sent some force from his two corps,"
  - Why: the cited May 6 quote, "A brigade was sent out to these roads," is passive.
- **VA083 `reported-force-scope`, `value`.**
  - Replace: "an effective infantry force of about 50,000 (3,609 officers and 50,155 men on its
    December 20 return)"
  - With: "an effective force of infantry amounting to 50,000 (his footnoted December 20 return
    totals 3,609 officers and 50,155 enlisted men, excluding Wise's brigade)"
  - Add citation:
    - Source: `humphreys-petersburg-selections-v1`
    - Section: `winter-1864-65`
    - Locator: `p.308 (inferred: chapter opening page without a running head in OCR; not checked against print)`
    - Quote: `Wise’s brigade is not included in the above numbers.`
- **VA051 `railroad-and-reconnaissance`.**
  - `value`: replace "Humphreys says Butler's May 9 operation aimed to destroy the railroad between
    Swift Creek and Chester Station." with "Humphreys says Butler's force destroyed the railroad
    between Swift Creek and Chester Station on May 9."
  - `rationale`: replace with "Stated aim from a summary; Humphreys reports the previous day's
    destruction, not an aim for May 10."

### PB-R6 — Figures and statements in values that no citation of the claim supports

Each fact below is in the value but in none of that claim's quotes. The supporting text is in the
same selected section. Add these citations; the values need no change. All quotes are verified
exactly in the named section. Locators use the OCR page markers and are not checked against print.

| Dossier / claim | Source | Section | Locator | Quote to add |
| --- | --- | --- | --- | --- |
| VA053 `reported-force-scope` | `humphreys-bermuda-selections-v1` | `drurys-bluff` | p.149 | `Ames being at Walthall Junction with his division, about 5,000 strong, Hinks with his division of 5,000 at City Point, and about 3,000 having been left in the Bermuda Hundred intrenchments.` |
| VA053 `recorded-result` | `or36-2-beauregard-drewrys-bluff-selections-v1` | `beauregard-1864-06-10` | p.204 | `leaving in our hands some 1,400 prisoners, 5 pieces of artillery, and 5 stand of colors.` |
| VA054 `reported-force-scope` | `humphreys-bermuda-selections-v1` | `ware-bottom-and-detachments` | p.159 | `Kautz’s cavalry, 2, 600 ; and Hinks’s colored cavalry, about 2,000.` |
| VA063 `reported-force-scope` | `humphreys-petersburg-selections-v1` | `assaults-june-15-18` | p.215 | `General Johnson’s division, whose effective strength, with¬ out Gracie’s brigade, was 3,500,` |
| VA063 `casualty-records` | `humphreys-petersburg-selections-v1` | `assaults-june-15-18` | p.224 | `Taking the usual pro¬ portion for the killed, we have 1,240,` |
| VA069 `reported-force-scope` | `humphreys-petersburg-selections-v1` | `deep-bottom-july` | p.249 | `on the 29th Field’s and Fitz Lee’s divisions united with them.` |
| VA070 `reported-force-scope` | `or40-1-burnside-petersburg-selections-v1` | `burnside-1864-11-26` | p.525 | `it was composed of less than 6,000 veterans,` |
| VA070 `salient-exposure` | `humphreys-petersburg-selections-v1` | `petersburg-mine` | p.256 | `concealed in woods, and well covered by traverses, so that we could not silence it.` |
| VA073 `command-roles` | `humphreys-petersburg-selections-v1` | `reams-station-august` | p.281 | `and the fine conduct of its commander, General Miles,` |
| VA073 `casualty-records` | `humphreys-petersburg-selections-v1` | `reams-station-august` | p.283 | `His casualties were 610 officers and enlisted men killed and wounded,` |
| VA079 `reported-force-scope` | `humphreys-petersburg-selections-v1` | `boydton-plank-road` | p.296 | `General Parke assigned 1,500 men to hold his intrench¬ ments ; General Warren 2,500 under the command of General Baxter, to hold his.` |
| VA084 `casualty-records` | `humphreys-petersburg-selections-v1` | `fort-stedman` | p.321 | `358 officers and enlisted men were captured from them.` |

### PB-R7 — Two `inherited` terrain claims include conditions that arose during the engagement

The assignment's rule is `inherited` only where the passage shows pre-existing conditions. Two
claims do not meet it:

- **VA051 `wooded-ridge-and-morass`.** It includes the Union fortifying "begun", the woods "fired
  early in the action" and the combat range. Its own rationale says these arose during the action.
- **VA053 `intrenchments-and-fog`.** It includes a fog that "suddenly enveloped both armies" just
  before day on May 16, inside the frozen May 12–16 interval.

Correction:

- **VA051 `wooded-ridge-and-morass`.**
  - `phase`: change `inherited` to `unresolved`.
  - `rationale`: replace with "Mixed claim: the ridge, woods and morass predate the action, but the
    Union fortifying, the woods fire and the close range arose during it, so the claim as a whole
    is not tagged inherited. No map verification."
- **VA053 `intrenchments-and-fog`.**
  - `phase`: change `inherited` to `unresolved`.
  - `rationale`: replace with "Mixed claim: the intrenched lines predate the battle, but the fog
    formed during it (just before day on May 16), so the claim as a whole is not tagged inherited.
    No map verification."
- **Equivalent alternative.** Split each into an `inherited` claim with only the pre-existing
  ground and works, and an `unresolved` claim with the rest. Keep the existing claim ID on the
  inherited part.

### PB-R8 — VA080 `casualty-records`: a frozen-description count is left out

The frozen description and the live NPS description both say "Confederate forces counterattacked,
taking some 600 prisoners." Neither this claim nor any other VA080 claim accounts for it. The
assignment asks that nothing in the frozen rows go unaccounted.

- **Add citation.**
  - Source: `arnold-cwsac-battles`
  - Row key: `{"battle": "VA080"}`
  - Column: `description`
  - Quote: `Confederate forces counterattacked, taking some 600 prisoners.`
- **`value`.** After the live figure, insert:

  > The frozen description says the Confederate counterattack took some 600 prisoners.

- **`rationale`.** Append:

  > The description's 600 prisoners, Lee's 'several hundred' on October 27 and Field's 'upward of
  > 400' may overlap and are not added.

## Advisories (no required change)

- **PB-A1 — Lee registry notes.** The dependency note on all three `lee-*-petersburg-selections-v1`
  records names the recipients as "the Secretary of War, the President and Bragg". The selected
  dispatches go to the Secretary of War (Seddon, and later Breckinridge) and to General S. Cooper
  (February 5 and the second Hatcher's Run dispatch). None selected goes to the President or
  Bragg. A `metadata_only` revision could fix the note.
- **PB-A2 — Humphreys registry note.** `humphreys-petersburg-selections-v1` copies the Overland
  dependency note. Its Petersburg-specific dependencies appear only in dossier text:
  - reliance on Hancock, Warren, Wilson and Stannard;
  - Lee's despatches quoted in the Boydton footnote;
  - his first-person roles on October 27, at Hatcher's Run and at Fort Stedman.

  An optional `metadata_only` revision could record them.
- **PB-A3 — VA079 `casualty-records`.** The Adjutant General's figures of 143, 653 and 488 belong
  to Boydton. They are the end of the Boydton footnote 4, printed on p.304, which falls inside the
  `fair-oaks` selection range. The attribution is right; the locator could say "Boydton footnote
  continued on p.304". Humphreys adds that the table's wounded are in error and its killed and
  missing correct. That qualifier could go in the rationale.
- **PB-A4 — VA072, text lost at the page break.** At the p.277/278 break the OCR loses a line:
  - "Warren’s own loss was 301 killed, [lost] wounded, and missing" (August 21) is not recorded;
  - the footnote quoted in `command-roles`, "too many conditions to impose upon him…", has lost
    its opening words.

  Both could be noted in the rationales. No count should be inferred.
- **PB-A5 — VA053 prisoner list.** The garbled rows are internally consistent with a two-row list
  and a total: 42 + 1 = 43; 1,174 + 171 = 1,345; 1,216 + 172 = 1,388. That supports reading
  43/1,345/1,388 as the totals row rather than a Petersburg row. The dossier's refusal to assign
  columns is still appropriate.
- **PB-A6 — VA077 and VA084 terrain tags.** Both `inherited` claims also carry non-terrain content:
  - VA077 `swamp-rear`: the loss of eight guns;
  - VA084 `close-lines-and-forts`: the pre-dawn darkness at the hour the attacker chose.

  Consider the PB-R7 treatment.
- **PB-A7 — VA080 overlap.** Lee's October 27 "several hundred prisoners and four stand of colors"
  and his October 28 "Field captured upward of 400 prisoners and 7 stand of colors" probably
  overlap. PB-R8 adds the note.
- **PB-A8 — VA084.** The frozen description's "captured more than 1,900" is not cited. Parke's
  1,949 is consistent with it and could be set beside it.
- **PB-A9 — VA053 families.** NPS, Humphreys and Beauregard respect the ceiling. Humphreys quotes
  Beauregard's reports and telegrams, so this record has no Union principal's own account and its
  three families are not three independent witnesses. Leaving Butler's telegrams out under the
  ceiling is sound and is recorded in the open questions.
- **PB-A10 — VA073 `command-roles`.** Humphreys reports that Gibbon's division "responded feebly"
  and that Gibbon said it could not retake its works. This is responsibility evidence in the
  selected passage that the claim omits.
- **PB-A11 — VA071.** "Lee called his loss small" comes from the August 16, 8.30 p.m. dispatch and
  covers that day only. The value could say so.
- **PB-A12 — VA067 `exhaustion-and-supply`.** The "81 hours" is uncited. Suggested citation:
  `During this interval of eighty-one hours` (section `wilson-1865-02-18`, p.624).
- **PB-A13 — VA074.** Lee's "400 prisoners" is itself relayed ("General Hill reports"). "Lee
  reports" is acceptable, but "Lee relays Hill's report" would be more exact.
- **PB-A14 — Memos, if corrections are applied.**
  - Bermuda: change "about 1,500" and the four `inherited` tags.
  - Petersburg: add VA084 to Humphreys' participant roles, and add the VA065 scope.
- **PB-A15 — Gillmore's section date.** Gillmore's June 12 note says the report was completed on
  June 10, but the section date is null. That is conservative and acceptable.
- **PB-A16 — Out-of-scope record.** The registry diff also adds `cox-atlanta-selections-v2`. I did
  not review it.

## Assessment of the specific decisions

- **Meade's Volume XL continuation kept in `meade-overland-report`: sound.** The selection's own
  footnote reads "For portion of report (here omitted) covering; operations from May 4 to June 13,
  1864, see Vol. XXXVI, Part I, p. 188". It is the same November 1 document, and the section date
  matches the Overland record.
- **One Lee group across three volumes: sound.** It follows the per-campaign `lee-*` convention
  and counts the campaign's dispatches as one family, which is conservative. The dossiers do not
  always carry the relay caveat into the value; see PB-R3 and PB-A13. The recipient note is wrong;
  see PB-A1.
- **Humphreys kept as a family for VA079 and VA083: acceptable, with labels.**
  - Both dossiers label him a participant.
  - As a result, neither record has a non-participant family other than NPS/CWSAC. Humphreys was
    Meade's chief of staff at VA079 and corps commander at VA083.
  - The same applies to VA084, where the role is unflagged; see PB-R4.
- **Butler's telegrams selected but not cited at VA053: sound.** They would be a fourth family.
  The deferral is recorded.
- **Null section dates where the OCR date is illegible: sound.** The cases are:
  - Hancock's "November 11, 1861";
  - Lee's "October <9" and "February d";
  - Gillmore's garbled heading;
  - Stannard's undated report;
  - Beauregard's addenda.

  The one date error found is the opposite case: a date carried onto an undated document by
  another author (PB-R2).
- **`inherited` and `commander_created` tags: mostly sound.**
  - The crater as `commander_created`, with the rationale that it hindered the attackers, is
    appropriate.
  - VA054 and VA098 are conservatively `unresolved`, and VA078's line (built after October 7,
    before October 13) is correctly `inherited`.
  - Exceptions: PB-R7 and PB-A6.
- **Other rule checks passed.**
  - No strength is adopted as an opening force.
  - All unknowns are null and carry no citations.
  - Multi-record totals are kept apart: raid-wide figures, Hampton's June 28–30 captures and army
    returns.
  - No listed commander gets automatic credit.
  - Disputes stay visible, including Hoke against Finegan, 170 against 176, the Hill and Lee
    capture counts, and the frozen against live casualties.
