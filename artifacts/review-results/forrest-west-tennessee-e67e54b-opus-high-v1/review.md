# Separate review: Forrest's Expedition into West Tennessee (TN009, TN011)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. Started as a fresh-context
  `evidence-reviewer` subagent with no access to the author's conversation. The reviewer cannot see
  its harness task ID.
- **Date:** 2026-09-24 to 2026-09-25 (the review ran across midnight).
- **Commits:** the prepared commit is `e67e54b7d95c880d4fcacbfc4447389eba09c471`, the previous commit is
  `ee1fb45faa68aa2b4b527d0b4cdb6f9db8889f43`, and the assignment bundle and worktree HEAD are
  `e865cffa9390b65fd2015ff19c2f8ce15e950ba2`. The only change from e67e54b to e865cff is the assignment and inputs files.
- **Assignment:** `assignment.md` sha256 `e36ba58f6348251119b1c9659855f45e189d7b9cf82b9b505855796abbbc423a`.
  `inputs.json` sha256 `b2ac12f94a2e68fc49a4aa28bf0ba87c56071b72b2130666eb5157484e8c14d5`.
- **Input verification:** I hashed all 35 bound paths in the worktree and at `e67e54b` with `git show`.
  **35/35 match, with no mismatches.**
- **Status:** This is an AI review. It is not human historical adjudication, independent corroboration
  or feature admission. It changes no model inputs.

## Scope actually inspected

- **Rules and docs.** I read AGENTS.md in full, plus the evidence contract. From the methodology I read the
  boundary/identification, AI-role and admission sections. I also read the ee1fb45→e67e54b diffs of README,
  methodology, roadmap, sources.md, cli.py, tests, quality, the research queue and the pilot report. I did not
  read README, roadmap and sources.md end to end beyond these diffs.
- **Dossiers and memo.** I read both dossiers in full: **18 claims, 61 citation occurrences, 2 null unknowns
  with no citations, and 7/7 dimensions in each**. I also read the memo in full.
- **Frozen rows.** I checked the TN009/TN011 battle, force and commander rows. Every cited CSV cell matches:
  - TN009 CS 400/400
  - TN011 US 3000/3000
  - TN011 CS strength blank
  - Forrest listed as Brigadier General in both records
- **NPS summaries.** I read both retained NPS summaries in full.
- **Source records.** I read all 7 new source records and checked the catalog metadata: identifier, title,
  creator "Jordan, Thomas", date 1868, publisher Blelock, Harvard/Google provenance.
- **Jordan and Pryor selection.** I read all four sections of the selection in full: title/preface with
  Forrest's prefatory note, the outset (pp.193–194), Jackson (pp.196–200) and Parker's (pp.209–216). I read the
  parent OCR only around the section boundaries and page markers (about chars 436,000–496,000 and the start of
  the title/preface).
- **Replays.** Both NPS HTML→text transforms reproduce exactly, and so do their hashes. All four half-open
  Jordan ranges reproduce exactly after split/join collapse. The boundaries are clean: the chapter summary, the
  end of Lexington, the "Battle of Parker's Cross-Roads. 209" running head, and the continuation after p.216.
- **Page-marker map.** OCR markers: 192, 194 (193 is the unmarked opening page of Chapter VII), 195, 196,
  197, 198, 199, 200, 209, `21Q`=210, 211–215, `2l6`=216. "note p. 209" at char 489,223 is a footnote
  cross-reference, not a marker. I placed all 28 Jordan citations mechanically: each quote occurs once in its
  section, and **28/28 page locators match the marker map**.
- **Coverage and registry.**
  - Coverage is 65/127 dossiers, 62 without, and 16/36 complete campaign groups.
  - The registry has 344 records / 341 paths (previously 337/334). All 337 earlier entries are identical.
  - All 63 earlier dossiers are identical, and so are the 18 files in `data/evidence/history`.
  - These are also unchanged: the cohort, both admission proposals, `admission-check.json` (`promoted_rows`
    0, `emitted_rows` []), `baseline.json` (23 battles / 13 groups; Brier 0.2768816348133779 vs 0.25) and
    `battles.json`.
- **Packets and receipt.** The packet JSON blocks parse (3 per packet). The embedded dossier, registry and
  battle record equal the repository files. `receipt.json` checks: 97 input-path hashes and 344 source hashes,
  with 0 mismatches.
