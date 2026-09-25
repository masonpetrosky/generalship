# Mine Run Campaign (VA044): separate source review

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), `high` reasoning effort, fresh-context `evidence-reviewer` subagent. This is an AI review. It is not human historical adjudication, independent corroboration or feature admission.
- **Date:** 2026-09-25.
- **Commits:** prepared `aa9d89a677415b4474ee3790dd7ed7f2aeb56530`, compared against `535f423`. The bundle and worktree are at `864760a05cbba2bb37cd69d87bf7d43776d83a65`.
- **Inputs:** `assignment.md` sha256 `520268a4…a4b4ac` and `inputs.json` sha256 `e26fcbb7…c51b3` both matched. All 30 bound paths match their `inputs.json` hashes at the prepared commit (checked with `git show`). Three paths differ in the worktree: `README.md`, `docs/roadmap.md` and `artifacts/receipt.json`. I read the diffs. They change only the Knoxville review text, the TN023/TN025/TN026 hashes and the Knoxville history-archive entries, which are out of scope. No bound Mine Run input changed.
- **Outcome:** **corrections required** (MR-R1 to MR-R4). Advisories MR-A1 to MR-A4 require no change.

## Scope actually inspected

- **Dossier:** `data/evidence/VA044.json` in full: 9 claims, 72 citation occurrences, 1 null unknown (`opening-personnel-unknown`), all seven dimensions, the boundary note and the open questions.
- **Documents:** the memo `docs/research/mine-run-first-pass-v1.md`, the Mine Run parts of the README/roadmap/sources docs, the evidence contract and the four new records in `data/sources.json`.
- **Frozen rows:** the VA044 rows in `cwsac_battles.csv` (1 row), `cwsac_forces.csv` (2 rows) and `cwsac_commanders.csv` (2 rows).
- **Source text:** the whole NPS text and all Humphreys and Lee sections, read in full. For boundary context only, I read the parent OCR around each selection boundary: the p.48 head before Chapter III, the start of Chapter IV, and the No. 99 abstract ahead of No. 100 and the No. 101 start after it.
- **Replays:** I replayed all three text derivatives from their pinned parents.
  - NPS: HTMLParser, then the Return to Results … Experience More slice. Matches byte-for-byte.
  - Both selections: every recorded character range, after whitespace collapse, equals its section.
  - Hashes: `humphreys-ocr-v2` (`56072cc1…`) and `or29-1-illinois-ocr-v1` (`bf4c70d5…`) are unchanged, and neither raw file nor metadata record differs from `535f423`.
- **Quote checks:** a script checked every quote. All 72 occur in the cited CSV cell or the one named section. I then checked entailment and locators by hand against the page markers.
- **Mechanical checks at `aa9d89a`:**
  - Coverage: 124/127 dossiers. The three without are TN027, TN028 and TN029. 35/36 campaign groups are complete.
  - Sources: 568 records / 548 paths, against 564/544 before. No old record changed.
  - Unchanged from `535f423`: all 123 older dossiers, all 92 history files, all older raw files, the cohort, both admission proposals, `admission-check.json`, `baseline.json` and `battles.json`.
  - Baseline: `promoted_rows` 0; 23 battles / 13 campaigns; Brier 0.2768816348133779 against 0.25.
  - Receipt: all 230 hash entries match.
  - Packet `VA044.md`: its three JSON blocks equal the battles.json record, the dossier and the whole registry.
  - Next group: independently confirmed as Operations about Dandridge (earliest start 1863-12-29), TN027/TN028/TN029.
- **`make check`:** run offline at the worktree and on a `git archive` export of `aa9d89a`. Both runs: 82 tests OK, `admission_promoted_rows: 0`, `artifacts_written: false`.
- **Not done:** no build or packet commands, no `generalship.cli` calls, no network, no new families.

## Checks that passed

