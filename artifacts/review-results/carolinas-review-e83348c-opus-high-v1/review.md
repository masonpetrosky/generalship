# Carolinas Campaign first pass: separate AI review

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a fresh-context subagent working only from the assignment and the repository.
- **Date:** 2026-09-25.
- **Bundle commit (worktree HEAD):** `63792ac36e59eb4b9ce9ec8ac9681d36d6d0e741`.
- **Prepared commit reviewed:** `e83348c4911c949390d89b96262a175eb9053f70`, against `a2be26f`.
- **Assignment:** `assignment.md`, sha256 `7ddb441c3a6fefa60ff7d5c9d2d933d0710f98468e27758f5c36f0186b6c3f5c`.
- **Input manifest:** `inputs.json`, sha256 `541007bd515f76a884c8caebfb066fc82ec49af6faff177a878f1c94e15ae589`.
- **Input verification:** I checked all 47 bound paths against `git show e83348c:<path>` and against the worktree files. There were **0 mismatches**.
- **Outcome:** **corrections required.**
  - Required: CAR-R1 to CAR-R5.
  - Advisory: CAR-A1 to CAR-A8.

This is a separate AI analysis. It is not human historical adjudication, proof of source independence or feature admission. I did no new research, opened no new source families and did not modify any primary artifact.

## Scope actually inspected

- **Guidance.** I read AGENTS.md; the research-depth, coverage and AI-validation sections of `docs/methodology.md`; `docs/evidence-contract.md`; `docs/cohort-v2.md`; the policy part of `docs/sources.md` and its Carolinas diff; and the memo `docs/research/carolinas-first-pass-v1.md` in full.
- **Dossiers.** I read all five dossiers (SC011, NC017, NC018, NC019, NC020) in full: 45 claims, 5 null unknowns and 292 citations. I checked these counts, the 16 disputed claims, the 7 dimensions per record and the cited independence groups with a script. Every non-CSV quote was read against its full surrounding passage.
- **Frozen rows and NPS pages.** I read the frozen `cwsac_battles`, `cwsac_forces` and `cwsac_commanders` rows for all five records, and all five NPS text snapshots in full. I did not render the NPS HTML parents; the `make check` hash checks cover their bytes.
- **Selection files.** I read all ten selection files in full: Blair, Harrison, Cox report, Cox history (title and Kinston), Bragg, Kilpatrick, Wheeler, Slocum, Hardee, Johnston, and the No. 3 return up to its totals.
- **Full OCR parent (`or47-1-full.txt`).** I consulted it only at targeted points:
  - the p.1055 running head (it reads "CAROLINA S. 1056", which supports the inferred p.1055);
  - Johnston's March 11 letter at p.1053, the source of the Bragg "about 7,000" and "about 500" figures cited in the NC017 open question.
- **Page locators.** A script compared every OR citation's locator with the last OCR page marker before its quote in the section. It found no mismatches.
- **Registry.** I read all 23 Carolinas source records. I also read the six metadata-only successors the same commit adds from the Franklin-Nashville/Savannah reconciliation (NASH-R1 to R3), including their diffs against their predecessors. I checked the registry for other records by the same authors (Kilpatrick, Wheeler, Hardee, Johnston, Bragg, Cox, Blair, Slocum and Harrison).
- **Validation.** `make check` passes offline: 134 tests OK, and `python3 -m generalship check` succeeds with `artifacts_written: false`. That run also regenerates `__pycache__` bytecode (ignored by git), and `git status --short` was clean afterwards apart from this review file.
- **Not inspected:**
  - any source outside the bound selections;
  - the remaining pages of the full OR parent, the Cox parent OCR and Cox Chapters X–XI;
  - print facsimiles;
  - the Franklin-Nashville, Savannah and Atlanta dossiers.

  I noted that local `origin/main` is at `dc7ca50` ("Reconcile the Opus review of the Franklin-Nashville and Savannah passes"), which is later than the bundle. I did not inspect that commit.

## Overall assessment

Extraction quality is high:

