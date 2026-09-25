# East Tennessee Campaign separate review (TN019, TN020)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`) subagent, reasoning effort `high`. The reviewer started with fresh context and read only the assignment and the repository.
- **Date:** 2026-09-25.
- **Commits:**
  - Review bundle: `396bd1f6d9243fee5d568cc37c014608fd28a355` (the worktree HEAD; clean before and after `make check`).
  - Prepared: `49312d9441d898e75b516d4efdcff50d5cab5b58`.
  - Previous: `5948133d5ea4010e0f644b5aa32749241c14f075`.
- **Assignment hashes:** `assignment.md` sha256 `915105687e4197a4655dab62e30a1c183133590991222b126946faea1ec29885`. `inputs.json` sha256 `cafc6ddba6b7e8ff32ae0de6ced21e9ee26ed245ea6bdacb54607922b9246bf2`.
- **Input verification:** All 36 bound paths match their recorded hashes at the prepared commit and in the worktree. There are no mismatches.
- **Status:** This is an AI review, a separate analysis. It is not human historical adjudication, not independent corroboration, and not feature admission.

**Outcome: corrections required.** The required findings are ET-R1 to ET-R4, all in TN020. The non-blocking notes are ET-N1 to ET-N4.

## Scope actually inspected

- **Guidance read:** AGENTS.md, the evidence contract, the research-depth section of the methodology, the opening of `docs/sources.md`, and the diffs to README, methodology, roadmap and sources between the two commits. I skimmed the rest of README and the roadmap only through those diffs.
- **Dossiers, memo and packets:**
  - Both dossiers in full: 19 claims, 80 citation occurrences and 2 null unknowns, with all 7 dimensions present in each record.
  - The memo, and both packets' prompt and JSON blocks.
- **Frozen CSV rows:** The complete TN019/TN020 row sets.
  - `cwsac_battles`: 2 rows, including the full description cells.
  - `cwsac_forces`: 4 rows.
  - `cwsac_commanders`: 4 rows.
- **Live NPS pages:** Both pages as HTML and text. Their descriptions are empty (`<dd></dd>`) and their force fields are blank.
- **OR selections:** All four selections read in full.
- **Parent OCR:** Context around every running head on pp.589–593, 601–605, 545–553 and 639–643. I also checked the report openings for Burnside's and Williams's reports and the "By the 30th" context.
- **Not inspected:** No maps, returns, print or facsimiles. I did no network access and no new research.

## Mechanical results

- **Text derivatives replay exactly.**
  - All 13 recorded character ranges across the four selections reproduce their sections under split/join whitespace collapse.
  - Both NPS texts reproduce from their HTML using the recorded HTMLParser transform.
  - All hashes match. The HTML hashes were checked on bytes, since the files contain CRLF line endings.
- **The parent is unchanged.** Both the parent record and the file `or30-2-illinois-ocr-v1` (`4e8fefcf…`) are byte-identical to the previous commit.
- **Citations are exact.**
  - Every quote occurs exactly once in its cited cell or section.
  - Both commander rows and all 11 frozen-cell quotes, including the description column, match.
- **Page map.** I recomputed a page for every OR citation from the running heads in the parent. Every locator matches and no quote straddles a page head.
  - Foster: pp.589/590/591/592/593.
  - Jones: p.601 printed "f>01", p.602, p.603 printed "003", pp.604/605.
  - Burnside: p.546 printed "54()", p.547, p.548, p.550, p.551, and p.552 printed "553".
  - Williams: p.639 printed "G89", pp.640/641/642/643.
  - The only locator that relies on a misread head is Burnside's p.552 citation. It is correctly marked inferred.
  - No citation falls on p.603 or p.639.
