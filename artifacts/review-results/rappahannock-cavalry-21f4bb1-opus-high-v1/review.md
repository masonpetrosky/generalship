# Separate review: Cavalry Operations along the Rappahannock (VA029, Kelly's Ford)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, fresh-context subagent (evidence-reviewer role). This is a separate AI analysis. It is not human historical adjudication, independent corroboration or feature admission.
- **Date:** 2026-09-25
- **Commits:** prepared `21f4bb1cbca40f987b5b1ad0deb30fad764c4070` against previous `b884e79bd4c9628ad27b766859f12c32ed78ce87`; assignment bundle `3044e666dcbb198697fea7cad53ae4f469151b9c`. The bundle commit changes only `assignment.md` and `inputs.json`.
- **Assignment:** `assignment.md` sha256 `38fba6fbfe3b2871fe8dc4dc7f975f6f08638022296f9cf7b2e65351647e8daf`; `inputs.json` sha256 `cf91fde1208a1a1d12682be16e03f3c0f866fdf4e39cadeec01af204776b107e`. Both match the hashes I was given.
- **Input hashes:** I checked all 32 bound paths in the worktree and at `21f4bb1` via `git show`. **All 32 match; there are no mismatches.**
- **Outcome:** **corrections required.** Findings VA029-R1 to VA029-R4 are required; VA029-N1 to VA029-N3 are optional.

## Coverage I actually inspected

- **Guidance read:** AGENTS.md, `docs/evidence-contract.md`, the first-pass memo, and the prepared-commit diffs to README, methodology, roadmap, sources.md, `cli.py` and the test. I did not reread the whole README, methodology and roadmap beyond those diffs.
- **Dossier:** all 9 claims and all 60 citation occurrences in `data/evidence/VA029.json`, including the null unknown, 7 `unresolved` and 2 `post_outcome` phase tags, the boundary note and the open questions.
- **Frozen rows:** the frozen battle row, both force rows (all side bounds blank) and both commander rows (Averell and Fitz Lee, each "Brigadier General").
- **Source text:**
  - the NPS text in full, replayed from its HTML with the recorded transform;
  - both OR selections in full;
  - the parent OCR at every selection boundary: the p.47 report list, the Southworth ending, the Union casualty return and Browne's opening after Averell, Stuart's orders and R. E. Lee's indorsement before Fitz Lee, the recapitulation inclosure, Taylor's indorsement, and Curtis's p.65 report after the General Orders;
  - the page markers pp.47–65;
  - the catalog metadata fields: identifier, title, creator, date, publisher, volume, contributor, scandate and publicdate.
- **Registry and artifacts:** the six new registry records; the packet `artifacts/research/VA029.md` (3 JSON blocks); and `receipt.json`, `quality.json`, `evidence-checks.json`, `research-queue.json` and `pilot-report.md`.
- **Not inspected:** the whole volume; Stuart's and the regimental reports; the Union return and revised statement beyond the boundary glance; print or facsimiles; and maps.
- **Constraints kept:** no network access, no new sources, no agents, and no build or packet commands.

## Mechanical results (all pass)

- **Replays:** the NPS HTML-to-text replay is byte-exact. All six selection sections replay exactly from the recorded half-open character ranges in the parent, using split/join whitespace collapse. Parent sha256 is `8070600a…12513817`; both selection hashes match the registry.
- **Page locators:** I recomputed all 49 OR citation pages from the OCR page markers. **49/49 are correct.** Averell's report opens after the "47" header. Fitz Lee's report opens after the "60" header. The General Orders fall on p.64, before Curtis's p.65. Quotes between the "PT I 50" marker and the "51 52" header correctly carry "pp.50–51". Every quote occurs exactly once in its section.
- **Edition claims:** the OCR title reads "SERIES I— VOLUME XXV— … PART I— REPORTS. WASHINGTON: GOVERNMENT PRINTING OFFICE. 1889." The catalog gives date 1880, publisher "Washington : Govt. Print Office", volume `v.25:1`, contributor University of Illinois Urbana-Champaign, and scandate 2017. The registry's edition, imprint and archival claims are consistent with both.
- **Registry counts:** 379 records / 376 paths. The first 373 records are identical to the 373/370 at `b884e79`.
- **Preserved files:** `data/evidence/history`, cohort, both admission proposals, admission-check, baseline, battles and the three CSVs are byte-identical to `b884e79`. The only dossier change is the new `VA029.json`.
- **Coverage:** 77/127 dossiers, 50 without; 36 groups, 20 complete by presence. Ordering by earliest date, the next group is Grant's Operations Against Vicksburg [March–July 1863]: AR008, LA011, LA014, MS004–MS008, MS010 and MS011 without dossiers, plus MS009, which already has one.
- **Baseline:** 23 battles / 13 groups. Strength Brier 0.2768816348133779 versus equal odds 0.25. Promoted rows: 0.
- **Packet:** the assigned-record block equals the `battles.json` VA029 entry. The dossier block equals `VA029.json`, and the registry block equals `sources.json`.
- **Receipt:** all 138 input, 379 source and 7 output hashes in `receipt.json` match.
- **`make check`:** runs offline and exits 0; 82 tests OK. It wrote no files, and the worktree stayed clean.

