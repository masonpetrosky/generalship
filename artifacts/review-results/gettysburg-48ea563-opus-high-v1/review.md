# Gettysburg Campaign separate review (VA035, VA107, VA036, VA037, VA038, PA001, PA002, MD004, MD006, VA108)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. I ran as a
  fresh-context `evidence-reviewer` subagent. This is an AI review: a separate analysis. It is not
  human historical adjudication, independent corroboration or feature admission.
- **Date:** 2026-09-25
- **Commits:**
  - prepared `48ea563ad2c79d61eb32e14ac6c457facd86473e`;
  - previous `a21e6aeca34f3a7c81053d4cefe64565bad1ed5e`;
  - worktree/bundle HEAD `d3eddc0dae19ec6cfb5241a2b40114b2c971f073`.

  The bundle commit differs from the prepared commit only by adding `assignment.md` and `inputs.json`.
- **Assignment and inputs:**
  - `assignment.md` sha256 `03f9854158022cf91aed951fcf97d8812161135075d724f0f6f3a42826950c26`;
  - input manifest `inputs.json` sha256 `f557a75497d8b817c0bf41ef65eeb0d1cc193a04332776d370f31c581e6ba04a`.

  All **72/72** bound paths match their manifest hashes, both in the worktree and in the
  `git show 48ea563:<path>` blobs. **No mismatches.**
- **Outcome: corrections required** (GB-R1 to GB-R11). All are extraction, scope, attribution, locator
  or registry-wording fixes, and none needs new research. Most value clauses are entailed by their
  passages. Disputes and unknowns are kept visible.

## Scope actually inspected

- **Claims.**
  - I read all 90 claims, including the 10 null unknowns (the opening strengths), across all 7 dimensions
    in all 10 dossiers. I also read the shared boundary note and open questions.
  - I compared every value clause with its citations. The counts are 320 citation occurrences: VA035 38,
    VA107 41, VA036 28, VA037 33, VA038 29, PA001 25, PA002 45, MD004 31, MD006 24 and VA108 26.
- **Sources read in full.**
  - Doubleday: all eight selection sections.
  - Humphreys: all three selection sections.
  - Lee: the title, transmittal, report opening and retreat sections.
  - Stuart: the August 20 opening, Loudoun, Hanover and Boonsborough sections.
  - NPS: all ten text summaries.
- **Sources read at cited passages only.**
  - Lee's Winchester and Gettysburg sections and Stuart's June 13 Fleetwood report were read at every
    cited passage, with about 500 characters of context each.
  - In Stuart's Fleetwood report I also read every Robertson, Stevensburg and Munford passage.
- **Not read.** I did not read the whole books or the whole OR volume. I did not read maps, returns,
  Meade's or Ewell's reports, or print.
- **Frozen rows.** I read all 10 `cwsac_battles` rows, 20 `cwsac_forces` rows and 21 `cwsac_commanders`
  rows. Every cited cell matches.
- **Replays.**
  - The ten NPS text files re-derive byte-for-byte from their HTML using the recorded HTMLParser
    transform, and their hashes match.
  - For Doubleday (8 sections from `doubleday-ocr-v1`), Humphreys (3) and Lee and Stuart (6 each from
    `or27-2-illinois-ocr-v1`), the recorded half-open ranges reproduce every section exactly after
    whitespace collapse.
  - Parent hashes match. Section date maps are complete, with no extra sections.
- **Page-marker maps.**
  - For each section I located the preceding parent marker and every in-section marker, including
    misspelled heads: Doubleday "CHANCBLLORSVILLE" (p.90) and "CHANCELLORS VILLE" (pp.92, 208); OR
    "$16" for p.316, "3HAP." at p.683, "K, 0., VA." at p.320 and "1ST, 0." at p.322.
  - The resulting start pages are:
    - Doubleday: 82, 88, 100, 120, 125, 196 and 208.
    - Humphreys: 1 (inferred before the "2" marker) and 8.
    - Lee: 313, 316 and 322.
    - Stuart: 679, 687, 688, 695 and 703.
  - All 200 book and report locators match the computed pages except one, PA001's "Omit, if published."
    (GB-R4). No locator depends on a missed header.
