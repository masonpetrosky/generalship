# Trans-Mississippi 1862 first passes: separate AI review

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a fresh-context subagent working only from the assignment and the repository.
- **Date:** 2026-09-25.
- **Bundle commit (worktree HEAD):** `aeeeecf9e3de705bf72fe52430e6b41c3fc05e18`.
- **Prepared commit reviewed:** `3d36bfe394ead1264b329d1d8b5b35ed794086f0`, against `0019009548110f6535c69deeb6ef9c3f7306d0db`.
- **Assignment:** `assignment.md`, sha256 `cccbdfde39d93bc1b697a1d5aa8ca81b03f5d43479172e5e19de54844208eb13` (verified).
- **Input manifest:** `inputs.json`, sha256 `fe3f4312e9bc195519c44aee23fac3c1ef89827259d6b77adb8954c6a91c768d` (verified).
- **Input verification:** I checked all 80 bound paths against `git show 3d36bfe:<path>` and against the worktree files. There were **0 mismatches**. The bundle commit differs from the prepared commit only by the assignment and `inputs.json`.
- **Outcome:** **corrections required.**
  - Required: TM-R1 to TM-R6.
  - Advisory: TM-A1 to TM-A8.

This is a separate AI analysis. It is not human historical adjudication, proof of source independence or feature admission. I did no new research, opened no new source families, spawned no agents and modified no primary artifact.

## Scope actually inspected

- **Guidance.** I read:
  - AGENTS.md;
  - the research-depth section of `docs/methodology.md`;
  - `docs/evidence-contract.md` and `docs/cohort-v2.md` in full;
  - the `docs/sources.md` diff for this pass, and its author-group policy paragraph.

  I did not read README or the roadmap.
- **Memos.** I read all five memos in full (New Mexico, Pea Ridge, White River, Cache River, Boston Mountains).
- **Dossiers.** I read all 11 dossiers in full. By script, they contain:
  - 100 claims, 11 null unknowns and 602 citations;
  - 7 dimensions per record;
  - phase tags limited to `unresolved`/`post_outcome`.

  Every citation's quote was read inside its full surrounding passage. The counts match the memos.
- **Frozen rows and NPS pages.**
  - Frozen rows: I read the `cwsac_battles`, `cwsac_forces` and `cwsac_commanders` rows for all 11 records, including the MO017 frozen description.
  - NPS pages: I read all 11 NPS text snapshots (header, forces, casualties, description and result). I did not render the HTML parents; `make check` covers their bytes.
  - Cohort and baseline: I confirmed that each of the five campaigns is complete in `cohort-v2.json`, and that none of the 11 IDs is in the v1 cohort or in `artifacts/baseline.json`.
- **Selections.** I read every selected report section in full:
  - Canby, including the Valverde return;
  - Sibley, Slough, Scurry and Chivington;
  - Curtis (both sections) and Van Dorn;
  - Fitch, Dunnington and Hindman (all three sections);
  - Hovey, McNeil, Buel, Foster and Salomon;
  - Cooper (all four sections, including the No. 5 return);
  - Blunt, Wickersham and Barstow;
  - Britton (preface, Independence, Lone Jack).

  I did not reread the title-page sections.
- **Parents.**
  - A script re-extracted every selection range for all 20 selections from its parent OCR. It confirmed that the whitespace-collapsed text equals each section, and that parent hashes match.
  - I inspected the OR IX OCR immediately after Chivington's No. 3 report.
  - I searched the Britton volume I OCR and its contents pages. It has no Kirksville or Clark's Mill chapter; Chapter XXV is the Lone Jack aftermath (Blunt's march, Coon Creek, Hays), not the battle.
- **Registry.**
  - I diffed `data/sources.json` against `0019009`: 46 records were added and none were changed or removed.
  - I read in full all 20 selection records, the OR IX/XIII parent and metadata records, and the MO017 NPS pair. The other NPS records were checked for group and path only.
  - I checked the registry for earlier records by the same authors (Curtis, Van Dorn, Sibley, Canby, Hindman, Cooper, Blunt, Britton, Foster, Buel and others). I also checked the deduplicated parents `or8-illinois-ocr-v1` and `britton-border-1-ocr-v1` (same scan identifiers and hashes).
- **Validation.** `make check` passes offline: 134 tests OK, and `python3 -m generalship check` succeeds with `artifacts_written: false`.
- **Not inspected:** any source outside the bound selections; unselected OR pages (apart from the targeted points above); print facsimiles; other campaigns' dossiers.

## Overall assessment

Extraction quality is high:

