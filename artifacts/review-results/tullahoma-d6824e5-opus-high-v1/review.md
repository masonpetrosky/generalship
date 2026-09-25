# Separate review: Tullahoma or Middle Tennessee Campaign (TN017, Hoover's Gap)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This is a fresh-context subagent working from the assignment and the repository only.
- **Date:** 2026-09-25. Worked offline, with no new research, no extra source families and no agents.
- **Commits:** prepared `d6824e51b354adffce6d255775a1e6888cbfdab0`, previous `d3eddc0dae19ec6cfb5241a2b40114b2c971f073`, and assignment bundle `8546a8f6a53f671b2a91863e48b746dd1f03a777` (the worktree HEAD). `git diff d6824e5 8546a8f` touches only the two bundle files.
- **Bundle hashes:** assignment.md `fb5b486a69a37c0db511756f3903e61d62e4e86dd2877e3e5b2da44140e8007f` and inputs.json `4a5def30aa6b546d4ce1d207394de4ebd69de3d1e0ab224158367c79258c1430`. Both match. All 32 bound inputs match both in the worktree and at `d6824e5`, with **0 mismatches**.
- **Outcome: corrections required** (R1–R7). Advisories A1–A3 are optional.

This AI review is a separate analysis. It is not human historical adjudication, independent corroboration or feature admission.

## Scope actually inspected

- **Dossier:** `data/evidence/TN017.json` in full: 9 claims, 41 citation occurrences, 1 null unknown and 7 dimensions.
  - I checked every citation for exact presence, section, locator and entailment: 30 citations to the selections, 6 to NPS and 5 to frozen cells.
  - I also read the memo, the boundary note and the open questions.
- **Frozen rows:** the TN017 row in `cwsac_battles.csv` (dates 1863-06-24 to 06-26, `forces_text`, `results_text`, `casualties_text` "Unknown"). I also read both `cwsac_forces.csv` rows, which have no counts, and both `cwsac_commanders.csv` rows (Thomas and Stewart, both Major General). The research queue lists `missing_numeric_strength`.
- **Source text and replays:**
  - I read the NPS text in full and replayed it from the HTML. The replay is byte-identical.
  - I read the Cist selection (title/preface and Chapter X, OCR pp.154–163) and the Bate selection (title and report, pp.611–614) in full. Every section replays exactly from its parent using the recorded ranges and whitespace-only collapse.
  - The parent `cist-cumberland-ocr-v1` (`data/raw/heartland-v1/cist-full.txt`) is unchanged between the two commits.
- **Page-marker maps:**
  - Cist: the parent shows `IN MURFREESBORO. 153` before Chapter X, so p.154 is implied. Markers for pp.155–163 are present, and p.161 is printed `1G1`.
  - Bate: `THE MIDDLE TENNESSEE CAMPAIGN. 611` immediately precedes the start range, and the 612, 613 and 614 headers are in the text.
  - I computed every selection locator mechanically from the nearest preceding header, and all 30 agree.
- **OR XXIII Part 1:**
  - I read the OCR title range and its neighbours.
  - I read the full Middle Tennessee report list (Nos. 1–102). It has no Stewart report. Johnson's report is No. 99 and Bate's is No. 100, so the reason for choosing Bate is confirmed.
  - I read the catalog metadata fields (date 1880, volume v.23:1).
- **Registry and receipt:**
  - The registry has 474 records and 464 paths. The previous 468 records are preserved as an identical prefix, with 458 paths.
  - All 474 raw hashes resolve.
  - All receipt input (181), source (474) and output hashes match.
  - The packet `artifacts/research/TN017.md` has 3 JSON blocks. The draft block equals `TN017.json` and the registry block equals `sources.json`.
- **Coverage and baseline:**
  - Coverage is 102/127 dossiers with 25 without. By presence, 25 of 36 campaign groups are complete.
  - The name-status diff shows no other evidence file changed. So the 101 older dossiers and all historical revisions are byte-identical, along with the cohort, both admission proposals, admission-check, baseline and battles.
  - There are 0 promoted rows. The baseline has 23 eligible engagements in 13 groups, with Brier 0.2768816348133779 against 0.25.
  - I independently computed the next group: **Morgan's Raid in Kentucky, Indiana, and Ohio [July 1863]**, starting 1863-07-09, with IN001, OH001 and OH002, none of which has a dossier.
