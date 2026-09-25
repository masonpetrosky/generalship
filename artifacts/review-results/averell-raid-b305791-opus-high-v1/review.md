# Separate review: Averell's Raid first pass (WV012, Droop Mountain)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, fresh-context subagent. This is an AI review. It is not human historical adjudication, independent corroboration or feature admission.
- **Date:** 2026-09-25
- **Commits:** prepared `b305791dc888d7c9569a6132dfd2a1c36246a775`; previous `216d15ec2c0bc3782f3564c65aca318bfef7a6b9`; review bundle / worktree HEAD `e18b7f36732ee4b079be347dfc24a6347c431e6d`.
- **Assignment:** `assignment.md` sha256 `eeba25db5f8965da151fa332de9a607e446c4a832b8fb0bce93713f810732e45`. **Input manifest:** `inputs.json` sha256 `7e33cd417ae836fc9b36e306cf028e24315407b57a229967108f99ccd1f2fb99`.
- **Outcome: corrections required** (R1–R4; all are extraction or wording fixes inside WV012 and its memo. None changes model inputs.)

## Coverage actually inspected

- **Input hashes:** I checked all 30 bound paths against `git show b305791:<path>`, and all 30 match. Each worktree copy is byte-identical to the prepared commit, so no bound path differs.
- **Guidance:** I read AGENTS.md, the evidence contract, the Averell's Raid memo, and the prepared-commit diffs of README, methodology, roadmap, sources.md, cli.py and test_evidence.py. I did not reread the older roadmap/sources history.
- **Dossier:** I read `data/evidence/WV012.json` in full: 9 claims, 44 citation occurrences, 1 null unknown (`opening-personnel-unknown`, with no citations), and all seven dimensions.
  - **Quote location:** Every quote is unique in its cited section, NPS text or CSV cell.
  - **CSV rows:** The frozen rows are one battle row (`Brigades`, `Union victory`, `526 total`), two force rows with blank strength/casualty fields, and two commander rows. Both commanders are `Brigadier General`.
- **Sources read in full:** the NPS WV012 text, the Averell selection (title, heading, November 7 and November 17 sections) and the Echols selection (November 19). I also read parent context at the selection boundaries: the No. 2 return header, Averell's November 14 report and the November 8 Duffié inclosure. None of them contradicts the dossier.
- **Derivative replay:**
  - **NPS:** I re-derived the NPS text from its HTML with the recorded HTMLParser transform, and the result is byte-exact.
  - **OR selections:** Every section of both OR selections equals the recorded half-open ranges of `data/raw/bristoe-v1/or29-1-full.txt` after whitespace collapse.
  - **Parent file:** The parent hash is `bf4c70d5…ff7`. It is unchanged since the Bristoe commit.
- **Page markers:**
  - **Averell:** The November 7 dispatch lies between the parent's 503 and 504 headers. The November 17 report runs from p.504 through p.508.
  - **Echols:** The report runs from p.528 through p.532. The 528 header precedes the report's start offset, and p.533 follows its end.
  - **Locators:** All 36 OR locators match the page computed from the in-section markers. No locator depends on a missed or misread header. The "W. YA.3", "XLL" and "XU." OCR variants are running-header noise only.
- **Counts:** At the prepared commit I confirmed the following.
  - **Dossiers and groups:** 118/127 dossiers, with 9 missing (GA005, TN023–TN029, VA044). Groups by presence: 32/36 complete.
  - **Registry:** 545 records / 526 paths. The previous 541/522 are preserved; all 541 older entries are identical and only the 4 new IDs were added.
  - **Unchanged files:** The only files under `data/`+`artifacts/` that changed are WV012 additions and the regenerated reports. All 117 older dossiers and all `history/` revisions are unchanged. So are the cohort, both admission proposals, `admission-check.json`, `baseline.json` and `battles.json`.
  - **Baseline:** 23 eligible engagements in 13 groups, with Brier 0.2768816348133779 against 0.25. `promoted_rows` is 0.
- **Next group:** I independently confirmed it by earliest start date among incomplete groups: Longstreet's Knoxville Campaign (1863-11-16) with TN023, TN025 and TN026.
- **Packet and receipt:**
  - **Packet:** The three JSON blocks in `artifacts/research/WV012.md` parse. The draft block equals the dossier, and the registry block equals `data/sources.json`.
  - **Receipt:** All 768 receipt hashes match the prepared-commit bytes. The receipt covers all 202 evidence files.
- **`make check`:** I ran it offline, and it passed: 82 tests OK, 118 draft dossiers, 0 promoted rows, `artifacts_written: false`. I ran no build or packet commands.

**Confirmed without correction:**
- **Scope:** The scope note correctly excludes the November 5 Mill Point skirmish, Duffié's column and the later march.
- **Strength figures:** All strength figures (1,175; 4,000; 1,700; 7,000; 3,500; nearly 10,000) are attributed to the right commander and none is adopted. The live zero is not treated as measured absence.
- **Casualties:** The frozen 526 and live 415 (140/275) figures are kept visible. So are Averell's ~100 and ~250 and Echols's 275 killed, wounded and missing; the note that 275 equals the live CS figure does not imply dependence.
- **Command credit:** The success credited to Moor and the ~4 p.m. withdrawal order are correctly attributed to Averell and Echols respectively. No automatic or additive commander credit is given.
- **Sources and tags:** The interested-account labels, the three-family grouping (with the OR volume as a shared container) and the phase tags are sound.

## Required corrections

