# Stones River Campaign first pass: separate AI review

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a separate subagent with fresh context. The author's conversation was not an input, and no task ID was visible to me.
- **Date:** 2026-09-24
- **Prepared commit:** `8005b6b484045b01f3e4674b593c8f8d7180e36e`. The previous commit is `e79f33d823a7df7d1428481e53f48fdf65c2a1c5`. The assignment bundle is at `e0c20eeb69319e0df90dd659f2adbd62bdd40ad8`, which adds only `assignment.md` and `inputs.json` on top of 8005b6b.
- **Assignment:** `assignment.md` sha256 `f56006d9560e5d7c8389fbea6e7c8fcad9fe13a9aefe73e9016a8b4bb38136ce`. **Input manifest:** `inputs.json` sha256 `0d999388d0193e092b75deecb98ed72ab0088211575167b058f7b13d4685c071`.
- **Input verification:** all 33 bound paths match their manifest hashes, both in the worktree and in `git show 8005b6b:<path>`. There were no mismatches.
- **Outcome: corrections required** (R1–R5). These are citation, attribution and scope fixes. None of them changes a frozen cell, an outcome value, a phase tag, a status or an unknown.

This is an AI review. It is a separate analysis, not human historical adjudication, independent corroboration or feature admission. I used no network, opened no new sources and used no agents. I wrote only this file.

## Scope actually inspected

**Guidance.** I read AGENTS.md, the evidence contract and the Stones River memo in full, plus the head of the roadmap. For README, methodology, roadmap, sources.md, `cli.py` and the tests, I read the e79f33d→8005b6b diffs rather than the full documents.

**Dossiers.** I checked all 20 claims and 58 citation occurrences in TN008 (27) and TN010 (31), including the 2 null unknowns (both opening strengths). All seven dimensions appear in each dossier.

**Sources.**
- Both retained NPS summaries, read in full.
- The whole Cist selection: the transcription note, title/preface and all five passages.
- In the parent OCR (`data/raw/heartland-v1/cist-full.txt`), I read only the text around each range boundary and the page markers from p.82 to p.128, including the unheaded Chapter VIII opening and the map-plate block ("…STONE'S RIVER. / 105 / Battle-Map Stone's River. / 104 TEE ARMY…"). I did not read the whole book.

**Frozen rows.** All battle, force and commander rows for TN008 and TN010: 2 battle, 4 force and 4 commander rows. Every cited cell matches exactly.

**Mechanical checks** (all pass):
- `make check` ran offline and exited 0, with 82 tests OK. It reports 127 battles, 23 eligible in 13 groups, strength Brier 0.2768816348133779 against 0.25 for equal odds, 59 draft dossiers and 0 promoted rows. The working tree was clean afterwards.
- **Text derivatives.**
  - The HTMLParser transform reproduces both NPS `.txt` files exactly.
  - All six Cist half-open ranges reproduce every section under split/join whitespace collapse: 303–2076, 172082–175586, 205682–215986, 216042–218773, 251202–266678 and 269922–272260.
  - The parent OCR hash matches, and the parent entry is byte-identical across the two commits (sorted-key compact sha256 `8e9b9244…5026`).
  - The new record copies every parent metadata field. The only difference is the URL (`/details/` against `/download/…djvu.txt`), which follows the `cist-heartland-selections-v1` precedent. Its `source_kind` is `retrospective_history`.
- **Page locators.** I mapped every Cist quote to the OCR page marker before it, and all 31 Cist locators agree.
  - The pp.102–103 locator falls after the full p.101, in the unheaded Chapter VIII opening, and before the map-plate block.
  - The p.104 locator follows the "104 TEE ARMY" header.
  - Each quote occurs exactly once.
- **Registry.** 324 records / 321 paths, against 319 / 316 before. The first 319 entries are unchanged and in order. All five additions are new, and every source hash matches its file.
- **Coverage.**
  - 59/127 engagements have a dossier; 68 do not.
  - 13/36 campaign groups are complete by dossier presence.
  - All 69 earlier evidence files (57 dossiers and 12 history revisions) are byte-identical.
- **Unchanged files.** Cohort, both admission proposals, `admission-check.json`, `baseline.json`, `battles.json` and the three CWSAC CSVs.
- **Next group.** I confirmed independently that the next incomplete group is **Fredericksburg Campaign [November-December 1862]: VA028**, starting 1862-12-11. Goldsboro follows at 1862-12-14.
- **Receipt, packets and evidence checks.**
  - The receipt's 85 input, 324 source and 7 output hashes all match.
  - Each packet's three JSON blocks equal the `battles.json` record, the dossier and `sources.json`.
  - The `evidence-checks.json` rows give 10 claims and 1 unknown for each dossier.

## Verified without correction