- **Next group.** Confirmed independently: Operations Against Vicksburg [December 1862–January 1863], MS003
  and AR006, is the earliest incomplete group (start 1862-12-26).
- **`make check`.** Ran offline: exit 0, 82 tests OK, `admission_promoted_rows` 0. The worktree is clean.
- **Not done.** I did no network access, no new research, no build/packet commands, no whole-book reading, no
  map or print inspection, and no checks of Dunham's report, the Rebellion Record or the Tribune.

## Checks that pass

- **Force scopes.** They stay separate and nothing is adopted:
  - Jackson: detachment approx. 400 (400/400), NPS brigade of 2,100, Jordan about 1,800 at the outset.
  - Parker's: 3,000 for two brigades.
  - The live zeros are flagged as not measuring absence.
- **Results.** Both are correctly `disputed`:
  - Jackson: "repulsed" in NPS against "driven to his intrenchments" in Jordan.
  - Parker's: NPS "Both sides claimed victory".
  - The frozen labels are retained.
- **Casualties.**
  - Jackson: frozen "Total unknown (US 6; CS unknown)" against live CS 0. The note says the zero is not
    measured absence.
  - Jackson: Jordan's ~30 (p.198, sunrise skirmish) and ~500 prisoners (p.199, "several combats") are scoped
    correctly.
  - Parker's: 737 (US 237; CS 500) agrees with the live field, and Jordan's differing figures are kept.
- **Other claims.**
  - The `commander_created` tag on the deception claim is attributed to the Forrest-endorsed history.
  - The effect on Union knowledge is left unestablished.
  - Napier's charge "with- out the orders or wish of his General" (p.212) and the "Halt and surrender!" ruse
    (p.214) are attributed correctly.
  - The unwarned arrival of Fuller is attributed to NPS.
  - The rank conflict (NPS headings "Major General" against the frozen and NPS-narrative Brigadier General) is
    visible and not adopted.
  - No commander gets automatic credit.
- **Dependency.** The registry `dependency_note`, the memo and both `open_questions` say the book is written
  from Forrest's papers and his notes, and that his prefatory note accepts responsibility "for the greater part
  of the statements". They say the book is therefore not independent of him. They also say the reports and
  newspapers quoted inside it are not separate families.
- **Terrain claims.** `jackson-works` as `inherited` is sound: pre-existing works, Jordan p.196.

## Required corrections

### FWT-R1 — TN011: Dunham-report and newspaper figures are misattributed; new citations needed

**What is wrong:**
- **1,554 is the book's total, not a quoted figure.** Jordan p.211 attributes the regimental components to
  "the official report of CoUmel C« T. Dunham" (405 + 525 + 529 + 65 + 30). The book then totals them: "or a
  total of 1554 men". The arithmetic reproduces.
- **1,824 is the book's inference, not a newspaper's figure.** The Chicago Tribune correspondent gives only
  two regimental figures, 604 and 600. The book says these "would make the brigade 1824 strong".
  Substituting them into the OCR components gives **1,704**, so the printed 1,824 does not reproduce. The OCR
  has not been checked against print.
- **The 8,000 is paraphrased, and it is pre-battle.** The book writes "Colonel Dunham states he had learned
  at Clarksburg" that the force was 8,000. That is a paraphrase, not a quotation, and it is timed to
  Clarksburg before the battle.
- **The arriving force is a source difference.** Jordan says "two brigades of the enemy" (p.214) and "two
  fresh brigades" (p.216) arrived. NPS names only "Fuller's Union brigade arrived from the north". The
  existing rationale follows NPS alone.

**Other gaps:**
- The value's "never exceeded" rests on p.216, which is not cited.
- The structured `strength_max` is not cited.
- Carroll's report to Forrest is not cited.

**Replacements** (all quotes verified unique in their section or file, and pages verified against the marker
map):

`TN011 reported-force-scope`:
- **value:** "The frozen force text gives two Union brigades of approx. 3,000 (structured US bounds
  3,000/3,000) and a Confederate expeditionary brigade; the live field reads 3000 total (US 3000; CS 0;).
  Jordan and Pryor say the Confederates present did not exceed 1,200 with six guns and at no moment in the day
  exceeded twelve hundred, against a Federal brigade, battery and cavalry detachment of not less than 1,800.
  They total regimental figures attributed to Dunham's official report as 1,554, and say a Chicago Tribune
  correspondent's figures for two regiments (604 and 600) would make the brigade 1,824. They describe the
  later Federal arrival as two fresh brigades; NPS names Fuller's brigade."
