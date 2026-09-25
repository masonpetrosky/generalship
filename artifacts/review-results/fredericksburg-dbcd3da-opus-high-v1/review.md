# Separate review: Fredericksburg Campaign first pass (VA028)

- Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This is a fresh-context
  subagent session that used only the assignment and the repository. The author's conversation was not an input.
- Date: 2026-09-24.
- Prepared commit reviewed: `dbcd3da1efa834a36528e5cdfe74ad780349712e`. Previous commit: `7c852429dd28e8e08363e814e4aa264ecbc0263a`.
  Review-bundle commit (worktree HEAD): `9d5b254beaf2767b6ba16340983c118fee8e91d0`.
- Assignment `assignment.md` sha256 `66f455f82d0bb4aace6745d75008b31993c2acbadc483fbe8d06c2345de22199`.
  Input manifest `inputs.json` sha256 `89f84a553e374ea6c6c7f544bb0e42cd4175ab71acb76f5cafc02b5f57407d90`.
- Input hashes: I checked all 29 manifest paths in the worktree and through `git show dbcd3da:<path>`. There were **0 mismatches**.
  Relative to `dbcd3da`, the bundle commit changes only `assignment.md` and `inputs.json`.
- **Outcome: corrections required.** There are seven required findings (FR-01 to FR-07) and six non-blocking notes (FR-N1 to FR-N6).
  None of them needs new research. I checked every replacement quote offline: each occurs exactly once in the named section, on the stated OCR page.

This is an AI review, a separate analysis only. It is not human historical adjudication or independent
corroboration, and it does not admit any feature. A source-backed claim can still be historically wrong.

## Scope actually inspected

- **Guidance:** I read AGENTS.md and the evidence contract (sections on source records, claims and phases). I read the memo `docs/research/fredericksburg-first-pass-v1.md` in full.
  For README, methodology, roadmap, sources.md, `cli.py`, `tests/test_evidence.py`, the pilot report, the research queue, `quality.json` and `evidence-checks.json`, I read only the prepared-commit diffs.
  I did not reread the complete README, methodology or roadmap.
- **Dossier:** I read `data/evidence/VA028.json` in full: 10 claims, 1 null unknown (`opening-personnel-unknown`) and 31 citation occurrences, with all seven dimensions present.
  The recount matches `evidence-checks.json`.
- **Sources:** I read all 3 new `data/sources.json` records.
  - I read the retained NPS text in full.
  - I read the whole Palfrey selection: the transcription note, title/preface and all seven Chapter IV sections.
  - From the parent `palfrey-antietam-ocr-v1` (`data/raw/maryland-v1/palfrey-full.txt`) I read only the section boundaries, the ~1,100 characters before `aftermath-and-withdrawal`, and the text after `losses`.
  - I did not read the whole book. I inspected no maps, print, originals, Swinton, OR volumes or network sources.
- **Frozen rows:** I read the full VA028 rows in `cwsac_battles`, `cwsac_forces` (US 100007/100007; Confederate 72497/72497) and `cwsac_commanders` (Burnside, Major General; Lee, General), plus the VA028 entry in `battles.json`.
  VA028 is `baseline_eligible: true` with point strength bounds. Its model inputs are unchanged.
- **Derivatives:** both replay exactly.
  - NPS: HTMLParser (script/style omitted), stripped text nodes joined with newlines, the Return-to-Results → Experience-More slice, then strip and one trailing newline.
  - Palfrey: all eight half-open ranges replay with split/join whitespace collapse: 395–1716, 305988–309394, 325576–326907, 331030–334275, 345833–349105, 360323–361987, 407411–410164 and 419705–422581.
  - Page locators: all 18 Palfrey citation locators match the last preceding OCR page marker. The parent markers are p.138 @307219, p.139 @309404, p.146 @325418, p.147 @327634, p.149 @332141, p.150 @334351, p.155 @345735, p.156 @348041, p.162 @361702, p.183 @408294, p.184 @410586, p.188 @419600 and p.189 @421750.
- **Mechanical checks:**
  - Coverage: 60/127 dossiers, 67 without. Campaign groups: 14/36 complete by presence.
  - Registry: 327 records / 324 paths. The previous 324 records (321 paths) are an identical prefix, and every source hash verifies.
  - Only `data/evidence/VA028.json` changed under `data/evidence/`. The other 59 dossiers and all 15 `history/` files are byte-identical.
  - Unchanged: the cohort, both admission proposals, `admission-check.json` (promoted_rows 0), `baseline.json` (23 battles / 13 campaigns; Brier 0.2768816348133779 against 0.25), `battles.json`, the three CWSAC CSVs and the Palfrey parent OCR.
  - Packet: an in-memory `research_packet` reconstruction byte-matches `artifacts/research/VA028.md`, and its 3/3 JSON blocks parse.
  - Receipt: all 423 hashes verify (89 inputs, 327 sources, 7 outputs).
  - `make check` passed offline: 82 tests OK, `generalship check` exit 0, 60 drafts, 23 eligible.
