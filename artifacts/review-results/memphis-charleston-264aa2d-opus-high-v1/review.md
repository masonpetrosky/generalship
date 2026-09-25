# Separate review: Operations on the Memphis & Charleston Railroad (TN022, Collierville)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. Fresh-context subagent. The author's conversation was not an input.
- **Date:** 2026-09-25
- **Prepared commit reviewed:** `264aa2d675e3533e1c2c581eda914ccabf7111cb`. **Previous commit:** `e0fa3588df0ac462d12a0f25e022b77bd00dd65f`. **Bundle/worktree HEAD:** `216d15ec2c0bc3782f3564c65aca318bfef7a6b9`.
- **Assignment:** `assignment.md`, sha256 `491d94ff7dbf729ec541bf9e88a65038d60627b143b01cb7854b337a3f4ce3aa`. **Input manifest:** `inputs.json`, sha256 `3d66aef428f760cb1999353ad41b4592af1e833ca93723992d59ec164669037e`. Both match.
- **Outcome: corrections required.** Required findings: MC-01 to MC-05. Non-blocking notes: N1 to N5.

This is an AI review, a separate analysis. It is not human historical adjudication, independent corroboration or feature admission. I worked offline and did no new research. I opened no other source families, spawned no agents and wrote only this file.

## What I inspected

- **Input hashes.** All 30 bound paths match `git show 264aa2d:<path>`. Every one is byte-identical in the worktree, so no bound path differs.
- **Dossier.** I read `data/evidence/TN022.json` in full: 9 claims, 41 citation occurrences and 1 null unknown (`opening-personnel-unknown`), covering 7 dimensions. I checked every citation against its source for entailment, attribution, locator, phase and status.
- **Memo, sources and docs.** I read the memo in full, the four new `sources.json` records, and the diffs to README, roadmap, methodology, sources.md, cli.py, the tests and the generated artifacts.
- **Frozen rows.** I read `cwsac_battles.csv` (1 row), `cwsac_forces.csv` (2 rows: US 850/850/cas 60; Confederate 2500/2500/cas 95) and `cwsac_commanders.csv` (2 rows: Hatch, Colonel; Chalmers, Brigadier General). The cited `forces_text`, `results_text`, `casualties_text` and `rank` cells match exactly.
- **Text derivatives, replayed independently:**
  - **NPS.** Parsing the HTML with HTMLParser and taking the span from "Return to Results" up to "Experience More" reproduces `nps-tn022.txt` exactly.
  - **Hatch and Chalmers selections.** Collapsing whitespace over each recorded half-open range of the parent reproduces every section exactly (Hatch: 6 sections; Chalmers: 3). Section order and the editorial `transcription-note` are also correct.
  - **Parent.** `or31-1-illinois-ocr-v1` is unchanged (`646c2e92…4e7d`, no diff since e0fa358).
- **Page markers in the parent.**
  - p.243: the header is at char 846428, before Hurlbut's No. 1 and outside the selection.
  - p.244: in the noon dispatch, after "badly whipped by 3 o'clock."
  - p.245: after "40 miles east."
  - p.246: read as "24G", after "and have found".
  - p.247: read as "^47" at char ~860203, *before* the Chalmers range begins at 860591, so the marker falls outside the selection.
  - p.248: after "the two regi-".
  - p.249: after "having heard".
  - p.250: begins immediately after "Grand total 95".

  Every dossier locator matches this marker map. No locator relies on a missed or misread header, and I found no missing header between consecutive pages.
- **Mechanical checks at the prepared commit:**
  - **Dossier coverage.** 117/127 cohort dossiers, 10 without, and 31/36 complete campaign groups by presence (previously 116, 11 and 30/36).
  - **Source registry.** 541 records / 522 paths (previously 537/518). All 537 older records are unchanged.
  - **Byte identity.** All 200 older top-level and `history/` evidence files are byte-identical. So are the cohort, both Shiloh admission proposals, `admission-check.json`, `baseline.json` and `battles.json`.
  - **Admission and baseline.** Zero promoted rows. The baseline has 23 battles in 13 groups, with Brier 0.2768816348133779 against 0.25 for equal odds.
  - **Next group.** The earliest incomplete group is Averell's Raid [November 1863], WV012 (1863-11-06). This matches the memo.
  - **Receipt.** Every input, source and output hash matches.
  - **Packet.** `artifacts/research/TN022.md` has 3 JSON blocks. They equal the `battles.json` TN022 row, the dossier and `sources.json`.
