# Middle Tennessee Operations: separate AI source review, v1

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a fresh-context subagent started for this assignment. No task ID was visible to the reviewer. I did not see the author's conversation.
- **Date:** 2026-09-25
- **Commits:** I reviewed the prepared commit `ba8d06850c1ccc671332a76af667a48e4457a0e8` against the previous commit `5521513d93b6bb0cca9557f13af17a24ee49ee7b`. The worktree was at bundle commit `a147b28331a916f5b608f03eb9b6ae08608076a3`, whose only change from `ba8d068` is this assignment directory.
- **Assignment:** `assignment.md` sha256 `889a7b3092aa323aa84920838b13414851e20506be7806d6dc48aa321b706d25`. Input manifest `inputs.json` sha256 `8f596a8e21d5f3ed22cae9b223933e84c58f615ae6932b69ee8262f6fc9192a4`.
- **Input hashes:** I checked all 46 bound paths against the manifest, in the worktree and in `git show ba8d068:<path>`. There were **0 mismatches**.
- **Outcome: corrections required.** Findings MT-R1 to MT-R4 are required. MT-N1 and MT-N2 are recommended only.
- **What this review is not:** it is an AI analysis. It is not human historical adjudication, independent corroboration or feature admission. I did no network access, no new research and no agents. I ran no build or packet command and made no `generalship.cli` writer calls. I edited no files other than this one.

## Coverage actually inspected

- **Dossiers:** I read all five dossiers (TN012–TN016) in full: **46 claims, 135 citation occurrences and 7 null unknowns**. That is 5 opening-strength claims plus logistics for TN014 and TN016. All seven dimensions appear in every dossier. Every value is null exactly where the status is `unknown`, and those claims carry no citations. All dossiers are `draft`, with both replacement dates null.
- **Frozen rows:** I read the complete TN012–TN016 battle, force and commander row sets. I checked every cited cell: `forces_text`, `strength_min`, `results_text`, `casualties_text` and `rank`.
- **NPS summaries:** I read all five retained summaries in full.
- **Book selections:** I read both new selections in full, including the transcription notes, the title/preface and every section. For boundary context I read about 1.5 KB before and 0.3 KB after each range in the pinned parents. I did not read the whole books.
- **Registry and memo:** I read the source-registry diff (12 records), the memo, and the diffs to README, roadmap, methodology, `docs/sources.md`, `cli.py`, the test, the queue and the report.

**Text derivatives.** All seven replay byte-exactly:
- Each of the five NPS HTML files, processed with HTMLParser (script/style omitted, text nodes stripped and joined, "Return to Results" to before "Experience More"), gives exactly the matching `.txt`. The parent hashes bind.
- Cist: 4 ranges from `cist-cumberland-ocr-v1` (`data/raw/heartland-v1/cist-full.txt`).
- Jordan and Pryor: 5 ranges from `jordan-pryor-forrest-ocr-v1` (`data/raw/forrest-west-tennessee-v1/jordan-full.txt`).
- Each range, after split/join whitespace collapse, equals its section. Both parents and their metadata are unchanged.

**Page locators.** Every book citation follows the OCR page markers.
- Jordan sections start on p.224, 232, 241 and 245. The explicit map holds: `128` = p.228, `22^` = p.229, `347` = p.247.
- Cist `1J4` = p.144. The Vaught's Hill section starts on p.143 and Dover on p.140.

**Registry.** There are 361 records and 358 paths. The first 349 records (346 paths) are byte-identical to the previous commit. Every registry hash matches its file.

**Unchanged inputs.** Between the two commits there is no diff in any of these:
- `data/evidence/history` (20 files)
- all 67 older dossiers
- cohort
- both admission proposals
- the three CWSAC CSVs
- the Cist and Jordan parent directories
- `admission-check.json`, `baseline.json` and `battles.json`

**Coverage and baseline.** Coverage is 72/127 dossiers, 55 without, and 18/36 complete campaigns. Promoted rows are 0. The baseline is 23 battles in 13 campaigns, with Brier 0.2768816348133779 against 0.25.

**Next group.** Longstreet's Tidewater Operations [March–April 1863] is confirmed independently from `battles.json`. It is the earliest incomplete group, starting 1863-03-13, and its records are NC010, NC011, VA031 and VA030.

**Packets.** Each of `artifacts/research/TN012–TN016.md` has 3 JSON blocks.
- The assigned record equals its `battles.json` entry.
- The existing draft equals the dossier.
- The source registry equals `data/sources.json`.

**Receipt.** I checked all 106 input hashes, all 7 output hashes (under `artifacts/`) and all 361 source hashes. Every one matches.

**Tests.** `make check` ran offline under Python 3.14.7: 82 tests passed, and it reported `artifacts_written: false`. The worktree was clean afterwards.