- Quotes are exact and read correctly in context.
- Opening strengths are null in all 11 records.
- Nominal, engaged, morning and enemy-estimate figures are kept apart and dated.
- The frozen-versus-live conflicts are visible: NM001's reversed NPS force field, and the NPS zeros.
- Nothing is tagged `inherited`.
- No listed commander receives automatic credit. Absent or off-field listed commanders (Hindman at AR003, Cooper at OK004) are identified as such.
- March 26 and 28 losses at Glorieta are not summed.
- Each record uses three or fewer families, plus at most one follow-up.

The follow-up choices are sound:

- **Glorieta (Chivington).** Chivington fills the Johnson's Ranch and March 26 gap that NPS treats as decisive. The Slough relay is disclosed.
- **Saint Charles (Hindman).** Dunnington gives no Confederate personnel count. Hindman fills that gap, though see TM-R3 on how his dependence is described.
- **Kirksville (two families).** Two families are acceptable under an effort ceiling that is not a quota, and the gap is recorded.
- **Compiled returns.** Keeping the returns inside the commanders' selections, as separate sections labelled as not the author's text, is sound. It is also conservative, because it never adds a family. Cooper's No. 5 return is correctly labelled "of unstated authorship", rather than asserted to be the compiler's work.
- **Independence and Clark's Mill bounds.** The frozen Union bounds equal the casualty figures (344 and 113). Recording this as an observation, without adopting or "correcting" the imported values, is appropriate. The records are outside the v1 cohort and baseline.
- **Parent deduplication.** Both parents are byte-identical to the 1861 West registrations, and all 20 selection ranges reproduce from them.

The required corrections concern:

- stale registry grouping and notes after the merge deduplication (TM-R1, TM-R2);
- one overread dependency (TM-R3);
- stale memo text (TM-R4);
- two value/rationale scope errors (TM-R5, TM-R6).

## Required corrections

### TM-R1: the Britton volume I selection sits in a retired group, and its dependency note is false

**Problem.** `britton-border-1-boston-mountains-selections-v1` uses group `britton-civil-war-on-border-1899`. Its dependency note says the author "has two registered groups … and britton-civil-war-on-border-1899 (the more recent Price selection)". At `0019009` this is wrong on two counts:

- **Price selection.** PRV-R4 (`britton-price-missouri-selections-v2`) had already moved the Price selection to `britton-civil-war-border-1899`. Its revision note calls the `-on-border-1899` name a misalignment. Only the superseded v1 still uses that name.
- **Parent group.** This record's own parent, `britton-border-1-ocr-v1`, is in a third group, `britton-civil-war-border`. That group also holds the 1861 Missouri, Indian Territory and Mount Zion selections.

The memo repeats the claim (`boston-mountains-1862-first-pass-v1.md`: "It is placed in the author's most recent registry group, `britton-civil-war-on-border-1899`…").

**Correction.** Follow the contract and the PRV-R4 precedent by adding a metadata-only successor.

- **Successor record.** Add `britton-border-1-boston-mountains-selections-v2`. It is identical to v1, with the same path, sha256, parent and ranges, except for:
  - `independence_group`: `britton-civil-war-border`;
  - `supersedes`: `{"source_id": "britton-border-1-boston-mountains-selections-v1", "metadata_sha256": "08dbe2bd14fa4ddc18873b543d5c0ef56d67626e6b969408a99a8492e24cc192"}`. I computed this hash as sorted-key compact UTF-8 JSON, and the same method reproduces PRV-R4's `c44ed0f7…`.
  - `revision_kind`: `metadata_only`;
  - `revision_note`: "TM1862-R1: independence group aligned with the registered parent britton-border-1-ocr-v1 after merge deduplication; same pinned raw bytes. v1 carried britton-civil-war-on-border-1899, which PRV-R4 had retired, and its dependency note described the author's groups incorrectly. Not an additional witness."
  - `dependency_note`: replace its second sentence ("The author has two registered groups, … two names denote one author family.") with: "Same scan, parent and group (britton-civil-war-border) as the 1861 Missouri, Indian Territory and Mount Zion selections. Britton's volume II records use britton-civil-war-border-1899, and the superseded britton-price-missouri-selections-v1 used britton-civil-war-on-border-1899. All three names denote one witness family." Keep the rest unchanged.
