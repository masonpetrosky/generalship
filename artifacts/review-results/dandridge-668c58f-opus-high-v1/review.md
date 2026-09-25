# Operations about Dandridge: separate source review (Opus `high`, v1)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a fresh-context subagent working offline. I did no new research and opened no extra source families.
- **Date:** 2026-09-25.
- **Commits checked:**
  - prepared `668c58f76fb16476172db6e6200e44209418c619`;
  - previous `34dc4bea2b45ab3227a76b0f0ac437508aa76e27`;
  - bundle/worktree HEAD `46c40a693fcaea4e161acc7a2d497a6f37470384`.
- **Assignment and input manifest:**
  - `assignment.md` sha256 `7e1bba5ace9bccb9b827cfaffecac0c61e97ee692cdd55173207e0608087302e` (matches);
  - `inputs.json` sha256 `d99c1a09643d76365f4742c7887099613f64c882e9699de11891c0d4d92596be` (matches).
- **Input hashes:** I checked all 42 bound paths against `git show 668c58f:<path>`. All 42 match, and every worktree copy is byte-identical to the prepared commit. There were no mismatches.
- **Outcome: corrections required.**
  - Required: DAN-R1 to DAN-R7.
  - Advisory: DAN-A1 to DAN-A5.

This is an AI review and a separate analysis. It is not human historical adjudication, independent corroboration or feature admission.

## Scope actually inspected

- **Dossiers.** I read all 27 claims and all 141 citation occurrences in TN027, TN028 and TN029 (53, 41 and 47 citations).
  - This includes the 3 null unknowns, which have no citations.
  - Each record covers all seven dimensions.
  - I also read the boundary notes and open questions, the memo, and the README, roadmap, methodology, sources and report diffs.
  - I skimmed the evidence contract in full.
- **Frozen rows.** I checked all 7 frozen battle, force and commander rows for TN027–TN029. Every cited CSV cell matches exactly, including:
  - the TN027 CS force of 2000/2000 with the "Sturgis reported…" text;
  - the blank US strength bounds;
  - the frozen casualty texts;
  - the frozen ranks, including McCook, Colonel, as TN029's third commander.
- **NPS pages.** I read all three NPS text pages in full. Replaying the recorded HTMLParser transform on each retained HTML file reproduces its text byte-for-byte (3/3).
- **OR selections.** I read all four selections in full.
  - Replaying every recorded character range with whitespace collapse against its parent reproduces every section (11/11 including titles).
  - The parents are `or31-1-illinois-ocr-v1`, which is unchanged since `34dc4be` (sha `646c2e92…`), and the new `or32-1-illinois-ocr-v1` (sha `a7f7ea09…`).
  - I also read the parent text immediately around every range boundary.
- **Page markers.** I built explicit marker maps and recomputed the page at both the start and end of every sectioned quote. All 141 locators agree, and there are 0 mismatches.
  - Sturgis OR XXXI: p.646 start, then 647, 648 and "049" (=649), with 650 for the Jan 1 letter.
  - Martin: 545–549.
  - Sturgis OR XXXII: 79, 80 and 81; then 131, 132, 133/134, 135, 136, 137 and 138.
  - Longstreet: 93 and 94; then 149 and 150.
  - I confirmed each section's starting page from the parent's preceding running head.
  - The only other numeric tokens in the sections are "83", a casualty total, and "*See p. 133", a sketch reference. Neither is a missed header.
  - The six p.649 locators correctly disclose the inferred reading of "049".
- **Registry.** It has 580 entries and 560 paths (previously 568/548). All 568 earlier entries are identical, and there are 12 new IDs.
- **Coverage.**
  - I independently computed 127/127 cohort dossiers with 0 missing and no extras. All 36/36 frozen campaign groups are complete by presence, so no group lacks a dossier.
  - All 221 evidence files at `34dc4be` are byte-identical at `668c58f`. That is 124 dossiers plus 97 historical revisions.
  - The following have no diff: cohort, both admission proposals, `admission-check.json`, `baseline.json`, `battles.json` and the three frozen CSVs.
  - There are 0 promoted rows. The baseline is 23 battles in 13 groups, with Brier 0.2768816348133779 against 0.25.
