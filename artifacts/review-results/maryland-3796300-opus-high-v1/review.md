# Maryland Campaign first pass: separate AI review

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. Separate subagent with fresh context; the author's conversation was not an input.
- **Date:** 2026-09-24
- **Prepared commit:** `3796300981ae53e5d94d8b2411af3eef3b53d7fd` (previous `7c4902bd8cb01fe0d026c11207daab07e9a3d80f`). The assignment bundle is at `8890c8253475dc140dc0abd3afc8102eaadbaf7d`, which adds only `assignment.md` and `inputs.json` on top of 3796300.
- **Assignment:** `assignment.md` sha256 `00d5a0e17d81b0b941ad4502c60a37f9e3eb543c2899a1874c66dfe2785e6e65`. **Input manifest:** `inputs.json` sha256 `267ffeb24698bf1717751ffd2abd823e303f94d1516b80051bf05505784952f4`.
- **Input verification:** all 39 bound paths match their manifest hashes, both in the worktree and in `git show 3796300:<path>`. There were no mismatches.
- **Outcome: corrections required** (R1–R4). The corrections are extraction, attribution and count fixes. None of them changes an outcome value, a frozen cell, a phase tag or an unknown.

This is an AI review. It is a separate analysis, not human historical adjudication, independent corroboration or feature admission. I did no network access, opened no new sources and used no agents. Only this file was written.

## Scope actually inspected

- **Guidance read:** AGENTS.md, the evidence contract and the Maryland memo in full. For README, methodology, roadmap, sources.md, `cli.py` and the tests, I read the 7c4902b→3796300 diffs rather than the full documents.
- **Dossiers:** all 29 claims and 79 citation occurrences in WV010, MD002 and WV016, including the 4 null unknowns (three opening strengths and WV016 logistics). Each dossier covers all seven dimensions. MD003 was not re-reviewed; it is byte-identical to the previous commit.
- **NPS summaries:** I read all three retained NPS summaries in full.
- **Palfrey:** I read the catalog metadata (identifier, title, creator, 1882 date, publisher, collection, sponsor, scan date), the transcription note, the title/preface and all four selected passages in full.
  - I checked every locator against the OCR running-header markers. Those markers include the misread p.24 ("21 ANTIETAM…") and p.34 ("0* 31 ANTIETAM…").
  - In the parent OCR, I checked only the text around each range boundary and the marker immediately before each section (p.18 after "17"/"18", p.23 after "22"/"23", p.27 as the unheaded chapter-II opening after "26", and p.128). I did not read the whole book.
- **Frozen CSV rows:** all battle, force and commander rows for WV010, MD002 and WV016, including the rank cell `Robert E. Lee` → `General`.
- **Mechanical checks** (all pass):
  - `make check` ran offline and exited 0: 82 tests OK; 127 battles / 23 eligible / 13 groups; strength Brier 0.2768816348133779 against 0.25 for equal odds; 54 dossiers; 0 promoted rows.
  - All four text derivatives replay byte-exactly. The NPS HTMLParser transform reproduces all three `.txt` files and their hashes. Palfrey's five half-open ranges (395–1716, 40212–44615, 51958–59382, 59846–91760, 285779–288589) reproduce every section under split/join whitespace collapse.
  - Registry: 310 records / 307 paths, up from 301 / 298. The previous 301 entries are unchanged, in order, and no earlier raw file changed. All 310 source hashes match their files.
  - Dossiers: 54/127 have one, 73 do not. 11/36 campaign groups are complete by dossier presence. All 58 earlier evidence files are byte-identical, including 51 dossiers and 7 history revisions.
  - Unchanged: cohort, both admission proposals, `admission-check.json`, `baseline.json`, `battles.json` and the three CWSAC CSVs.
  - The next incomplete group by earliest date is **Iuka and Corinth Operations [September-October 1862]: MS001, MS002, TN007** (earliest 1862-09-19), which I confirmed independently.
  - Receipt: 75 input hashes, 310 source hashes and 7 output hashes all match.
  - Packets: each packet's three JSON blocks equal the `battles.json` record, the dossier and `sources.json`.
  - `evidence-checks.json` rows match the claim and unknown counts.

## Verified without correction