- **Dossiers.** Repoint all Britton citations in MO014 (25) and MO015 (25) to `-v2`, with quotes and sections unchanged.
- **Memo.** In the Boston Mountains memo, replace the sentences from "It is placed in the author's most recent registry group…" through "…the primary will deduplicate." with: "It uses the registered parent `britton-border-1-ocr-v1` and that parent's group, `britton-civil-war-border` (see TM1862-R1). The author's other group names, `britton-civil-war-border-1899` and the retired `britton-civil-war-on-border-1899`, denote the same witness family."

### TM-R2: Cooper's 1862 reports ignore his registered group, and the note says none exists

**Problem.** The 1861 West pass already registered Douglas H. Cooper's January 20, 1862 Indian Territory report as `or8-cooper-indian-territory-selections-v1`, in group `cooper-indian-territory-report`.

- **The new record.** `or13-cooper-newtonia-old-fort-wayne-selections-v1` creates `cooper-indian-territory-1862-reports`. Its dependency note says "No earlier registry group for this author in this worktree", which is false after the merge.
- **The memo.** It says "No earlier registry group exists for any of these authors."
- **The pass's own rule.** The pass reuses existing author groups for Canby and Hindman, so the new Cooper group is inconsistent with it.

**Correction.**

- **Successor record.** Add metadata-only `or13-cooper-newtonia-old-fort-wayne-selections-v2`. It is identical to v1 except:
  - `independence_group`: `cooper-indian-territory-report`;
  - `supersedes.metadata_sha256`: `368b670eefdbd6557d2f20070e9d0fa1945407b5734093b3303d2caf64f3b0e6`;
  - `revision_kind`: `metadata_only`;
  - `revision_note`: "TM1862-R2: aligned with the author's registered group after merge; same raw bytes; not an additional witness.";
  - `dependency_note`: replace "No earlier registry group for this author in this worktree." with "Same author family and group (cooper-indian-territory-report) as his January 20, 1862 Indian Territory report (or8-cooper-indian-territory-selections-v1)."
- **Dossiers.** Repoint MO016 (16 citations) and OK004 (18 citations).
- **Memo.** In the Boston Mountains memo:
  - change the Cooper table group to `cooper-indian-territory-report`;
  - replace "No earlier registry group exists for any of these authors." with "Cooper joins his registered group `cooper-indian-territory-report` (his January 1862 Indian Territory report); no earlier registry group exists for the other authors."

If the primary prefers to keep a separate group name, which the `docs/sources.md` policy permits, the dependency-note and memo sentences must still be replaced as above.

### TM-R3: Hindman is said to "rely on and refer to Dunnington's and Williams's report", but the passage does not say so

**Evidence.** In `hindman-1863-06-19-saint-charles`, Hindman writes: "For further particulars of the heroic conduct of this officer and of Captains Dunnington and Williams, with the officers and men under them, I refer to the detailed report of the engagement heretofore forwarded through the headquarters of the Western Department."

- **Author not named.** He does not name the author of that report.
- **Figures not in Dunnington.** The figures the dossier takes from Hindman ("manned by 79 men of the crews of the Maurepas and Pontchartrain", "Captain Williams' armed men, 35 in number") do not appear in Dunnington's report. The White River memo itself says Hindman "fills the gap left by Dunnington, who gives no count of Confederate personnel".
- **Consequence.** Reliance on Dunnington for those figures is contradicted, and their basis is unestablished; Williams's report was not read. Non-independence as a non-eyewitness still holds.

**Correction.**

- **Registry.** In `or13-hindman-cache-river-selections-v1`, replace "at Saint Charles he relies on and refers to Dunnington's and Williams's report" with: "at Saint Charles he refers for particulars to 'the detailed report of the engagement heretofore forwarded' without naming its author, and gives personnel figures (79 men of the crews, 35 armed men) that do not appear in Dunnington's report; their basis is unestablished (Williams's report was not read), and he is not treated as independent of the participants' reports". Make this change through a metadata-only `-v2`, with predecessor hash `41387fd1625d2649b6d733ff573015697c5f295bb96260313fee963405010b53`. Then repoint AR002 (11) and AR003 (12).
- **AR002 `open_questions`.** In the last entry, replace ", which refers to Dunnington's and Williams's report and is not independent of it." with ". Hindman was not present, refers for particulars to an unnamed 'detailed report of the engagement heretofore forwarded', and gives personnel figures not found in Dunnington's report, whose basis is unestablished; it is not an eyewitness account and is not independent corroboration."
- **White River memo.** Replace "Hindman was not present; he refers to Dunnington's and Williams's report and is not independent of it." with "Hindman was not present. He refers for particulars to an unnamed earlier detailed report, and his personnel figures do not appear in Dunnington's report, so their basis is unestablished; he is not an eyewitness and is not counted as independent corroboration."