**R1 — `mountain-and-breastworks` value: silent OCR correction, uncited figure, dropped qualifier.**
- **Problem:** The value says "cultivated nearly to the summit 2½ miles from the foot". The OCR reads "partially cultivated nearly to the summit, a distance of 2| miles". The ½ is an unreported correction, the distance is not cited, and "partially" was dropped.
- **Replacement clause:** "says the northern slope was partially cultivated nearly to the summit, a distance the OCR reads as \"2| miles\" from the foot (fraction not checked against print),"
- **Add citation:** `{"source_id": "or29-1-averell-droop-mountain-selections-v1", "section": "averell-1863-11-17", "locator": "p.505 (OCR page markers; not checked against print)", "quote": "a distance of 2| miles from the foot."}`

**R2 — `recorded-result`: "otherwise controlled retreat" is not entailed; Echols's admission of detached men is omitted.**
- **Problem:** The cited passage supports only the horse-holder confusion. On p.530 Echols also says some men "became detached and made their way out through the woods". The claim is a disputed characterization, so both sides of that dispute should be shown.
- **Replacement sentence:** "Echols says he ordered the troops to fall back slowly, that on the 4-mile mountain road an alarm produced some confusion among the horse-holders of the dismounted cavalry and some men became detached and made their way out through the woods, and that the rear guard held the pursuit in check; he judges the expedition's results to the enemy at nothing."
- **Add three citations** (section `echols-1863-11-19`, locator "p.530 (OCR page markers; not checked against print)"):
  - "at about 4 p. m. I gave orders to the troops to fall back slowly,"
  - "some of the men of the com- mand became detached and made their way out through the woods."
  - "but were held in check by our rear guard of cavalry,"
- **Memo:** In the memo, replace "Echols describes some confusion in an otherwise controlled withdrawal." with "Echols describes an ordered slow withdrawal, some confusion among horse-holders, some men detached through the woods and a rear guard checking the pursuit."

**R3 — `marches-and-ammunition`: second 14-mile march uncited; detached battalion and post-battle timing not stated.**
- **Problem:** The cited quote for the second march is only "I accordingly moved my brigade at 2 a. m.,". The 14 miles and the detachment of the Twenty-sixth Battalion are in the next sentence. Averell's ammunition statement comes from the November 7 dispatch, written after the battle.
- **Replacement for the first sentence:** "Echols says his brigade marched 14 miles on the 5th and, moving at 2 a.m., reached Jackson's position about 9 a.m. having marched 14 miles, except the Twenty-sixth Battalion, detached with one gun some 12 miles from the position to hold another road; his artillery and trains came away safely except a howitzer whose carriage broke during the retreat."
- **Replacement for the last sentence:** "In his November 7 dispatch, the day after the battle, Averell reported his troops in excellent spirits with plenty of ammunition."
- **Rationale append:** "Averell's statement is a post-battle report, not a pre-battle supply return; Echols's trains statement concerns the retreat. The detachment bears on who was present but is not a strength count."
- **Add two citations** (section `echols-1863-11-19`, locator "p.529 (OCR page markers; not checked against print)"):
  - "The brigade reached the point designated about 9 a. m., having marched 14 miles,"
  - "which was detached with one piece of artillery some 12 miles from the position,"

**R4 — `turning-attack-and-raid-aims`: "avoided pressing" and "held the right" overstate the text.**
- **Problem:** Averell says it was "not thought proper to press the enemy vigorously". The printed sentence contains the editorial "[not ?]", and he also tried to cut off Jackson's retreat. On the 6th, the demonstration was made "to divert the enemy's attention".
- **Replacement for Averell's portion:** "Averell says a direct attack was thought difficult, so he sent the infantry to attack the Confederate left and rear while a demonstration on the right diverted attention; for the 5th he says it was not thought proper to press the enemy vigorously, in order to keep him as far as possible from Lewisburg and to gain the advantage of Duffié's arrival there (the printed sentence contains an editorial \"[not ?]\"), though three mounted regiments tried unsuccessfully to cut off Jackson's retreat."
- **Add three Averell citations** (section `averell-1863-11-17`):
  - "To divert the enemy's attention from this," (p.506)
  - "and [not ?] to permit him to be re-enforced from that direction," (p.505)
  - "An attempt was, however, made to capture the force under Jackson by sending three mounted regiments to cut off his retreat." (p.505)

I verified every proposed quote: each occurs exactly once in its cited section, on the stated OCR page.

## Advisory (not required)

- **A1 — Averell's own-force figure.** The rationale in `reported-force-scope` and the memo say "Each commander gives/assigns the larger number" to the opponent. Averell's only figure for his own side is the 1,175-man infantry column, not his total force. Consider adding: "Averell gives no total for his own force."
- **A2 — Memo list omits 3,500.** The memo's "none adopted" list leaves out Jackson's 3,500 as reported by Echols. The dossier includes it.
- **A3 — Live commander citation.** `command-roles` says "frozen and live commanders" but cites only the CSV. The NPS text lines "Brigadier General William Averell [US]" and "Brigadier General John Echols [CS]" could be cited.
- **A4 — Inclosure and boilerplate wording.** Duffié's November 8 inclosure is printed after the November 17 report but falls outside the selected range. The boilerplate "letters inclosed with a report are part of that report" could therefore mislead. The registry inspection note discloses that the inclosure was read and not selected. Leave the raw snapshot unchanged; clarify it only through a versioned metadata revision if desired.

## Unresolved (retained, not errors)

The following stay open, as the dossier records:
- Opening strength.
- The frozen 526 against the live 415.
- Averell's "about 100" against the garbled No. 2 return.
- The rout versus withdrawal characterization.
- The reports of Moor, Jackson, Patton and Duffié.
- Maps and print verification.

No extra depth is required for this first pass.