## Substantive checks that pass

- **Force scopes** are kept apart and none is adopted:
  - frozen "Divisions (3,000 total)" and strength 3000, with blank side bounds;
  - live "0 total";
  - NPS 2,100 and about 800;
  - Averell's ordered 3,000, detached about 900, and marching about 2,100 (775 + 563 + 760 = 2,098, plus the battery);
  - Fitz Lee's "certainly not less than 3,000".
  - In the inspected passages Fitz Lee gives no count of his own brigade.
- **Withdrawal:** the dispute is correctly kept visible. NPS says mid-afternoon. Averell's 5.30 p.m. is a decision time, not a recrossing time. Fitz Lee says the enemy recrossed about 7.30 p.m. under close pursuit.
- **Casualties:** 179 = 99 + 80. Fitz Lee's 11 + 88 = 99 killed and wounded, and 11 + 88 + 34 = 133. The live US 99 / CS 80 split does equal Fitz Lee's CS killed-and-wounded figure and Averell's US killed/wounded/missing aggregate, with the sides reversed. It is correctly labeled as a computation and not adopted. The differing categories are stated.
- **Command:** Stuart's presence is not given to a frozen commander. The NPS "Major General Fitzhugh Lee" heading conflicts with the frozen "Brigadier General" and his signature "Brigadier- General , Commanding ." and is correctly left unadopted. No additive credit, causal effect, probability or morale score appears.
- **Other:** the "perpendicular"/"at right angles" correction is represented accurately. OCR readings in quotes ("ot", "Duffle", "rail- roads", "u at right angles.”") are kept as printed, not corrected. The phase tags are reasonable draft hypotheses with the replacement boundaries unset.

## Required corrections

### VA029-R1: Value clauses not supported by the cited words (six claims)

Each clause below has no support in its cited quote, although the supporting words are in the same section. Add or extend citations as follows. All quotes are verified exact and unique. Locator strings:

- **L47, L48, L49, L52, L60, L61, L62, L63:** "p.N (OCR page markers; not checked against print)"
- **L50–51:** "pp.50–51 (OCR p.51 header printed after that page's text; not checked against print)"

**`ford-wall-and-ground`**
- Clause "rapid current": replace the quote "was about 4 feet 5 inches deep." with "The stream has a very rapid current at the ford, and was about 4 feet 5 inches deep." (L48).
- Clause "in front of the first wood": replace the stone-wall quote with "in front of the first wood there is a deep, broad ditch, along which runs a heavy stone wall," (L50–51).
- Clause "impeded cavalry": add "which was impassable for cavalry except around the right flank and where it was broken down in the center, and this impeded my operations somewhat." (L52).

**`ammunition-and-horses`**
- Clause "unreliable fuses": add "the fuses were unreliable," (L50–51).
- Clause "many horses unfit after the winter": add "by the large number of horses unfit for duty by ex- posure to the severe winter," (section `fitz-lee-1863-03-23`, L61).

**`warning-and-reports`**
- Replace the telegram quote with "My first intimation of their approach was in a telegram received at 11 a. m. on 16th, from headquarters Army of Northern Virginia." (L60).
- Replace the 7.30 quote with "the first intimation I received from that point was at 7.30 a. m., to the effect that they had succeeded in crossing," (L61).
- Add "Accompanying the orders were several reports" (L47).
- Add "I requested that a regiment of cavalry be sent to Catlett’s Station," (L47).

**`rout-or-destroy`**
- Clauses "cross the Rappahannock … near Culpeper Court-House": add "for the purpose of crossing the Rappahannock River and attack- in g the cavalry forces of the enemy, reported to be in the vicinity of Culpeper Court-House," (L47).

**`command-roles`**
- Clause "two of his regiments wavered": add "I must confess that two regiments wavered," (L50–51).
- Clause "Duffié's charge": add "Had it been possible to reach the enemy’s flank when Duffie charged" (L49).
- Clause "rather than attack the entrenched position": add "it was necessary to advance my cavalry upon their intrenched positions, to make a direct and desperate attack, or to withdraw across the river." (L50–51).
- Clause "credits Stuart": add "assisted immensely by his sagacious counsels, large expe- rience," (L63).
- Clause "Munford … at a court-martial": add "Col. T. T. Munford, of tbe Second, I regret to say, was president of a court-martial in Cul- peper Court-House," (L62).