- **Force scopes.**
  - Hartsville: about 2,000 effectives (Cist, p.82), with no Confederate count. The live zeros are not treated as absence.
  - Stones River: NPS about 44,000 against more than 37,000, the live field 45,000 (US only), and Cist 43,400 against his computed 46,604. The 46,604 arithmetic checks: 39,304 + 5,638 + 1,662. It is kept separate from "slightly inferior" (p.101). Which army was larger stays disputed, and no figure is adopted.
- **Casualties.** The differences are kept:
  - Hartsville 2,004 against 2,235, with Cist's Moore 150 plus the captured command and Morgan 125.
  - Stones River 23,515 against 23,000, with Cist's Bragg 10,125 and Rosecrans 1,553 killed, 7,245 wounded and about 2,800 captured.
  - The frozen force-row casualties sum to the frozen totals.
  - Captured troops are not used as an opening strength.
- **Picket-warning dispute.** The dispute is real: NPS says the pickets "sounded the alarm"; Cist says "No warning was given". Moore's report is correctly described as summarized by NPS, not inspected.
- **Phase tags.** The `inherited` guard mission is sound, since Thomas posted the brigade. Rosecrans's two decisions are tagged `commander_created`, and the claim notes that Cist was Rosecrans's staff historian. The remaining tags are defensible with null boundaries.
- **Attribution.**
  - Bragg's "movement as a whole was a failure" is inside his report as quoted by Cist.
  - The mirror-plans "exact counterpart" is Cist's judgment.
  - Retreat timing: Cist has Bragg's army in retreat by 11 p.m. in his January 3 narrative; NPS gives January 4–5. Both are outside the frozen interval.
  - No listed commander receives sole credit, and no credit is added across the two intervals.

## Required corrections

Every quote below appears exactly once in the named `cist-stones-river-selections-v1` section (or in the NPS text) and carries the stated OCR page marker. I checked this mechanically. Keep the existing locator wording, "p.N (OCR page markers; not checked against print)", and the existing NPS locators.

If R1–R5 are adopted as written, citations become **77**: TN008 **30**, TN010 **47**. Claims stay at 20 and unknowns at 2. Change "58" to "77" in:
- the memo, line 5, and its table (27→30, 31→47);
- README line 117;
- roadmap line 126;
- the `cli.py` report text;

then regenerate. Instead of adding a citation, the author may delete the uncited clause; the counts would then need recomputing.

### R1 — TN008 `morgan-rank-timing`: the timing at the centre of the dispute is not quoted

The value says the commission was signed "after Hartsville". The cited p.83 quote contains only the signing.

- Replace the Cist quote with `Mr. Davis, who was on a visit to Murfreesboro shortly after this engagement, signed and handed him his commission as Brigadier-General.` (hartsville, p.83).

### R2 — TN010 `breckinridge-and-retreat`: the order and the notes are uncited, and the retreat decision is misattributed

- The order and the subordinates' notes have no quote.
- Cist attributes the decision to retreat to "consultation with his generals" at noon, in his narrative of January 3. The value says instead that Bragg decided after the notes.

Replacements:
- **Value:** "Cist says Breckinridge received Bragg's orders for the January 2 attack on the crest held by Van Cleve's division, and quotes Bragg's report calling the movement a failure. He says that at 12.15 on the night of the 2d Cleburne and Withers sent a communication urging that disaster be avoided by retreat, endorsed by Polk at 12.30 a.m. January 3, and that at noon Bragg, on consultation with his generals, decided to retreat."
- **Citations** (stones-river-january-1-to-3):
  - Add p.120 `Breckinridge, reporting to Bragg, received his orders.`
  - Add p.120 `The crest of ground near the river, where Van Cleve's division was in position, was the point against which the main attack was to be directed.`
  - Keep p.123 `but the movement as a whole was a failure`
  - Replace the p.124 quote with `At noon Bragg, on consultation with his generals, decided to retreat, leaving the field in possession of his opponent.`
  - Add p.124 `after Breckinridge's failure, Cleburne and Withers had sent a communication to Bragg's`
  - Add p.125 `They expressed their fears of great dis- aster which should be avoided by retreat.`
  - Add p.125 `This was en- dorsed by Polk at 12.30 a.m., January 3d,`
  - Add p.125 `We could now per- haps get off with some safety`

### R3 — TN010 `reported-force-scope`: the NPS timing scope is missing, and the rationale overstates both sources' basis

- NPS's 44,000 is Rosecrans's strength when he left Nashville on December 26.
- NPS gives no return basis for either figure.
- The December 10 return is not in any cited quote.

Replacements:
- **Value:** "The live NPS field reads 45000 total (US 45000; CS 0;); the narrative says Rosecrans left Nashville on December 26 with about 44,000 men against Bragg's army of more than 37,000. Cist gives Rosecrans 43,400 on the battlefield and computes Bragg's effective force at 46,604 from a December 10 field return less cavalry absent on raids, calling Rosecrans's army slightly inferior."
- **Rationale:** "The sources disagree on which army was larger. NPS gives a December 26 departure figure for Rosecrans and an undated Confederate figure with no stated basis; Cist gives a battlefield figure for Rosecrans and his own adjustment of Bragg's December 10 return. None is adopted as matched opening strength. Live zero is not measured absence."
- **Citations:**
  - Replace the NPS Description quote with `Rosecrans left Nashville on December 26, with about 44,000 men, to defeat Bragg's army of more than 37,000.`
  - Add p.127 `Bragg's field return of December 10, 1862, shows an effective total of 51,036` (stones-river-results-and-numbers).