- **Locators:** the page-marker map holds. The misread heads are "SO" (p.50), "5 1" (p.51), "$6" (p.56), "6l" (p.61), "6?" (p.67) and "JO" (p.70). No p.60 head appears. The three "p.59 or p.60" citations fall between the p.59 and p.61 heads, and every other Humphreys and Lee locator sits under the correct marker. Lee's selection runs over pp.823–830, and there are 8 telegrams (one to Davis, seven to Cooper). OCR readings are reported, not silently corrected, for example "Eapidan", "MINE BUN" and "Afras".
- **Disputes preserved:**
  - Rosser's raid: Lee's December 2 letter gives 18 wagons, 280 mules and 150 prisoners; Humphreys, citing Rosser, gives 8 wagons, 7 ambulances, 280 mules and 95 prisoners.
  - Johnson's loss: 498 against 545.
  - Payne's Farm: the Lee, Humphreys and NPS accounts are kept separate.
  - Frozen against live figures: casualties and the result text.
- **Ranks:** the live "Major General" rank for Lee is not adopted, and the frozen ranks are cited correctly.
- **Source labels:** Humphreys's "Chief of Staff, Army of the Potomac, 1863-64" is present in the parent's publisher list.
- **Strength:** no strength figure is adopted against the frozen bounds, and the unknown claim carries no citation.
- **Attribution and invented values:** no additive or automatic commander credit, and no invented scores or probabilities.

## Required corrections

**MR-R1: terrain claim `forest-rapidan-and-mine-run-line`, and the memo's Tags bullet. The "not inherited" statement is stated too categorically.**

The pieces that are right: Lee (p.829) and Humphreys (pp.63, 65) describe the Mine Run position as intrenched and strengthened after the night-of-November-27 withdrawal. Phase `unresolved` is right.

The problem is the rationale's flat "the works are not inherited". It omits evidence already in the inspected sources:

- The frozen description and NPS both say Lee "withdrew to prepared field fortifications along Mine Run".
- Humphreys p.49 describes a pre-movement intrenched right-flank line running to "the vicinity of Bartlett's Mill on Mine Run".
- Humphreys p.67 says the intrenchments "had been extended to Bartlett's Mill, and now connected with those of the Rapidan".

**Replace the rationale with:**

> Natural ground plus field works. Lee and Humphreys describe the Mine Run position as intrenched and strengthened after the withdrawal on the night of November 27, within the frozen interval. The frozen description and NPS call them 'prepared field fortifications', and Humphreys describes an earlier intrenched right-flank line reaching the vicinity of Bartlett's Mill on Mine Run, which the later works joined. How much of the defended line existed before November 27 is unresolved; the works are tagged neither inherited nor commander-created, and no commander-created credit is assigned. No map verification.

**Append to the value:**

> Humphreys also says Lee had earlier constructed an intrenched line to protect his right flank from the Rapidan to the vicinity of Bartlett's Mill on Mine Run, and that the Mine Run intrenchments were later extended to Bartlett's Mill and connected with those of the Rapidan; the frozen description and NPS say Lee withdrew after dark to prepared field fortifications along Mine Run.

**Add these citations:**

- `arnold-cwsac-battles` {battle: VA044}, column `description`: "After dark, Lee withdrew to prepared field fortifications along Mine Run."
- `nps-va044-v1`, locator "Description", same quote.
- `humphreys-mine-run-selections-v1`, section `plan-and-crossing`, locator "p.49 (inferred: precedes the p.50 running head read \"SO\"; the chapter opens after the parent's p.48 head; not checked against print)": "To protect his right flank, General Lee had constructed an intrenched line from a point on the river between Raccoon Ford and Morton's Ford to the vicinity of Bartlett's Mill on Mine Run."
- The same source, section `mine-run-and-withdrawal`, locator "p.67 (inferred from OCR page markers; the p.67 running head reads \"6?\"; not checked against print)": "As the enemy's intrenchments had been extended to Bartlett's Mill, and now connected with those of the Rapidan,"

**Replace the memo's Tags bullet with:**

> **Tags.** Lee and Humphreys describe the Mine Run works as built or strengthened after the November 27 withdrawal, but the frozen description and NPS call them prepared, and Humphreys describes an earlier right-flank line reaching Bartlett's Mill; their pre-interval extent is unresolved. They are tagged neither `inherited` nor commander-created. All claims stay `unresolved` or `post_outcome`.

**MR-R2: `command-roles`. Lee's credit is truncated to Johnson alone.**

The source sentence (p.828) reads: "The promptness with which this unexpected attack was met and repulsed reflects great credit upon General Johnson and the officers and men of his division." Two things are wrong in the dossier. The quote stops at "General Johnson", and the value's "Lee credits Johnson's promptness" makes the promptness Johnson's personally.

