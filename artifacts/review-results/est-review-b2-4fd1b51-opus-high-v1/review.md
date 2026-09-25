# Best-estimate ledger, separate review batch 2 of 4 (est-review-b2)

**Outcome: corrections required.** Required findings: R1–R10. Advisories: A1–A13.

This is a separate AI analysis. It is not historical adjudication, independent
corroboration, feature admission or authorization of any fit. It applies the accepted rules
to the recorded inputs and does not re-derive them.

## Reviewer record

| Item | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`; a fresh-context subagent started from the assignment file, with no access to the author's conversation |
| Date | 2026-09-25 |
| Prepared commit under review | `4fd1b512f9e4db0402537bfe577031a6cc6939f6` |
| Previous commit | `5151b5700f50fc494b167cc7c4d742c8fc17cc13` |
| Bundle and worktree HEAD | `2c490165397e7991b8a2fbaf2859e9a939cf61e8`. It differs from the prepared commit only by the b1 and b2 assignment bundles. |
| `assignment.md` sha256 | `e1432785d1b33fd13566a242ae1b2b29b0340a8b2e22d7762921cfe09a105ae7` (verified) |
| `inputs.json` sha256 | `3c3d44031bacf0e03bb86c936b63bd653ee3cb7c887a350425dcfc622490c388` (verified) |
| Bound inputs | All 25 paths match `git show 4fd1b51:<path>`, with no mismatch. The worktree copies are identical. |
| Documents read but not bound in `inputs.json` (hashes at the worktree, same as at `4fd1b51`) | `docs/strength-estimates.md` `795212ad…4ba3`, which equals the ledger's design binding; `docs/feature-admission-reported-strength.md` `0699152d…c048`; `docs/research/reported-strength-scoping-v1.md` `aa8bb163…1a1a` |
| Checks run offline | `make check`: 107 tests OK, `generalship check` OK, exit 0. `python3 -m generalship estimate-check`: exit 0, 62/25/23/72, fit-eligible 21/31/40, post-start 6. The checker also verified the bound dossier hashes. No build, packet or network command was run. |

## Coverage actually inspected

- **Engagements.** All 22 assigned engagements, both sides (44 sides, 96 ledger inputs):
  TN006, VA022, VA025, VA026, KY007, WV010, KY008, MD002, MS001, WV016, MS002, TN007, KY009,
  TN008, VA028, NC007, NC009, TN009, MS003, TN010, TN011 and AR006.
- **Per engagement:**
  - every dossier `strength` claim and each of its citations;
  - the frozen CWSAC forces row, and the battles row where it bore on scope;
  - each input's resolved passage with about 350 characters of context, or the CSV cell;
  - its codes, basis, `loss_timing`, `bound`, `reproduction_of` and class;
  - the stored estimate;
  - the inventory and the rationale.
- **Livermore transcription sections:** p87, p88, p89, p90, p94, p95, p96, p97 and p98.
- **Livermore page images:** p87 (including a zoomed crop of note 4), p88, p89, p90, p91, p95,
  p96, p97 and p98. The OCR (`livermore-ocr-v1`) was used only to look for further 1862
  entries. Its Harper's Ferry remark lies on a page before p.78, outside the pinned images, and
  was not used.
- **Wider source reads:**
  - Palfrey `south-mountain` (the Turner's and Crampton's Gap narrative);
  - a search of all Palfrey sections for the Crampton's Gap forces and a cavalry escape;
  - Ropes `cedar-mountain` (the "as has been stated" figure);
  - the MD002 `subordinate-command` and `casualty-records` citations, for scope only.
- **Replay.** All corrections below were replayed in memory with the repository's own
  `estimate_side`, `estimate_row` and `nested_sets`. No file other than this review was
  written.
- **Not inspected:** other batches, the out-of-scope records, non-strength dimensions (except
  as noted), and any print or unregistered copy.

## Required corrections

Each correction names the engagement, side, input and field. "Result-neutral" means the side's
grade, point, range and labels do not change.

### R1. VA022 Cedar Mountain: Livermore's totals are partial (page image p.87, note 4)

**Evidence.** The p.87 page image, note 4, reads: "…and 102 for Pick-ett's division. This
division is not included in the force engaged, because, before it arrived, the Union line was
driven back and the battle was decided; and, although its loss occurred where the Union line
made its stand in the rear, it was after dark in an encounter which had no effect on the
combat… comparison of numbers and losses strictly confined to the forces involved in the
decision of it… On the same theory, Field's, Gregg's, and Stafford's (2d Louisiana) brigades
are omitted on the Confederate side."

The division name is quoted as printed. Livermore therefore presents both totals as parts of
each side, excluding forces that were engaged within the frozen August 9 interval. That is
tier-2 §3 item 1, `partial_scope`. The registered transcription omits notes 1–4, 6 and 7, so
the ledger could not see this.

**Changes:**

- **US `us-lv`:** `codes` → `["partial_scope"]`, `bound` → `"lower"`, `class` → `"bound"`. Add
  to `note`: "p.87 note 4 (page image livermore-p87-image-v1): a Union division engaged after
  dark on August 9 is excluded."
- **Confederate `cs-lv`:** `codes` → `["partial_scope"]` (keep `loss_timing: "not_prior"`),
  `bound` → `"lower"`, `class` → `"bound"`. Add the same note reference, for Field's, Gregg's
  and Stafford's brigades.

**Consequences under design §4 rule 2.** `us-lv` (Livermore) and `us-cw` (NPS/CWSAC) have equal
values, so they are grouped, and `us-nps` joins them through `reproduction_of`. The group
becomes bound-only.

- **US estimate:**
  `{"grade":"D","point":null,"low":null,"high":null,"exact":null,"point_basis":null,"method":"grade_D_no_candidate","labels":["whole_engagement_leakage"],"point_groups":[],"range_groups":[]}`.
- **New US `null_reason`:** "No candidate value: the frozen CWSAC, NPS and Livermore 8,030 form
  one rule-2 group that Livermore p.87 note 4 presents as excluding a division engaged after
  dark on August 9 (partial_scope, lower bound 8,030); Ropes's 'did not reach a total of 8,000'
  is a one-sided bound."
- **Confederate estimate:** the numbers are unchanged. The labels become
  `["single_input","whole_engagement_leakage"]`, because `basis_mixed` needs both points.
- **Nested sets:** `{"sets":[],"excluded_post_start_information":false}`. The row becomes
  incomplete, so a frozen baseline row leaves the fit-eligible set.

The primary should confirm note 4 on the page image before applying this.

### R2. MD002 South Mountain: the Confederate McClellan input cites the Union sentence

`cs-mcclellan` cites dossier citation 2, "into action with about thirty thousand men." That is
McClellan's figure for his **own** force. The Confederate figure is in the preceding sentence of
the same registered Palfrey section. That sentence gives no basis, and its population is "the
Confederate force … in all", not "into action".

**Changes:**

- **Confederate `cs-mcclellan`:** `ref` →
  `{"citation":{"source_id":"palfrey-maryland-selections-v1","section":"south-mountain","locator":"p.38 (OCR page markers; not checked against print)","quote":"He calls the Confederate force \"probably some thirty thousand in all,\""}}`.
  This quote was verified to resolve in the section, and it contains `printed_text`
  "thirty thousand".
- `basis` → `"unknown"`.
- `codes`: see R3.

**§2 question for the primary.** The dossier claim value states "Palfrey quotes McClellan's
30,000 on each side", but no dossier citation carries the Confederate sentence. If §2 is read
as limiting inputs to the exact dossier quotes, this input must be dropped instead. The
Confederate side would then be grade D and the row incomplete.

### R3. MD002 South Mountain: whole-side scope against the frozen record

The frozen record covers Crampton's, Turner's and Fox's Gaps: CWSAC `other_names` and
`description`. The dossier calls Crampton's Gap "a separate sub-action" of this record.

Palfrey (`south-mountain`) describes the two passes as "quite isolated from the other". It gives
Franklin's corps against the brigades "of Cobb, Semmes, and Mahone" at Crampton's. It tests
McClellan's 30,000 against "the aggregate of the First and Ninth Corps" (Turner's/Fox's Gap).

Livermore's p.90 entry lists "1st and 9th corps" for the Union. For the Confederates it lists
"D. H. Hill's, Hood's, and Jones's divisions, and Evans's brigade" and Rosser's cavalry. It
names no Crampton's Gap defenders.

**Changes:**

- **US `us-mcclellan`:** `codes` → `["scope_unresolved"]`, `class` → `"C"`. The relaying passage
  ties the 30,000 to the First and Ninth Corps but does not settle whether Franklin is excluded.
  A stricter `partial_scope` would make both sides grade D.
- **US `us-lv`:** `codes` → `["partial_scope"]` (keep `loss_timing: "not_prior"`), `bound` →
  `"lower"`, `class` → `"bound"`.
- **US `us-palfrey-cap`:** `codes` → `["one_sided_bound","partial_scope"]`, `bound` → `null`.
  A cap on two corps does not bound the whole side.
- **Confederate `cs-mcclellan`:** `codes` → `["adversary_or_hearsay_estimate","scope_unresolved"]`
  (class stays `"C"`).
- **Confederate `cs-lv`:** `codes` → `["partial_scope"]` (keep `not_prior`), `bound` →
  `"lower"`, `class` → `"bound"`.

**Replayed result, with R2 applied:**

- **US:**
  `{"grade":"C","point":30000,"low":21000,"high":39000,"exact":{"point":"30000","low":"21000","high":"39000"},"point_basis":"reported_engaged","method":"rule3_median","labels":["applicability_unresolved","basis_mixed","single_input","whole_engagement_leakage"],"point_groups":["us-mcclellan"],"range_groups":["us-mcclellan"]}`
- **Confederate:**
  `{"grade":"C","point":22500,"low":15000,"high":30000,"exact":{"point":"22500","low":"15000","high":"30000"},"point_basis":"unknown","method":"rule4_opponent_only","labels":["applicability_unresolved","basis_mixed","opponent_estimate_point","single_input","whole_engagement_leakage"],"point_groups":["cs-mcclellan"],"range_groups":["cs-mcclellan"]}`
- **Nested sets:** `{"sets":["set3_ABC"],"excluded_post_start_information":false}`. The row is
  no longer excluded as post-start.

### R4. MS001 Iuka: Greene's 3,000–4,000 covers two brigades, not the side

The passage reads: "fought on the Confederate side by Little's division, and mainly by two
brigades of it, numbering between three and four thousand men." The ledger's own note says
"the two brigades that did the fighting". This is `partial_scope`.

**Change.** Confederate `cs-greene`: `codes` → `["partial_scope"]`, `bound` → `"lower"`,
`class` → `"bound"`.

**Replayed Confederate result:** the point and range are unchanged (3,200; 3,040–14,700). The
`labels` add `bound_conflict`, because the lower bound's midpoint, 3,500, exceeds the point.
`point_groups` → `["cs-cw"]` and `range_groups` → `["cs-cw","cs-nps-price"]`.

### R5. MS002 Corinth: Greene states the Union basis

The passage reads: "The returns of his army on that day show that he had 48,000 effective men,
as follows: … 23,000 under Rosecrans at Corinth."

**Change.** US `us-greene`: `basis` → `"reported_effective"`, `class` → `"A"`.

**Replayed US result:** the numbers are unchanged. `range_groups` → `["us-nps"]`, and `labels`
add `single_input`.

### R6. NC007 Kinston: Smith's 30,000 is a post-start estimate

The source is Smith at Goldsborough, December 15: "Enemy now estimated at 30,000, and scouts
report re-enforcements constantly arriving". The frozen start is 1862-12-14. Tier-2 §3 item 2
excludes an estimate state-dated after the start (`post_engagement_state`).

**Change.** US `us-smith-est`: `codes` →
`["adversary_or_hearsay_estimate","post_engagement_state"]`. The class stays `"C"`, because row 2
precedes row 3.

**Replayed result:**

- US `labels` add `post_start_information`; the point is unchanged at 22,500 (15,000–30,000).
- Nested sets: `{"sets":["set3_ABC"],"excluded_post_start_information":true}`. The row leaves
  the fits.

### R7. VA028 Fredericksburg: Palfrey's 113,000 is from December 13 morning reports

The passage reads: "showed by their morning reports of December 13th, about one hundred and
thirteen thousand men present for duty." The frozen start is 1862-12-11.

**Change.** US `us-palfrey`: `codes` → `["post_engagement_state"]`, `class` → `"C"`.

**Result-neutral.** Its present-for-duty basis is not the point basis.

### R8. KY009 Perryville: the NPS narrative "nearly 55,000" is a one-sided bound, not a reproduction

Tier-2 §3 item 4 names "nearly" as a one-sided bound. The ledger memo states that NPS narrative
restatements are not linked as reproductions, because linking would merge an engaged-basis
figure with an unstated one. The ledger follows that elsewhere (IN001, OH002, TN010, TN015).

**Change.** US `us-nps-desc`:

- `basis` → `"unknown"`;
- `codes` → `["derivation_unknown","one_sided_bound"]`;
- `bound` → `"upper"`;
- delete `reproduction_of`;
- `class` → `"bound"`.

The `reproduction_of` link must go. If it stayed, rule 2 would make the whole `us-nps` group
bound-only. With the link removed the change is result-neutral.

### R9. TN006 Murfreesboro: the NPS narrative "about 1,400" is not an engaged-basis reproduction

This is the same memo policy as R8.

**Change.** Confederate `cs-nps-desc`: `basis` → `"unknown"`, delete `reproduction_of`, `class`
→ `"B"` (keep `derivation_unknown`).

**Result:** the numbers and labels are unchanged. `range_groups` →
`["cs-cist","cs-cw","cs-nps-desc"]`.

### R10. Inaccurate inventory reasons (all result-neutral)

- **(a) MD002 `inventory.livermore.reason`.** "return and loss lines precede the totals" omits
  two alternative Confederate totals on p.91, which is not transcribed. Replace with: "Return and
  loss lines precede the p.90 totals. p.91 (page image only; not in livermore-transcription-v1)
  gives an alternative 'Total engaged 17,852' from the July 20 return less August losses, and
  note 3 computes 13,400 from reports of men in action, which Livermore does not adopt. Both
  name only the Turner's/Fox's Gap divisions (partial_scope for this record) and are not
  entered."
- **(b) KY009 `inventory.livermore.reason`.** "entire entry entered" is inaccurate. Replace
  with: "Entry lines entered. Notes not entered (page image p.95; truncated in the
  transcription): note 1's conditional Union 'less than 25,000' engaged if six brigades are
  deducted (partial_scope, one_sided_bound, not_prior), and note 2's Confederate 'infantry
  present for duty … at least 15,300' (partial_scope, one_sided_bound)."
- **(c) WV010 `dossier_claims` `reported-force-scope`.** The entry "NPS surrender figure
  (post-outcome); zero display" misnames the code. The claim is not tagged `post_outcome`.
  Replace with: "NPS 'surrendered the garrison of more than 12,000' is a one-sided surrender
  count (one_sided_bound, loss_timing not_prior; residual class C, so rule 7 cannot apply it);
  zero display."
- **(d) VA022 `dossier_claims` `reported-force-scope`.** The entry "NPS description 14,000 is a
  July detachment (other_engagement)" misnames the reason. The passage itself says Jackson "was
  later reinforced by A.P. Hill's division". Replace with: "NPS description 14,000 is Jackson's
  July force before A. P. Hill joined (partial_scope; pre-engagement, engagement_link_unknown;
  residual class C, not applicable as a bound)."

### Consequential updates

The replay combines R1–R9. The totals in `docs/research/strength-estimates-ledger-v1.md` would
change as follows.

| Measure | Now | After R1–R9 |
| --- | --- | --- |
| Side grades A / B / C / D | 62 / 25 / 23 / 72 | 61 / 24 / 24 / 73 |
| Fit-eligible rows A / AB / ABC | 21 / 31 / 40 | 21 / 30 / 39 |
| Rows excluded as post-start | 6 | 6 (MD002 leaves, NC007 enters) |
| Common rows / newly covered rows | 22 / 18 | 21 / 18 |

The table rows for VA022, MD002 and NC007 would change with these totals. Other batches may
change these totals further.

## Advisories (no required change)

- **A1. Partial figures coded as upper bounds.** These are KY007 `cs-smith` ("not more than
  5000", apparently without cavalry) and MS003 `us-greene-assault` (the assaulting brigades).
  A cap on a part is not an upper bound on the whole side. Set `bound: null`. This is
  result-neutral now, only because their basis differs from the point basis.
- **A2. NC009 `us-smith-est` ("certainly over 15,000").** It has `one_sided_bound` but
  `bound: null`; `"lower"` is the accurate direction. Result-neutral: an opponent residual never
  applies.
- **A3. TN010 dating.** Livermore dates Stones River December 31–January 1; the frozen record
  runs December 31–January 2. The scoping memo flagged this, but no ledger input records why
  Livermore's figures are treated as matching.
  - If they were coded `interval_unresolved`, the Confederate side would become
    A 46,600 (33,000–53,590) from Cist's 46,604, instead of 34,730. The US side would be
    unchanged.
  - Record the decision and its reason in the input notes.
- **A4. KY009 Union basis.** The NPS table's 55,000 carries the engaged basis by extractor
  policy. But the NPS narrative calls it Buell's army "numbering nearly 55,000" on October 7.
  Cist says "less than one-half of this entire force was in the action". Livermore's note 1
  gives a conditional "less than 25,000" engaged. This is a policy-level tension, kept visible,
  not a coding error.
- **A5. Transcription gaps in `livermore-transcription-v1`.** The record is immutable; these are
  for any versioned successor.
  - p87: notes 1–4, 6 and 7 are omitted (note 4 drives R1).
  - p90: omits entry lines, not only loss lines: Rosser's cavalry 700, 12,984, the Toombs
    deduction of 733, 12,251 and 17,214. As transcribed, 12,284 → 11,393 does not reproduce.
    Note 3 is also missing.
  - p91: not transcribed.
  - p95: notes 1 and 2 are truncated.
  - p98: note 2 is truncated before "and Dunnington's brigade is to be added."
  - The transcription note says only loss lines and some notes are omitted.
- **A6. AR006 Confederate point.** Churchill's own "about 3000 effectives" sets an A point that
  Livermore disputes in the same note: two brigades had at least 3,190 enlisted men, and
  Dunnington's brigade is to be added (page image). A basis mismatch keeps rule 7 from
  labelling `bound_conflict`. Keep the dispute visible in the rationale.
- **A7. TN006 Union point.** The frozen 900 is below Cist's 1,700 surrendered in the same
  engagement. Class C post-start keeps that count out of the range. Keep the dispute visible in
  the rationale.
- **A8. TN011 `us-jp-1800`.** It is coded `adversary_or_hearsay_estimate`, contrary to extractor
  policy 1: Jordan and Pryor count as compiled unless the passage visibly shows an opponent's
  estimate. It is also the first Federal brigade only, so `partial_scope`. The 1,824 reason
  "does not reproduce" is not a design reason. Better: one brigade (`partial_scope`), from a
  newspaper correspondent's figures. Both are result-neutral.
- **A9. VA025 Livermore entry.** Livermore's composite "Manassas and Chantilly, August
  27–September 2" spans VA025's August 28 date, but VA025 records `livermore: null`. List it as
  `other_engagement` for completeness, as for VA026.
- **A10. MS002 earlier returns.** Greene's September 28 and October 1 return figures are coded as
  linked to the engagement. Under extractor policy 4 they are arguably `engagement_link_unknown`.
  That would add `applicability_unresolved` on the Confederate side without moving any point.
- **A11. VA028 November 10 figure.** Palfrey's November 10 127,574 is given the reason "other
  date". More precisely, it is an earlier return (`engagement_link_unknown`) that is "said to
  have been". Result-neutral.
- **A12. MS001 Union range.** The ledger reads the description range 4,000–4,500, giving a point
  of 4,250 against the frozen structured 4,000. This is disclosed in the note. It is acceptable,
  but the point differs from the frozen input by construction.
- **A13. Registry binding.** Design §7 says the ledger binds "the source registry snapshot". The
  ledger binds only the cited sources' metadata and raw hashes, which the memo flags as a
  deliberate choice. This batch cannot settle it; it is recorded here for reconciliation.

## Confirmed without change

- **Grade D sides.** The recorded reason matches the inspected sources, and no usable figure was
  missed in the dossier, the CWSAC row or the matching Livermore entry:
  - VA025 (both sides) and VA026 (both; only a wing bound and a composite entry);
  - KY008, WV016, TN007 and NC009 (both sides each);
  - WV010 Confederate, TN008 Confederate and TN009 Union;
  - TN011 Confederate (two one-sided upper bounds only).
- **Other sides.** No change beyond the advisories above:
  - KY007;
  - WV010 Union (the surrender count is a class C candidate under row 3 and sets the lower-median
    point by rule);
  - TN008 Union, TN009 Confederate, MS003, TN010 and AR006;
  - VA028 apart from R7, KY009 apart from R8 and R10(b), and MS002 Confederate.

## Review limits

- The page-image readings (R1, R10 and A5) are the reviewer's readings of the registered images
  and should be checked by the primary.
- Scope judgements (R3, R4) rest only on the cited passages, not on outside knowledge of the
  orders of battle.
- No source family was added and no new research was done.
