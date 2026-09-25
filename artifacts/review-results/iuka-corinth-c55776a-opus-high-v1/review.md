# Separate review: Iuka and Corinth Operations first pass (MS001, MS002, TN007)

- Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This is a fresh-context
  subagent session using only the assignment and the repository; the author's conversation was not an input.
- Date: 2026-09-24.
- Prepared commit reviewed: `c55776a89d1d10d43bba36fefe04512d19b0e1e9`. Previous commit: `8890c8253475dc140dc0abd3afc8102eaadbaf7d`.
  Review-bundle commit (worktree HEAD): `1ec5695de3315bdc87380f1bfe6ba09c5c3d7d07`.
- Assignment `assignment.md` sha256 `c70a5791079dbf0b9cc2d972c63807ad2966c3f906f5aea16e30ebb970ad00dd`.
  Input manifest `inputs.json` sha256 `da83067e82371b558e6721f6b8e7e945131efcf2620164f62735fa32978b786a`.
- Input hashes: I checked all 39 manifest paths in the worktree and via `git show c55776a:<path>`. There were **0 mismatches**.
  The bundle commit changes only the assignment and `inputs.json` relative to `c55776a`.
- **Outcome: corrections required.** There are eight required findings (IC-01 to IC-08) and six non-blocking notes (IC-N1 to IC-N6).
  None of them needs new research. Every replacement quote below was checked offline and occurs exactly once in the named source or section, on the stated OCR page.

This is an AI review, a separate analysis only. It is not human historical adjudication or independent
corroboration. It does not admit any feature. A source-backed claim can still be historically wrong.

## Scope actually inspected

- **Guidance read:** AGENTS.md, `docs/evidence-contract.md` in full, and the memo `docs/research/iuka-corinth-first-pass-v1.md`.
  I read only the prepared-commit diffs of README, methodology, roadmap, sources.md, `cli.py`, `tests/test_evidence.py`,
  the pilot report, the research queue, `quality.json` and `receipt.json`. I did not read those files in full.
- **Dossiers:** all 3 dossiers in full. That covers all 28 claims, including the 3 null unknowns and 76 citation occurrences.
  Each dossier covers all seven dimensions. My recount gave 9/1/27, 10/1/27 and 9/1/22 (claims/unknowns/citations), and the per-battle `evidence-checks.json` entries agree.
- **Sources:** all 12 new `data/sources.json` records.
  - I read all three retained NPS text summaries in full, including Iuka's long one.
  - I read the Greene catalog fields: identifier, title, creator, date, publisher, collection, sponsor, contributor and scandate.
  - I read the whole selection derivative: the transcription note, title/preface, the `iuka` passage (OCR pp.37–42) and the `corinth-and-hatchie` passage (pp.43–54).
  - From the parent OCR I read only the section boundaries and the omitted 713-character gap between the two ranges. That gap holds the p.43 marker and the railroad paragraph.
  - I did not do whole-book reading, and I did not inspect any maps, print, originals or network sources.
- **Frozen rows:** the full `cwsac_battles`, `cwsac_forces` and `cwsac_commanders` rows for all three battle IDs, including `strength_min` and `strength_max`. I also read the three rows in `artifacts/battles.json` and MS001's baseline prediction.
- **Derivatives:** all four replay byte-for-byte. The three NPS texts replay with HTMLParser (script/style omitted), stripped nodes joined with newlines, and the Return-to-Results / Experience-More slice. The Greene selection replays from its three half-open Unicode ranges (319–1971, 78577–90866, 91579–115248) with split/join whitespace collapse.
  All 38 Greene citation locators match the last preceding OCR page marker. The `corinth-and-hatchie` section opens on p.43 because the p.43 marker falls in the omitted gap.
- **Source metadata:** `greene-mississippi-ocr-v1` and the selection record both have `source_kind: retrospective_history`, and the catalog record is `digital_catalog_metadata`. The `dependency_note` records the author's non-participation and the Official Records dependence.
  The NPS pairs are in the `nps-cwsac` group. No quoted officer is counted as a separate family.
- **Mechanical checks:**
  - Coverage: 57/127 dossiers, with 70 cohort engagements lacking one. Campaign groups: 12/36 complete by presence.
  - Registry: 319 records / 316 paths. The first 310 records (307 paths) are unchanged, and every source hash verifies.
  - All 54 earlier dossiers and all 7 `history/` revisions are byte-identical to `8890c82`.
  - Also byte-identical: the cohort, both Shiloh admission proposals, `admission-check.json` (0 promoted rows, no emitted rows), `baseline.json` (23 battles / 13 campaigns; strength Brier 0.2768816348133779 against equal odds 0.25), `battles.json` and the three CWSAC CSVs.
  - The three packets `artifacts/research/{MS001,MS002,TN007}.md` byte-match the `research_packet` reconstruction. All three JSON blocks in each packet parse.
  - All 404 receipt hashes verify.
  - `make check` passed offline: 82 tests OK, `generalship check` exit 0, 57 drafts, 23 eligible.