**Items the assignment named, confirmed correct:**
- **Frozen force bounds:** Dover 800/2,500, Vaught's Hill 1,300/3,500 and Brentwood 400.
- **Surrender counts** are not treated as opening strengths.
- **Casualty pairs, frozen/live:** 796/965, 2,206/1,957, 435/188, 311/532 and 237/237.
- **Command events:** Gilbert's order to advance (Cist p.142), Granger's false report and Stanley's unordered attack (NPS).
- **Forrest's objection at Dover** is attributed through the Forrest-endorsed history.
- **`inherited` tags** on Dover's works and the Brentwood site are defensible, draft-only hypotheses.
- **Heading ranks:** the live ranks for Harding and Forrest are recorded and not adopted.
- **Jordan and Pryor** are described everywhere as not independent of Forrest. The preface and Forrest's note say this.
- **No automatic attribution** of the result to the listed commanders, and no additive credit.

## Required corrections

### MT-R1: Franklin's "May 10" date is also in the frozen row, not only the live page

The frozen `arnold-cwsac-battles` TN016 `description` cell says "Van Dorn advanced northward from Spring Hill on May 10". The frozen `start_date` and `end_date` are both `1863-04-10`. The live narrative is identical to the frozen description, and this is true for all five records. So the conflict is internal to the frozen row. It is not a live-versus-frozen difference, and the two copies are one NPS/CWSAC text, not two witnesses.

Jordan's "10th" also appears only as the OCR reading "loth". It is not cited: the dossier cites only "about the 9th of April".

**Fix for TN016 `recorded-result`.**

Replace the `value` with:

> "The frozen and live results read Union victory. NPS says Van Dorn withdrew to Spring Hill, as do Jordan and Pryor. The frozen CWSAC description and the identical live NPS narrative both date the advance to May 10, conflicting with the frozen start and end dates of 1863-04-10; Jordan and Pryor place the reconnaissance on the 10th (OCR "loth") after events of about April 9."

Replace the last sentence of the `rationale` with:

> "The May 10 narrative date conflicts with the frozen row's own April 10 interval and is not adopted; the frozen description and live page are one NPS/CWSAC text, not two witnesses."

Add these citations:
- `arnold-cwsac-battles`, row `{"battle":"TN016"}`, column `description`, quote `Van Dorn advanced northward from Spring Hill on May 10`
- `arnold-cwsac-battles`, row `{"battle":"TN016"}`, column `start_date`, quote `1863-04-10`
- `jordan-middle-tennessee-selections-v1`, section `franklin-reconnaissance`, locator p.245, quote `ordered a reconnoissance in force of the position on the loth.`

**Fix for the memo and roadmap wording.**

In `docs/research/middle-tennessee-first-pass-v1.md`, replace "Franklin's date, where the live NPS narrative says May 10 against the frozen April 10, which Jordan and Pryor support" with:

> "Franklin's date, where the frozen CWSAC description and the identical live NPS narrative say May 10 against the frozen April 10 interval, which Jordan and Pryor support"

In `docs/roadmap.md`, replace "Franklin's live narrative date (May 10 against the frozen April 10)" with:

> "Franklin's narrative date (May 10 in both the frozen description and the live page, against the frozen April 10 interval)"

### MT-R2: Dover gunboats — Jordan's timing is not fully covered by the cited quotes and rests on cropped lines

The cited Jordan quotes are "Federal gunboats came up about eight o'clock at" and "doing no harm whatsoever". Neither supports "after the Confederates had withdrawn" or "at night". Those words come from cropped line starts.

The surrounding p.229 text reads "…r the Confederates had been withdrawn from under e Federal gunboats…" and "…Confede- rho, an hour later, began to retire". So in Jordan's account the Confederates had been withdrawn from under fire, but they were still near Dover when the gunboats fired, and they retired an hour later. The dispute with Cist is therefore about whether naval fire came during the assaults. It is not about whether the Confederates had already left.

**Fix for TN012 `gunboat-timing`.**

Replace the `value` with:

> "Cist says six gunboats aided Harding in the latter part of the engagement; Jordan and Pryor, in cropped OCR lines, say the Federal gunboats came up about eight o'clock, after the Confederates had been withdrawn from under the Federal fire, cannonaded without doing any harm, and that the Confederates began to retire an hour later."

Append to the `rationale`:

> "Jordan's timing and the words completing 'at' and 'from under' are cropped in the scan; only intact words are quoted and 'at night' is not verified against print."

Add these citations, both `jordan-middle-tennessee-selections-v1`, section `dover`, p.229:
- `the Confederates had been withdrawn from under`
- `an hour later, began to retire`

### MT-R3: Brentwood surrender sequence — Jordan does report a refusal, at the separate bridge stockade

