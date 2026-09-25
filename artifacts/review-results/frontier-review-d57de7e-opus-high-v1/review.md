# Frontier and Texas coast first passes: separate AI review

**Outcome: corrections required** (15 required findings, FRC-01 to FRC-15; 14 advisories, FRA-01 to FRA-14).

This is a separate AI analysis. It is not human historical adjudication, independent corroboration,
proof of source independence or feature admission. The corrections below are proposals; the primary
agent should check each against the cited passage before changing evidence.

## Review record

| Item | Value |
|---|---|
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, fresh-context subagent; no task identifier was exposed to the reviewer |
| Date | 2026-09-25 |
| Assignment | `artifacts/review-results/frontier-review-d57de7e-opus-high-v1/assignment.md`, sha256 `f107fb33dfa1bc09f8a29240bce6c2542d311476a4238db769993882d8c46127` (verified) |
| Input manifest | `inputs.json`, sha256 `ccf70cdb5365e98cd3bfa59de7fe93cb6daee19b536dec18fba39b86e9f7e099` (verified) |
| Prepared commit | `d57de7e5a8fd26540f132c1aa845ca711d66fc0f` |
| Previous commit | `c7f5799595db240736cc9176f345fd69720615a7` |
| Worktree / bundle commit | `5a09f91d54f816372f6ef6907649d4b5f4dbea1f` (differs from the prepared commit only by the two bundle files) |
| Input hashes | All 107 manifest paths match both `git show d57de7e:<path>` and the worktree; no mismatch |
| `make check` (offline) | 134 unit tests OK; `python3 -m generalship check` exited 0 |
| Network / build / packet | None run. No primary artifact modified; only this file was written |

## Scope actually inspected

- **Docs:** AGENTS.md; `docs/methodology.md`, `docs/evidence-contract.md`, `docs/cohort-v2.md` in
  full; the `docs/sources.md` diff for this batch; all nine memos in full.
- **Dossiers:** all 14 dossiers (MN001, MN002, TX001, TX002, TX003, TX005, TX006, ID001 and
  ND001–ND005, CO001). I read every claim, value, rationale, status, phase and citation (127 claims,
  579 citation occurrences). I compared each text quote with its selection section and page marker by
  reading, and scripted a check for numbers in claim values that no cited quote contains.
- **Frozen rows:** the Arnold battle, force and commander rows for all 14 records.
- **NPS pages:** the 14 NPS text snapshots were read in full. The HTML originals were not read; their
  hashes were verified through the manifest.
- **Selections:** all 30 selection files were read in full. A script re-extracted every
  `selection_character_ranges` span from its parent OCR and compared it with the whitespace-collapsed
  section text; all 30 match. The same script confirmed that each `parent_sha256` equals the
  registered parent. The validator does not perform this range check.
- **Source records:** all 66 added records. The 38 non-NPS records had every metadata field read. For
  the 28 NPS records, the id, group, parent linkage and inspection note were read. The Bancroft and
  committee catalog JSON were spot-checked.
- **Parents:** the parent OCR volumes were **not** read beyond the selections, apart from:
  - a case-insensitive search for "inkpa"/"ink-pa" in the OR XXII part 1 and OR XLI part 1 parents,
    which found no match (other spellings are not excluded);
  - a keyword check of the Bancroft catalog JSON and OCR for "edition".
- **Excluded:** no new research and no other source family was opened.

## Required corrections

Section and page locators below are those of the selection files, with OCR page markers not checked
against print.

**FRC-01 — The memos and two registry notes still describe parent records that were deduplicated at
merge.** The memo counts total 74 records, but the registry adds 66 (28 NPS, 8 catalog/OCR and 30
selections). The OR XIII, OR XV, OR XXVI part 1 and ORN 19 parents were registered before this batch
(OR XV at `be711a9`, `data/raw/baton-rouge-1862-v1/or15-full.txt`).

- `docs/research/sioux-1862-first-pass-v1.md`: replace "This pass adds **10 source records**: two NPS
  HTML/text pairs; OR XIII catalog metadata and full OCR (`ia-or13-illinois-metadata-v1`,
  `or13-illinois-ocr-v1`); and the selections" with "This pass adds **8 source records**: two NPS
  HTML/text pairs and the selections". Then add: "The selections reuse the registered Volume XIII
  parent `or13-illinois-ocr-v1`; this pass's byte-identical copy was not registered again."