- **Next group:** I confirmed it independently. The earliest-start incomplete group is **Goldsboro Expedition [December 1862]**: NC007, NC008 and NC009, starting 1862-12-14.

**Confirmed without correction:**

- The frozen 172,504 (US 100,007; CS 72,497) is kept as recorded.
- The live "US 0; CS 100007" field is identified as a side misassignment and is not adopted.
- Present-for-duty is not treated as engaged strength.
- Casualties 17,929 (frozen) and 17,900 (live) are kept. Palfrey's column totals 1,180 / 9,028 / 2,145 are printed, and their sum of 12,353 is correctly labelled as computed.
- Longstreet's five-day 1,894 and Jackson's 3,415 are not added together.
- The Hancock formation quote is correct.
- The result and interval are kept.
- The new dependency note omits the unsupported claim that Palfrey served in the campaign. The inspected title page supports only "formerly colonel Twentieth Massachusetts".
- Reports, Hardie, Swinton and the London Times writer are not counted as separate families.
- There is no automatic commander attribution, additive credit, score, probability or causal effect.

## Required corrections

**FR-01 (`reported-force-scope`): the dates are attached to the wrong documents, and a hedge is lost.**
Palfrey dates the 113,000 to the grand divisions' *morning reports* of December 13, as conveyed by Burnside's report; the report itself is not dated in the passage. He dates the 78,000 to Lee's *morning report* for December 10. He introduces the November 10 figure with "is said to have been".
Replace the value's third sentence with:
"Palfrey says that, according to Burnside's report, Sumner's, Franklin's and Hooker's morning reports of December 13 showed about 113,000 men present for duty, either across the river or able to cross; that Lee's morning report showed upward of 78,000 present for duty on December 10; and that the army's present for duty on November 10 'is said to have been' 127,574."
Make these citation changes (all in `palfrey-fredericksburg-selections-v1`):
- Add `positions-and-strength` p.149: "According to Burnside's report, Sumner, Franklin, and Hooker showed by their morning reports of December 13th".
- Add `positions-and-strength` p.149: "These were either across the river or able to cross it upon the receipt of orders."
- Replace the p.138 quote with "The total present for duty of the army on the 10th of November is said to have been 127,574 officers and men."

**FR-02 (`stone-wall-and-heights`): the rationale's claim about agency is unsupported, and the wall description is uncited.**
The rationale says "The works were prepared before the interval by the defending commander." Palfrey describes the stone walls as existing boundaries of the Marye estate and the road. He says earth "was piled up" without saying when or by whom. NPS gives Lee's entrenching only as undated narrative before December 11.
Replace the second rationale sentence with:
"Palfrey describes the stone walls as existing estate and road boundaries and says earth was piled against the road wall without saying when or by whom; NPS places Lee's entrenching on the heights before the December 11 crossing in narrative order only, undated."
Add these `marye-ground` p.161 quotes: "another sim- ilar wall, shoulder high, makes the eastern boundary of this road in front." and "Earth was piled up against the eastern face of this eastern wall".
In the memo, replace "The stone wall and works were prepared by the defender before the interval; no terrain effect is estimated." with:
"The stone walls were existing boundaries; who piled earth against the road wall, and when, is not stated, and NPS's entrenching is undated; no terrain effect is estimated."

**FR-03 (`pontoons-and-crossing`): the value overgeneralizes, and the phase tag covers in-interval action.**
Palfrey says a lower bridge "was laid without much opposition". Only the upper and middle bridge parties were driven off. The December 11 crossing also falls inside the frozen December 11–15 interval, so the whole claim is not an `inherited` condition.
Replace the value's second clause with:
"on December 11 Confederate sharpshooters drove away the working parties at an upper and the middle bridge, while one lower bridge was laid without much opposition; the bridges were finished after troops were sent over in pontoons."
Add these `december-11-crossing` p.146 quotes: "One of the lower bridges was laid without much opposition" and "One of the upper bridges, near the Lacy house, and the middle bridge, were about two-thirds built at six o'clock".
Change `"phase": "inherited"` to `"phase": "unresolved"`, and append to the rationale:
"The pontoon delay (to November 25) precedes the frozen interval; the contested December 11 crossing lies inside it, so the combined claim is not tagged inherited."
In the memo, replace "The pontoon delay and contested crossing are tagged `inherited` for the December 11 boundary." with:
"The pontoon delay precedes the interval; the December 11 crossing lies inside it, so the combined claim is tagged `unresolved`."

