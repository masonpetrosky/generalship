# Separate review: Goldsboro Expedition first pass (NC007, NC008, NC009)

- Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a fresh-context subagent session. My only inputs were the assignment and the repository; the author's conversation was not an input.
- Date: 2026-09-24.
- Commits:
  - Prepared commit reviewed: `9de5b1dd90633345ebc7b2d6e54a520c54718ee1`.
  - Evidence commit it completes: `4a9136809714700f5c760cb478e0a15fac38a0c8`.
  - Previous commit: `9d5b254beaf2767b6ba16340983c118fee8e91d0`.
  - Review-bundle commit (the worktree HEAD): `8b6f70a62618b29c9b63a079764c56a5d826bb62`.
- Hashes:
  - `assignment.md` sha256: `0ad2e1a4e7834b3492c1553198b585bf983e3fd169ad572565f5f703d2bd04e1`.
  - `inputs.json` sha256: `160f42202ecf528a803240c30fed3e1eb0636bada875c40511f44ee54513cc34`.
  - I checked all 40 manifest paths, both in the worktree and via `git show 9de5b1d:<path>`. There were **0 mismatches**.
  - Relative to `9de5b1d`, the bundle commit adds only `assignment.md` and `inputs.json`.
- **Outcome: corrections required.** There are five required findings (GB-01 to GB-05) and six non-blocking notes (GB-N1 to GB-N6). None of them needs new research.
  - Every replacement quote below was checked offline.
  - Each one occurs exactly once in the named section, on the stated OCR page.

This is an AI review, a separate analysis only. It is not human historical adjudication or independent corroboration, and it does not admit any feature. A source-backed claim can still be historically wrong.

## Scope actually inspected

- **Guidance.**
  - Read in full: AGENTS.md, `docs/evidence-contract.md` and the memo `docs/research/goldsboro-first-pass-v1.md`.
  - Read as diffs only: the `9de5b1d` changes to README, methodology, roadmap, sources.md, `cli.py` and `tests/test_evidence.py`, plus the research-queue and quality diffs.
  - Read in part: the methodology section on phase boundaries.
  - I did not read README, methodology, roadmap or sources.md in full.
- **Both commits.**
  - `4a91368` adds all the evidence, sources, raw files and packets.
  - `9de5b1d` changes only README, methodology, roadmap, sources.md, `cli.py`, the test's expected set, the pilot report and the receipt. It changes no evidence or source files.
  - I did not run `make check` at `4a91368`. Its failure is documented in the `9de5b1d` commit message.
- **Dossiers.** I read all three in full: 28 claims (9/9/10), 4 null unknowns (1/2/1), 70 citation occurrences (29/19/22) and all seven dimensions per dossier. `evidence-checks.json` agrees with these counts.
  - Citations by source: Arnold battles 9, Arnold commanders 1, NPS 13, Foster 27, Smith 20.
  - Every NPS quote occurs at its locator. Every CSV quote matches its frozen cell.
  - Every OR quote occurs exactly once in its section. All 47 OR locators match the last preceding OCR page marker.
- **Sources.** I read all 10 new source records.
  - I read the three NPS text summaries in full.
  - OR XVIII catalog fields: identifier, title, creator, date (1880, the series date), publisher, volume (v.18), contributor, sponsor, scandate and collection.
  - I read both selection derivatives in full: the transcription notes, the title and every report section.
  - From the parent OCR I read only the section boundaries, the compiler's heading (No. 1, just before 185553), the report list, the p.59 footnote, and the p.60 context after the Foster range.
  - I did not do whole-book reading, and I inspected no print, facsimiles, originals, maps or network sources.
- **Replays.** All five derivatives replay byte-for-byte.
  - The three NPS texts replay with HTMLParser (script/style omitted), stripped nodes joined with newlines, sliced from Return to Results up to Experience More.
  - The two OR selections replay from their half-open Unicode ranges with split/join collapse.
    - Foster has four ranges: title plus the December 14, 20 and 27 reports.
    - Smith has six ranges: title plus the December 15 report, the December 16 letter, the December 16 telegram, and the December 18 and 29 reports.
  - The section-date maps are complete and section-specific, and the source-wide `document_date` is null.
  - `source_kind` values follow the Eastern Kentucky pattern:
    - NPS: `government_secondary_history`.
    - Catalog: `digital_catalog_metadata`.
    - OCR and both selections: `official_report_compilation`.
- **Page markers.** I confirmed these OCR markers:
  - 53: the compiler's header, just before the Foster range.
  - 54.
  - `S5` = 55.
  - 56.
  - `61` = 57.
  - `1)8` = 58.
  - 59.
  - `m` = 107, just before Smith's December 15 report.
  - 108, 109 and 110.
- **Frozen rows.** I checked all battle, force and commander rows for NC007–NC009: 3 battle, 6 force and 6 commander rows.
  - The force rows have no structured strengths.
  - All three commander rows for Foster read `Brigadier General`.
  - All three battles are `baseline_eligible: false` in `battles.json`.