- **Mechanical checks.**
  - All receipt hashes verify: 238 inputs, 580 sources and 7 outputs.
  - Each packet `TN027–TN029.md` has three JSON blocks. The draft block equals its dossier, and the registry block equals `data/sources.json`.
  - `make check` passed offline with 82 tests OK and `generalship check` OK, leaving the tree clean.
  - I did not run build or packet commands.
- **Not inspected:** print pages, maps, subordinate reports, returns, or the rest of either volume.

Checks that passed:

- **Scope.** The out-of-scope actions (Dec 24/27, Jan 14/16, Jan 26 and Jan 28) are context only.
- **Phase tags.** All claims are `unresolved` or `post_outcome`, with nothing tagged `inherited`.
- **Source families and dates.** The family grouping and section dates are correct.
- **OCR readings.** "LOO" is reported and 100 is labeled as a computation (18+77+5). The 96 total (7+66+18+5) is kept separately.
- **Disputes and figures kept visible:**
  - the Mossy Creek withdrawal dispute;
  - 44 against about 50 prisoners;
  - Sturgis's cavalry-only 83;
  - the Fair Garden gun and prisoner descriptions;
  - the live ranks, which are not adopted;
  - interested-source labels.
- **Command credit.** No commander receives automatic or additive credit.
- **Relay attribution.** The Dec 29 dispatches are correctly Sturgis's. The Strawberry Plains relay heading and Parke's "P. S. — All right" are described accurately in the source metadata and are not cited as Sturgis's words.

## Required corrections

**DAN-R1 — TN027 `casualty-records`: Sturgis's loss estimate is misattributed.**

- **Problem.** The value says "He estimates Confederate losses at 250 to 400". The p.649 passage attributes the figures to others: "General Elliott reckons it at 400 killed and wounded ; others at from 250 to 300". Sturgis's own figure is in the Jan 1 letter: "was between 300 and 400".
- **Replace this sentence:** "He estimates Confederate losses at 250 to 400, says 44 prisoners were taken and 22 dead buried, while his evening dispatch says about 50 prisoners."
- **With:** "For Confederate losses his January 8 report gives General Elliott's reckoning of 400 killed and wounded and others' 250 to 300; his January 1 letter puts the enemy loss between 300 and 400. His report says 44 prisoners were taken and 22 dead buried, while his evening dispatch says about 50 prisoners."
- **Citations:** unchanged.

**DAN-R2 — TN028 `forage-clothing-and-shoes` and the memo: Longstreet's pursuit reasons are misstated.**

- **Problem.** Longstreet gives shoes only as the reason his *infantry* could not pursue. Clothing and unshod horses describe the cavalry, which he says "was sent forward, however" to distress the enemy.
- **Replace in the value:** "Longstreet says his infantry could not pursue, half the men being without shoes, that nearly half the cavalry horses were unshod, and that his workmen could make only one hundred pairs of shoes a day. NPS adds lack of cannons and ammunition as reasons the Confederates could not pursue; the inspected Longstreet passages name shoes and clothing."
- **With:** "Longstreet says his infantry was not in condition to pursue, half the men being without shoes; that his cavalry was almost as badly off for clothing, with nearly half its horses unshod, but was sent forward to distress the enemy; and that his workmen could make only one hundred pairs of shoes a day. NPS says the Confederates were unable to pursue for lack of cannons, ammunition and shoes; the inspected Longstreet passage gives shoes as the infantry's reason and reports that the cavalry was sent forward."
- **Add two citations.** Both use `or32-1-longstreet-dandridge-selections-v1`, section `longstreet-1864-01-19-dandridge`, locator "p.94 (OCR page markers; not checked against print)". Both quotes were verified present and unique.
  - "Our cavalry is almost as badly off for want of clothing,"
  - "It was sent forward, however, with orders to make the effort to distress the enemy,"