- **`make check`:** 82 tests OK, then `generalship check` with `artifacts_written: false`. The tree stayed clean.
- **Not inspected:** print scans, maps, returns (including OR No. 5 and No. 90), the Thomas, Reynolds, Wilder and Johnson reports, and the rest of either book.

## Confirmed without change

- The reading that treats Liberty Gap as a separate action is supported. NPS gives "Other Name: Liberty Gap", but Cist narrates Johnson's (McCook's) Liberty Gap fighting separately (pp.158–159), and its 231 is not added.
- Force scopes are kept apart and none is adopted: 43,089 is army-wide, "less than 700" is about half a brigade, and 650 is the number engaged. The null opening-strength unknown is appropriate.
- The frozen Unknown, the live 583 (US 583; CS 0) and Bate's 146 all stay visible. Live zeros are not treated as measured.
- OCR errors inside quotes (`tioover’s`, `figlit`, `in- trenchruents`, `Beynolds`) are retained, not corrected.
- Phase tags and statuses are reasonable. Attributions to Cist, Bate and NPS are qualified as interested or summary accounts.
- There is no automatic commander credit, no score and no probability. No other Stewart report was missed.

## Required corrections

**R1 — `reported-force-scope`: scope quote and a visible size dispute.**
- *Problem 1.* The cited Cist quote, "was 43,089, of all arms.", does not itself carry the June 20 date or the army-wide scope the claim states.
- *Fix 1.* Replace that citation's quote with the following, keeping p.155 and the section: `as reported by Bragg as the strength of his army on June 20, 1863, at Shelbyville, was 43,089, of all arms.`
- *Problem 2.* Cist sizes the attack on Wilder at two brigades, while Bate says less than 700 men (about half his brigade) fought on June 24. That dispute is not stated in the claim.
- *Fix 2.* After the Cist sentence, add: "Cist says Wilder found the enemy about to attack him with two brigades."
- *Fix 2 citation.* Add `cist-tullahoma-selections-v1`, section `advance-on-tullahoma`, locator `p.159 (OCR page markers; not checked against print)`, quote `finding the enemy about to attack him with two bri- gades`.

**R2 — `gap-and-defiles`: two different artillery sections are conflated.**
- *Problem.* The current value says Bate's "artillery on an eminence commanded the exit ... and that he later placed it on heights". Bate's text says otherwise:
  - Woods's section on the eminence on his right, together with the skirmishers, commanded the east exit (p.612).
  - What he moved was "the artillery then engaged on the left" (p.613).
  - The force "guarding the east exit from the gap" stayed where it was.
- *Fix.* Replace the Bate sentence with: "Bate says one artillery section on an eminence on his right, with his advanced skirmishers, commanded the exit from the gap going east, and that he later moved the artillery engaged on his left to hills in his rear that overlooked the entire battle-ground."
- *New citations.*
  - `or23-1-bate-hoovers-gap-selections-v1`, section `bate-1863-07-15`, `p.612 (OCR page markers; not checked against print)`, quote `on an eminence on my right`.
  - Same section, `p.613 (OCR page markers; not checked against print)`, quote `I removed the artillery then engaged on the left to a line of hills immediately in our rear`.

**R3 — `command-roles`: uncited parts and an overstated role.**
- *Problem.*
  - "Reynolds's division led" has no citation.
  - "Wilder's brigade held ... against a two-brigade attack" leaves out Cist's statement that Reynolds supported Wilder with his other brigades.
  - The "live commanders" have no citation.