- `docs/research/texas-coast-1862-first-pass-v1.md`:
  - replace "**13 source records**: two NPS HTML/text pairs; OR XV catalog metadata and full OCR
    (`ia-or15-illinois-metadata-v1`, `or15-illinois-ocr-v1`) and ORN 19 catalog metadata and full OCR
    (`ia-orn19-trent-metadata-v1`, `orn19-trent-ocr-v1`); and the selections" with "**9 source
    records**: two NPS HTML/text pairs and the selections";
  - replace "so the primary can deduplicate them at merge" with "and were deduplicated at merge; the
    selections reuse `or15-illinois-ocr-v1` and `orn19-trent-ocr-v1`".
- `docs/research/texas-coast-1863-first-pass-v1.md`:
  - replace "**7 source records**: one NPS HTML/text pair; OR XXVI part 1 catalog metadata and full
    OCR (`ia-or26-1-illinois-metadata-v1`, `or26-1-illinois-ocr-v1`); and the selections" with "**5
    source records**: one NPS HTML/text pair and the selections";
  - replace "so the primary can deduplicate it at merge" with "and was deduplicated at merge; the
    selections reuse `or26-1-illinois-ocr-v1`".
- `docs/research/galveston-1863-first-pass-v1.md` line 21: replace "registered with the Texas coast
  1862 pass" with "registered by an earlier Gulf pass as `or15-illinois-ocr-v1`".
- In `or15-davis-galveston-selections-v1` and `or15-magruder-galveston-selections-v1`,
  `dependency_note`: replace "Reuses the Volume XV parent registered in the texas-coast-1862 batch."
  with "Reuses the registered Volume XV parent (or15-illinois-ocr-v1)." If these records are treated
  as committed, use `metadata_only` revisions.

**FRC-02 — TX001 omits a one-day disagreement in the reports over when the attack took place.**

Crocker's account runs day by day:

1. arrival on the 23rd and a failed crossing that night;
2. "the next day" only the Rachel Seaman crosses, near nightfall;
3. "the next day" the Henry Janes is kedged over and both vessels attack;
4. that night the battery is evacuated;
5. the next morning, the surrender.

Spaight instead has fire opening early the morning after the vessels anchored on the 23rd, and the
evacuation complete by the following daylight. The claim `bar-and-range` paraphrases Crocker without
flagging this.

In `recorded-result`, append to `value`: "Crocker's day-by-day account puts the Henry Janes's crossing
and the attack on the day after the Rachel Seaman crossed near nightfall, one day later than Spaight's
account of fire opening early on the morning after the vessels anchored on the 23rd; Debray, writing
at Houston on the 25th, relays a report of heavy cannonading 'this morning'." Append to `rationale`:
"The frozen September 24-25 interval is retained; the reports' dates are not reconciled." Add these
citations:

- `orn19-crocker-sabine-pass-selections-v1`, `crocker-1862-10-02`, p.218: "The next day, with all the
  boats, the Henry Janes was kedged over, and both vessels immediately took up a position to attack."
- `or15-spaight-sabine-pass-selections-v1`, `spaight-1862-09-26`, p.144: "Early the next morning the
  two sail vessels, having crossed the bar, took position and opened fire on our works"
- `or15-debray-sabine-pass-selections-v1`, `debray-1862-09-25`, p.143: "except the report of heavy
  cannonading this morning in the direction of Sabine Pass."

**FRC-03 — In TX001 `express-and-messenger`, the timing of Spaight's statement is misstated.** "I have
no information as to the force of the enemy" was written on September 26 about the vessels then off
the town, after the evacuation. It is not pre-battle intelligence. Replace the `value` with: "Debray
learned of the attack at Houston from an express and a messenger's report of heavy cannonading.
Spaight, writing on September 26 after the evacuation, says the two sail vessels had anchored
opposite the town and that he had no information on the enemy's force." Add the citation
`or15-spaight-sabine-pass-selections-v1`, `spaight-1862-09-26`, p.145: "As I learn to-day the two sail
vessels have anchored opposite the town and sent some men ashore."