### TM-R4: memo text and record counts predate the merge deduplication

**Problem.** `docs/sources.md` correctly says the pass adds 46 records, and that the Volume VIII and Britton volume I parents were deduplicated. The memos, however, total 50 records and describe those parents as newly pinned, with a deduplication still "to come".

**Correction.**

- **Pea Ridge memo.**
  - Replace "was newly pinned with catalog metadata and full OCR." with "is the parent already registered by the 1861 West pass (`or8-illinois-ocr-v1`, catalog `ia-or8-illinois-metadata-v1`); this pass's byte-identical registration was deduplicated to it at merge."
  - Delete "A parallel pass may register the same volume; the primary will deduplicate."
  - Replace "The pass adds **6 source records**:" and its list with "The pass adds **4 source records**: one NPS HTML/text pair; two OR selections (Curtis, Van Dorn)."
- **Boston Mountains memo.**
  - In the Britton paragraph, replace "was newly pinned with catalog metadata and full OCR." with "is the parent already registered by the 1861 Missouri pass (`britton-border-1-ocr-v1`); this pass's byte-identical registration was deduplicated to it at merge."
  - Replace "The pass adds **25 source records**:" with "The pass adds **23 source records**:".
  - Replace the bullet "Britton volume I catalog metadata, full OCR and one selection;" with "one Britton volume I selection;".
  - The group sentence is covered by TM-R1.

### TM-R5: MO016's Salomon figure of about 150 is a September 29 detachment, not a phase of the frozen day

**Evidence.** Salomon (`salomon-1862-10-01`): "On the 29th ultimo I sent scouting parties … The scouting party to Newtonia was commanded by Colonel Lynde, and consisted of the Ninth Kansas Volunteer Cavalry (about 150 men) and two mountain howitzers." No inspected passage gives the Union strength engaged on September 30.

- **Value.** Scoping error: the MO016 `reported-force-scope` value omits the date.
- **Rationale.** Scoping error: the rationale calls the figures "all for different phases of the day".
- **Memo.** It lists "Salomon's 150-man scouting party" among the Newtonia figures without a date.

**Correction.**

- **MO016 `reported-force-scope` value.** Replace "Salomon says his scouting party to Newtonia was the Ninth Kansas Cavalry (about 150) with two howitzers, that he left some 400 Indians and two guns with the train," with "Salomon says his September 29 scouting party to Newtonia was the Ninth Kansas Cavalry (about 150) with two howitzers, that on the 30th he left some 400 Indians and two guns with the train,".
- **Rationale.** Replace "A detachment count and each side's estimate of the other, all for different phases of the day;" with "A September 29 detachment count, a September 30 train guard and each side's estimate of the other; no inspected passage gives the Union strength engaged on September 30;".
- **Boston Mountains memo.** Replace "Newtonia: Salomon's 150-man scouting party and prisoners' 7,000;" with "Newtonia: Salomon's 150-man scouting party of September 29 and prisoners' 7,000;".

### TM-R6: MO017's rationale says Wickersham's figures "match" Barstow's morning skirmish, but the enemy counts differ

**Evidence.**

- Wickersham: "Our loss was 2 killed and 2 wounded. Enemy's loss was 8 killed."
- Barstow's morning skirmish: "killing 9 of their men and several horses. My loss was 2 men killed, 2 wounded".

**Correction.** In the MO017 `casualty-records` rationale, replace "Wickersham's figures match Barstow's morning skirmish, not his totals;" with "Wickersham's Union loss (2 killed, 2 wounded) matches Barstow's morning-skirmish loss, not his day totals, while Wickersham's 8 enemy killed differs from Barstow's 9 in that skirmish and 34 for the day;". The memo's wording ("Wickersham's 2 killed and 2 wounded match Barstow's morning skirmish") is already accurate.

## Advisories

These are optional and do not block the pass.

- **TM-A1 (NM002, completeness).**
  - **Slough's enemy-loss estimate.** Slough's March 29 report gives an enemy-loss estimate that the `casualty-records` claim omits: "The enemy's loss is in killed from 40 to 60 and wounded probably over 100. In addition we took some 25 prisoners". Consider adding it alongside the synopsis's "at least 100 … at least 150".
  - **Unattributed total line.** The OR IX OCR has the line "27 killed j 63 wounded. Total, 90." immediately after Chivington's No. 3 report, outside the selected range; the registry inspection note records this. Its attribution is unclear. Consider listing it as an unattributed printed figure in the open questions, not as evidence.