- **Registry.**
  - 468 entries / 458 paths. The first 440 entries are byte-identical to the previous registry (430
    paths).
  - The 28 new records are 20 NPS records, 4 OR records, 1 Doubleday record and 3 Humphreys records.
  - All 468 raw hashes verify.
  - Edition and date claims checked against OCR:
    - OR title "WASHINGTON: government printing office. 1889." Catalog date 1880, `v.27:2`, scan 2017.
    - Lee's report is dated "January — , 1864"; the transmittal is dated January 20, 1864.
    - Humphreys' title page and "June, 1883" preface. Catalog: Cornell, MSN sponsor, scan 2006.
    - Doubleday's preface is dated "New Yobk, January, 1883".
- **Coverage.**
  - Dossiers: 101/127, with 26 without a dossier. There are 36 campaign groups, of which 24 are complete
    by presence.
  - `git diff a21e6ae 48ea563` shows only additions under `data/evidence/`. All 91 older dossiers and
    all 65 history files are unchanged.
  - Byte-identical: the cohort, both admission proposals, `admission-check.json` (0 promoted rows),
    `baseline.json`, `battles.json` and the frozen CSVs.
  - The `cli.py`/test edits only update the report paragraph and the expected dossier set.
- **Next group.** Tullahoma or Middle Tennessee Campaign [June 1863], TN017 (start 1863-06-24), is the
  earliest incomplete group. I confirmed this independently.
- **Packets.** In all ten packets:
  - the assigned-record block equals the `battles.json` record;
  - the draft block equals the dossier file;
  - the registry block equals `data/sources.json`.
- **Receipt.** 180 input hashes, 468 source hashes and 7 output hashes all verify. All 101 dossiers
  and 65 history files are bound.
- **`make check`** (offline):
  - 82 tests OK and `generalship check` exit 0.
  - 23 eligible / 13 groups. Strength Brier 0.2768816348133779 against 0.25 for equal odds.
  - `draft_dossiers` 101, `admission_promoted_rows` 0 and `artifacts_written: false`.

  I ran no build or packet command and did not import `generalship.cli`.

### Confirmed without correction

- **Overlaps.**
  - Middleburg overlaps Aldie, and Boonsboro lies inside Williamsport's interval. Both overlaps are
    stated, and no Boonsboro figure is added to MD004.
  - The Count of Paris's 23,186 and 22,728 are campaign-scoped ("in this campaign") and are not assigned
    to PA002.
- **Force scopes.**
  - VA107 and PA002 keep the imported bounds, which are unchanged.
  - 83,289 + 75,054 = 158,343 is correctly labelled as a computation against the frozen 158,300, and
    the live field gives 158,343.
  - Doubleday's relayed Brandy Station figures keep his "apt to overstate" caveat.
  - Humphreys' 47,087 is kept as a July 5 return of enlisted men armed and equipped in seven corps, not
    an opening strength.
  - Live zeros are not treated as measurements.
- **Disputes.** These are preserved: Pleasonton's claimed success against NPS's "without discovering
  Lee's infantry"; Middleburg's regiment against division; Hanover's end state; and every casualty
  comparison.
- **Ranks.** The live heading gives Lee as Major General (PA002, MD004), while the frozen row and his
  own signature give "General". Hampton appears as Lieutenant General, and Stuart has no rank. No
  heading rank is adopted.
- **Stuart's footnote and Sabbath decision.**
  - The footnote says the italic sentence was "inclosed in brackets by General Lee, nth the note, 'Omit,
    if published.'" It is attributed to the compiler.
  - Stuart's Sabbath reason is recorded as his stated reason, and his counterfactuals are attributed.
- **Interested participants.** Doubleday's title page ("COMMAND- IKG THE FIRST CORPS AT GETTfSBURG")
  and his "my division of the First Corps" (p.196) are handled as interested participation.
- **No automatic credit.** No listed commander receives automatic credit, and no causal effect,
  probability or morale score is introduced.
- **Acceptable date readings.** Humphreys' OCR "nth" (11th) and "iothof" (10th) are readable from the
  surrounding 10th/12th sequence. Adding "(OCR 'nth')" to MD004's rationale would be optional.
