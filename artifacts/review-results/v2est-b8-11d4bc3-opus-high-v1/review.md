# Separate review: strength ledger v2, batch 8 of 8

**Outcome: corrections required.** There are three required findings (R1–R3) and six advisories (A1–A6).

## Reviewer identity and bindings

| Item | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, fresh-context subagent |
| Date | 2026-09-25 |
| Prepared commit reviewed | `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` (against `96110cf`) |
| Worktree HEAD (bundle commit) | `c08ab6f1c424772520144afa9ab146dc9bafb77a`; `git diff 11d4bc3 HEAD` touches only `artifacts/review-results/*/assignment.md` and `inputs.json` |
| `assignment.md` sha256 | `cb656f37f0ca680d419742d2802a2ad04e96ee317fc77a13dfd2107c474625e3` (verified) |
| `inputs.json` sha256 | `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (verified) |
| Ledger `data/estimates/side-strength-v2.json` | `e594047072a99c84e5239658df444f2946c945916d744de2ca6a82c8082629e8` |

**Input hashes.** All 25 paths in `inputs.json` match at the prepared commit (`git show 11d4bc3:<path>`) and in the worktree. There are no mismatches.

**Assignment and manifest differ on the addendum.** The assignment names the addendum as `docs/ledgers-v2.md`, but `inputs.json` binds `docs/research/ledgers-v2.md`, which is the extraction record. I read both. The ledger's own bindings cover the following files, and `estimate-check` verified them: `docs/ledgers-v2.md`, `docs/strength-estimates.md`, `generalship/estimates.py`, `generalship/estimates_v2.py`, the cohort, the owner decision and all 30 dossiers. `docs/feature-admission-reported-strength.md` is not bound by either. I read it at the worktree commit, where it is unchanged from `11d4bc3`.

**Commands, run offline:**
- `make check`: 143 tests OK, exit 0.
- `python3 -m generalship estimate-check --ledger data/estimates/side-strength-v2.json`: exit 0. It reports 305 in scope, 79 out of scope, grades A/B/C/D 184/60/114/252, fit-eligible rows 61/83/130, and 20 rows excluded as `post_start_information`.

I ran no build or packet command, modified no primary artifact, and wrote only this file. My helper scripts were read-only and lived in `/tmp`.

## Scope actually inspected

**Engagements.** All 30 assigned engagements, both sides: GA025, GA026, SC010, GA027, GA028, NC014, VA081, VA082, NC015, NC016, SC011, NC017, NC020, VA123, FL006, AL005, AL006, VA085–VA090, VA092–VA094, VA096, VA097, AL007 and TX005.

**For every engagement I checked:**
- every ledger input: its quote resolved through the dossier citation or CSV cell, printed value, bounds, `printed_text`, basis, codes, `loss_timing`, `bound`, `reproduction_of` and class;
- both frozen CWSAC forces rows;
- every citation of every `strength`-dimension dossier claim, against the inventory text;
- the null reasons and rationale.

**Wider passage context.** I read the surrounding text in the registered sections for:
- Woods (GA025);
- Hazen (GA028);
- Butler and the Baltic brigade (NC014);
- Breckinridge and Stoneman (VA081, VA082);
- Cox's report and history (NC017);
- Johnston's March 27 report (NC020);
- Canby's June 7 report (AL005, AL006);
- Andrews and the NPS text (AL006);
- Jordan (AL007);
- Smith and Hatch (SC010);
- Ewell (VA093).

**Livermore.** I read the `livermore-transcription-v2` sections p134–p139. I checked page images p134, p135, p137, p138 and p139 for the figures that are entered or that force a grouping: 16,127; 16,895; 45,247; 20,030; 63,823; 63,299; 25,452; 19,652. All match the transcription. I did not view p136 (campaign aggregate, inventory only).

**Estimates.** I replayed the estimates with the unchanged engine and simulated each correction in memory.

**Not done.** No new sources, no source-lineage research, and no other batches. The 91 carried-forward v1 entries are out of scope.

## Required corrections

### R1: NC020 Bentonville, US, input `us-johnston-44000`, loss timing

- **Change:** `loss_timing` `"none"` → `"not_prior"`. Append to `note`: `"; 'including losses' adds undated losses (design §3 loss_timing)"`.
- **Evidence:** Johnston's March 27 report (`or47-1-johnston-carolinas-selections-v1`, `johnston-1865-03-27`; the dossier quotes it at `reported-force-scope` citation 10): "On the 20th and 21st the whole army Avas before us, amounting to near 44,000, including losses."
- **Rule:** Design §3 says an input "whose passage shows losses … added … is `prior_engagements_only` only if the passage dates every such loss before the frozen start date; otherwise it is `not_prior`."
  - Here the losses are included but not dated. The same paragraph counts the Federal loss of March 19–21 ("greatest in the thick woods in which the action of the 19th terminated").
  - The frozen start is 1865-03-19.
- **Effect (engine replay):**
  - The input stays class C (`opponent_or_hearsay`, because row 2 precedes row 3).
  - The US point, low and high are unchanged: 33,000 (22,000–44,000).
  - The US labels gain `post_start_information`, and the row becomes `excluded_post_start_information: true`.
  - Ledger totals change: rows excluded as post-start go from 20 to 21, and `set3_ABC` fit-eligible rows from 130 to 129.
  - The extraction memo `docs/research/ledgers-v2.md` needs the same updates: "Rows with both sides A–C" 130/93 → 129/92, and "Rows excluded as `post_start_information`" 20/13 → 21/14.
- **Rationale text:** Update the NC020 `rationale` to say the Union point's only candidate includes undated losses, so the row is excluded from the fits.

### R2: GA028 Fort McAllister II, Confederate, input `cs-hazen-garrison`, code and class

- **Change:**
  - `codes`: `["post_outcome_claim"]` → `[]`.
  - `loss_timing`: `"none"` → `"not_prior"`.
  - `class`: `"unusable"` → `"C"`.
  - `note`: → `"Hazen's captures: the garrison including killed, a count of this engagement's captured and killed (design §3 row 3)"`.
- **Rationale text:** Replace "Hazen's post-capture count is unusable" with "Hazen's count of the captured garrison including killed is class C post-start information and does not enter the range."
- **Evidence:** Hazen report (`or44-hazen-fort-mcallister-selections-v1`, `hazen-report`): "The captures were as follows: The garrison, including killed, 250 men and officers, 24 pieces of ordnance …". The dossier quotes this at citation 4.
- **Rule:**
  - Tier-2 §3 item 6 reserves `post_outcome_claim` for "a strength figure whose claim is tagged `post_outcome`". The cited claim `reported-force-scope` has `phase: unresolved`.
  - Design §3 row 3 covers exactly this case: "a value that uses losses, captures, surrenders or survivors of … this engagement".
  - The reviewed v1 precedent codes surrender counts the same way (TN006 `us-cist-surrendered`, WV010 `us-surrendered`: codes `[]`, `not_prior`, class C).
- **Effect (engine replay):** The Confederate estimate is unchanged at A 120 (110–210) with the same labels. A C post-start candidate enters neither the class-A point nor the range.

### R3: SC010 Honey Hill, Confederate, input `cs-sc-reserves`, printed value and scope

- **Change:** Delete input `cs-sc-reserves`. In the `reported-force-scope` inventory list, replace `"cs-sc-reserves"` with:

  > "Chesnut's South Carolina reserves ('about 3o0 effective muskets' in OCR; the middle digit is unreadable and is not corrected) reached Grahamville Station at midnight, after the action, and are not part of the engaged force"

- **Minimal alternative:** Keep the input with `codes: ["partial_scope", "unreadable_value"]` and `printed: {"lower": 300, "upper": 390}`, with the note stating that the OCR middle digit is unreadable.
- **Evidence:**
  - The passage (`or44-gw-smith-selections-v1`, `smith-report`) reads: "During the night the enemy retired rapidly … At midnight Brigadier-General Chesnut arrived at Grahamville Station with about 3o0 effective muskets of South Carolina reserves."
  - The dossier's rationale says: "The later arrivals are not part of the engaged force."
  - The ledger already records Baker's 860, from the same passage, in the inventory for that reason.
- **Why the current entry is wrong:**
  - The printed value 350 is an unsupported correction of "3o0". Tier-2 §3 item 4 says: "OCR readings are reported, not silently corrected. Unreadable figures are `blocked: unreadable_value`." An OCR "o" is at least as likely to be a "0" as a "5".
  - A body that arrived after the action is not a part of the side's engaged force, so it is not a valid lower bound.
- **Effect (engine replay):** The estimate is unchanged at A 1,400 (1,330–1,470).

## Advisories (no change required)

- **A1: AL005 US `us-canby-assembly` (32,200).** The cited Canby section shows that part of this Mobile Point assembly served at Blakely (AL006) inside the AL005 interval:
  - "On the 30th Veatch's division (Thirteenth Corps) was withdrawn from the line of investment";
  - "Veatch was ordered in from Holyoke to report to [Steele]";
  - "On the 3d Garrard was ordered in to complete the investment on the left", where Garrard's is a Sixteenth Corps division.

  So the figure spans troops in two frozen records. A reviewer could code it `other_engagement` (design §3 row 1, a composite spanning several frozen records). The US side would then be grade D, and the row, already incomplete, would be unchanged. The current `scope_unresolved` + `engagement_link_unknown` (C) is defensible under the whole-interval target, because those divisions began the interval at Spanish Fort. I'd still extend the input note to record the transfers.

- **A2: FL006 Confederate `cs-cw` (frozen 1,000) coded `partial_scope`.**
  - The reading follows the dossier: the frozen text's "reinforcements from Georgia amounting to approx. 1,000 men" appears to follow Newton's postscript phrase "re-enforcements from Georgia … amounting to over 1,000 men".
  - However, the table's `strength_min` field assigns 1,000 to the side.
  - If the owner or primary reads the scope as unresolved (`scope_unresolved`, C), the replay gives C 1,000 (700–1,750) on the `reported_engaged` basis, instead of the current rule-4 C 1,310 (880–1,750). The row stays in `set3_ABC`.
  - This is a genuine reading dispute. It should stay visible, but I do not require a change.

- **A3: "near" as a one-sided bound (NC020 `us-johnston-44000`, "amounting to near 44,000").**
  - The ledger treats "near N" as approximate in NM001, MO010 and FL005, but as `one_sided_bound` in OK004.
  - NC020 follows the majority. If "near" were read as "nearly", the NC020 US side would lose its only candidate and become grade D.
  - A single ledger-wide convention would remove this inconsistency. The cases outside this batch are out of my scope.

- **A4: VA086 US `us-lv` (45,247).** Livermore's entry adds "loss of 5th corps, March 29 and 30" (p.137, page image checked), which is dated before the frozen start of March 31. `loss_timing` should read `prior_engagements_only`, not `none`. There is no class effect, because `other_engagement` (row 1) governs.

- **A5: AL007 US `us-jordan` ("still at least 9000 strong").** The recorded extractor policy lists Jordan and Pryor as compiled secondary histories "unless the passage shows the figure is visibly an opponent estimate". The passage is the compilers' own narrative statement, so `adversary_or_hearsay_estimate` looks unsupported. There is no effect: the input is bound-only either way, and its basis (`unknown`) is not the point basis.

- **A6: Consistency across batches (outside my scope).** Other batches code surrender or capture counts as `post_outcome_claim`: GA001 `cs-gillmore-385`, LA010 `cs-prisoners`, KY011 `us-morgan-hobson`. The same reasoning as R2 may apply to them. I did not inspect their claim phases.

## Checks with no finding

- **Grade D sides.** I confirmed every null reason and found no missed whole-side figure in the inspected sources for these sides:
  - GA025 (both), GA026 CS, GA027 (both), NC014 (both), VA081 (both), VA082 (both), NC015 (both);
  - AL005 CS;
  - VA085, VA086, VA087, VA088, VA090, VA092 (both sides of each);
  - VA093 CS, VA094 (both), VA096 (both), VA097 (both), TX005 (both).

  VA093's statement that Gordon's corps is uncounted is supported by the dossier boundary note ("the Second Corps' fight with Gordon at Perkinson's mill").
- **VA086 frozen values.** The frozen 45,247 and 20,030 equal Livermore's composite Dinwiddie–White Oak Road totals (page images p137–p138). They are correctly grouped (rule 2) and correctly unusable, as at v1 VA032.
- **Inventories.** Every figure in the bound dossier strength claims and in the matching Livermore entries is an input or is recorded with an accurate reason. This includes Bentonville (p134–p135), Dinwiddie–White Oak Road (p137–p138), the Petersburg assault (p138–p139) and the Appomattox campaign aggregate (p135–p137).
- **Results.** No estimate is implausible given its inputs beyond the declared rule consequences:
  - Rule-4 points: NC020 both sides, FL006 CS and VA093 US.
  - Class-C candidates widening class-A ranges: VA123 US (high 10,500 from Pond's raid-start 10,000) and NC017 CS (high 16,000 from Cox's opponent estimate).
  - NC020's rule-4 outcome is a declared consequence (design B3). R1 changes only its fit eligibility, not its point.
- **VA123 CS.** The frozen 1,600 equals the prisoner count; the dossier treats this as an observation only. It carries `derivation_unknown`, as the design requires. I made no finding.

This is an AI review: a separate analysis, not human historical adjudication, independent corroboration, feature admission or authorization of any fit. The primary should check each finding against its passage before applying it.