- **Next group:** I confirmed it independently. The earliest-start incomplete frozen group is **Stones River Campaign [December 1862-January 1863]**, TN008 and TN010, starting 1862-12-07. Fredericksburg (VA028) follows from 1862-12-11.

**Confirmed without correction.** The dossiers get the following right:

- They keep the population differences at Iuka: frozen approx. 4,000–4,500 US and 3,200 CS, the NPS army figure of 14,000, and Greene's 9,000 and 6,000 column figures, 2,800 engaged-division figure and 3–4 thousand brigade figure.
- They treat Corinth's 23,000 / 22,000 as possibly dependent on the returns, not as corroboration.
- They keep the casualty differences: 1,482 against 1,384, with Price's 496 against the provost marshal's 1,438 (which includes prisoners and an estimate); 7,197 against 7,150, where Greene's figure of over nine thousand is identified as a ratio inference; and Hatchie's Bridge, where both give 900.
- The Fulton-road responsibility dispute is kept.
- The following are all adequately supported:
  - Van Dorn's command as senior officer.
  - Hébert's delay, as an attributed judgment.
  - The succession from Ord to Hurlbut.
  - Not adopting Ord's live heading rank.
  - Greene's conflicting "October 5th" date.
  - The `inherited` tag, which is limited to works existing before Oct 3.
  - The post-outcome pursuit delay, which is not added to Corinth's result.
- There is no automatic commander attribution, additive credit, score, probability or causal effect.

## Required corrections

**IC-01 (MS001 `reported-force-scope`): the frozen structured bounds are not recorded.**
The value says "the frozen force fields give approx. 4,000–4,500 US". However, `cwsac_forces` row (MS001, US) has
`strength_min` = `4000` and `strength_max` = `4000`. `battles.json` uses low = high = 4000, and MS001 is
baseline-eligible, with `strength_sensitivity_p_min` equal to `p_max`. The text range therefore never reaches the model input, and the evidence contract requires imported bounds to stay visible. The model input stays unchanged.
Replace the value's first sentence with:
"The frozen `forces_text` describes approx. 4,000–4,500 US (2nd and cavalry divisions) and approx. 3,200 CS (1st Division). The frozen structured US bounds are 4,000/4,000 (the upper bound is not 4,500) and the CS bounds are 3,200/3,200; the live field reads zero."
Append to the rationale: "The imported model row uses the structured 4,000 point value; the text's 4,500 upper bound is not carried into it. This is recorded, not corrected."
Add two citations: `{"source_id":"arnold-cwsac-forces","row_key":{"battle":"MS001","belligerent":"US"},"column":"strength_min","quote":"4000"}` and the same with `"column":"strength_max"`.

**IC-02 (MS001 `unheard-battle`): an unsupported clock and an uncited Ord statement.**
The OCR reads "12. -10 p.m.", so "12:40 p.m." is the author's reading and appears in no inspected passage.
Replace the value with:
"Greene says the wind kept the firing from being heard, and that Rosecrans's midday message saying he was within eight miles (OCR '12. -10 p.m.'; the clock is not verified against print) reached Grant only after night. NPS says Ord later said he never heard any fighting and Grant remarked he had heard no sounds of battle."
Add `greene-iuka-corinth-selections-v1` / `iuka` / p.39: "Eosecrans sent word, at 12. -10 p.m., that he".
Add `nps-ms001-v1` / Description: "Ord did nothing, later proclaiming that he never heard any fighting".

**IC-03 (MS001 `march-route-and-delay`): wrong attribution and an added causal link.**
Greene reports what "word was received from Rosecrans" said. He does not say the guide's fault left a division at Jacinto; the delay and the division's position are two separate clauses.
Replace the Greene clause with:
"Greene says an after-midnight message from Rosecrans reported that, through a guide's fault, his march had been slightly delayed and one division was still at Jacinto, twenty miles from Iuka."
Replace the Greene quote with "word was received from Eosecrans that, through the fault of a guide, his march had been slightly delayed" (p.39).
Add "one of his divisions was still at Jacinto, twenty miles from Iuka" (p.39).