- **Optional scoping in PA002.** PA002's use of Doubleday's "few rounds for his cannon" is explicitly
  scoped "on the retreat". Moving it to MD004 is optional.

## Required corrections

**GB-R1: Stuart's Loudoun loss total runs to June 22, not June 21.** This affects the boundary note in
all ten dossiers, the casualty-records rationales in VA036, VA037 and VA038, and memo line 61.

- **Evidence.** Stuart's closing sentence is "Our loss in these operations was 65 killed, 279 wounded,
  and 166 missing." (p.691). It follows the June 22 pursuit:
  - "When the mist had sufficiently cleared away next morning, it was evident the enemy was retiring"
  - "Major [John] Eells ... was killed in a charge upon the enemy near Goose Creek Bridge"
  - "Monday, the 22d, was -consumed in their re-establishment."

  The same narrative includes "Hampton met the enemy’s advance toward Cul- peper, at Warrenten" (p.689)
  and Rosser's skirmishing "beyond Goose Creek" on the 20th (p.690).
- **Boundary note replacement.** Replace "Stuart's June 17–21 losses" with "Stuart's Loudoun loss total
  for June 17–22".
- **Rationale replacement (VA036, VA037, VA038).** Replace the sentence with: "Stuart's loss of 65
  killed, 279 wounded and 166 missing is for 'these operations': his Loudoun narrative from June 17
  through the June 22 pursuit toward Aldie, including Aldie, Middleburg, Upperville, Hampton's action at
  Warrenton and the June 20 skirmishing beyond Goose Creek. It is not assigned to one engagement."
- **Memo replacement.** Change "covers June 17–21" to "covers Stuart's Loudoun operations from June 17
  through the June 22 pursuit".

**GB-R2: VA037 `shoeing-and-rain` has population and timing scope errors.**

- **Evidence.**
  - The brigades are specified at p.689: "our pickets beyond Middleburg were driven back upon the main
    body, composed of Robertson’s and W. H. F. Lee’s brigades ... met ... by these two brigades, which
    rough roads had already decimated".
  - The rain falls on June 20, after VA037's frozen end (June 19), at p.690: "Hampton’s brigade arrived
    on the 20th, too late to attack the en- emy, still in possession of Middleburg. A continuous rain was
    also an obstacle".
- **Value replacement.** "Stuart says that on June 19 rough roads had already decimated two of his
  brigades, Robertson's and W. H. F. Lee's (under Chambliss), for want of adequate shoeing facilities.
  He places a continuous rain on June 20, after the frozen Middleburg interval."
- **Rationale addition.** "The rain statement falls between the Middleburg and Upperville frozen dates
  and is context, not an in-interval condition."

**GB-R3: MD006 reconstructs garbled OCR silently.**

- **Evidence.** The OCR at p.703 reads:
  - "too soft from recent rains to operate successfulfy with n ^" — there is no "mounted";
  - "WaS infor.™ed that the enemy was heavily re- Jas neerre" — the continuation is unintelligible;
  - "retire toward Tunkstown".
- **`soft-ground` value.** "Stuart says the fight from Beaver Creek Bridge to the verge of Boonsborough
  was principally on foot, 'the ground being entirely too soft from recent rains to operate successfulfy
  with' [rest garbled in OCR]. NPS says the Confederate cavalry held the South Mountain passes."
- **`ammunition` value.** "Stuart's OCR is heavily garbled here; intelligible fragments mention
  ammunition 'by this protracted engagement' and an order to 'retire toward Tunkstown' (OCR; presumably
  Funkstown, not checked against print)."
- **`reinforcement-report` value.** "Stuart's garbled OCR says he 'WaS infor.™ed that the enemy was
  heavily re-'; the continuation is unintelligible, so 'reinforced' is a probable but unverified
  reading."
- **`recorded-result`.** Replace "that he later retired toward Funkstown" with "that, in a garbled
  passage, there was an order to retire toward 'Tunkstown' (OCR; presumably Funkstown)".

**GB-R4: PA001 has an OCR correction, uncited clauses and one locator error.**