- *Fix.* Replace the Cist sentence with: "Cist says Reynolds's division was in advance; Wilder, finding the enemy about to attack with two brigades, occupied a strong position on the hills at the southern entrance of the gap, and when his brigade was attacked Reynolds supported him with his other brigades."
- *New citations.*
  - Cist, `p.159 (OCR page markers; not checked against print)`, quote `Beynolds's division in advance,`.
  - Cist, `p.160 (OCR page markers; not checked against print)`, quote `Eeynolds supported liim at once with his other brigades,`.
  - `nps-tn017-v1`, locator `Principal Commanders`, quote `Major General George Thomas [US]`.
  - `nps-tn017-v1`, locator `Principal Commanders`, quote `Major General Alexander Stewart [CS]`.

**R4 — `recorded-result`: an uncited statement and a scope problem.**
- *Problem.* "On the 27th took Manchester" has no citation, and Bate's holding action was by part of his brigade, not the whole brigade.
- *Fix.* Change "Bate says his brigade held the Federals at bay" to "Bate says the fewer than 700 men of his brigade engaged held the Federals at bay".
- *New citation.* Cist, `p.163 (OCR page markers; not checked against print)`, quote `took possession of Manchester,`.

**R5 — `casualty-records`: population and timing scopes are missing.**
- *Problem.* Cist's 231 is the Union loss of Johnson's command, including Carlin's brigade, in a later attack at Liberty Gap. The claim does not say so.
- *Fix for the Cist sentence.* Replace it with: "Cist gives 231 killed and wounded for Johnson's Union command, including Carlin's brigade, in the Confederate attack at Liberty Gap that he places on the day after Johnson's advance to the gap; this separate action is not assigned to Hoover's Gap."
- *Fix for the Bate sentence.* Replace it with: "Bate says his list of killed and wounded of the 650 engaged, in his account of the June 24 action, was 146, which he puts at nearly twenty-five per cent."
- *New citations.*
  - Cist, `p.159 (OCR page markers; not checked against print)`, quote `in this attack Johnson's command, including Carlin's brigade,`.
  - Cist, `p.158 (OCR page markers; not checked against print)`, quote `0:i the following day, late in the afternoon, an attack was made on`.
- *Memo.* In the memo's Scope bullet, change "its 231 killed and wounded are not added" to "its 231 Union killed and wounded (Johnson's command including Carlin's brigade) are not added".

**R6 — Locator relies on a misread header without reporting it.**
- *Problem.* The `rain-and-roads` Cist citation reads "The incessant rains ...". Its page, p.161, is inferred from the OCR header `1G1` without saying so.
- *Fix.* Change its locator to `p.161 (OCR page header reads "1G1"; not checked against print)`.
- *Check.* No other locator depends on a missed or misread header.

**R7 — The OR XXIII Part 1 imprint year is in the pinned OCR.**
- *Problem.* All three records (`ia-or23-1-illinois-metadata-v1`, `or23-1-illinois-ocr-v1` and `or23-1-bate-hoovers-gap-selections-v1`) say the imprint year "was not read in the inspected OCR title passage". But the parent OCR reads `GOVERNMENT PRINTING OFFICE. \n\n1889.`, with `1889` at character offset 1084, three characters after the selected title range ends (1081). Other volumes record the year from the same place in the OCR title.
- *Fix.* Following the repository's versioned-record practice (compare `ia-or24-2-illinois-metadata-v2`), set `publication_year` to 1889 and the `edition` to: "Washington: Government Printing Office, 1889 per OCR title (parent offset 1084, immediately after the selected title range; not checked against print); series I volume XXIII part I per OCR title and catalog volume v.23:1. Catalog date 1880 describes the series and is not substituted for the volume imprint."

## Advisories (not required)

- **A1.** The new Cist record's `dependency_note` repeats "across five records", but the `cist-cumberland-1882` group now has seven records. Reconcile the count in a later versioned record so it is not mismatched against the immutable older records.
- **A2.** Extend two quotes so each covers all of its sentence:
  - `rain-and-roads`: the Brannan clause, `by preventing Brannan join- ing the Fourteenth Corps as soon as was expected.`
  - `turn-the-right`: the Elk River clause.
- **A3.** Whether the live 583 includes Liberty Gap is still unknown. The open question already defers this; keep it visible.

Finding IDs: R1, R2, R3, R4, R5, R6, R7 (required); A1, A2, A3 (advisory).