**IC-04 (MS001): propositions without a supporting citation.** Add these `nps-ms001-v1` Description citations:
- `converging-plan` (Bragg's order): "ordered him to prevent Maj. Gen. William S. Rosecrans's Army of the Mississippi troops from moving into Middle Tennessee".
- `fulton-road-uncovered` ("Grant approved"): "Grant later approved this decision."
- `recorded-result` ("Both sources say Price escaped by the Fulton road"): "Price's army evacuated via the uncovered Fulton Road".

**IC-05 (MS002): a missing second source and a misattributed count.**
- `command-and-delay` says "Both sources say Van Dorn took command as senior", but only NPS is cited.
  Add `greene-iuka-corinth-selections-v1` / `corinth-and-hatchie` / p.44: "Van Dorn took command, being the senior officer."
- `casualty-records` says "Rosecrans's 2,268 prisoners and 1,423 Confederate burials". In Greene the burial figure comes from Rosecrans's Medical Director, and neither number is cited.
  Replace with "Rosecrans's statement of 2,268 prisoners taken and his Medical Director's count of 1,423 Confederates buried".
  Add these p.53 quotes: "Rosecrans states that he took 2,268 prisoners, and his Medical Director says that 1,423 Confederates were buried on the field." and "The usual proportion of wounded to killed being about five to one".

**IC-06 (TN007 `reported-force-scope`): the status understates a source conflict.**
The value and rationale both say the sources differ on Hurlbut's formation ("4th Brigade" against "his division"), and Greene's "whole of Van Dorn's army" differs from the frozen CS "Army of the West". A claim that contains conflicting accounts should not read as `supported`, and MS001's analogous claim is `disputed`. The memo also calls this a disagreement.
Change `"status": "supported"` to `"status": "disputed"`. The value and citations stay as they are.

**IC-07 (TN007 `pursuit-congestion`): timing scope.**
Greene's "lack of preparation for an extended movement" refers to Rosecrans's and Hurlbut's pursuit to Ripley, which came after the October 5 action, when Grant recalled them.
Replace the value's second clause with:
"…and that when Rosecrans and Hurlbut later pursued as far as Ripley, Grant ordered them back owing to their lack of preparation for an extended movement."
Append to the rationale: "The Ripley recall follows the October 5 action and is campaign context, not the Hatchie's Bridge result."
Add p.52: "Rosecrans and Hurlbut pursued as far as Ripley,".

**IC-08 (TN007): parts of two claims are uncited.**
- `sequential-command`: add `nps-tn007-v1` / Description "Ord took command of the now-combined Union forces" and Greene p.52 "in which Ord was severely wounded."
- `recorded-result` ("Van Dorn escaped and continued his retreat"): the current Greene quote only covers self-defence.
  Replace it with p.52 "he managed to defend himself against Ord, and to continue his retreat on the east bank of the Hatchie".

These corrections add 14 citation occurrences (76 → 90) and leave claims (28) and unknowns (3) unchanged. The memo, README, roadmap, report and packets need updating with the regenerated counts.

## Non-blocking notes

- **IC-N1 (TN007 `river-crossings`):** "instead" implies the sources conflict, but they don't. Greene also says Van Dorn's advance guard "was imme- diately attacked by Ord and driven back across the bridge" (p.52), and NPS also has the scouts finding another crossing. Suggested wording: "…Greene says the advance guard was driven back across the bridge and the army continued on the east bank six miles to Crum's Mill, where it crossed during the night."
- **IC-N2 (MS001 `casualty-records`):** In the OCR, Price's "86 killed and 408 wounded" sums to 494, but the printed total is "496". The print was not checked, so the rationale could record this arithmetic difference.
- **IC-N3 (MS002 `heat-water-and-fatigue`):** The claim combines a Confederate halt on October 3 with Rosecrans's post-outcome justification for delaying pursuit. The second part overlaps `pursuit-delay` and should not be read as an in-battle Union condition.
- **IC-N4 (TN007 `sequential-command`):** The live NPS narrative itself says "Maj. Gen. Edward O.C. Ord", so the heading's "Brigadier General" also conflicts with the page's own narrative.
- **IC-N5 (MS001):** Greene's figure of about 14,000 for Price comes from the September 28 return, after Iuka (p.44). NPS's "about 14,000" is presented at Iuka and has an unknown date. Neither is an engaged count.
- **IC-N6 (MS002 `fortification-lines`):** The Greene redoubt clause is uncited. The optional p.46 quote is "doubts, constructed within a short distance of the town", which is split by map-label text.

## Limits

This review inspected only the bounded draft extraction. No returns, reports, maps or print pages were checked. The ratings of Greene's and NPS's reliability and dependence are not changed. Explicit unknowns are accepted without further depth. I edited no primary artifact and made no commit or push.