- **Memo line 52:** replace `gives about 44,000 against more than 37,000` with `gives about 44,000 when Rosecrans left Nashville on December 26 against more than 37,000`.

### R4 — TN010 `supplies-and-cavalry`: the timing is stated wrongly and 10,070 is uncited

Cist gives no date for sending for the trains. He places it with the decision to await attack after the December 31 fighting, not "after December 31".

- **Value:** "Cist says that after the December 31 fighting, having decided to await attack, Rosecrans sent for the provision trains and ordered up fresh ammunition (no separate date or clock given), and that with Morgan and Forrest absent on raids Bragg's cavalry was reduced from 10,070 on the December 10 return to 5,638."
- **Citation:** add p.127 `composed of 39,304 infantry, 10,070 cavalry, and 1,662 artillery.` (stones-river-results-and-numbers).

### R5 — Stated facts lack a supporting quote

Keep all existing citations unless a replacement is stated.

**TN008** (all in the hartsville section):
- **`reported-force-scope`.** The brigade's composition is uncited. Replace the p.82 "making a force…" quote with `consisted of three infantry regiments, a battalion of cavalry, and a section of artillery, making a force of about two thou- sand effective men.`
- **`warning-dispute`.** "Moore was surprised" is uncited. Add p.82 `Moore was surprised in his camp early in the morning.`
- **`guard-mission`.** "Watch the Lebanon road" is uncited. Replace the Cist quote with `where he had been posted by Thomas to guard the ford of the Cumberland Biver, and to watch the enemy on the Lebanon road.` (p.82).
- **`union-command-conduct`.** The p.83 quote does not name Tafel. Add p.82 `Colonel Tafel, in command of the One Hundred and Sixth Ohio, becoming separated from the`.
- **`recorded-result`.** "Ended with the whole command surrendering" is uncited. Add p.82 `the white flag was raised, and the entire com- mand surrendered.`

**TN010:**
- **`mirror-plans`.** Rosecrans's plan, Bragg's wheel and the seven o'clock hour are uncited. Add, in stones-river-ground-and-plans:
  - p.100 `press everything before them into Murfreesboro`
  - p.101 `the main attack was to be made by the forces on the left`
  - p.101 `The movement to be made by a steady wheel to the right`
  - p.101 `crans's orders were for the troops to breakfast before day- light and attack at seven o'clock.`
- **`rosecrans-holds`.** The generals' urging is uncited. Add p.119 `In the face of an earnest effort on the part of some of his general officers to persuade him to fall back to Nashville` (stones-river-january-1-to-3).
- **`recorded-result`.** "Rosecrans claimed the victory" is uncited. Add NPS Description `as the Confederates retired, he claimed the victory`.
- **`casualty-records`.** The guns lost are uncited. Add, in stones-river-results-and-numbers, p.127 `Rosecrans lost twenty-eight pieces of` and p.128 `Bragg lost three pieces of artillery.`

## Advisory (not required)

- **A1.** The frozen commander rank for Bragg is `General`; the live NPS heading reads "Major General Braxton Bragg [CS]". Neither is adopted, but TN010 does not record the conflict, unlike Morgan's in TN008. Consider an open-question note.
- **A2.** The new record copies the parent's `dependency_note` verbatim, as the assignment requires. That note says "across five records" and lists quoted officers "(Duke, Bragg, Buell)". Cist is now used across seven dossiers, and this selection quotes Bragg, Breckinridge, Polk, Cleburne and Withers. A later `metadata_only` revision could update the note; the source family and `source_kind` are unaffected.
- **A3.** In TN010 `recorded-result`, Cist writes "Bragg admitted that he had gained nothing but a victory barren of results". That is Cist's paraphrase, not a quoted Bragg document. "Cist says Bragg admitted…" would state the attribution more exactly.
- **A4.** The Chapter VIII opening follows a p.101 that is already about a full page long, so the quote cited at pp.102–103 is most likely on p.102, with the map as p.103. The OCR header "105" may be a misread. The hedged range is acceptable without a print check.
- **A5.** Cist's retreat "except his cavalry" by 11 p.m. and NPS's "Bragg left the field on the January 4-5" need not contradict each other. Keeping them as "differs", not adjudicated, is appropriate.

## Unresolved and out of scope

These remain open by design and need no further research: both opening strengths, the picket warning, Morgan's commission date, casualty reconciliation, and original orders, returns and reports. Neither the author nor I inspected any original, map or print page. Other pending campaign reviews, such as Iuka and Corinth, are out of scope.