- **rationale:** "Brigade, army and reported figures differ in scope and timing. The 1,554 and 1,824 totals
  are the book's arithmetic from figures it attributes to Dunham's report (not inspected) and a newspaper;
  substituting 604 and 600 into the OCR components gives 1,704, so the printed 1,824 does not reproduce (OCR
  not checked against print). The book's two arriving brigades differ from NPS's Fuller brigade. None is
  adopted as matched opening strength."
- **Keep** all 7 existing citations. **Add:**
  - `arnold-cwsac-forces` {battle TN011, belligerent US} `strength_max` "3000"
  - `parkers-cross-roads` p.211 "reports the strength of the Fif- tieth Indiana at 604 men and the One Hundred and Twenty-second Illinois at 600"
  - `parkers-cross-roads` p.216 "by a force at no moment in the day exceeding twelve hundred"
  - `parkers-cross-roads` p.216 "and finally by two fresh brigades."
  - `parkers-cross-roads` p.214 "down upon him, two brigades of the enemy"
  - `nps-tn011-v1` Description "Fuller's Union brigade arrived from the north"

`TN011 warning-failure`:
- **value:** "NPS says Confederate security detachments failed to warn of Fuller's approach; Jordan and Pryor
  say Colonel Carroll informed Forrest that a fresh and superior force had reached the field, and that Forrest
  was within eighty yards of its line before he could discover it. They also say Dunham's report states he had
  learned at Clarksburg that the Confederate force was 8,000 strong with 12 guns."
- **rationale:** "Retrospective accounts of what each side knew. Dunham's statement is paraphrased inside the
  book (report not inspected) and concerns information he had at Clarksburg before the battle, not his
  knowledge during it."
- **Replace** the p.211 citation with "Colonel Dunham states he had learned at Clarksburg that the Confederate
  force was 8000 strong, with 12 pieces of artillery".
- **Add** p.213 "informed his leader that a fresh and superior force of Federals had reached the field".

**Memo** (`docs/research/forrest-west-tennessee-first-pass-v1.md`), Decisions bullet 1:
- **Replace** "Jordan and Pryor say the Confederates never exceeded 1,200 against Dunham's brigade of at least
  1,800, quoting Dunham's own 1,554 and a newspaper's 1,824."
- **With** "Jordan and Pryor say the Confederates never exceeded 1,200 against at least 1,800 Federals; they
  total figures attributed to Dunham's report as 1,554 and use a newspaper's two regimental figures to reach a
  printed 1,824, which the OCR components do not reproduce (1,704)."

Memo, Command bullet:
- **Replace** "Dunham's reported belief in 8,000 Confederates"
- **With** "Dunham's reported pre-battle information at Clarksburg of 8,000 Confederates".

### FWT-R2 — TN009 `railroad-objective`: the sources disagree on when the raids happened, and the claim hides it

**What is wrong:**
- **NPS frames the concurrency as Forrest's view.** NPS says: "To Forrest, the fight amounted to no more than
  a feint and show of force intended to hold Jackson's Union defenders in place while two mounted columns
  destroyed railroad track". The value turns that into the fact that Forrest "held Jackson's defenders in
  place while..." the columns worked.
- **Jordan puts the raids before the fight.** Forrest reached Jackson "on the afternoon of the 18th" (p.196)
  and detached the columns "at eight o'clock at night" (p.196). They captured stations about 2 a.m. and
  returned "about daylight" (p.197). All of this came before the skirmish that began "About sunrise" (p.198).
- The shared objective is supported. The timing is a source disagreement.

**Replacements:**
- **value:** "NPS says Forrest wished to interrupt Grant's rail supply line and that, to Forrest, the Jackson
  fight was a feint to hold the defenders in place while two mounted columns destroyed track north and south of
  the town. Jordan and Pryor say detachments sent out at eight o'clock the previous night broke the railroad,
  captured stations and returned about daylight, before the sunrise skirmish."