- **`wagon-train`.** Replace "that skirmishing had almost exhausted his ammunition" with "that his
  'numerous skirmishers' (OCR reading, not checked against print) had almost exhausted his ammunition".
  The OCR at p.696 reads "My numerous skirmishers had greatly diminished — almost exhausted — my supply
  of ammunition."
- **`reported-force-scope`.** Two value clauses have no citation in this claim: the 200 wagons and
  Custer's arriving brigade. Add these citations:
  - `or27-2-stuart-gettysburg-selections-v1`, section `stuart-1863-08-20-hanover`, p.695: "owing to the
    great elongation of the column by reason >f the 200 wagons and hilly roads,"
  - `doubleday-gettysburg-selections-v1`, section `hanover`, p.121: "it was finally decided in our favor
    by the arrival of Custer's brigade from Abbotsford."
- **`command-roles`, "Omit, if published."** Change the locator from "pp.695–696" to "p.695 (OCR page
  markers; not checked against print)". The quote ends before the "696 [Chap. XXXIX." header.

**GB-R5: VA035 has attribution and scope wording errors.**

- **`reported-force-scope` value.**
  - Replace "Gregg's estimate of about nine thousand Union cavalry and six batteries, a third of it
    detached toward Stevensburg" with "Gregg's estimate of about nine thousand Union cavalry and six
    batteries, of which, Doubleday adds, a third was detached toward Stevensburg". Doubleday writes "but
    — as will be seen hereafter — a third of this force was detached", so the detachment is his
    statement.
  - Replace "Stuart says the entire Union cavalry crossed with much artillery and sixteen infantry
    regiments" with "Stuart says he was aware that the entire Union cavalry had crossed with a large
    proportion of artillery, supported by nine infantry regiments on the road to Kelly's and seven on the
    road to Beverly Ford". Stuart never states sixteen.
- **`command-roles`.**
  - Replace "not conforming to the enemy's move toward Stevensburg" with "not conforming to the movement
    of the enemy to the right, of which Robertson was cognizant".
  - The p.683 passage does not name Stevensburg. The Stevensburg column was a separate two-regiment
    force (p.680, "moving in the direction of Stevensburg"). The column that threatened Fleetwood had
    "turned to the right from the Stevensburg road" (p.681).

**GB-R6: VA107 has an unflagged computation, an overbroad paraphrase and an uncited clause.**

- **`casualty-records`.** Replace "Early's 3,358 prisoners sent to Richmond" with "Early's 108 officers
  and 3,250 enlisted men sent as prisoners to Richmond".
- **`clear-the-valley`.** Replace "Doubleday says the garrison had to be cleared for Lee's advance and
  that Milroy remonstrated against withdrawing" with "Doubleday says it was essential to Lee's advance
  that the valley be cleared of Union troops, and that Milroy remonstrated against orders to send his
  armament and supplies back to Harper's Ferry".
- **Citations to add** (`winchester` section, p.88):
  - "It was essential to Lee's advance that the valley should be cleared of Union troops,"
  - "to send his armament and"

**GB-R7: VA107 `forts-and-ridges` tags in-battle events as `inherited`.** Lee's "The loss of the
advanced works, however, rendered the others untenable" (p.314) describes the result of Hays's June 14
assault. That is an in-interval, commander-created event, not an inherited condition.

- **Change.** Remove that sentence's citation and clause from `forts-and-ridges` and add them to
  `recorded-result` as "Lee says the loss of the advanced works rendered the others untenable, and the
  enemy retreated in the night."
- **Value replacement.** "Doubleday says Milroy's main forts stood on Applebie Ridge, with rifle-pits
  begun on Flint Ridge to command the western roads. Lee says Early found that an intrenched position
  northwest of the town, near the Pughtown road, would command the principal fortifications."
- **Rationale replacement.** "Works present before or at the start of the frozen interval, per an
  interested history and the opposing commander; Early's reconnaissance and Hays's capture are
  in-interval actions, not inherited conditions. No map verification."
- **Tag.** Keep `inherited`.

**GB-R8: PA002 `reported-force-scope` misstates the scope of Lee's numbers statements.**

- **Evidence.**
  - "Largely superior numbers" is what two of Heth's brigades encountered (p.317, "two brigades were sent
    forward to reconnoiter ... subsequently encountered largely superior num- bers").
  - "Overwhelming numbers of fresh troops" is a risk Lee cites for not attacking: "Without information as
    to its proximity, the strong position ... could not be at- tacked without danger of exposing the four
    divisions present ... to overwhelming numbers of fresh troops." (pp.317–318)
- **Value replacement.** Replace "Lee writes of largely superior numbers on July 1 and of fresh troops in
  overwhelming numbers" with "Lee says two of Heth's brigades encountered largely superior numbers on July
  1, and that attacking that evening, without information on how near the rest of Meade's army was,
  risked exposing his four weakened divisions to overwhelming numbers of fresh troops".
- **Rationale addition.** "The second is Lee's stated risk assessment, not an observed count."

**GB-R9: MD004 `river-and-bridge` drops "partially".**

- **Evidence.** Humphreys (p.4): "the ponton bridge had been partially destroyed by a cavalry detachment
  sent for the purpose by General French".
- **Replacement.** Change "Humphreys says French's cavalry detachment destroyed the bridge during the
  battle of Gettysburg" to "Humphreys says a cavalry detachment sent by French from Frederick partially
  destroyed the ponton bridge during the battle of Gettysburg".

**GB-R10: VA108 `shenandoah-impassable` reverses Lee's statement.**

- **Evidence.** Lee (p.324): "He succeeded in passing part of his command ... As soon as a pontoon bridge
  could be laid down, the rest of his corps crossed the river".
- **Replacement.** Change "and that part of Longstreet's command crossed on a pontoon bridge" to "and
  that Longstreet passed part of his command over the Shenandoah, the rest of his corps crossing once a
  pontoon bridge could be laid".
- **Citation to add.** p.324, "He succeeded in passing part of his command".

**GB-R11: two Humphreys dependency statements are not source-backed.** This affects the dependency
notes of `ia-humphreys-metadata-v1`, `humphreys-ocr-v1` and `humphreys-gettysburg-rapidan-selections-v1`,
and MD004 `command-roles`.

- **Problem 1: "from July 1863".** "Meade's chief of staff from July 1863" does not appear in the
  inspected pages. The title reads "CHIEF OF STAFF ARMY OF THE POTOMAC", and the publisher's list in the
  same OCR (offset ~149333) reads "Chief of Staff, Army of the Potomac, 1863-64".
- **Problem 2: dependence on the printed compilation.** "depending partly on the Official Records
  compilation" is anachronistic.
  - The preface thanks "the Secretary of War for making accessible to me alL the papers of his
    Department" and "Col. Scott, in charge of the preparation of the 'Official Records ...' for
    publication".
  - Volume XXVII Part 2 was printed in 1889, after the 1883 book.
- **Registry fix.** Add `metadata_only` `-v2` revisions, per the evidence contract, with this dependency
  note: "One retrospective history by Andrew A. Humphreys, styled on the title page 'CHIEF OF STAFF ARMY
  OF THE POTOMAC' and in the publisher's list in the same OCR 'Chief of Staff, Army of the Potomac,
  1863-64'; the start date of that role is not established in the inspected pages. An interested
  participant account. By his preface the Secretary of War made the Department's papers accessible to
  him, and he thanks Col. Scott, then preparing the Official Records for publication; Volume XXVII was
  printed in 1889, after this book, so any dependence is on shared underlying papers, not the printed
  compilation. Relationship to later NPS summaries is unestablished."
- **MD004 rationale replacement.** Change "Humphreys was Meade's later chief of staff; his defense of
  Meade is attributed." to "Humphreys was chief of staff of the Army of the Potomac in 1863–64 per his
  publisher's list; the inspected pages do not establish whether he was the unnamed 'Chief of Staff' who
  examined the Williamsport position with Meade (p.6). His defense of Meade is attributed."

## Unresolved and limits

These findings are extraction checks, not historical adjudication. I did not verify the OCR against
print or maps. I also did not verify:

- whether the frozen or live casualty figures are correct;
- whether Doubleday's "division" for Duffié is right;
- how Hanover ended.

All dossiers remain drafts. This review admits no feature and changes no model input.