The claim sets NPS's "Bloodgood refused" against Jordan's "without further parley". But Jordan, p.242–243, reports that a demand at the bridge stockade "was curtly declined". That garrison, "some 230", yielded after "a single shot" from Freeman's gun. The NPS sequence (refusal, then artillery, then surrender) may match Jordan's stockade episode rather than conflict with his account of Bloodgood's post. The draft also compresses NPS's timing: within half an hour Forrest had artillery in place, and Bloodgood then "decided to surrender".

**Fix for TN015 `surrender-sequence`** (the status stays `disputed`).

Replace the `value` with:

> "NPS says Bloodgood refused a surrender demand under a flag of truce, and that within half an hour Forrest had artillery in place and the Federals surrounded, after which Bloodgood decided to surrender. Jordan and Pryor say the surrender at Brentwood was made without further parley, and place a refusal at the separate bridge stockade (about 230 men), whose garrison declined the demand and yielded after a single shot from Freeman's gun. Whether the accounts conflict about one post or describe different posts is unresolved. The live heading ranks Forrest Major General against the frozen Brigadier General."

Add these citations:
- `nps-tn015-v1`, locator Description, quote `Within a half hour, though, Forrest had artillery in place to shell Bloodgood's position and had surrounded the Federals with a large force. Bloodgood decided to surrender.`
- `jordan-middle-tennessee-selections-v1`, section `brentwood`, p.243, quote `demanded through his aid-de-camp, Captain C. W. Anderson, was curtly declined.`
- `jordan-middle-tennessee-selections-v1`, section `brentwood`, p.243, quote `A single shot, however, from Freeman's gun, hurtling and crashing through the stockade, wrought an immediate change of purpose`

### MT-R4: Attribution precision in two claims

**(a) TN015 `reported-force-scope`.** Jordan gives the 529 figure "according to Federal accounts". The draft presents it as Jordan's own count.

Replace the sentence "Jordan and Pryor say 529 officers, men and teamsters surrendered there and about 230 more at the stockade, 759 in all." with:

> "Jordan and Pryor, citing Federal accounts, say some 529 officers, men and teamsters surrendered there, and about 230 more at the stockade, 759 in all."

Append to the `rationale`:

> "The OCR prints the total as '7591'; 759 follows from 529 plus 230 and is not checked against print."

Add this citation: `jordan-middle-tennessee-selections-v1`, section `brentwood`, p.242, quote `according to Federal accounts`.

**(b) TN012 `command-roles`.** Wharton's inability to attack simultaneously is, in Jordan, Wheeler's explanation. It is not the authors' own finding.

Replace "Jordan and Pryor say Forrest's views passed without heed and Wharton was unable to attack simultaneously;" with:

> "Jordan and Pryor say Forrest's views passed without heed, and report Wheeler explaining that Wharton had been unable to get ready to attack simultaneously;"

Add this citation: `jordan-middle-tennessee-selections-v1`, section `dover`, p.228, quote `General Wheeler reappeared at this juncture`.

**Effect on counts.** Adopting R1–R4 adds 10 citation occurrences (135 → 145) and changes no claim or unknown counts. The primary agent should re-verify, recount and update the memo, README, roadmap, `cli.py` text and the prepared packets.

## Recommended (non-blocking)

### MT-N1: Cite value clauses that currently have no citation

Some value clauses rely on passages that are in the same sections but are not cited. All quotes below are exact and present:

| Claim | Uncited clause | Quote to add | Source and locator |
| --- | --- | --- | --- |
| TN012 `ammunition-shortage` | "withdraw for want of it" | `were obliged, from want of ammunition` | Jordan `dover` p.229 |
| TN012 `reported-force-scope` | Cist's "Forrest's brigade with four guns" | `Forrest to move his brigade with four guns` | Cist `dover` p.140 |
| TN013 `command-roles` | Jackson's frontal attack | `Jackson's dismounted 2nd Division made a frontal attack` | `nps-tn013-v1` Description |
| TN016 `recorded-result` | NPS on the withdrawal to Spring Hill | `caused Van Dorn to cancel his operations and withdraw to Spring Hill` | `nps-tn016-v1` Description |

TN012 `casualty-records` also needs a wording change. Its "wounded" rests on the cropped "td", so the rationale should say the category list is partly reconstructed.

### MT-N2: Retain Jordan's Franklin footnote as an open question

For Franklin (TN016), Jordan's footnote (p.245) infers from Granger's telegraphic report that Granger was "prepared for it with Stanley's Division of cavalry". This sits uneasily with NPS's surprise, "without orders" framing. The Stanley claim needs no change. Keep the tension in the open questions.

## Inspected and not deferred

I found no quote-presence, section, locator, hash, count, row-set or cell errors. Opening strengths remain unknown, and no morale, probability, causal or ranking value is introduced. No original orders, returns, maps or print were inspected, by the author or by me.