- **Replace the quote with the full sentence above.** It is verified present in `lee-1864-04-27`.
- **Replace the value sentence with:** "Lee says the promptness with which the unexpected attack was met and repulsed reflects great credit upon General Johnson and the officers and men of his division."
- **In the memo, replace** "Lee's credit to Johnson" **with** "Lee's credit to Johnson and his division's officers and men".

**MR-R3: `command-roles`. Humphreys's "paralyzed" judgment is attributed to French personally, and "three times Johnson's force" has no quote.**

Humphreys p.63 makes the Third Corps the subject of that judgment, and he qualifies it. The "three times" figure appears in the value but in none of the cited quotes.

**Replace the value clause** "that French halted at Morris's, remained on the defensive with three times Johnson's force, and in effect paralyzed the whole army" **with:**

> that the corps remained halted at Morris's because French held the contrary opinion; that with three times Johnson's force, and the Sixth Corps near at hand, French remained on the defensive; and that the Third Corps' remaining near Morris's and on the defensive all day in fact paralyzed the whole army so far as carrying out the plan was concerned

**Replace the citation** "in fact paralyzed the whole army," **with** "in fact paralyzed the whole army, so far as concerned its carrying out the plan of operations successfully." (p.63).

**Add these citations:**

- "the Third Corps remained substantially in the vicinity of Morris's all day, and on the de- fensive," (p.63).
- "With three times the force of Johnson," with the existing "p.59 or p.60 …" locator.

All three strings are verified in `robertsons-tavern-and-paynes-farm`.

**MR-R4: `reported-force-scope`, and memo lines 52–53. Keep the second arithmetic difference and the return date visible.**

The footnote's enlisted figures (4,297, 6,562 and 4,790) sum to 15,649, not the text's 15,650. The footnote also dates its figures to the November 20 return. The contract requires printed arithmetic discrepancies to remain visible.

**Replace the value sentence** beginning "His footnote's division figures…" **with:**

> His footnote gives Ewell's divisions present for duty equipped, per the Army of Northern Virginia return of 20 November 1863, as 404, 527 and 505 officers and 4,297, 6,562 and 4,790 enlisted men, which sum to 1,436 officers and 15,649 enlisted men (computations here from unverified OCR), against his text's 1,321 and 15,650.

**Replace** "Meade's best contemporary information put Lee's strength" **with** "Meade's best information at the time put Lee's strength during the October and November operations".

**Citation changes:**

- Add "according to the return of the Army of Northern Virginia of the 20th November, 1863," (p.57).
- Replace "it was but little less than that of the Army of the Potomac ;" with "during the operations of October and November, it was but little less than that of the Army of the Potomac ;" (p.70, same locator).

Both strings are verified. **Update the memo footnote sentence to match.**

## Advisories (no change required)

- **MR-A1: the p.55 page head is outside the selection.** It lies in the 35-character gap between `plan-and-crossing` and `robertsons-tavern-and-paynes-farm` (parent characters 89736–89771), where it is read correctly as "LEE MOVES AGAINST MEADE. 55". The p.55 locator for the Early quote is therefore correct, but it can be checked only in the parent. "Contiguous" in the memo and the record's inspection note is loose. A future metadata revision could say so.
- **MR-A2: stragglers and prisoners.** Humphreys assigns the 200 stragglers to Hill and the 300 to Early. From its placement, Lee's "about 500 prisoners" covers the operations generally. Do not equate the two.
- **MR-A3: Lee's two documents on Rosser's raid.** The April 27 report repeats 280 mules and 150 prisoners but gives no wagon count. Its agreement with the December 2 letter is same-family, not independent.
- **MR-A4: the unselected No. 99 abstract.** In the parent, its garbled columns appear to include "15,649" near the Second Army Corps total, consistent with the footnote sum in MR-R4. It is not selected or adopted, and it is not the basis of any correction here.

## Findings

MR-R1, MR-R2, MR-R3 and MR-R4 are required corrections; MR-A1 to MR-A4 are advisories. None of these corrections changes the 124/127 coverage count, frozen inputs, the baseline or feature admission.