**FRC-04 — TX003 `casualty-records` omits the Union naval dead given in both selected reports.**
Append to `value`: "Davis says Commander Renshaw, four of his chief officers and six of his men died
when the Westfield was blown up; Magruder says Captain Wainwright and Lieutenant Lea of the Harriet
Lane were killed. These naval deaths are outside Davis's statement about his troops." Add these
citations:

- `or15-davis-galveston-selections-v1`, `davis-1863-01-10`, p.207: "Commander Renshaw, with four of
  his chief offi- cers and six of his men, being blown up in her."
- `or15-magruder-galveston-selections-v1`, `magruder-1863-01-02`, p.211: "Captain Wainwright and
  Lieutenant Lea, executive officer of the Har- riet Lane, were both killed"

**FRC-05 — TX003 `guns-rail-and-stores` supplies an agent the passage does not name.** The cited
passage says only that the track "had been permitted to remain". In `value`, replace "the railroad
from Virginia Point, never cut by the Union forces, carried his heavy gun toward the fleet" with "the
railway track from Virginia Point to Galveston, which had been permitted to remain, carried his heavy
gun toward the fleet".

**FRC-06 — Two ID001 statements lack support.**

- (a) In `casualty-records`, the value's Bancroft figure of 200 killed has no citation. Add
  `bancroft-utah-bear-river-selections-v1`, `bear-river`, p.632: "the former placing it at 200, and a
  great many wounded".
- (b) In `stated-aims`, "the marshal, who held warrants for Bear Hunter, San Pitch and Sagwich" is not
  in the source. Connor says Chief Justice Kinney requisitioned troops to arrest them. Replace "and
  told the marshal, who held warrants for Bear Hunter, San Pitch and Sagwich, that he did not intend
  to take prisoners" with "and, after Chief Justice Kinney had made a requisition for troops to arrest
  Bear Hunter, San Pitch and Sagwich, told the marshal that he did not intend to take any prisoners".
  Add `or50-1-connor-bear-river-selections-v1`, `connor-1863-02-06`, p.187: "made a requisition for
  troops for the purpose of arresting the Indian chiefs Bear Hunter, San Pitch, and Sagwich."

**FRC-07 — The Bancroft edition field makes an unsupported "First edition" claim.** The field appears
in `bancroft-utah-ocr-v1`, `ia-bancroft-utah-metadata-v1` and
`bancroft-utah-bear-river-selections-v1`. The retained catalog has no edition field, and its
description reads "Also published separately, 1890". In `edition`, replace "First edition." with
"Printed as Works vol. XXVI (1889); the catalog notes the work was 'Also published separately, 1890';
edition priority is not established." Use `metadata_only` revisions if the records are treated as
committed.

**FRC-08 — ND001 `casualty-records` presents an expedition-wide loss without its scope.** Sibley's 3
cavalry killed and 4 wounded is his column's loss "in actual combat" for the whole expedition, just as
his 150 is. It is not a Big Mound figure.

- In `value`, replace "Sibley gives, for the whole column in combat, 3 cavalrymen killed and 4
  wounded" with "Sibley gives his column's loss in actual combat for the whole expedition as 3
  cavalrymen killed and 4 wounded".
- Append to `rationale`: "Sibley's 3 killed and 4 wounded, like his 150, covers the whole expedition
  and is not assigned to this record; it coincides with McPhaill's nominal-list 3 and 4 and may be the
  same casualties."
- Add `or22-1-sibley-dakota-selections-v1`, `sibley-1863-08-07`, p.358: "the loss sustained by my
  column i in actual combat was very small."

**FRC-09 — ND003 `reported-force-scope` misstates the basis of the 10,000 figure.** Sibley cites
"various sources, including that obtained from the savages themselves, in their conversations with
our half-breed scouts". He does not mention prisoners.

- In `value`, replace "from scouts' and prisoners' information" with "from various sources including
  the Indians' own conversations with his half-breed scouts".
- In `rationale`, replace "(10,000 souls, undated, from scouts' and prisoners' information)" with
  "(10,000 souls, undated, from various sources including the Indians' conversations with his
  half-breed scouts)".
- Add `or22-1-sibley-dakota-selections-v1`, `sibley-1863-08-07`, p.356: "including that obtained from
  the savages themselves, in their conversations with our half- breed scouts".