- **Registry.** The registry has 512 records / 496 paths. The previous 504/488 are preserved as an exact prefix, with 8 additions.
- **Coverage.** There are 110/127 dossiers, with 17 without. 28/36 campaign groups are complete by presence.
- **Unchanged files.** The following are byte-identical to the previous commit:
  - All 108 older dossiers and all 76 historical revisions.
  - The cohort.
  - Both admission proposals.
  - `admission-check.json` (0 promoted rows, 0 emitted rows).
  - `baseline.json`: 23 battles / 13 campaigns; Brier 0.2768816348133779 against 0.25.
  - `battles.json`.
- **Next group.** The next incomplete group by earliest start date is Bristoe Campaign [October-November 1863], starting 1863-10-13: VA039, VA040, VA041, VA042, VA043.
- **Packets and receipt.**
  - The packets' draft blocks equal the dossiers, and their registry blocks equal `sources.json`.
  - The assigned records match `battles.json`.
  - The prompt prefix is identical to TN018's.
  - Every `receipt.json` hash matches: 200 inputs (including all 186 evidence files), 512 sources and 7 outputs.
- **`make check`:** Run offline, 82 tests OK. `generalship check` reported `artifacts_written: false`.

## Substantive checks that passed

- **Scope.**
  - The following are kept as context outside the frozen dates: the Bristol raid (September 19), the Zollicoffer skirmish (September 20), and Jones's "not less than 2,000, all mounted" of September 20.
  - The boundary notes also exclude the October 3/5 skirmishes and the October 11 fighting.
- **Force figures.** No force figure is adopted, and both opening strengths remain null. This covers:
  - Foster's 6,000 at Zollicoffer.
  - Jones's 2,000.
  - Williams's 5,000 and 15,000, and the 75–100-man center.
  - Burnside's 6,000 Ninth Corps. "By the 30th" is correctly read as September, since the selection's next step is October 5.
- **Disputes stay visible and unreconciled:**
  - who burned Blountsville;
  - the frozen noon attack against Foster's time expressions;
  - the Blue Springs evening assault;
  - Williams's purpose.
- **Casualties.**
  - Foster's about 6 killed and 14 wounded is set against the frozen US 27, with status disputed.
  - Burnside's "about 100" is scoped as including the pursuit.
- **Commanders.**
  - The live "Colonel John Williams" is not adopted.
  - No commander gets automatic or additive credit.
  - Attributed judgments are not treated as causal effects.
- **Source labels.** The source records label all four report families as interested accounts. They also record:
  - Jones's report as written in February 1864, after he was relieved;
  - Burnside's report as written in November 1865;
  - Williams's supplement as revised after he read Burnside's report.
- **OCR.** OCR readings stay in the quotes, and the dossier reports "I piece" rather than silently correcting it.

## Required corrections (TN020)

**ET-R1: `command-roles`. The 5 p.m. clock and the order are misattributed to the cited passage.**
- **Problem.** The claim says Burnside "ordered Potter to break the Confederate center and that Ferrero's division attacked about 5 p.m." The cited 1865 passage says only that Potter was ordered to "endeavor to break tlirough the center" and "By 5 p. m. he had formed General Ferrero's division for the attack."
- **Replace the first sentence with:** "Burnside says he ordered Potter to move up and endeavor to break through the Confederate center, that by 5 p.m. Potter had formed Ferrero's division for the attack, and (in his October 17 dispatch) that he sent in a division of infantry on the infantry's arrival about 5 p.m.; he says that during the pursuit on the morning of October 11, outside the frozen date, the intercepting force at Henderson's withdrew through some misunderstanding."
- **Add these citations** (`or30-2-burnside-blue-springs-selections-v1`, section `burnside-1863-10-17`, locator "p.547 (OCR page markers; not checked against print)"):
  - "Skirmishing continued till the arrival of the infantry, about 5 p. m., when I sent in a division of infantry,"
  - "We pursued in the morning with infantry and cavalry."