- **`make check`.** Run offline: 82 tests pass, then `generalship check` exits 0 with `artifacts_written: false`. I ran no build or packet commands.

**Not inspected:** print, facsimiles, maps, subordinate reports, or parent OCR beyond the page-marker and range-boundary context.

## Required corrections

After making them, update the citation count everywhere it is stated: the memo, README, roadmap, sources.md if applicable, the `cli.py` report string, and the regenerated pilot report. MC-02 and MC-05 each add one citation, so the count goes from **41 to 43**; claims and unknowns are unchanged. Then regenerate and update the TN022 packet.

**MC-01: `stockade-and-ridge` turns Chalmers's pre-attack expectation into an observation.**
- **Problem.** The value says "Chalmers says he found the enemy behind intrenchments". The passage (p.247) reads: "feeling able to encounter, even behind intrenchments, the two regi- [248] ments of cavalry, I changed my plan". That is a conditional judgment made before the attack, not a report of what he found.
- **Second problem.** "later crossed back over Coldwater" is attributed to Chalmers, but no citation supports it. The boundary note also places the Coldwater stand outside the record.
- **Replacement value:** "Hatch says he ordered Trafton to throw the Collierville force into the stockade and that the First Illinois Light Artillery came into position at a gallop on a ridge east of the town. Before attacking, Chalmers says he felt able to encounter the two supposed cavalry regiments \"even behind intrenchments\"; this states his expectation, not what he found. After the engagement, at the Coldwater (outside this record), Hatch says the Confederates had a position almost impregnable."
- **Citation change.** Replace the quote `"even behind intrenchments,"` with `"feeling able to encounter, even behind intrenchments, the two regi-"`. Keep the same source, section and p.247 inferred locator. The new quote is an exact substring that appears once.
- **Rationale.** Append: "Chalmers's intrenchment phrase is a conditional pre-attack judgment."

**MC-02: `command-roles` states an uncited Second Iowa order.**
- **Problem.** "brought the Second Iowa up dismounted" has no supporting quote.
- **Replacement value (first sentence):** "Hatch says he ordered Trafton to put the Collierville force into the stockade, ordered the Second Iowa to move rapidly toward Collierville, and had ordered the Sixth Illinois to move behind the line and charge when a Confederate brigade charged the Union left and rear."
- **Citation to add:** `{"source_id": "or31-1-hatch-collierville-selections-v1", "section": "hatch-1863-11-09", "locator": "p.245 (OCR page markers; not checked against print)", "quote": "also ordered the Second Iowa to move rapidly toward Col- lierville"}`

**MC-03: `casualty-records` drops a category from Chalmers's Quinn's Mill figures.**
- **Problem.** The source says "killing 2, wounding 4 too severely to move, and capturing a lieutenant and 26 men" (p.248). The value omits the 4 wounded, even though the rationale requires categories to be preserved.
- **Replacement (last sentence of the value):** "He separately says that at the Quinn's Mill picket his men killed 2, wounded 4 too severely to move and captured a lieutenant and 26 men."
- **Citation change.** Replace the quote `"capturing a lieutenant and 26 men."` with `"killing 2, wounding 4 too severely to move, and capturing a lieutenant and 26 men."`. Keep the same source, section and p.248 locator.

**MC-04: The inspection record contradicts itself.**
- **The conflict.**
  - The memo says "No maps, McCulloch's, Slemons's or Richardson's reports, or print pages were inspected."
  - The `or31-1-chalmers-collierville-selections-v1` record says "McCulloch's and Slemons's reports were read in part but not selected."
  - The Hatch record says Hurlbut's No. 1 and Trafton's No. 3 were "read in full but not selected", yet the dossier lists them as "deferred" without saying so.