**FRC-10 — ND004 `ravines` (phase `inherited`) has an uncited clause that describes a deployment.**
"They formed a line from which only a charge could dislodge them" has no citation, and it records the
defenders' line of battle, not pre-existing ground. "About 15 miles west of the James River" is also
uncited. Replace the `value` with: "Sully says the camp lay in ravines where the Indians felt secure,
and places the field about 15 miles west of the James River near a hill the Indians called White
Stone Hill; House says the ground was very uneven and the Indians collected in a ravine to fight."
Add `or22-1-sully-white-stone-hill-selections-v1`, `sully-1863-09-11`, p.560: "about 15 miles west of
James Biver". If the line-of-battle statement is kept, put it in a non-`inherited` claim with p.560:
"the Indians had formed line of battle with good judg- j ment, from which they could be dislodged only
by a charge."

**FRC-11 — ND004 `casualty-records` omits Sully's conflicting figure for the September 5 ambush.**
Sully says one of the parties sent to find Surgeon Bowen fell into an ambush in which 4 were killed.
Hall, whose scout was searching for Bowen, reports 6 killed.

- Append to `value`: "Sully says one of the scouting parties sent to find Surgeon Bowen fell into an
  ambuscade in which 4 were killed; Hall reports 6 men killed on his scout for Bowen."
- Append to `rationale`: "Sully's 4 and Hall's 6 appear to describe the same September 5 skirmish;
  not reconciled."
- Add `or22-1-sully-white-stone-hill-selections-v1`, `sully-1863-09-11`, p.559: "One of these fell
  into an ambuscade, by which 4 of the party were killed and the rest driven in."

**FRC-12 — TX006 `command-roles` omits the clock dispute that underlies Crocker's charge against
Franklin.** Append to `value`: "The accounts also differ on when the attack began: Crocker says it was
4 p.m. before Franklin was ready to co-operate, Franklin that the gunboats' movement commenced at 3,
and Dowling that the fleet stayed out of range until 3.40." Add these citations:

- `or26-1-crocker-sabine-pass-selections-v1`, `crocker-1863-09-12`, p.301: "It was 4 o’clock in the
  afternoon before General Franklin was ready to co-operate"
- `or26-1-franklin-sabine-pass-selections-v1`, `franklin-1863-09-11`, p.297: "The movement of the
  gunboats commenced at 3 o’clock"
- `or26-1-dowling-sabine-pass-selections-v1`, `dowling-1863-09-09`, p.311: "remained out of range
  until 3.40 o’clock"

**FRC-13 — Three CO001 statements lack support, and one command statement is missing.**

- (a) `recorded-result` says "The committee calls it a massacre", but the cited committee quote does
  not contain that word. Add `joint-committee-sand-creek-report-selections-v1`, `committee-report`,
  p.iv: "how unprovoked and unwarranted was this massacre."
- (b) `reported-force-scope`: Smith's "about 500 people at five to a lodge" has no citation (the
  numeral 500 matches only the Arnold field). Add `smith-sand-creek-testimony-selections-v1`,
  `smith-testimony-1865-03-14`, p.6: "About- 500 ; we estimate- them at five to a lodge."
- (c) `command-roles` omits Smith's testimony about orders, which is a command-authority statement in
  the selected passage.
  - Append to `value`: "Smith says that when he told Chivington on the day of the attack what the
    Indians' character was, Chivington replied that his orders were positive to attack them; Smith
    did not know who gave the orders and presumed General Curtis."
  - Add `smith-sand-creek-testimony-selections-v1`, `smith-testimony-1865-03-14`, p.8: "He said he
    could not help it; that his orders were positive to attack the Indians."
  - Add the same source and section, p.8: "I do not know; I presume from General Curtis."

**FRC-14 — The committee report depends in part on Smith's testimony.**