- Quotes are exact and are read in context.
- Opening strengths stay null in all five records.
- Campaign-wide figures (Blair 384, Kilpatrick 604 and 5,068, Slocum 2,352, Wheeler's effective totals) are kept out of the records.
- No claim is tagged `inherited`.
- No listed commander gets automatic credit.
- Each record uses three families, plus the No. 3 return as its single follow-up where one is used.

The No. 3 return totals check arithmetically:

- Kinston: 5+60+25+294+23+930 = 1,337.
- Bentonville: 12+182+67+1,045+7+214 = 1,527.
- Averasborough: 682 = 116 + 485 + 81 in the recapitulation's aggregate column, so the positional reading is sound.

The required corrections are one registry-grouping problem (R1–R2, created by the NASH successors in the same commit) and three places where the value text goes beyond its passage or scope (R3–R5).

## Required corrections

### CAR-R1: Kilpatrick's Carolinas report is registered in a retired author group

**Problem.** The same prepared commit adds `or44-kilpatrick-selections-v2` (NASH-R3), which moves Kilpatrick's Savannah report into `kilpatrick-atlanta-reports`.

- After that change, the only other member of `kilpatrick-savannah-report` is the superseded `or44-kilpatrick-selections-v1`.
- Yet `or47-1-kilpatrick-carolinas-selections-v1` is placed in `kilpatrick-savannah-report`, "the most recent".
- Its dependency note describes the pre-NASH state.

The memo repeats this ("Kilpatrick joins `kilpatrick-savannah-report`"), and it lists Kilpatrick among authors with two groups. The number of families within NC018 does not change, but the registry now contradicts the author-family decision made in the same commit.

**Fix.** The v1 record is already on `main`, so add a `metadata_only` successor `or47-1-kilpatrick-carolinas-selections-v2`. It keeps the same path, hash, format and parent hash.

- `supersedes`: `or47-1-kilpatrick-carolinas-selections-v1` together with its entry hash.
- `independence_group`: `kilpatrick-atlanta-reports`.
- `dependency_note`: replace the sentence "Kilpatrick already has registered author groups kilpatrick-atlanta-reports and kilpatrick-savannah-report; this report is placed in the latter, the most recent, and the two groups are one author family." with:

  > "The same author's Lovejoy raid dispatch and report (or38-2-kilpatrick-lovejoy-selections-v1) and his Savannah report (or44-kilpatrick-selections-v2, moved from kilpatrick-savannah-report by NASH-R3) are registered in group kilpatrick-atlanta-reports; following the Humphreys precedent, this report is placed in that author family, whose name reflects the earlier reports."

- Repoint all NC018 citations of the v1 ID to v2.

**Memo.** Replace "Kilpatrick joins `kilpatrick-savannah-report`." with "Kilpatrick joins `kilpatrick-atlanta-reports`, where NASH-R3 placed his Savannah report." Then remove the Kilpatrick bullet from the "more than one registered group" list.

### CAR-R2: Cox's report and Carolinas selection use a retired group and a superseded parent

**Problem.** The same commit adds `cox-march-ocr-v2` and `ia-cox-march-metadata-v2` (NASH-R2), which move *The March to the Sea* into `cox-atlanta-1882`. However:

- `or47-1-cox-kinston-selections-v1` and `cox-carolinas-selections-v1` both stay in `cox-march-to-the-sea-1882`. Every other member of that group is now superseded.
- `cox-carolinas-selections-v1` has `parent_source_id: cox-march-ocr-v1`, which is superseded.
- Its dependency note still says "Cox's earlier volume Atlanta is not registered in this pass", which NASH-R2 found false.

**Fix.** Add `metadata_only` successors for both records. Keep the raw bytes, and keep the parent hash `63813545…bc499` for the book selection.

- **`cox-carolinas-selections-v2`:**
  - `independence_group`: `cox-atlanta-1882`.
  - `parent_source_id`: `cox-march-ocr-v2`.
  - `dependency_note`: replace the final sentence "Cox's earlier volume Atlanta is not registered in this pass." with the corresponding final two sentences of `cox-march-ocr-v2`'s note, starting "Cox's earlier volume Atlanta (Campaigns of the Civil War IX, 1882) is registered as ia-cox-atlanta-metadata-v1, cox-atlanta-ocr-v1 and cox-atlanta-selections-v1 …" and ending "The two books are one author family, not independent witnesses."
- **`or47-1-cox-kinston-selections-v2`:**
  - `independence_group`: `cox-atlanta-1882`.
  - `dependency_note`: replace "Cox's 1882 history The March to the Sea; Franklin and Nashville is registered in group cox-march-to-the-sea-1882, whose dependency note assigns any later use of his official reports to that author family; this report is placed there." with:

    > "Cox's 1882 histories Atlanta and The March to the Sea; Franklin and Nashville are registered in group cox-atlanta-1882 (the latter moved there from cox-march-to-the-sea-1882 by NASH-R2), whose dependency notes assign any later use of his official reports to that author family; this report is placed there."

- Repoint the NC017 citations to both v2 IDs.

**Memo.** Replace "Cox's report joins `cox-march-to-the-sea-1882`" with "Cox's report joins `cox-atlanta-1882` (NASH-R2)".

**Unchanged.** Treating Cox's report and history as one family at Kinston is sound.

### CAR-R3: NC017 `command-roles` over-attributes the dispositions of March 8–10 to Cox

**Problem.** The value says Cox "ordered the March 7 advance and the dispositions of the 8th–10th". Only the March 7 order is cited. In the passage:

- On the 8th, with the department commander beside him, Cox states the orders in the passive voice ("General Carter was at once ordered…", "he and General Palmer were directed…").
- The 10th is also passive.
- Only on the 9th does he write in the first person.

Because the frozen commander is Schofield and his presence is disputed, this attribution matters.

**Fix, value.** Replace "Cox reports that he ordered the March 7 advance and the dispositions of the 8th–10th, and that the general commanding the department" with:

> "Cox reports that he ordered the March 7 advance and, on the 9th, sent Thomas' brigade to support Palmer's flank and ordered the breastworks extended to the left; most orders of the 8th and 10th are stated in the passive voice. He reports that the general commanding the department"

**Fix, citations.** Add two citations, each with source `or47-1-cox-kinston-selections-v1` (or its v2 from R2), section `cox-1865-05-16` and locator "p.978 (OCR page markers; not checked against print)":

- "induced me to send Thomas’ brigade, of Ruger’s division, to support that flank,"
- "I ordered the line of breast-works to be well extended to the left,"

### CAR-R4: NC018 `command-roles` misreads Kilpatrick's "gaining" and adds a personal lead he does not claim

**Problem.** The value says Kilpatrick "regained the cavalry camp on foot and led the counterattack". The cited passage says he *reached* the camp on foot ("On foot I succeeded in gaining the cavalry camp a few hundred yards in the rear"). His men were then "forced back some 500 yards farther to a swamp". The counterattack is narrated in the first person plural ("We rallied…", "We retook the cavalry camp").

**Fix, value.** Replace "and that he himself regained the cavalry camp on foot and led the counterattack;" with:

> "and that he reached the cavalry camp a few hundred yards in the rear on foot, after which his men, forced back to a swamp, rallied, advanced and retook the camp and the artillery;"

**Fix, citations.** Add two citations, each with source `or47-1-kilpatrick-carolinas-selections-v1` (or its v2 from R1) and section `kilpatrick-march`:

- "We rallied and at once advanced upon him.", locator "p.861 (OCR page markers; not checked against print)";
- "We retook the artillery,", locator "p.862 (OCR page markers; not checked against print)".

### CAR-R5: NC020 `casualty-records` states the 2,462 recapitulation without its out-of-interval rows

**Problem.** The addenda table "Casualties at Bentonville" whose recapitulation totals 2,462 includes a row for Hoke on **March 22** (6) and a cavalry row for **March 18 to 21** (113). Both fall outside the frozen March 19–21 interval. The value presents 2,462 beside the three-day letter figure and the 2,606 statement without noting this. The 2,606 statement is headed March 19 to 21.

**Fix, value.** Replace "the recapitulation in his addenda totals 2,462 (239 killed, 1,550 wounded, 673 missing), with a compiler's footnote that the next statement shows 1,694 wounded; that statement's legible grand total ends '239 1,694 2, 606'." with:

> "the 'Casualties at Bentonville' table in his addenda, whose rows include Hoke's division on March 22 (6) and the cavalry for March 18 to 21 (113), recapitulates 2,462 (239 killed, 1,550 wounded, 673 missing), with a compiler's footnote that the next statement shows 1,694 wounded; that statement, headed March 19 to 21, has a legible grand total ending '239 1,694 2, 606'."

**Fix, rationale.** Append: "The 2,462 table includes rows dated March 22 and March 18 to 21, outside the frozen interval; it is not a strict three-day total."

**Fix, citations.** Add four citations, each with source `or47-1-johnston-carolinas-selections-v1` and section `johnston-addenda`:

- "Casualties at Bentonville.", locator "p.1059 (OCR page markers; not checked against print)";
- "March 22 : Hoke . 1 3 2 6", locator "p.1059 (OCR page markers; not checked against print)";
- "March 18 to 21 ; Dfl.vnlry . . . . . . _ . 15 '80 18 113", locator "p.1059 (OCR page markers; not checked against print)";
- "Caaualties in the Confederate forces near Bentonville, N. C., March 19 to 21, 1865.", locator "p.1060 (OCR page markers; not checked against print)".

All eight new quotes in R3–R5 occur exactly once in their sections (checked by script).

## Advisories (optional; no change required)

- **CAR-A1 (NC017, NPS rank).** The live page lists "Major General Braxton Bragg [CS]" against the frozen rank "General". Neither the dossier nor the memo records this, although the other rank conflicts are recorded. Optional: add the citation `nps-nc017-v1`, Principal Commanders, "Major General Braxton Bragg [CS]" to `command-roles`, with the phrase "the live page gives Bragg as Major General".
- **CAR-A2 (NC019, information).** Hardee's 1.30 a.m. dispatch of March 17 (already in a cited section) relays Hampton's view of the force engaged. Slocum describes four divisions, two from each corps. This perception is not extracted, and it could be added to `contact-and-dispatches`. The quote is: "General Hampton says all the army has crossed except the Fourteenth Corps and one division of the Twentieth Corps, which were on the plank road, and which we fought yesterday."
- **CAR-A3 (NC019, the 682 reading).** The positional reading can be strengthened in the rationale: the recapitulation's aggregate column reads 116 + 485 + 81 = 682. The 485 also matches the Twentieth Corps total line.
- **CAR-A4 (NC018, dispute framing).** Kilpatrick's "Hampton led the center division (Butler's)" and Wheeler's "I took command of my own and Butler's cavalry" are in tension but not strictly incompatible. Keeping the claim disputed is acceptable; the rationale could say so.
- **CAR-A5 (NC020, guns).** Johnston implies four Union guns were taken on the 19th: three brought off, "a fourth was left". Slocum says the Confederates were "capturing three pieces of artillery" (in the cited section). This small difference is not recorded as a dispute.
- **CAR-A6 (NC020 and memo, Right Wing timing).** Slocum also reports Hazen's Fifteenth Corps division arriving on the morning of the 20th ("General Hazen, of the Fifteenth Corps, with his entire division, arrived on the field"). The memo's "Slocum says the Right Wing arrived on the 21st" should not be read as "no Right Wing troops before the 21st". The dispute with Johnston concerns March 19 and is correctly framed in the dossier.
- **CAR-A7 (registry wording, `or47-1-blair-salkehatchie-selections-v1`).** The dependency note says the crossing "at Rivers' Bridge" was made by the First and Fourth Divisions. Blair puts Smith's Fourth Division crossing "at a point about midway between the two bridges". Adjust at the next revision. SC011's "on February 3" for Mower's daylight work is a sound inference from the sequence, since the next paragraph dates the following morning February 4. The rationale could say that it is inferred.
- **CAR-A8 (memo accuracy).**
  - The dispute list for Averasborough omits the live CS 865 (the dossier records it).
  - The registry diff at `e83348c` adds 29 records, the 23 Carolinas records plus six NASH successors. The commit message says so, but the memo and `docs/sources.md` do not.