**ET-R2: `supplies-and-roads`. October 11 material is not labeled with its date.**
- **Problem.** "We passed on without the loss of a wagon or a single head of beef cattle" follows Williams's account of routing Foster's brigade "at daybreak on Sunday (11th instant)." The boundary note excludes that fighting.
- **Replace the last sentence with:** "Williams says that after routing Foster's brigade at daybreak on October 11, outside the frozen date, he passed on without losing a wagon or a single head of beef cattle."
- **Add this citation** (`or30-2-williams-blue-springs-selections-v1`, section `williams-1863-10-23`, locator "p.641 (OCR page markers; not checked against print)"): "at daybreak on Sunday (11th instant) came upon the brigade of the enemy commanded by Colonel Foster,"
- The Henderson's part of the correction is in ET-R1.

**ET-R3: `reported-force-scope`. The population scope and basis of the 15,000 figure are lost.**
- **Problem.** Williams gives 15,000 as the strength of Burnside's "nearly his entire army," on the basis of subsequent information and Burnside's report. The dossier's "a force not far short of 15,000" drops that scope and basis.
- **Replace the clause with:** "later wrote, on the basis of subsequent information and Burnside's report, that he had greatly underestimated the enemy and that Burnside was present with nearly his entire army, which did not fall far short of 15,000 men,"
- **Add these citations** (`williams-1863-11-03`, locator "p.642 (OCR page markers; not checked against print)"):
  - "General Burnside was in that engagement himself with nearly his entire army,"
  - "as well as the official report of General Burnside,"
- **Append to the rationale:** "Williams's revision depends partly on Burnside's report and is not independent of that family."

**ET-R4: Value content without a cited passage.**
- **`clear-the-flank-or-divert`:** "set out to disrupt Union communications" is not quoted. Add the citation `arnold-cwsac-battles`, row TN020, column `description`: "set out to disrupt Union communications and logistics."
- **`command-roles`:** Carter's and Giltner's wing commands are not quoted. Add this citation (`williams-1863-10-23`, locator "p.640 (OCR page markers; not checked against print)"): "the right wing under command of Colonel Carter, of First Tennessee Cavalry, and the left under Colonel Giltnei*,"

After these edits, TN020 would have 46 citations and the batch 86. The memo, README, roadmap, report text, packet and receipt counts would need regenerating by the primary agent.

## Non-blocking notes

- **ET-N1 (TN019 `recorded-result`).** Jones's night-of-the-22d withdrawal was of Williams's force from Carter's Depot, not from Blountsville. Suggested wording: "Jones says he withdrew Williams from Carter's Depot to Zollicoffer on the night of the 22d." An optional citation is `jones-1864-02-06-blountsville`, p.605: "My force being altogether too small to enable me to hold both Carter’s Depot and Zollicoffer,"
- **ET-N2 (TN019 timing).**
  - The memo says Foster met the enemy at 9 a.m., but no dossier claim cites that clock. The quote is on p.592 of `foster-1863-09-22`, in OCR as "tliis morning at 9 o’clock,".
  - `command-roles` holds a visible timing difference but has status `supported`. Consider citing the clock and marking the timing difference as disputed.
- **ET-N3 (TN020 `recorded-result`).** The frozen description gives its own account of the assault, which is not cited: "Ferrero's men broke into the Confederate line, causing heavy casualties, and advanced almost to the enemy's rear before being checked." It is the NPS/CWSAC family, and it is not an independent witness to either report.
- **ET-N4 (memo and metadata).**
  - The memo's "Three OCR running heads are misread" omits Jones's p.601 head, which reads "f>01". No locator uses it, because the p.601 `jones-heading` section is not cited.
  - `document_dates_by_section` maps Burnside's dates without noting the OCR readings: OCR "October 17, 1803" becomes 1863-10-17, and OCR "November 13, 18G5" becomes 1865-11-13. The readings are unambiguous and no claim relies on them.
  - If these are to be recorded, use a `metadata_only` revision. Do not edit the source records.

No morale/readiness score, probability, causal effect or ranking was found or introduced. Unresolved historical questions remain unresolved: the Blountsville fire, the Blountsville clocks, the Blue Springs assault and the opening strengths. This review does not change any evidence, admit features, or alter model inputs.