- **Memo bullet.** Replace "Dandridge's pursuit: NPS names cannons, ammunition and shoes; the inspected Longstreet passages name shoes and clothing." with "Dandridge's pursuit: NPS says the Confederates could not pursue for lack of cannons, ammunition and shoes; Longstreet gives shoes as the reason his infantry could not pursue and says his cavalry, short of clothing and horseshoes, was sent forward to distress the enemy."

**DAN-R3 — TN027 `reported-force-scope` and the memo: attribution of the frozen force text.**

- **Problem.** The frozen text reads "(Sturgis reported that the Confederate cavalry was supported by a brigade of infantry; approx. 2,000 men)". Because of the semicolon, it does not say whether the 2,000 is part of Sturgis's report. The rationale's "Each commander assigns the larger number to the other side" is also not entailed, because Sturgis gives no own-force count in the inspected passages.
- **Value, first sentence.** Replace it with: "The frozen Confederate force text attributes to Sturgis a report that the Confederate cavalry was supported by a brigade of infantry, followed after a semicolon by \"approx. 2,000 men\"; it does not state whether that figure belongs to the attributed report. The live field reads zero."
- **Rationale.** Replace it with: "Martin gives the force opposing him as larger than his own; the inspected Sturgis passages give no count of his own force and contain neither a brigade of infantry nor a 2,000 figure. Martin's own-force 2,000 equals the frozen figure, but no derivation is established. None is adopted. The live zero is not measured absence."
- **Memo.** Replace "The frozen force text attributes to Sturgis a brigade of infantry and about 2,000 men." with "The frozen force text attributes to Sturgis a supporting brigade of infantry; its following \"approx. 2,000 men\" is not clearly part of that attribution."

**DAN-R4 — Longstreet selection metadata and the memo: Lawton's indorsement is not in the snapshot.**

- **Problem.** The range for `longstreet-1864-01-19-dandridge` ends at 326298, immediately before "[Indorsement.] Quartermaster-General's Office, Richmond, January 29, 1864 … A. R. LAWTON" (p.94). The record nevertheless says `author` "James Longstreet; indorsement by A. R. Lawton…" and `dependency_note` "…with a printed indorsement…". The memo also lists the selection as the "report with Lawton's indorsement (pp.93–94)".
- **Registry fix.** Following the contract, add a `metadata_only` revision `or32-1-longstreet-dandridge-selections-v2`. It supersedes v1 and keeps the same path, hash and ranges. Set these fields:
  - `author`: "James Longstreet; volume title supplied by compiler"
  - `dependency_note`: "Report and telegrams of the Confederate department commander; interested accounts. A. R. Lawton's January 29, 1864 Quartermaster-General's indorsement follows the report in the parent (p.94) and is not in this selection. Shared OR container with the other Volume XXXII Part 1 selections; later NPS dependence is unestablished."
  - `inspection`: "Title, Longstreet's January 19 Dandridge report, Lawton's following indorsement (read, not selected), and his January 29 and February 1 telegrams (the section carries no single date) read in full."
- **Memo.** Replace "January 19 report with Lawton's indorsement (pp.93–94)" with "January 19 report (pp.93–94; Lawton's indorsement on p.94 read but not selected)".
- **Counts and citations.** Update the counts to 581 entries / 560 paths. Existing citations can keep resolving to v1, or be repointed to v2 at the primary's choice.

**DAN-R5 — TN029 `forage-and-exhaustion`: pursuit wording and parched-corn scope.**

- **Problem.** The source says Wolford and Garrard "arrived at Fair Garden too late to take part in the pursuit, their commands being completely exhausted". It does not say they were too exhausted to join. The parched-corn statement covers "nearly two months", not this action.
- **Replace:** "that his troops were worn down with continuous fighting and little to eat and lived mainly on parched corn, and that Wolford's and Garrard's divisions arrived too exhausted to join the pursuit."
- **With:** "that his troops were very much worn down with continuous fighting and little to eat, that for nearly two months his command had been compelled to live mainly on parched corn, and that Wolford's and Garrard's divisions arrived at Fair Garden too late to take part in the pursuit, their commands completely exhausted."
- **Add one citation:** `or32-1-sturgis-dandridge-fair-garden-selections-v1`, section `sturgis-1864-02-04-fair-garden`, locator "p.138 (OCR page markers; not checked against print)", quote "for nearly two months my command has been almost daily engaged with the enemy".