- **Mechanical checks.**
  - Coverage: 63/127 dossiers, 64 without. Campaign groups: 15/36 complete by presence.
  - Registry: 337 records / 334 paths. All 327 earlier records (324 paths) are unchanged, and their raw files are byte-identical. All 337 source hashes verify.
  - All 60 earlier dossiers and all 15 `history/` revisions are byte-identical to `9d5b254`.
  - Also byte-identical to `9d5b254`: the cohort, both Shiloh admission proposals, `admission-check.json` (0 promoted rows, no emitted rows), `baseline.json` (23 battles / 13 campaigns; strength Brier 0.2768816348133779 against equal odds 0.25), `battles.json` and the three CWSAC CSVs.
  - The receipt has 92 input, 337 source and 7 output hashes, and all of them verify.
  - All three JSON blocks in each packet parse.
  - `make check` passed offline: 82 tests OK, `generalship check` exit 0, 63 drafts, 23 eligible, 0 promoted.
- **Procedural disclosure.** To compare packets, I called `generalship.cli.research_packet` in-process. I did not realise that it writes `artifacts/research/<id>.md`, and it rewrote all three packets.
  - The rewritten files are byte-identical: `git status` is clean, and their sha256 values equal the manifest.
  - So no content changed, but this was a packet-generation call that the assignment excluded. It does confirm that the packets match reconstruction.
- **Next group.** I confirmed it independently. The earliest-start incomplete frozen group is **Forrest's Expedition into West Tennessee [December 1862-January 1863]**, TN009 and TN011, starting 1862-12-19.

**Confirmed without correction:**

- **Force figures are kept separate.** These are each kept separate, and none is adopted:
  - Foster's 10,000 infantry covers the whole expedition at departure.
  - Foster's figure of 6,000 with twenty guns is his estimate of the enemy at Kinston.
  - Smith gives Evans 2,000.
  - Smith's 30,000 is a passive "Enemy now estimated", which is correctly described as relayed.
  - Smith's "certainly over 15,000" is dated December 18.
- **Casualty differences are kept.**
  - Kinston: 685 frozen and 685 live.
  - White Hall: 150 frozen against 0 live, marked disputed.
  - Goldsborough Bridge: 220 frozen against 0 live, marked disputed.
  - The expedition-wide 90/478/9 and 71/268/about 400 are recorded once, in NC009, and not allocated.
  - The p.59 footnote does read "But sec revised statement, p. GO".
- **The White Hall result dispute is kept.** Foster says his batteries "silenced" the Confederate guns; Smith says the Federals were "driven back". The frozen label is Inconclusive and the live label is Indecisive.
- **Report dates are handled correctly.** They are section-specific and not treated as event times.
- **Source families are counted correctly.** NPS/CWSAC, Foster and Smith are three families, and the OR volume is a shared container.
- **The inherited tag is acceptable.** The `inherited` tag on Kinston's approach delays is an acceptable draft hypothesis, because the rationale states the Kinston boundary (see GB-N3).
- **Nothing is invented or over-attributed.** There is no automatic commander attribution, additive credit, score, probability or causal effect.

## Required corrections

**GB-01 (NC007 `command-roles`): the OR half of the rank conflict is uncited.**
The value says Foster's "OR reports are headed Major General", but no OR citation supports it. The compiler's heading ("Reports of Maj. Gen. John G. Foster") is in the parent OCR, outside the selected range.
- Replace the last sentence of the value with: "The frozen and live records rank Foster Brigadier General; he signs his December 27 OR report 'Major-General, Commanding Department'."
- Add this citation: `{"source_id":"or18-foster-selections-v1","section":"foster-1862-12-27","locator":"p.59 (OCR page markers; not checked against print)","quote":"Major-General^ Commanding Dejgartment."}`

**GB-02 (NC007 `reported-force-scope`): the artillery and cavalry figures are uncited.**
"40 guns and about 640 cavalry" is not in the quoted passage.
- Add this citation: `{"source_id":"or18-foster-selections-v1","section":"foster-1862-12-27","locator":"p.54 (OCR page markers; not checked against print)","quote":"total, 40 guns; the Third New York Cavalry, about G40 men."}`
- Append to the rationale: "The OCR reads 'G40' for the cavalry figure; 640 is a reading not checked against print."

**GB-03 (NC009 `recorded-result`): the Goldsborough framing is incomplete and partly uncited.**
The claim says "Smith says the county bridge was saved", but its only Smith quote is "can be replaced at once". It also omits Smith's statement that the Confederate advance drove the Federals back. That statement conflicts with Foster's account that the advance was "a disastrous failure" (currently cited only under `command-roles`).
- Replace the value with: "The frozen and live results read Union victory. Foster reports the railroad bridge burned and a Confederate advance on his rear guard repulsed as a disastrous failure; Smith says his brigades drove the Federals back from their position on the railroad line and saved the county bridge, and that the burned superstructure could be replaced at once."
- Change `"status": "supported"` to `"status": "disputed"`.
- Append to the rationale: "Both reports agree the railroad bridge burned; they conflict over the Confederate advance that followed. Neither account is adopted."
- Add these three citations:
  - `{"source_id":"or18-smith-selections-v1","section":"smith-1862-12-18","locator":"p.109 (OCR page markers; not checked against print)","quote":"They attacked and drove the enemy back and saved the county bridge."}`
  - `{"source_id":"or18-smith-selections-v1","section":"smith-1862-12-29","locator":"p.110 (OCR page markers; not checked against print)","quote":"The enemy were driven back from their position on the line of the rail- road"}`
  - `{"source_id":"or18-foster-selections-v1","section":"foster-1862-12-27","locator":"p.58 (OCR page markers; not checked against print)","quote":"it was a disastrous failure."}`