## Answers to the assignment's source questions

- **No. 3 return as the single targeted follow-up.** Sound. It is a compiler's table from nominal lists, not an interested narrative. It addresses the most consequential gap: the frozen and live Union casualty figures conflict in all three records, and Cox's and Slocum's reports carry footnotes pointing to it. Each record uses it once, beyond three families. The registry correctly says it is not independent of the NPS figures that match it, and that only the grand totals are relied on.
- **Authors with several groups placed in the most recent one.**
  - Acceptable in principle for Johnston, Bragg, Hardee and Wheeler. Under `docs/sources.md`, groups by the same author are one witness family, whatever their names, and each dependency note names the other groups.
  - Hardee's `or-beauregard` documents are properly left unmerged: that group is Beauregard's container, not a Hardee author group.
  - Kilpatrick fails: "most recent" selects a group that the same commit retired (R1).
  - Cox's report in the Cox book group is correct in substance, but it needs the NASH-R2 group name (R2).
- **Harrison as a separate author family.** Sound. The February 3 return is written and signed by Harrison for one detachment, though it is printed among Hardee's reports. Hardee's own dispatches are not used in SC011, so no double counting arises.
- **Frozen-record issues.** Recording the NC020 "Sherman's Right Wing (XX and XIV Corps)" label as conflicting with Slocum's heading, Johnston's March 27 report and the NPS narrative is sound. Recording the NC019 CS 5,400 coincidence with Johnston's March 19 return, without adopting it, is also sound: the figure is dated three days after the action and follows Hardee's losses.
- **Cox's report and book disagreement on Upham's regiments.** Correctly preserved as a disagreement within one author family, not adjudicated. The report's own organization table lists Upham as colonel of the Fifteenth Connecticut, which is context for later readers, not a resolution.
- **Null imprint year for OR XLVII Part 1.** Sound. The OCR reads "18 0 5", and the catalog date is correctly not substituted.

## Unresolved (outside this review)

These historical disputes are preserved in the dossiers and were not adjudicated here:

- the Kinston guns (three versus one);
- Schofield's presence at Kinston;
- the Averasborough guns (three versus two);
- the Mill Creek bridge (burned versus saved);
- the Union and Confederate casualty totals;
- the opening strengths of all five records.