- **South Mountain result.** The frozen `Union victory` is retained. The live NPS `Indecisive` and Palfrey's "tactical defeats to the Confederates, but strategical victories won by them" (p.40) are cited, and the claim is marked disputed. That is correct.
- **Harpers Ferry force scopes.** These are kept as separate scopes: 9,000 at the ferry plus 2,500 withdrawn from Martinsburg (p.23), 11,000 surrendered (p.26) and NPS "more than 12,000". No surrender count is used as an opening strength. The surrendering officer (Miles per NPS, White per Palfrey p.26) is disputed and unresolved.
- **South Mountain force figures.** McClellan's 30,000, the 35,155 First+Ninth Corps cap and the brigade counts (18 Federal, 15 excluding Ricketts, against 14 Confederate counting Rosser's command) are kept separate and none is adopted.
- **Casualties.** The differences are preserved: 12,922 against 13,005 (the frozen forces rows sum to 12,636 + 286); 4,500 against 4,625; 625 against 654.
  - Palfrey's 1,568, about 530 and prisoner figures are not summed.
  - For the 118th Pennsylvania, NPS 269 and Palfrey "282 out of 800" (footnote, p.128) are both kept.
  - A. P. Hill's "3,000 … killed and drowned" is quoted as Hill's claim and ridiculed by Palfrey. It is not used as a count.
  - Captured guns are four (NPS) against five (Palfrey).
- **Phase tags.** Halleck's hold order is tagged `inherited`, and the rationale correctly places the decision with the General-in-Chief. The no-night-march decision is tagged `commander_created`. Other tags are defensible given null boundaries.
- **Command roles.** These are correctly separated:
  - Cox and Reno at Fox's Gap.
  - Cobb and Franklin at Crampton's Gap.
  - Pendleton on the 19th (NPS) and A. P. Hill on the 20th (Palfrey p.129). All three WV016 frozen commanders are named, and none receives sole credit.
  - Lee's live heading rank "Major General" is recorded against the frozen `General` and is not adopted.
  - No additive credit is claimed across overlapping Maryland intervals.
- **Palfrey source record.** `source_kind` is `retrospective_history`. The dependency note records his use of Official Records advance sheets, and the preface text supports it. Palfrey is its own family, distinct from NPS/CWSAC, and each new battle uses exactly two families.

## Required corrections

These are primary-artifact changes for the author to verify and apply. The locators and quotes below are exact strings in the named `palfrey-maryland-selections-v1` section; I checked each one for a single occurrence and for its page marker. Follow the repository's existing revision practice (for example, the history archives) when amending the drafts. If R2–R4 are adopted exactly as written, citations become **86** (WV010 24, MD002 38, WV016 24). Claims stay at 29 and unknowns at 4. Update the memo table and the "79 citations" statements in the memo, README, roadmap and `cli.py` report text, then regenerate.

### R1: The source-record count is wrong

The registry grows from 301/298 to 310/307, which is **9** records. The memo lists them as three NPS pairs plus three Palfrey records, which is also 9. Two documents say 12:

- In `docs/research/maryland-first-pass-v1.md` line 53, replace `Twelve new source records bring the registry to` with `Nine new source records bring the registry to`.
- In `docs/sources.md` line 73, replace `adds **12 records**, bringing` with `adds **9 records**, bringing`.

### R2: MD002 `lost-order-and-reports` misattributes the unknown receipt hour

The problem is attribution, not a missing fact:

- Palfrey writes "It has been said that it does not appear at what hour…" (p.28). That attributes the statement to others. He then gives the 6.20 p.m. date of the letter to Franklin.
- The McLaws clause in the value has no citation.
- Palfrey's hedge on Stuart ("seems to have come from Stuart") was dropped from the value.

Replacements:

- **Value:** "Palfrey says McClellan had a copy of Lee's order at Frederick on the 13th. He reports that it has been said that the hour of receipt does not appear, and notes that McClellan's letter to Franklin giving the order's substance is dated 6.20 p.m. He says McLaws did not attach much importance to early indications of an advance, and that Lee's information seems to have come from Stuart."
- **Rationale:** "Retrospective reconstruction. The inspected source does not establish the receipt hour; Palfrey attributes the statement that it does not appear to others ('It has been said') and reports the Franklin letter's 6.20 p.m. date, which is not an inspected original and is not a receipt time. The Stuart attribution is Palfrey's hedged inference."
- **Citations:**
  - Keep p.27 `with the copy of Lee's order in his hands.`
  - Replace the p.28 quote with `It has been said that it does not appear at what hour on the 13th McClellan came into possession of Lee's order.`
  - Add p.28 `is dated 6.20 p.m.`
  - Add p.31 `he did not attach much importance to these indications`
  - Keep p.32 `Lee's information seems to have come from Stuart`
