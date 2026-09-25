# Reopening the Tennessee River (TN021 Wauhatchie): separate AI source review

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a fresh-context subagent working offline. It did no network access, opened no new source families and spawned no agents.
- **Date:** 2026-09-25.
- **Commits:**
  - prepared `a71231105d0b86140739ffb20163311fa2439ac1`;
  - previous `35ecf46496fdcb9515e0fd68a54d3a94d24e1552`, an ancestor of the prepared commit;
  - bundle/worktree HEAD `e0fa3588df0ac462d12a0f25e022b77bd00dd65f`.
- **Assignment and inputs:** `assignment.md` sha256 `ab2ae02040b03f9927b89a79203e818822b0e28662608c35ecebce3820fb1463`; `inputs.json` sha256 `96c3a4e47a9e3b64d4f7fa867c9a9c5bda775dcbad27efd0bfae7a2bf248e4fe`.
- **Hash verification:** All 32 bound paths match `git show a712311:<path>` and are byte-identical in the worktree. There were no mismatches.
- **Outcome: corrections required.** Five findings (R1–R5) are minor extraction and attribution fixes. None changes a status, a phase tag or the disputed/unknown structure.
- **Nature of this review:** This is a separate AI analysis. It is not human historical adjudication, independent corroboration or feature admission.

## Scope actually inspected

- **Guidance:** AGENTS.md, the evidence contract and the first-pass memo, read in full. I read only the diffed portions of README, methodology, roadmap and sources.md.
- **Dossier and derivatives:**
  - All 9 claims and 40 citation occurrences in `data/evidence/TN021.json`, including 1 null unknown across all seven dimensions. The counts per claim are 0/4/5/4/4/3/6/6/8.
  - The full NPS text and the Cist and Bratton selections, read in full.
  - The Cist and Bratton parent OCR, read only at the selection boundaries and page headers.
  - The OR report list for "October 26-29, 1863 — Reopening of the Tennessee River" (Nos. 1–43).
  - One incidental "Jenkins" string search in the OR OCR, used to confirm the report list.
  - The OR catalog metadata fields.
- **Frozen rows and registry:**
  - Frozen battle row: one row.
  - Force rows: two, with blank `strength_min`/`strength_max`.
  - Commander rows: two.
  - The six new registry records, and the unchanged `cist-cumberland-ocr-v1` record and its raw file.
- **Not inspected:** No maps or print. No Longstreet, Law, Sheffield or Robertson report, Union report, court of inquiry or return was read as evidence.

## Mechanical results (all pass)

- **Derivative replay.**
  - NPS: HTMLParser text nodes, the "Return to Results" → "Experience More" slice, strip, plus a newline. This equals `nps-tn021.txt`.
  - The Cist sections (`title-and-preface`, `supply-crisis`, `brown-ferry-and-wauhatchie`) and the Bratton sections (`title`, `bratton-1863-11-01`) equal whitespace-collapsed parent slices at the recorded ranges.
  - The parent hashes match. `data/raw/heartland-v1/cist-full.txt` is unchanged from 35ecf46.
- **Page markers.**
  - Cist `supply-crisis` starts after the parent header "232 THE ARMY OP THE CUMBERLAND." (offset 492285), and "233" falls inside the selection.
  - `brown-ferry-and-wauhatchie` starts after "…CHATTANOOGA. 237" (503528). Inside it the headers run 238, 239, "24:0" (510295), 241 and 242.
  - Bratton starts after the "231" header (805354). The 232 and 233 headers fall inside the selection. The next header, "234", comes after the section end, after the footnote "Not found".
  - All 40 locators agree with these markers. None relies on a missed or misread header. The p.240 "24:0" inference is correctly labeled.
- **Report list.** The list's Confederate entries run from No. 38 (Longstreet) to No. 43 (Robertson), with No. 42 being Bratton. There is no Jenkins report, which supports the memo's statement. Separately, the OCR has a compiler footnote at 764304: "Jenkins' report not found."
- **Coverage.**
  - 116/127 dossiers, 11 without; 30/36 complete campaign groups by presence.
  - The next group by earliest start is Operations on the Memphis & Charleston Railroad [November 1863], TN022 (1863-11-03). This is confirmed.
- **Registry.**
  - 537 records / 518 paths; previously 531/512. All old records and all 512 old raw files are unchanged.
  - All 115 older dossiers and all 84 history files are byte-identical.
  - Unchanged: cohort, both admission proposals, `admission-check.json`, `baseline.json` and `battles.json`.
- **Packet and receipt.**
  - The packet `artifacts/research/TN021.md` has 3 JSON blocks. The assigned record matches the frozen rows, with `missing_numeric_strength`. The draft equals the dossier, and the registry equals `data/sources.json`.
  - All `receipt.json` hashes match: 214 inputs, 537 sources and 7 outputs. The only changes are `cli.py`, `sources.json`, the added TN021, 6 added sources and 4 regenerated outputs.
- **`make check`.** Passes offline: 82 tests OK.
  - Baseline: 127 pilot / 23 eligible / 13 groups.
  - Strength Brier 0.2768816348133779 versus equal odds 0.25.
  - Admission: 0 promoted rows (18 blocked / 22 excluded).

## Substantive checks that pass