**DAN-R6 — Memo: Parke's role in the withdrawal is broader than the cited evidence.**

- **Problem.** The selected passage supports only "was ordered by Major-General Parke to retire the cavalry". The infantry and trains were "already moving" when Sturgis returned. The dossier's scope is correct.
- **Replace:** "Parke, not a listed commander, ordered the Dandridge withdrawal."
- **With:** "Sturgis reports that Parke, not a listed commander, ordered him to retire the cavalry; the selected passages do not cite the order for the infantry's withdrawal (Parke's January 18 report was read but not selected)."

**DAN-R7 — TN028 `casualty-records` and the memo: whose losses Longstreet's 150 describes.**

- **Problem.** The sentence reads "I have no report yet of the casualties of the two days' skirmishing, but do not think that they can exceed 150". It names no side. Reading it as his own losses is reasonable, but it is an interpretation. The basis of the frozen US 150 is also not established, so the text should not assert what that figure is.
- **Value.** Replace "thought his own losses in the two days' skirmishing could not exceed 150, possibly not half of that" with "thought the casualties of the two days' skirmishing — read here as his own, since he awaited the report; the sentence names no side — could not exceed 150, possibly not half of that".
- **Rationale.** Replace "Longstreet's 150 is his upper estimate of Confederate losses and is not the frozen Union figure;" with "Longstreet's 150 is read as an upper estimate of his own losses and must not be adopted as or equated with the frozen Union 150, whose basis is not established;".
- **Memo.** Replace "Longstreet's own-loss estimate of at most 150 is not the frozen Union 150." with "Longstreet's estimate that the two days' casualties could not exceed 150 (read as his own; no side is named) must not be equated with the frozen Union 150, whose basis is not established."

**Count changes.** Applying R2 and R5 changes the citation counts to **144** (TN028 43, TN029 48). The claim and unknown counts are unchanged. Update the memo, README, roadmap, report text and `cli.py` accordingly, then regenerate.

## Advisory (not required)

- **DAN-A1 — TN027 `divided-force-and-recall`.** "because the whole Confederate force had moved" adds a causal link. The dispatch only places the two sentences side by side. Suggested wording: "…found no enemy at Dandridge, and that the whole Confederate force had moved to his front in the night."
- **DAN-A2 — TN029 open question.** There is a typo: "are is a separate family" should read "are a separate family".
- **DAN-A3 — Memo loss bullet.** "the frozen US 151 against live CS 0" should read "the frozen CS unknown against live CS 0 (both give US 151)".
- **DAN-A4 — Selection boundaries worth noting:**
  - The OR footnote to "LOO.*" ("But see revised statement, p. 651") falls just outside the Sturgis Jan 8 range. The dossier could mention the footnote.
  - Sturgis's own 6 p.m. Jan 27 postscript ("but I am pushing them up now, tired as they are, with the hope of making this rout complete.", p.134, already in the selection) sits in tension with his report's "too late to take part in the pursuit". It could be preserved as an intra-source difference.
- **DAN-A5 — TN029 Sturgis figures.**
  - "About 150" and "over 100" prisoners are compatible numbers, and the two gun descriptions may describe the same two pieces. The current wording "differ" is acceptable, but they should not be counted as separate captures.
  - In `concentration-and-flank-move`, the Morgan/Armstrong identification refers to the 26th.

## Remaining limits

I did not inspect print pages, maps, subordinate reports or returns. The OCR page markers have not been checked against print. The Sturgis and Martin accounts are interested and remain unreconciled. The opening strengths remain unknown in all three records. Draft status is unchanged, and no features are admitted.