- **Memo:** replace "South Mountain's lost-order receipt time is explicitly unknown in Palfrey." with "South Mountain's lost-order receipt time is not established; Palfrey reports that it has been said the hour does not appear and gives the 6.20 p.m. date of the letter to Franklin."

### R3: MD002 `timing-decision` overstates the order and the counterfactual

Two points in the value go beyond the source:

- Palfrey says no portion of the army was ordered to move that night "with the possible exception of Couch" (p.30).
- His "substantially unopposed" counterfactual concerns only Franklin's pass (p.30). The both-passes counterfactual (p.41) does not say "unopposed".

The phase stays `commander_created`.

- **Value:** "Palfrey says McClellan ordered Franklin to move at daybreak rather than that night, and that no portion of the army was ordered to move that night, with the possible exception of Couch. He argues that had Franklin marched to the foot of the range that night he could have passed through it the next morning substantially unopposed, and that a night march of both wings would have given McClellan possession of both passes early on the 14th."
- **Rationale:** "Attributed command decision; Palfrey's counterfactuals are interested retrospective judgments, not estimated effects. 'Substantially unopposed' refers to Franklin's pass only."
- **Citations:**
  - Add p.28 `move at daybreak in the morning by Jefferson and Burkittsville`
  - Replace the first p.30 quote with `No portion of it was ordered to move that niglit, with the possible ex- ception of Couch`
  - Keep p.30 `he could have passed through it the next morning substantially un- opposed`
  - Add p.41 `would have given him possession of both passes early in the morn- ing of the 14th`
- **Memo:** this sentence is wrapped across lines in the memo. Replace "Palfrey's claim that a night march would have won the passes unopposed is an attributed counterfactual." with "Palfrey's claims that a night march would have let Franklin pass Crampton's substantially unopposed and given McClellan both passes early on the 14th are attributed counterfactuals."

### R4: Stated facts lack a supporting quote

- **WV010 `reported-force-scope`.** The figure 2,500 is not in any cited quote. Replace the p.18 quote with `2,500 men at Martinsburg under General "White, and 9,000 men at Harper's Ferry, under Colonel Miles`. In JSON this is `"2,500 men at Martinsburg under General \"White, and 9,000 men at Harper's Ferry, under Colonel Miles"`. The OCR's stray `"` is retained.
- **MD002 `subordinate-command`.** "Near dark" is not in the cited NPS text. "Franklin carried it" has no citation. Palfrey reports Cox's senior-command statement as a notification to Pleasonton.
  - **Value:** "Palfrey says Cox notified Pleasonton that he would command as senior until Reno came up; Reno was killed at about dark; Cobb was sent to take command of Crampton's Gap, and Franklin gained the crest there. NPS says Reno and Garland were killed. The frozen commanders are McClellan and Lee; the live heading ranks Lee Major General against the frozen General."
  - **Citations:** replace the p.34 quote with `notified Pleasonton that if the command got into an engage- ment, he should command as senior till Eeno should come up.` Add p.40 `was killed almost as soon as he came up to the line occupied by his men, at about dark.` Add p.32 `he gained the crest after a spirited action of three hours`. Keep the other citations.
- **WV016 `reported-force-scope`.** The four volunteer regiments have no citation. Add p.128 `Volunteers from the Fourth Michigan, One Hundred and Eighteenth Pennsylvania, and Eighteenth and Twenty-second Massachusetts, crossed the river`.

## Advisory (not required)

- **A1, WV010 `holding-decision`.** Palfrey's judgment is only partly represented. He also says Halleck was "mistaken in the facts" and that "the error probably resulted favorably for the Union arms" (p.19). Consider adding the latter clause for balance. The `inherited` tag is unaffected.
- **A2, MD002 `reported-force-scope`.** Palfrey rejects McClellan's 30,000 figures ("about as oriental as usual", p.38). Stating this in the value would make it explicit that the figure is quoted in order to be disputed.
- **A3, Palfrey dependency note.** "A Union participant in the campaign" is not established by the inspected passages. The title page gives "formerly Colonel Twentieth Massachusetts Infantry", and the preface cites "my own recollection, memoranda, and correspondence". Consider "a former Union colonel of the 20th Massachusetts who says he drew on his own recollection…", or note that his campaign service is not shown in the inspected text. This does not affect family assignment or `source_kind`.

## Unresolved and out of scope

- These remain open by design and need no additional research work: the receipt hour, opening strengths, the surrendering officer, per-gap casualty allocation, the Shepherdstown day split, and original returns and messages. No original orders, returns, maps or print pages were inspected by the author or by me.
- MD003 was not re-reviewed.
- The pending Northern Virginia review is out of scope.