- In the memo's Goldsborough bullet, replace "Smith says the county bridge was saved and the superstructure could be replaced at once." with: "Smith says his brigades drove the Federals back and saved the county bridge, and that the superstructure could be replaced at once; the claim is disputed."

**GB-04 (NC007 `casualty-records`): an uncited, repeated expedition-wide number.**
The quote "Most of the latter were taken prisoners at Kinston Bridge" does not contain "about 400". Stating the number again in NC007 also conflicts with the memo's rule that it is recorded once, in NC009.
- Replace "Smith says most of about 400 Confederate missing were taken at Kinston Bridge." with: "Smith says most of the Confederate missing in his expedition-wide loss statement (recorded in NC009) were taken prisoners at Kinston Bridge."
- Replace that citation's quote with "miss- ing. Most of the latter were taken prisoners at Kinston Bridge". The source, section and p.110 stay the same.

**GB-05 (memo): the "explicit page-marker map" is not actually recorded.**
The memo records only the p.57 misprint. Several locators depend on unrecorded readings: "S5", "1)8" and "m", and the p.53 and p.107 markers that fall before the selected ranges.
- Replace "Running headers misprint p.57 as "61"; locators use an explicit page-marker map." with:
  "Locators follow OCR running-header markers, read as: Foster p.53 (compiler header before the selected range), 54, 55 (OCR "S5"), 56, 57 (misprinted "61"), 58 (OCR "1)8"), 59; Smith p.107 (OCR "m", before the selected range), 108, 109, 110. Pages are not checked against print."

**Count effects.** These corrections add 5 citation occurrences, taking the total from 70 to 75 (NC007 29 → 31; NC009 22 → 25). Claims (28) and unknowns (4) are unchanged.
The following need the regenerated counts: the memo, README, roadmap, the `cli.py` report text, the pilot report and the packets.

## Non-blocking notes

- **GB-N1 (NC007/NC009 `reported-force-scope`):** "Foster's 1st Division" is a gloss. The frozen cell reads "Department of North Carolina, 1st Division". Foster's own list also includes "General Wessclls' brigade of General Peck's di\dsion (kindly loaned to me)" (p.54). The better course is to quote the frozen label verbatim.
- **GB-N2 (NC008 `confederate-cavalry-shortage`):** Evans's appeal comes from Smith's account of the night of December 15–16 ("At 12 o'clock midnight it was reported", p.107). It concerns Evans's command, not White Hall specifically. The rationale could scope it as department-level context from before the December 16 action.
- **GB-N3 (NC007 `roads-and-obstructions`):** `inherited` is defensible only at a tactical Kinston boundary. The felled trees and the destroyed Beaver Creek bridge were opponent-made, and Foster's Vine Swamp detour was his own choice. At a campaign boundary, these could be commander-created mediators. The rationale could say this.
- **GB-N4 (uncited narrative clauses; optional additions, all verified):**
  - NC007 terrain, foster-1862-12-14 p.53: "found the enemy strongly posted at a defile through a marsh bordering a creek".
  - NC007 information, p.58: "duced him to retain several regiments on the Kinston side of the Neuse".
  - NC007 responsibility, p.56: "before I could attack the enemy they had retired".
  - NC008 responsibility, p.57: "leaving sharpshooters in rear to continue the fight".
  - NC009 information, smith-1862-12-29 p.109: "with two brigades and five pieces of artillery".
  - NC009 responsibility, p.110: "Evans’ and Olingman’s bri- gades were ordered to cross". Also p.58: "laeiUenant Graham, Twenty-third New York Battery, acting as aide- de caini) to Colonel Heckman, fired the bridge." This would replace the bare "fired the bridge."
- **GB-N5 (NC008 `recorded-result`):** Foster's December 20 report also frames White Hall as a success: "I encountered and defeated the enemy at Kinston , White Hall, Thompson’s Bridge, and Goldsborough." (p.54). This is optional additional evidence for the dispute.
- **GB-N6 (selection boundary):** The `smith-1862-12-15-goldsborough` range ends with "Weldon", which is the place line of the next, unselected telegram. It is not cited. The selection is immutable, so a later version could simply record this.

## Limits

This review covers only the bounded draft extraction.

- I checked no returns, subordinate reports, maps or print pages. I did not re-rate the reliability or dependence of NPS, Foster or Smith. I accepted the explicit unknowns without asking for further depth.
- Apart from the byte-identical packet rewrite disclosed above, I edited no primary artifact. I made no commit or push.
