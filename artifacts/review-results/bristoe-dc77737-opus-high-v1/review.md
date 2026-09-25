# Bristoe Campaign first pass: separate review

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), `high` reasoning effort. Fresh-context subagent working from this assignment only; the author's conversation was not an input.
- **Date:** 2026-09-25.
- **Commits:** prepared `dc77737bbeb20024b5817e9292d6ace5a6a7ddfc` against previous `2203b712059f37ada174fc171b56f46cca331a2e`. The bundle is at `f7ca7d26b5a4c6aa375a373a081077e03c2b9b03`, whose only commit after dc77737 adds this assignment. I worked in a worktree at f7ca7d2.
- **Inputs:** `assignment.md` sha256 `5162ba1e…cbac6a` and `inputs.json` sha256 `03771655…29f5` both match. All **50/50** bound paths match their hashes, both at `git show dc77737:<path>` and in the worktree. There were no mismatches.
- **Outcome:** **corrections required.** Findings BR-R1 to BR-R4 are extraction and attribution fixes. None changes a result, strength, date or phase decision.

This is an AI review. It is not human historical adjudication, independent corroboration, proof of source independence or feature admission. Offline only: I did no new research, used no extra source families and started no agents.

## Coverage actually inspected

- **Guidance:** AGENTS.md, the evidence contract, the Bristoe memo, and the relevant parts of the roadmap, sources.md and methodology (current priority, first-pass protocol and phase boundaries). I skimmed rather than fully read README, methodology and roadmap.
- **Dossiers:** all 5 dossiers, **45 claims, 5 null unknowns and 190 citation occurrences**. Each claim's value and rationale was read against its cited passages. Every record has all seven dimensions. Each unknown is null, tagged `unknown`, and has no citations.
- **Frozen rows:** the battle, force and commander rows for VA039–VA043, and every cited cell. This includes VA043 `results_text` "Union victory" against `result` "Inconclusive", and the VA043 force row's `captured` value of 1600.
- **Five NPS summaries:** read in full. Each text snapshot was replayed from its HTML with the recorded HTMLParser transform, and all five match byte for byte.
- **Four sectioned selections:** Stuart, Hill, Lee and Humphreys were read in full.
  - Every section replays exactly from its recorded half-open range with split/join whitespace collapse. There are no extra sections, and the date maps are complete.
  - The parents `or29-1-illinois-ocr-v1`, the metadata, and `humphreys-ocr-v2` (`56072cc1…6303`, file not in the diff) are unchanged and match their hashes.
  - The 16 new registry records bring the totals to 531 records / 512 paths, from 515 / 496. All 515 earlier records are unchanged.
- **Page-marker maps:** I found start pages from the parent OCR before each section, then mechanically checked all 190 quotes. Each is present and occurs exactly once in its section, and every page locator matches its computed page. NPS quotes fall under the field they are cited to.
  - **Stuart:** pp.438–439 and 447–449, starting at 451 → 452.
  - **Hill:** pp.426–428. The p.427 head reads "Chap. Xtl.]".
  - **Lee:** pp.609–613 and 616. Pages 614 ("614 [Chap. XLI.") and 615 are bare running heads, and no locator relies on them.
  - **Humphreys:** pp.20–30, 33–35 and 37–48. The p.30 head reads "3<3" and, **not disclosed**, the p.40 head reads "4-0" (BR-R1).
- **Repository at the prepared commit:**
  - Coverage: **115/127** dossiers, 12 without, and **29/36** complete groups by presence.
  - Unchanged: all 110 older dossiers, all 82 history files, the cohort, both admission proposals, `admission-check.json` (0 promoted rows), `baseline.json` (23 eligible / 13 groups; Brier 0.2768816348133779 against 0.25) and `battles.json`.
  - Code and test diffs change only the report text and the expected dossier ID set.
  - The receipt matches: 211 inputs, 531 sources and 7 outputs.
  - Each packet's three JSON blocks equal the `battles.json` record, the dossier and `sources.json`.
- **Next group:** by earliest date among incomplete groups, it is **Reopening the Tennessee River [October 1863], TN021** (1863-10-28).
- **Tests:** `make check` passed offline (82 tests OK, `artifacts_written: false`). I ran no build or packet commands.

## Overlaps, disputes, scopes and tags

These items were checked and are acceptable.

- **Overlaps:**
  - Both Auburn records and Bristoe Station are kept separate.
  - Humphreys' combined Auburn-and-Bristoe loss figures (Second Corps 30 officers and 403 men; Confederates 782; p.30) are quoted in VA040 but explicitly not assigned to any record.
  - Rodes's Kelly's Ford losses are quoted but not added to VA043.
- **Buckland date:** Stuart's October 20 dispatch says "yesterday" and Humphreys narrates the fight on "the 20th"; both are recorded, and the frozen October 19 is kept.
- **Force scopes:** 8,243 / 3,000 / 17,223 / 15,000, 6,867 / 3,500, 2,117 / 1,950, Stuart's ten regiments and Lee's "three army corps" are each quoted with their scope, and none is adopted. The Buckland sum of 230 is labelled as the author's computation.
- **Disputes preserved:**
  - Auburn brigade composition.
  - NPS's "Harry Hays's division" against Humphreys' Union General Alexander Hays.
  - Third Corps (Hill) against Fifth Corps (Humphreys).
  - Kilpatrick's rank.
  - Lee's "slight" works against Wright's statement relayed by Humphreys.
  - The two frozen VA043 result fields.