- **What to do.** The primary must confirm which statement is true from its own inspection. The replacements below follow the more specific registry records.
- **Memo replacement:** "Hurlbut's and Trafton's reports were read in full, and McCulloch's and Slemons's in part, but none was selected or cited. No maps, Richardson's report or print pages were inspected."
- **First `open_questions` entry, replacement:** "Hurlbut's and Trafton's reports (read in full) and McCulloch's and Slemons's reports (read in part) were not selected or cited; Richardson's report was not inspected. Their evidence remains deferred."
- **If the registry is wrong instead,** correct its `inspection` strings before review closure. The records are unreviewed and in the same commit.

**MC-05: `scouts-and-surprise` overgeneralizes the scouts' report.**
- **Problem.** The value says "one regiment at each post". Chalmers names only two places: "there was only one regiment of cavalry at Germantown and one at Collierville". No citation in this claim supports the regiment count.
- **Replacement (first clause of the value):** "Chalmers says his scouts reported that the enemy was evacuating the railroad, with only one cavalry regiment at Germantown and one at Collierville, and that citizens confirmed it; …" The rest of the value is unchanged.
- **Citation to add:** `{"source_id": "or31-1-chalmers-collierville-selections-v1", "section": "chalmers-1863-11-16", "locator": "p.247 (inferred: the preceding running head reads \"^47\" in OCR, before the p.248 header; not checked against print)", "quote": "there was only one regiment of cavalry at Germantown and one at Collierville"}`

## Checks that passed (no change needed)

- **Scope.** The morning Quinn's Mill picket capture, the Coldwater stand, the November 4 pursuit and the other 1863 Collierville actions are excluded or marked unestablished. No picket losses are added to the casualty comparison.
- **Force comparison.** Hatch's "about 850 men" (p.246) matches the frozen US bound, and the bounds are left unvalidated. No inspected source gives a Confederate count, and none is invented. The live NPS field reads zero. Opening strength stays an explicit null unknown.
- **Casualty comparison.**
  - Hatch's "will not exceed 60" is labelled an upper estimate.
  - Chalmers's 6 killed / 63 wounded / 26 prisoners (the OCR reads "misoners" and is reported as such) sums to 95. This agrees with the garbled return's "Grand total 95" and the frozen and live CS figure of 95. No canonical reconciliation is claimed.
- **Chalmers's change of plan and withdrawal.** Both are attributed to Chalmers with passages that entail them.
- **Attribution and labels.**
  - Each commander family has its own independence group and an "interested accounts" label.
  - The OR volume is described as a shared container, not an additional witness.
  - NPS and the Arnold tables are treated as one family.
  - No commander gets automatic or additive credit, and no causal effect, probability or morale/readiness score appears.
- **Phase tags.** Both outcome claims are `post_outcome`; the other claims are `unresolved`.
- **OCR artefacts.** All are retained verbatim ("I, was", "W e", "misoners", "24G", "^47"); none is silently corrected.

## Non-blocking notes (no required change)

- **N1: section label.** Section id `hatch-1863-11-03-noon` labels a dispatch whose text postdates "3 o'clock". The claim text rightly says "afternoon", and the id is only a label.
- **N2: disputed force composition.** Chalmers says the enemy had "infantry, artillery, and cavalry" at the first fire. Hatch's report lists only cavalry and artillery at Collierville, and his 8.30 p.m. dispatch mentions infantry "coming up". The dispute is visible in `reported-force-scope` and could be named in its rationale.
- **N3: uncited phrase.** In `recorded-result`, "and in full retreat" sits past the p.244 header and is not in the cited quote. Optional quote: "full retreat, and my sabers are charging them." (p.244).
- **N4: overlapping loss figures.** Chalmers's separate "9 men and 15 horses killed" at Quinn's Mill includes the "morning and evening" skirmishes. It is unknown whether Hatch's 60 includes the picket losses. The current rationale already bars adding or reconciling these figures.
- **N5: page markers outside the selections.** The p.243 and p.247 markers lie outside the selection text, so a reader of the selection alone cannot see them. The p.247 locator says so. The p.243 locators say "OCR page markers" without noting that the marker is outside the selection. Both are accurate against the parent.