- **TM-A2 (OK004).** The No. 5 return's unit aggregates can be read as 37 (1st Cherokee), 4 (2d Creek) and 22 (Howell's battery). These sum to 63 (a computation), which matches the final "63" in the total line. The component columns remain garbled. Consider recording the readable aggregate as a compiled-return observation distinct from Cooper's 6 killed and about 30 wounded and from the frozen CS 150, rather than calling the whole total line unreadable.
- **TM-A3 (MO015, timing).** The `march-horses-and-ammunition` rationale sets two statements against each other that refer to different times:
  - Foster: Cockrell said, after the fight, that the Confederates were "completely out of ammunition".
  - Britton: the forces "fighting Major Foster were fairly well supplied", from captures at Independence.

  Consider saying this in the rationale ("possibly different times: supply on entering the fight versus exhaustion at its end"), whether or not the claim stays `disputed`.
- **TM-A4 (NM001).**
  - **Revised Valverde figures.** Canby's February 22 estimate carries a footnote in the OCR ("But see revised statement on p. 493"), which links it to the compiled return. This is worth noting in the casualty rationale.
  - **When the brigade was poorly equipped.** Sibley's "poorly armed, thinly clad … almost destitute of blankets" describes the brigade at Fort Bliss in mid-January 1862. The value's "had reached the area" could say "at Fort Bliss in mid-January".
- **TM-A5 (AR001).** Curtis writes "in conformitv with the orders of the general of the 22d ot February". "Halleck's orders" is an inference from the addressee (Halleck's AAG), not the text. Consider "the department commander's orders of February 22".
- **TM-A6 (MO014).**
  - **Stone wall.** Buel also reports the camp companies falling back to "a stone wall running parallel with the south side of the camp". This shows that the fence is not only Britton's account, although Britton depends on the OR.
  - **Herington's detachment.** Buel's Herington detachment of 65 men differs from Britton's forty. Both could be noted.
- **TM-A7 (MO015, MO016).** The frozen numeric bounds (MO015 US 800/800; MO016 US 1,500/1,500) are named in the memo but not cited as `cwsac_forces` cells in the dossiers. MO014 and MO017 do cite theirs. Adding them would make the four records consistent.
- **TM-A8 (Boston Mountains memo).** "The frozen CS 150 equals the figure Blunt attributes to Confederate wounded" is ambiguous. Blunt reports that Confederate wounded found in houses gave their loss as 150 killed and wounded. The OK004 dossier value states this correctly; the memo could match it.

## Items checked without findings

- **Opening strengths and figures.**
  - Opening-strength nulls are present in all 11 records.
  - No figure is adopted. Nominal, present, engaged and estimated bases are kept apart, including Canby's 3,810 "aggregate present" and Sibley's 1,500 and 1,750 engaged.
- **Frozen and live values.**
  - The NM001 live force field reverses its own description (US 2,500 and CS 3,000, against Sibley's 2,500 and Canby's more than 3,000), and this is flagged.
  - Rank discrepancies are recorded without replacing the frozen ranks: Canby, Chivington's "Major General", Curtis, McNeil, Cooper, Hovey and Hindman.
- **Computations.** These are labelled as computations and are correct: Britton's Lone Jack components (2+51+13+144+1+43 = 254), Hovey's 6+57 = 63, and Scurry's 24+1+8 = 33 against his March 30 figure of 33.
- **Glorieta.**
  - The March 26 and 28 losses are kept separate.
  - The 80 against about 60 wagon dispute is kept, and the train effect is distinguished from the tactical result.
- **Command roles.**
  - The Green hand-off is reported with both of Sibley's timings.
  - Canby's statement that Roberts commanded until 2.30 is recorded.
  - Cooper's illness and Buster's command at OK004 are recorded.
  - At Independence, Britton's internal inconsistency over Thompson and Hays is recorded.
  - At Clark's Mill, Burbridge/Greene against Wickersham's "General Green" is recorded.
- **Kirksville.** Executions are kept apart from battle losses, and the frozen interval through August 9 is noted, including its possible bearing on US 88.
- **Section dates.** They are correct for every selection. The Curtis dispatch section is null because it contains several dates and Confederate letters. Returns are null. Foster's report is dated May 1, 1863 and flagged as more than eight months after the action. Hindman's is dated 1863-06-19.
- **Editions.** They are recorded from the OCR title pages: OR IX 1883, OR XIII 1885, OR VIII "1 883", and Britton volume I as the second edition, revised, with imprint "]89i" and copyright 1890. They do not substitute the 1880 catalog series date.