**FR-04 (`expectations-and-fog`): a conditional has become an assertion, and a counter-observation is omitted.**
Palfrey writes "If such was his expectation, he was all wrong". On p.156 he also says Franklin's dispositions, made under Burnside's directions, show Burnside "was not confident" of that expectation. On the fog, he says the artillery could not fire accurately enough *to drive away the sharpshooters*.
Replace the value with:
"Palfrey says Burnside's language makes his expectations hard to determine but that he seems to have expected Franklin's movement to strike the extreme Confederate right, and that if so he was wrong, since Confederate artillery and infantry were on Franklin's left; Palfrey also reads Franklin's en potence dispositions, made under Burnside's directions, as evidence Burnside was not confident of that. Fog on the morning of December 11 kept the Union artillery from firing accurately enough to drive away the sharpshooters."
Add these `franklin-orders` quotes: p.155 "If such was his expecta- tion, he was all wrong" and p.156 "he was not confident, when he issued them, that such an attack as Franklin was ordered to make was to be an attack upon the extreme right of the Confederates."
Replace the p.146 quote with "The morning was foggy, and the Fed- eral artillery were unable to fire with sufficient accuracy to drive away the sharpshooters."
In the memo, replace "his expectation of striking the Confederate right as mistaken" with "his apparent expectation of striking the Confederate right as mistaken if held".

**FR-05 (`stated-plan`): the move on Richmond is uncited.**
Add `plan-and-pontoons` p.138: "then make a rapid and direct movement upon Richmond."

**FR-06 (`renewed-assault-proposal`): the Swinton attribution is not in the retained text, and the details are uncited.**
The retained section begins mid-sentence at "also says that". Its subject, "Swinton", sits at parent offset 419696 (p.188), nine characters before the range start of 419705. There Palfrey writes "Swinton, who was present, says …" and then "Swinton also says …". The text does not show whether "So far was he from assenting, that he proposed…" continues Swinton's account or is Palfrey's own narration. "The wiser counsels … prevailed" reads as Palfrey's narration. The "eighteen regiments" and "in person" details are uncited.
Replace the value with:
"Palfrey, following Swinton's account, says Burnside's chief commanders urged him at the end of the day to recross the Rappahannock, and that he instead proposed to renew the attack the next day by storming the heights in person with a column of eighteen regiments of the Ninth Corps; Palfrey says the wiser counsels of Burnside's chief officers prevailed and the attack was not made."
Replace the rationale with:
"The retained selection begins mid-sentence ('also says that'); the subject 'Swinton' lies immediately before the range in the pinned parent OCR (p.188), and whether the proposal sentence continues Swinton or is Palfrey's narration is not explicit. Swinton was not separately inspected. The proposal falls on the evening of December 13, inside the frozen December 11–15 interval; `post_outcome` here means after the December 13 assaults, not after the recorded engagement. Not an estimated effect."
Add these `aftermath-and-withdrawal` p.188 quotes: "also says that the chief commanders earnestly urged him, at the end of the day, to recross the Rappahannock" and "by storming the heights with a column of eighteen regiments of the Ninth Corps, and to direct the assault in person."
A v2 selection whose range starts at 419696 would make the attribution self-contained. That is optional and would need its own versioned record.

**FR-07 (memo page spans): the stated OCR spans do not match the selection ranges.**
`plan-and-pontoons` ends at 309394, before the p.139 marker at 309404. `december-11-crossing` (325576–326907) lies entirely within p.146, whose next marker is p.147 at 327634.
In the memo, replace "OCR pp.137–139" with "OCR pp.137–138" and "pp.146–147" with "p.146".

Together these corrections add 11 citation occurrences (31 → 42). Claims (10) and unknowns (1) stay the same. The memo, README, roadmap, pilot report, `cli.py` next-action text, evidence checks, packet and receipt need regenerating with the new counts.

## Non-blocking notes

- **FR-N1 (`orders-to-franklin`):** "no disapproval reached Franklin" should follow the source's "was sent back from Burnside to Franklin". Suggested wording: "no word of disapproval was sent from Burnside to Franklin for six or seven hours".
- **FR-N2:** The live NPS heading gives "Major General Robert Lee [CS]", but the frozen commander row gives "General". The dossier doesn't record this rank conflict, which follows the same not-adopted pattern as the force field.
- **FR-N3 (`casualty-records`):** The OCR cell "Right Grand Division 491 S, 933 737" is corrupt. The printed wounded total of 9,028 is consistent only with a reading of 3,933, and the print was not checked. The frozen US 13,353 and Palfrey's computed 12,353 differ by exactly 1,000. Nothing inspected explains this, so it should stay unreconciled.
- **FR-N4 (`recorded-result`):** Palfrey's "Monday night" withdrawal is undated in the selection and may run past the frozen December 15 end date. No change is needed; the interval stays as it is.
- **FR-N5:** The crossing passage names the Twentieth Massachusetts among the units sent over in pontoons. That is not evidence of Palfrey's own presence, and the dependency note correctly does not infer it.
- **FR-N6 (`reported-force-scope`):** The rationale could also cite Palfrey's own p.149 caveat that the Federals "habitually took into action a vastly less number of men in proportion to their morning reports". It supports keeping present-for-duty separate from engaged strength. The caveat is Palfrey's own general assertion.

## Limits

This review inspected only the bounded draft extraction and the stated boundary context. It checked no returns, orders, Swinton text, maps or print pages. Explicit unknowns are accepted without further depth. The ratings of Palfrey's and NPS's reliability and dependence are unchanged. I edited no primary artifact, and I made no commit or push.