- **Brown's Ferry scope.** The frozen interval is 1863-10-28/29. Brown's Ferry is a live other name. Cist's October 27 Brown's Ferry losses ("six killed, twenty-three wounded, and nine missing", p.240) are in the selection but correctly not added.
- **Casualties are kept separate and marked disputed:**
  - frozen 828 (US 420; CS 408), which matches the frozen force-row casualties;
  - live 572 (US 216; CS 356);
  - Cist 76+339+22 = 437, "in the attack";
  - Cist "rebel loss is unknown";
  - Bratton brigade total 356.
- **Withdrawal order.** It is correctly left unattributed. Bratton says only that he "received orders" and that "the answer … was delivered". No issuer is named, and no listed commander gets sole or additive credit.
- **Source labels.** Cist is labeled an interested Union history, Bratton an interested account, and NPS/CWSAC one family. The strength unknown is null with no citation, and the live zeros are not treated as measured absence.

## Required corrections

**R1. `cracker-line`: the Kelley's Ferry road object is misattributed to Hooker.** Cist (p.240) ties it to Geary's encampment: "With the object of holding the road to Kelley's Ferry, Geary's division was ordered to encamp near Wauhatchie,".
- **Value:** Replace "; Hooker was to hold the road to Kelley's Ferry." with "; Geary's division was ordered to encamp near Wauhatchie with the object of holding the road to Kelley's Ferry."
- **Quote:** Extend the third citation's quote, keeping the same section and locator, to `With the object of holding the road to Kelley's Ferry, Geary's division was ordered to encamp near Wauhatchie,`.

**R2. `command-roles`: an uncited and broadened Hooker statement, plus an uncited "live" commander statement.** Cist says only that "Hooker ordered Howard to double-quick his nearest division, Schurz's, to Geary's assistance." Steinwehr's division "had arrived", with no order attributed.
- **Value:** Replace "and says Hooker sent Howard's divisions and ordered Orland Smith's charge." with "and says Hooker ordered Howard to double-quick his nearest division, Schurz's, to Geary's assistance and ordered Orland Smith's charge."
- **Add Cist citation:** `{"source_id":"cist-reopening-tennessee-selections-v1","section":"brown-ferry-and-wauhatchie","locator":"p.241 (OCR page markers; not checked against print)","quote":"Hooker ordered Howard to double-quick his nearest division, Schurz's, to Geary's assistance."}`
- **Add NPS citations** to support "live": `{"source_id":"nps-tn021-v1","locator":"Principal Commanders","quote":"Major General Joseph Hooker [US]"}` and `{"source_id":"nps-tn021-v1","locator":"Principal Commanders","quote":"Brigadier General Micah Jenkins [CS]"}`.

**R3. `reported-force-scope`: "Bratton names the six regiments of Jenkins' brigade he put in" has no supporting citation.** The only Bratton quote in this claim is the line-of-fire sentence.
- **Value:** Replace "Bratton names the six regiments of Jenkins' brigade he put in and says the enemy's line of fire was not more than 300 or 400 yards long." with "Bratton says the enemy's line of fire was not more than 300 or 400 yards long."

**R4. `casualty-records` and the memo: two inclosure rows, not one, show only three figures in OCR.** The second row is "6th South Carolina 13 3 16", on p.233 in the selection.
- **Dossier value:** Replace "one row (Palmetto Sharpshooters, '6 35 44') lacks a figure in OCR." with "two rows show only three figures in OCR (6th South Carolina '13 3 16'; Palmetto Sharpshooters '6 35 44'); blank or dropped cells are not reconstructed or checked against print."
- **Add citation:** `{"source_id":"or31-1-bratton-wauhatchie-selections-v1","section":"bratton-1863-11-01","locator":"p.233 (OCR page markers; not checked against print)","quote":"6th South Carolina 13 3 16"}`
- **Memo** (`docs/research/reopening-tennessee-first-pass-v1.md`): Replace "One inclosure row lacks a figure in OCR." with "Two inclosure rows show only three figures in OCR."
- **Reviewer note (not proposed for the dossier):** The column arithmetic is consistent with a blank 6th SC killed cell and a dropped Palmetto missing figure. It does not establish either.

**R5. `valley-camps-and-night`: the OCR reading is silently corrected.** The value says "some three miles", but the cited OCR reads "Borne three miles". The value also says "camped" where Cist says "was ordered to encamp".
- **Value opening:** Replace "Cist says Geary's division camped near Wauhatchie, some three miles up Lookout Valley from Howard's camp," with "Cist says Geary's division was ordered to encamp near Wauhatchie, some three miles (OCR \"Borne three miles\") up the valley from Howard's position,".
- **Rationale:** Append "Cist's OCR reads \"Borne three miles\"; read as \"some\" and not checked against print."

## Advisory (not required)

- **A1.** In the `casualty-records` rationale, consider adding that the live CS 356 matching Bratton's one-brigade total does not establish that the live figure comes from Bratton, or that it covers the other Confederate brigades.
- **A2.** The Cist family `dependency_note` still says "across five records". There are now 1 OCR and 7 selection records. Changing it would need a versioned metadata-only revision; this is inherited and not specific to TN021.
- **A3.** The compiler footnote "Jenkins' report not found" and Law's report (No. 40) bear on who issued the withdrawal order. They remain deferred and uninspected by the author. I did not evaluate them as evidence.

**Finding IDs:** R1, R2, R3, R4, R5 (required); A1, A2, A3 (advisory).