- **Attributed judgments:** Hill's self-criticism, the Lee, Seddon and Davis indorsements, NPS's rebuke remark (not in the inspected reports), Stuart's credit to Fitzhugh Lee and his counterfactual, and Lee's explanation are all attributed to their authors. None is treated as a causal effect, and no commander receives automatic or additive credit. Interested-source labels are present in each dossier's `open_questions`.
- **`inherited` tags:** defensible at the battle boundary as draft hypotheses (see advisory A1).

## Required corrections

**BR-R1 — the p.40 locators rely on a misread running head that is not disclosed.** Humphreys' p.40 head is printed "4-0 GETTYSBURG TO THE RAPIDAN." in the OCR. Two VA043 citations give a plain p.40 locator, and the memo mentions only p.30.

- In VA043 `pasturage-and-siege-guns` (quote "ten siege guns were assigned to the column.") and `hold-the-bridgehead-or-force-it` (quote "drive the enemy from his posi- tions on both banks…"), replace the locator with: `p.40 (inferred: the running head reads "4-0" in OCR, after the p.39 head; not checked against print)`.
- In the memo's Humphreys bullet, replace "Rappahannock Station (pp.37–48)." with "Rappahannock Station (pp.37–48; p.40's running head reads "4-0")."

**BR-R2 — OCR and source readings were normalized silently in values.**

- **VA040 `reported-force-scope`:** the OCR prints "according to the return of the loth of October," (p.29).
  - Replace "on the October 10 return" with "on the return OCR-read as 'the loth of October' (probably the 10th; not checked against print)".
  - Add a citation: `humphreys-bristoe-selections-v1`, section `bristoe-station`, locator p.29 (OCR page markers; not checked against print), quote "according to the return of the loth of October,".
- **VA042 `broad-run-and-chestnut-hill`:** replace "within about two and a half miles of Warrenton" with "within '2-J' miles of Warrenton (OCR; the October 20 dispatch reads '2£'; probably 2½, not checked against print)".
- **VA041 `reported-force-scope`:** NPS prints "Owens". Replace "NPS names Owen's and Smyth's Union brigades" with "NPS names 'Owens and Smyth's' Union brigades".
- **VA041 `command-roles`:** Stuart's Auburn passage says "one of his regiments (the old First)" and does not name the state. Replace "Stuart says Gordon ordered the First North Carolina forward and that Colonel Ruffin fell" with "Stuart says Gordon ordered forward one of his regiments, 'the old First', whose colonel, Ruffin, fell in the charge".

**BR-R3 — accounts relayed from other reports are attributed to the relaying author.**

- **VA039 `recorded-result`:** Stuart's passage opens "It appears from General Lomax’s report that" (p.449).
  - Replace "Stuart says Lomax, cut off at Auburn, was attacked and held until ordered to retire." with "Stuart, citing Lomax's report (not inspected), says Lomax was attacked after Stuart left Auburn and that his sharpshooters held until ordered to retire."
  - Add a citation: `or29-1-stuart-bristoe-selections-v1`, section `stuart-1864-02-13-auburn`, locator p.449 (OCR page markers; not checked against print), quote "It appears from General Lomax’s report that".
- **VA043 `reported-force-scope`:** Humphreys writes "General Russell states that the number of his troops engaged" (p.46).
  - Replace "Humphreys says Russell's assaulting force numbered 2,117" with "Humphreys relays Russell's statement that the troops who captured and held the works numbered 2,117".
  - Add that quote as a citation: section `rappahannock-station`, locator p.46 (OCR page markers; not checked against print).

**BR-R4 — VA043 `casualty-records` attributes computed components to Humphreys.** Humphreys prints Early's figures as "at six enlisted men killed, three officers and thirty-two enlisted men wounded, 119 officers and 1,512 enlisted men miss- ing." (p.45). The figures 35 and 1,631 do not appear in the text; they are sums made by the author.

- Replace "Humphreys relays Early's figures as 6 killed, 35 wounded and 1,631 missing (1,672 total)" with "Humphreys relays Early's figures as 6 enlisted men killed, 3 officers and 32 men wounded, and 119 officers and 1,512 men missing (35 wounded and 1,631 missing, a computation here), 1,672 in total".
- Add that quote as a citation: section `rappahannock-station`, locator p.45 (OCR page markers; not checked against print).

## Advisory observations (no change required)

- **A1 — `inherited` tags.**
  - VA040's embankment claim includes Hill's statement that the position was "covered by … batteries on the rising ground". Those batteries were placed on the day (Humphreys p.26). The rationale's "use on the day … not tagged" covers this; splitting the claim would make it plainer.
  - In VA043, the works were Union-built, but Lee's army converted them before the battle. They are inherited at the battle boundary and are a potential campaign-level mediator for Lee.
- **A2 — indorsement dates.** The date map assigns 1863-10-26 to the whole Hill section and 1863-11-07 to the whole Lee letter section. Those sections also contain indorsements dated 21 and 24 November and 8 and 14 November, plus undated Davis indorsements. This follows the disclosed convention, and no claim relies on these dates. A future metadata-only revision could split them.
- **A3 — Davis's indorsement.** It says "the Third Army Corps of the enemy got a position". This is relevant to the corps dispute and could be quoted there.
- **A4 — Buckland date, further support.** Stuart's later report says "On the next day, October 20," which also supports October 19. It is the same source family as the dispatch, so it is not independent.
- **A5 — Russell's totals.** Humphreys' brigade totals (263 + 63) sum to 326, while the printed division total is 336. Other units may account for the gap; keep the printed number.

No other corrections are required. Five null opening-strength unknowns remain explicit. No new source families, independent human review or feature admission are implied.