**`withdrawal-account`**
- Clause "was driven back": add "At that time my artillery arrived, and they were driven back," (L61).

### VA029-R2: Averell's "over 200" is a conditional extrapolation

In `casualty-records`, the value says Averell "estimates Confederate killed and wounded at over 200". That drops his stated basis, his condition and his own caveat.

Replace "he estimates Confederate killed and wounded at over 200 and prisoners at 47." with:

> "he counts 2 officers and 68 men killed and seriously wounded left on the field and, if twice as many slightly wounded escaped, reckons Confederate killed and wounded at over 200, which he says may be an overestimate; he puts prisoners at 47, with 15 more reported but unaccounted for."

Add these citations (all section `averell-1863-03-20`, L52):
- "the enemy must have left 2 officers and 68 men killed and seriously wounded on the field."
- "If twice as many slightly wounded escaped,"
- "I think the above may be an overestimate,"
- extend the prisoner quote to "The enemy’s loss in prisoners was 47 ; 15 more are reported"

### VA029-R3: Fitz Lee's recapitulation inclosure shows different figures, and the records disagree on whether it was read

The Fitz Lee registry record says "The recapitulation table … [was] read but not selected." The memo, however, says "both compiled casualty tables … were not inspected", and the dossier lists the table as deferred.

The parent OCR of that inclosure (between the report and the March 26 letter) prints the men's figures under "Killed. Wounded.! Taken prisoners" as "11 77 33 133". Those do not sum to 133 and differ from the narrative's 88 wounded and 34 prisoners. The horse figures (71/87/12/170) agree with the narrative. The table layout is garbled and was not checked against print. The discrepancy must stay visible without being adopted.

1. **`casualty-records` rationale:** append the following. No citation is needed; it is an uncited open reading.
   > "The OCR of Fitz Lee's recapitulation inclosure (parent or25-1-illinois-ocr-v1, not selected) prints the men's columns as 11, 77, 33 and 133, which do not sum to 133 and differ from the report's 88 wounded and 34 prisoners; the table layout was not checked against print, so no reading is adopted."
2. **Open question 1:** replace "and Fitz Lee's recapitulation table remain deferred." with:
   > "remain deferred; Fitz Lee's recapitulation inclosure was read in OCR but not selected, and its garbled figures are unreconciled with his report."
3. **Memo:** replace "Stuart's report, the Union regimental reports, both compiled casualty tables and the revised Union statement were not inspected." with:
   > "Stuart's report, the Union regimental reports, the compiled Union return and its revised statement were not inspected; Fitz Lee's recapitulation inclosure was read in OCR but not selected, and its figures (11, 77, 33, 133) are not reconciled with his report's 11/88/34/133."

### VA029-R4: The morning clocks conflict but are not recorded

`warning-and-reports` cites Fitz Lee's 7.30 a.m. news of the crossing. Averell's own timetable puts the head of his column at the ford at 8 a.m., with half an hour of failed attempts before the crossing. Fitz Lee dates the attack on his picket to about 5 a.m.

Append to the rationale:

> "Local clocks conflict and are not synchronized: Fitz Lee says the attack on his picket commenced about 5 a.m. and news of the crossing reached him at 7.30 a.m., while Averell says his column reached the ford at 8 a.m. and crossed after half an hour of attempts. Neither timetable is adopted."

Add these citations:
- "which commenced about 5 a. m." (`fitz-lee-1863-03-23`, L61)
- "The head of my column arrived at the ford at 8 a. m." (`averell-1863-03-20`, L48)
- "After half an hour had passed in endeavors to cross," (`averell-1863-03-20`, L48)

Changing the status to `disputed` is optional, because every value clause is attributed.

## Optional observations (no correction required)

- **VA029-N1:** In `reported-force-scope`, the rationale "not a stated two-sided total" could be misread as saying the frozen 3,000 is not two-sided. Clearer wording: "The frozen 3,000 numerically equals the ordered and Confederate-estimated Union figures; the frozen field gives no side split and its population basis is not established."
- **VA029-N2:** The values spell "Duffié", while the OCR prints "Duffie"/"Duffle". This is acceptable as a name in the author's prose, since the quotes keep the OCR spelling.
- **VA029-N3:** The registry's statement that the catalog date 1880 "describes the series" is an interpretation, not a catalog statement. It is harmless, because 1880 is correctly not substituted for the 1889 imprint.

## Limits

- After these corrections the citation count will exceed 60. The primary should recount and regenerate the packet and receipt.
- None of these findings changes the null opening-strength unknown, any disputed status, frozen inputs, the baseline or admission.
- I did not assess whether the OR reports are historically accurate. Averell and Fitz Lee are interested participants, and their shared OR container is not corroboration.
