# Overland Campaign first pass: separate review (v1)

**Outcome: corrections required.** Required findings: OVR-R1 to OVR-R12. Advisories: OVR-A1 to OVR-A12.

This is an AI review, which is a separate analysis. It is not human historical adjudication, proof that sources are independent, or feature admission. It proposes corrections; the primary agent checks each one against the sources before changing any evidence.

## Reviewer record

| Field | Value |
| --- | --- |
| Reviewer | Fresh-context `evidence-reviewer` subagent. No task ID was exposed to the reviewer. |
| Model / effort | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high` |
| Date | 2026-09-25 |
| Prepared commit reviewed | `ec3f5843b73987db72ef9d23815ec3622063108f` (against `d41c3ce`) |
| Worktree / bundle commit | `1e791f7b8e9da05b030e355815ac0b68c43adf92`. Its only change from `ec3f584` is the two bundle files. |
| `assignment.md` | sha256 `b53a5bb0ca91f0eca56302d9a41a5e5a708e08744c5fefc05fbbbe603a2aed93` (verified) |
| `inputs.json` | sha256 `c9fc47bad7bf0d27f96b31ec05f95fd4ce8af3d186404614a778dbcdc5e1dea9` (verified) |
| Input hashes | All 68 paths match `git show ec3f584:<path>`, and the worktree copies match too. No mismatch. |
| `make check` (offline) | Exit 0. 134 unit tests OK. `python3 -m generalship check` passes with `draft_dossiers: 138`. No build, packet or network command was run. |

## Scope actually inspected

**Documents**
- AGENTS.md.
- `docs/methodology.md`: only the "Research depth and coverage" section.
- `docs/evidence-contract.md` and `docs/cohort-v2.md`, in full.
- The memo `docs/research/overland-first-pass-v1.md`, in full.
- The `ec3f584` diffs of `docs/sources.md` and `tests/test_evidence.py`.

**Frozen data and NPS pages**
- The frozen CWSAC battle, force and commander rows for all eleven records.
- All eleven NPS text snapshots, read in full. The HTML parents were not opened; their hashes pass in `make check`.

**Dossiers**
- All eleven dossiers: 100 claims and 453 citation occurrences.
- For every text citation, the quote was located in its section and read with about 300–350 characters of context on each side.
- Wider context was read where support was doubtful: Humphreys pp.53, 56, 58 (footnote), 114–116, 191–192, and the Warren passage on p.23.
- A heuristic check compared each of the 162 Humphreys page locators with the OCR running heads. The only one flagged is p.111, where the head reads "Ill", which the memo already notes.
- The record counts, dispute counts, phase counts and families per record were recomputed. All match the memo.

**Selections**
- Read in full: the Butler, Wild and Hampton selections.
- Read only around cited passages, plus targeted searches: the Meade, Sheridan and Humphreys selections.
- Full OCR parents: targeted searches only (Sheridan's "During ffie 8th…" and "half rations"). They were not read in full.

**Source registry**
- All 34 new records were inspected.
- Fields were read in full for the Humphreys (3), OR (4) and report-selection (5) records, and for the NPS records of VA046 (both) and VA056 (text).
- For the remaining 19 NPS records, only the group, kind, URL and inspection fields were read.
- The pre-existing Humphreys group records at `d41c3ce` were compared.
- Registry counts were verified: 643 entries and 622 paths, previously 609/588.

**Not inspected:** any source outside the bound, the unselected parts of the OCR parents, and Humphreys' unselected chapters.

## Required corrections

The first eleven findings are extraction or attribution errors. None of them needs new research. All proposed quotes were verified to occur exactly once in the named section.

**OVR-R1 — VA046 `contact-reports`: misattributed time.** "a quarter past seven" is when Meade *received* Warren's despatch, not when Warren sent it.
- `value` → "Humphreys says Wilson reported at 5 a.m. that his pickets had reported nothing new from the enemy; that at a quarter past seven Meade, on his way to Warren's headquarters, received a despatch from Warren that the enemy's infantry was on the pike in some force about two miles from Wilderness Tavern; and that Wilson's parties had indicated the Confederate corps were no further advanced than in November. Meade says information was received that the enemy had appeared on the Orange pike."
- Add a citation to `humphreys-overland-selections-v1`, section `wilderness-opening`, locator p.23: "At a quarter past seven General Meade, while on his way to General Warren’s headquarters near the Old Wilderness tavern, received a despatch from that officer".

**OVR-R2 — VA046 `command-roles`: unsupported "on learning of Ewell's approach".** Humphreys says the attack "would soon develop what part of Lee’s army was there". In other words, headquarters did not yet know it was Ewell.
- In `value`, replace "Humphreys says Meade, on learning of Ewell's approach, directed Warren to halt and attack with his whole force" with "Humphreys says Meade, on receiving Warren's report of enemy infantry on the pike, at once directed Warren to halt and attack with his whole force, which would show what part of Lee's army was there".
- Add a citation to the same source, section `wilderness-opening`, locator p.23: "This would soon develop what part of Lee’s army was there."

**OVR-R3 — VA048 `command-roles`, and the memo's command bullet: Humphreys' Warren passage is misread as criticism.** The passage is a p.58 footnote.
- It places the obstruction at about eleven o'clock during the night march that began on the evening of May 7, not on May 8.
- It names the cause as the Provost-Marshal-General's mounted troops occupying the road.
- It calls Warren's staying at the Lacy house "the most important part of his duty". The "had he been at the head" sentence is a counterfactual about how quickly the obstruction would have been reported.

Proposed changes:
- In `value`, replace "and that Warren's absence from the head of his column contributed to the May 8 delay" with "and, in a footnote, that at about eleven o'clock on the night march begun the evening of May 7 the head of Warren's column was halted and seriously delayed by the Provost-Marshal-General's mounted troops occupying the road, while Warren stayed near the Lacy house overseeing the withdrawal, 'the most important part of his duty'; had he been at the head of the column, Humphreys adds, he would have reported the obstruction at once".
- Keep the existing p.58 citation and add three more, all in section `spotsylvania-opening`, locator p.58:
  - "While at General Hancock’s headquarters it was learnt, about eleven o’clock, that the head of Warren’s column was near by,"
  - "halted and seriously de¬ layed by the mounted troops of the Provost-Marshal-Genera],"
  - "General War¬ ren had remained in the vicinity of the Lacy house to oversee the withdrawal of his troops, the most important part of his duty."
- `rationale` → "Direction is attributed as the sources state; Humphreys treats Warren's location as a duty and the mounted troops as the obstruction, not Warren as at fault. The live rank for Lee is not adopted. No listed commander receives automatic sole credit."
- In the memo's "Command roles and ranks" bullet, replace "Warren's absence on May 8" with "Humphreys' note that Warren, overseeing the withdrawal, was not at the head of his column when it was obstructed on the night of May 7–8 (Humphreys calls this his most important duty)". "Criticisms" then covers only the Smith order and Sheridan's objection.

**OVR-R4 — VA048 `casualty-records`: the cavalry exclusion is unsupported, which matters for double counting.** The selected passage (pp.115–117) says nothing about the Cavalry Corps. Yellow Tavern (VA052) falls inside this interval.
- `rationale`: replace "Humphreys' Union totals end on May 19–20 and exclude the cavalry; his Confederate figure is an inference." with "Humphreys' Army of the Potomac totals run from the morning of May 8 to the night of May 19; the selected passage does not say whether the Cavalry Corps' raid losses (VA052, inside this interval) are included, so the two records must not be added. His Confederate figure is an inference."
- Add a citation to section `spotsylvania-close`, locator p.116: "from the morning of the 8th to the night of the 19th,".

**OVR-R5 — VA052 `forage-and-rations`: "half-rations for one day" refers to forage.** Two passages show this:
- The 1866 report says "when out of forage, of which we had half rations for one day".
- The garbled May 13 line ("all hand with the command was half-rations tor one day") is Sheridan's forage statement.

As written, the value reads as food rations. Proposed changes:
- In `value`, replace "Sheridan says the command had half-rations for one day when it set out, that only three days' rations were taken" with "Sheridan's May 13 dispatch says what was on hand was half-rations for one day (garbled in OCR), and his 1866 report says this was forage — he was to go to the James 'when out of forage, of which we had half rations for one day'; his May 14 dispatch says only three days' rations were taken".
- Add a citation to `or36-1-sheridan-overland-selections-v1`, section `sheridan-1866-05-13-richmond-raid`, locator p.789: "and when out of forage, of which we had half rations for one day,".

**OVR-R6 — VA052 `recorded-result`: the rationale uses outside knowledge.** No inspected passage places Gordon's wound at Meadow Bridge or on the next day. Humphreys reports him killed in the Yellow Tavern paragraph.
- `rationale`: replace "Gordon's wounding at Meadow Bridge the next day is outside this record." with "Humphreys reports Gordon killed in his Yellow Tavern paragraph; no inspected passage gives the place or date of Gordon's wound, and this record neither adopts nor corrects that placement."

**OVR-R7 — VA056 `reported-force-scope`: "three guns" is misattributed, and a composition conflict is missing.**
- "Having three guns" is Wild's own opening description, not what the prisoners said.
- Butler's first telegram says Fitzhugh Lee attacked "with cavalry, in[f]antry, and art[i]llery". Wild says the attackers were "supposed to be cavalry".

Proposed changes:
- `value`: replace from "Butler says the post" to the end with: "Butler says Fitzhugh Lee attacked with cavalry, infantry and artillery, that the post was garrisoned by two regiments of Black troops, and that Wild commanded 1,800 men. Wild says the attackers were supposed to be cavalry with three guns, probably horse artillery; that he had no accurate count of them (his estimate is garbled in OCR: 'and probably triple'); and that prisoners stated they were detachments from three cavalry brigades."
- Add citations, all locator p.269 or p.270 as shown:
  - `or36-2-butler-wilsons-wharf-selections-v1`, section `butler-1864-05-25`, p.269: "with cavalry, in- atry, and artdlery^ an attack upon my post at Wilson’s Wharf".
  - `or36-2-wild-wilsons-wharf-selections-v1`, section `wild-1864-05-25`, p.270: "sTPPose(^! be cavalry, having three guns, probably horse artillery,". This may replace the shorter existing quote.
- Append to `rationale`: "Butler, who was not present, reports infantry; Wild supposed a cavalry force. The composition is not resolved."

**OVR-R8 — VA056 `summons-and-reports`: an unmarked timing conflict.**
- Butler: "Before the attack Lee sent a flag".
- Wild: "After fighting an hour and a half, they sent to! a flag of truce".

Proposed changes:
- `status` → `disputed`.
- `value` → "Wild says that after fighting an hour and a half the attackers sent a flag of truce with a summons in Fitzhugh Lee's name, which he declined, and that contrabands later said the attackers went to Bottom's Bridge. Butler's telegram says Lee sent the flag, claiming force enough to take the place, before the attack. The reports differ on when the summons came."
- Add a citation to section `wild-1864-05-25`, locator p.270: "After fighting an hour and a half, they sent to! a flag of truce,".
- Append to `rationale`: "Butler relays a sequence that conflicts with Wild's; neither is adopted."

**OVR-R9 — VA056 `recorded-result`: a Butler statement has no citation.** "Butler says the attack was repulsed" is supported only by the CWSAC description.
- Add citations to `or36-2-butler-wilsons-wharf-selections-v1`, section `butler-1864-05-25`, locator p.269: "lian^s°mely repulsed." and "having completely failed;".

**OVR-R10 — VA056 `casualty-records`: "about 20 dead" is not what Butler says.** Butler gives "He lost 20 ea" (the noun is garbled), with no "about". The 20 also has no citation.
- In `value`, replace "and says the enemy left about 20 dead and 19 prisoners" with "and says the enemy lost 20 (the noun is garbled in OCR), whom he left on the ground in Union hands, and that 19 prisoners were taken".
- Add a citation to section `butler-1864-05-25`, locator p.269: "He lost 20 ea, whom he left on the ground in our hands."

**OVR-R11 — VA099 `hunter-and-rear-reports`: two accounts are merged into one sequence that neither source states.**
- The June 16 dispatch says that "up to this time" there was no definite information about Hunter, and that report placed him at Staunton.
- The 1866 report says prisoners taken on the 11th placed him at or near Lexington.

Proposed changes:
- `status` → `disputed`.
- In `value`, replace the first sentence with "Sheridan's June 16 dispatch says that up to that time he could get no definite information of Hunter's position and that report placed him at Staunton; his 1866 report says prisoners taken on the 11th told him Hunter was at or near Lexington instead of coming toward Charlottesville. The dispatch also says prisoners and citizens reported Pickett's division coming."
- Add citations:
  - `or36-1-sheridan-overland-selections-v1`, section `sheridan-1864-06-16`, p.785: "Report placed him and his command at Staunton, destroying the railroad."
  - Section `sheridan-1866-05-13-trevilian-and-saint-marys`, p.796: "troin prisoners, of which we had captured about 500, I learned that Hun- ter,".
- Append to `rationale`: "The contemporary dispatch and the 1866 report differ on what Sheridan knew of Hunter and when."

**OVR-R12 — Memo "Validation" section: stale and contradicted by the commit.** The memo says one test is an expected failure and that "this pass did not edit shared tests". In fact, `ec3f584` edits `tests/test_evidence.py`, and all 134 tests pass.
- Replace the two validation bullets with: "`make check` passes offline: 134 unit tests OK and `python3 -m generalship check` passes with 138 draft dossiers. This commit edits `tests/test_evidence.py` so that `test_repository_dossiers_have_resolvable_passages` requires every frozen v1 dossier and admits further dossiers only inside the cohort v2 frame."

## Advisories (optional)

- **OVR-A1 — VA048 `salient-and-intrenchments`.** "Much the greater part of this intrenchment was concealed by wood" refers to Lee's intrenchments generally. For the salient itself, Humphreys says "The eastern half or more of the salient was covered by wood ;" (p.75). Consider citing that and rewording "mostly concealed by wood".
- **OVR-A2 — VA048 `casualty-records`.** Humphreys objects that Badeau's *wounded* figure is too small, not that the 13,601 total is. Suggested wording: "he says Badeau's wounded are too few".
- **OVR-A3 — VA055 `reported-force-scope`.** Badeau's 9,162 comes from Pickett's return of November 27, 1863. State the date, and consider citing "Badeau states that Pickett’s Division Return for November 27, 1863," (p.124).
- **OVR-A4 — VA062 `reported-force-scope` and `casualty-records`:**
  - Attribute Hoke's "a little less than 6,000" to Taylor, as Humphreys does.
  - "nominal" is not in the source.
  - The 14,129 is McParlin's estimate: 11,729 "may be estimated … excluding the Eighteenth Corps" plus an estimated 2,400. It runs from the Pamunkey crossing, so it also covers the VA057–VA059 intervals. Say so in the rationale.
- **OVR-A5 — VA052 and VA099: Sheridan's "superior in numbers".** Sheridan says he was "led to believe, on information", and he means the whole period of the report. Hampton's "disparity in numbers" sits in a report covering June 8–24. Scope both statements accordingly.
- **OVR-A6 — VA052 `fight-the-cavalry`.** "on the 8th" is not in the cited selection; the section starts just after "During ffie 8th". Either drop the date or cite the full-OCR parent.
- **OVR-A7 — VA052 `casualty-records`.** The May 25 dispatch also gives 46 killed ("1 ot a 1 killed, 46."), next to the 379 wounded. Consider adding it.
- **OVR-A8 — VA058 `recorded-result`.** Sheridan's report, though garbled, also says the enemy was driven back leaving his dead. Record it with the "hard contested" quote.
- **OVR-A9 — VA059 `recorded-result`.** The dispatch says "drove them down to Cold Harbor", not "toward".
- **OVR-A10 — VA046:**
  - `intrenched-lines-may-7` also covers May 5. The May 5 intrenching is relayed from Griffin ("General Griffin stated…").
  - In `trains-and-crossing`, "halting places were fixed" paraphrases the judgment "to let the troops remain for the night where they had halted".
- **OVR-A11 — VA062 `recorded-result` and the memo.** Meade's "about 11 a.m. offensive operations closed" and Humphreys' "at half-past one … suspended" may describe different events: the end of the assaults, and the suspension order. Keep both, but describe the conflict as possibly one of reference rather than a flat contradiction. Relatedly, in VA099 `ammunition-forage-and-wounded`, "exhaust" overstates "reduced … to a very small compass".
- **OVR-A12 — Registry and families:**
  - The Humphreys selection ranges `north-anna` (…323465) and `cavalry-corps-yellow-tavern` (322286…) overlap by 1,179 characters, so some text appears in both sections. The inspection note should say so.
  - In VA056, the agreement between the CWSAC description and Butler on 1,800 should be labeled non-corroborating. The basis of the CWSAC figure is unestablished and may be the OR telegram.
  - The rationale's "works predate the attack" is not passage-backed.

## Answers to the assignment's questions

**1. Support.** OVR-R1 to R11 are the claims whose values say more than, or something other than, their quotes support. All other claims checked are supported in context, including:
- every figure, with its date, basis and scope;
- the Humphreys killed figure in VA057, where "1 400" is a footnote marker plus 400. This was checked arithmetically against his totals of 10,433 and 12,970.

**2. Completeness within the bound.** The following were missed within the selected passages: Butler's composition statement and the summons-timing conflict (R7, R8), Sheridan's 46 killed (A7), and the "driven back" in the Haw's Shop report (A8).

Every frozen and live value that can matter to a claim is accounted for: forces, casualties, results, commanders and ranks, and the VA056 description. Unused name-only values, such as the frozen other name "Nance's Shop" for VA066, are immaterial.

**3. Rules.**
- No strength is adopted; each of the eleven opening strengths is null.
- Disputes are marked, except R8 and R11.
- `inherited` is used only for the Wilderness forest and the Totopotomoy swamps, which is appropriate.
- Every outcome claim is `post_outcome`.
- No commander receives automatic credit.
- Overlapping records are named and period totals are not assigned, except for the unsupported cavalry exclusion in R4.
- Each record uses exactly three independence groups, and the groupings are correct.

**4. Sources.**
- The registry records are accurate against what I inspected: the edition and 1891 imprints, `document_dates_by_section`, dependency notes, and inspection notes that match the memo.
- **Reusing the Humphreys Bristoe group is sound.** It is the same author, which is the conservative choice, and the mismatch with the group name is documented. The earlier records are left unchanged.
- **Counting Butler's telegrams as a family at Wilson's Wharf is sound for the effort ceiling only.** They are a distinct document by a different author, and they diverge from Wild (1 vs 2 killed, the summons timing, composition). They are relays, however, and the registry correctly marks them as dependent on Wild's and Hinks's reports. The memo's "Families: 3" for VA056 should not be read as three independent witnesses.
- Humphreys, Meade and Sheridan likewise share headquarters papers, as the dependency notes state.

## Unresolved (not adjudicated here)

These remain source disputes. They are not extraction errors:
- the Wilson's Wharf attacking force and its composition;
- Butler's and Wild's Union killed;
- the salient prisoner counts;
- the Bethesda Church and Haw's Shop outcomes;
- relative numbers at Trevilian and at Saint Mary's Church;
- the gaps between frozen and live casualty figures.

The primary agent should check each required correction against the sources before editing. This review changes no model input.