The report's flag passage closely follows Smith's words (p.iii: "with a small white flag under it., as
he had been ad¬ vised to do in case he met with any troops on the prairies."). It also relies
generally on the interpreter's testimony (p.ii: "The Indian agents, 4 the Indian interpreter and
others examined by your committee, all testify to the good character of those Indians."). Counting
the two as separate families for the effort ceiling is acceptable, but their agreement must not be
read as independent corroboration.

- Replace the `dependency_note` of `joint-committee-sand-creek-report-selections-v1` with: "The
  committee's report on the attack, based on the testimony it took in March 1865; a political body's
  findings and characterization, not a participant account. It quotes Anthony's testimony, and its
  account of Black Kettle's flags and of the interpreter being fired on closely follows John S.
  Smith's testimony in the same volume, which it cites generally ('the Indian interpreter and others
  examined by your committee'); agreement between the report and Smith's testimony is not independent
  corroboration. Shares its container with the Smith testimony selection." Use a `metadata_only`
  revision if the record is treated as committed.
- Append to CO001 `open_questions[1]` and to the memo's family paragraph: "The committee report draws
  on the testimony it took, including Smith's; agreement between them is not independent
  corroboration."

**FRC-15 — The Sand Creek memo states the Cheyenne/Arapaho gap but not what it means for the
evidence.** The other frontier memos do. In `docs/research/sand-creek-1864-first-pass-v1.md`, replace
"- **No Cheyenne or Arapaho account was inspected.**" with "- **No Cheyenne or Arapaho account was
inspected.** The camp's numbers, status, aims and losses therefore rest on Chivington's reports, the
committee's findings (which draw on the testimony it took) and Smith, a white interpreter trading in
the village, with NPS as a modern summary."

## Advisories

These are optional and not required for this pass.

- **FRA-01 (Sibley groups).** Keeping `sibley-sioux-reports` and `sibley-new-mexico-1862-reports`
  apart is sound. However, `docs/sources.md` justifies it only by "opposite sides of different
  campaigns". The frozen commander table gives the identical full name "Henry Hastings Sibley" to the
  Confederate NM001 commander and to the Union MN002/ND001–ND003 commander. Neither the author strings
  nor the frozen names can separate the two, so the note should say so. Whether the NM001 name is a
  frozen-table error is outside these inputs.
- **FRA-02 (`docs/sources.md`).** Add to the batch sentence "No Dakota, Shoshone, Cheyenne or Arapaho
  account was obtained": "; no Confederate account of Palmito Ranch was found in the inspected report
  list."
- **FRA-03 (TX005).** Barrett wrote in August 1865 after detailed reports had gone to New Orleans. His
  column figures may depend on Branson's report, so agreement on 250/50/200 is not independent. Note
  this in the Barrett `dependency_note`.
- **FRA-04 (ND005).** NPS quotes Sully as reporting warriors "strongly posted in wooded country, very
  much cut up with high, rugged hills, and deep, impassible ravines." That wording is not in the
  inspected July 31 report, and neither is NPS's "running fight of almost nine miles". Record both as
  NPS statements that were not found.
- **FRA-05 (TX006).** Crocker signs as "Acting Volunteer Lieutenant". Franklin calls him
  "Lieutenant-Commander" and "Captain", and the frozen rank is "Captain". Record the discrepancy as MN002
  does for Sibley.
- **FRA-06 (CO001).**
  - Smith's two statements on the dead under the bank differ ("the greater portion women and
    children" vs "Perhaps one-half were men").
  - Chivington's "I captured no prisoners" conflicts with Smith's children "taken prisoners near the
    camp".
  - The killing of Jack Smith on November 30 falls inside the frozen interval.
  - The committee says Chivington "had no authority whatever over" Anthony.
- **FRA-07 (TX002).** `recorded-result` says "NPS says" but cites the Arnold description. The two are
  one family, so cite `nps-tx002-v1` or say "the frozen description".
- **FRA-08 (TX003, TX006).** "Prisoner counts include naval crews" is an inference; write "may
  include".
- **FRA-09 (ND003).** Sibley names the combined bands (Little Crow's remnant, Sissetons, Cut-heads,
  Chank-ton-ais), which bears on the opposing force's composition. His naming of Little Crow's band is
  not evidence about Inkpaduta.
- **FRA-10 (ND001/ND002).** McPhaill's July 24 pursuit reached Dead Buffalo Lake ("we drove them from
  their conceal- ment in the rushes and wild rice of Dead Buffalo Lake"). The place name therefore
  belongs to both records' passages; keep his 31 killed unassigned between them.
- **FRA-11 (ND004).** Hall says he went "in a northeasterly direction"; NPS says northwest. Sully's
  "Indian reports make it over 200" and House's "about 100" are both undated.
- **FRA-12 (TX001).**
  - Debray's express overstated the Union force ("one gunboat and three or four transports").
  - His relief column of about 900 is context and is not engaged.
- **FRA-13 (MN002).** For "Marshall led the charge", Sibley's p.279 "after a few volleys he led his men
  to a charge and cleared the ravine of the savages." supports the claim more directly than the
  current Marshall quote.
- **FRA-14 (Magruder group).** Reusing `magruder-big-bethel-reports` is correct for one author, but
  the name is now misleading. A future registry-wide rename would need a documented migration.

## Assessment of the specified decisions

- **Sand Creek and Bear River characterizations.** Both records keep the result `disputed` and quote
  both sides. On Bear River:
  - on the frozen and NPS side: "Union victory (massacre)", "Massacre at Boa Ogoi" and "Union
    Victory";
  - from Connor's selection: Wright's "Our victory was complete";
  - Bancroft's butchery/massacre remark.

  On Sand Creek: Chivington's "most bloody battles"; the committee's language (needs FRC-13a); and
  Smith. No characterization is adopted. **Sound**, subject to FRC-13a.
- **Inkpaduta and Ford.** No inspected selection names either man. My search of the OR XXII part 1
  and XLI part 1 parents found no "inkpa"/"ink-pa" string. Resting both on the frozen tables and NPS,
  with an explicit "role not established", is **sound**.
- **Missing Native and Confederate accounts.** The gaps are stated in every relevant memo and in the
  dossier rationales, with consequences, except in the Sand Creek memo (FRC-15). `docs/sources.md`
  omits Palmito Ranch (FRA-02).
- **Targeted follow-ups.** Counting them as a fourth family is consistent with the methodology's
  ceiling of three families plus one follow-up. TX001, ND001, ND002, ND004, ND005, CO001 and TX006
  each have at most four families. ND002 reuses McPhaill only for the statement that his losses
  include the 26th, which is **sound**; see FRA-10.
- **Wright's transmittal.** It is correctly placed in `connor-bear-river-report` as a dependent
  document, not a family. **Sound.** That its casualty figures come "from [Connor's] unprinted list"
  is a reasonable inference, not a stated fact.
- **Committee and Smith as separate families.** They are acceptable as separate authors for the effort
  ceiling. The committee's dependence on Smith must be recorded (FRC-14).
- **Author groups.** Reusing Magruder is sound (FRA-14). One group each for Sibley (1862/1863), Sully
  (1863/1864) and Crocker (1862 ORN and 1863 OR) is sound; the frozen rows use one name for each
  across records. Keeping the Sioux-campaign Sibley apart from the New Mexico Sibley is sound
  (FRA-01).
- **Parent deduplication.**
  - Verified: the selections resolve to the pre-registered `or13-illinois-ocr-v1`,
    `or15-illinois-ocr-v1`, `or26-1-illinois-ocr-v1` and `orn19-trent-ocr-v1`, with matching parent
    hashes, and no duplicate parent was added.
  - The memos and two dependency notes are stale (FRC-01).
- **Other rules.**
  - No strength is adopted as an opening force; each dossier's opening strength is `unknown` with a
    null value.
  - `inherited` is used only on terrain claims (TX005, TX006, ND004, ND005); ND004 needs FRC-10.
  - Outcome claims are `post_outcome`.
  - No commander receives automatic credit.
  - No aggregate is added across records, apart from the scope issue in FRC-08.
- **Other source-record fields.** The other checked fields are accurate: edition imprints per OCR
  title, dates by section (including the undated committee report and House/Hall reports), kinds,
  inspection notes and archival identifiers.

## Remaining limits

- **Page locators.** Checked against the OCR page markers in the selections only, not against print.
- **Unverified fields.** NPS HTML originals and the catalog JSON were not read in full.
- **Historical questions left open.** The review does not resolve any historical question, including:
  - the TX001 dates;
  - the Sand Creek, Bear River and Whitestone Hill characterizations;
  - the casualty figures;
  - the Crocker–Franklin responsibility dispute.

  These remain as preserved disputes. The AI review does not admit features or change model inputs.