- **rationale:** "Stated objectives from a summary and a commander-endorsed history; no inspected order. Both
  describe railroad destruction, but NPS makes the raids concurrent with the fight while Jordan and Pryor place
  them on the night of December 18–19, before it. The sequence is unresolved and no holding effect is
  established."
- **Status:** stays `supported`.
- **Replace** NPS quote 2 with "To Forrest, the fight amounted to no more than a feint and show of force
  intended to hold Jackson's Union defenders in place".
- **Keep** "while two mounted columns destroyed railroad track north and south of the town" and the p.197
  quote. **Add:**
  - `jackson-operations` p.196 "at eight o'clock at night, de- tached Colonel Dibrell"
  - `jackson-operations` p.197 "to their positions about daylight with their captures"
  - `jackson-operations` p.198 "About sunrise the enemy threw forward a strong line of skirmishers"

### FWT-R3 — TN009 `armament-shortfall`: one `inherited` tag covers two different kinds of claim

**What is wrong:** The claim combines two things:
- The outset shortfall (p.194), which is inherited at any Jackson boundary.
- Arms captured by detachments Forrest himself ordered out on the night before the skirmish and then
  distributed (pp.196–197). Jordan also places Forrest's arrival and first skirmishing at Jackson on the
  afternoon of December 18.

With both replacement boundaries null, the captured-arms part could be inherited or commander-created. The
methodology requires uncertain classifications to stay `unresolved`.

**Replacements:**
- **phase:** `unresolved`.
- **rationale:** "Combines an outset condition (inherited at any Jackson boundary) with arms captured by
  detachments Forrest ordered out the night before the December 19 skirmish and distributed on their return;
  Jordan and Pryor place his arrival and first skirmishing at Jackson on the afternoon of December 18. With
  replacement boundaries unset, the captured-arms part may be inherited or commander-created. From the
  commander-endorsed history; no ordnance return inspected."
- **Keep** the value and citations.
- **Memo:** replace "Jackson's works and Forrest's armament shortfall at the outset are tagged `inherited`."
  with "Jackson's works are tagged `inherited`; the armament claim combines the outset shortfall with arms
  captured by Forrest-ordered night raids and stays `unresolved` while boundaries are unset."

The claim, unknown and citation counts in the README, roadmap and report would change only as follows:
- **R1:** 61 → 68 citations. It adds 6 citations to `reported-force-scope` and 1 to `warning-failure`, and
  replaces one quote.
- **R2:** 68 → 71 citations. It adds 3 and replaces 1.
- **R3:** no change in counts.

The primary should recount after applying them.

## Advisory (not required)

- **A1** TN009 `deception-of-numbers`: the word "captured" (drums) comes from a cropped footnote, "These drums
  had been recently man … iptnred". Either drop "captured" or cite that footnote as OCR-uncertain.
- **A2** TN011 `casualty-records`: Jordan scopes the Confederate losses to "In the several conflicts of the
  day, between the hours of six A.M. and three p.m." (p.215). Consider adding that timing to the rationale.
- **A3** TN009 strength: the p.197 footnote gives Jordan's estimates of the Jackson garrison ("not … less than
  10,000 infantry", and the Tribune's 13,000/5,000). These are a different population from the two engaged
  regiments. Consider mentioning them, without adopting them.
- **A4** Name and date details:
  - The NPS TN009 heading says "Colonel Adolphus Englemann", while the frozen record and the NPS narrative say
    "Adolph".
  - NPS dates its 2,100 to the December 15–17 river crossing, while Jordan dates his 1,800 to the outset.
  - Both could be noted.
- **A5** Parker's: Jordan's "numerous white flags" and "capitulation" (p.213), and the chapter summary
  "capitulatiug en masse", sit alongside NPS's "Dunham refused". Consider noting this in the result or command
  rationale.
- **A6** README: "all two frozen Forrest's West Tennessee expedition records" should read "both frozen …
  records".

Checked and not adopted: the p.197 footnote "Confederate loss was three privates killed and five wounded" is
positioned with Lexington context. The dossier correctly does not assign it to Jackson.

## Outcome

**Corrections required: FWT-R1, FWT-R2, FWT-R3.** The advisories A1–A6 are optional. All other extraction,
locator, replay, hash and invariant checks pass. The dossiers remain drafts, the baseline is unchanged, and no
features are admitted.
