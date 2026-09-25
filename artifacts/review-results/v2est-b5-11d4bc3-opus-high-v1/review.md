# Strength ledger v2, batch 5 of 8: separate review

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a fresh-context subagent. The author's conversation was not an input.
- **Date:** 2026-09-25
- **Prepared commit reviewed:** `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` (previous `96110cf`)
- **Bundle / worktree HEAD:** `09c3a6b873b6bbafac2c1363cd3f60185a7c45da`
- **Assignment:** `assignment.md`, sha256 `bb0476c829391b601b70c97d2f3be8afebb1d480ccf18389956bb8d98920cc8d`
- **Input manifest:** `inputs.json`, sha256 `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0`
- **Ledger:** `data/estimates/side-strength-v2.json`, sha256 `e594047072a99c84e5239658df444f2946c945916d744de2ca6a82c8082629e8`
- **Outcome:** **corrections required** (R1)

This is an AI review: a separate analysis. It is not historical adjudication, independent corroboration, feature admission or authorization of any fit.

## Input verification

All 25 paths in `inputs.json` match their recorded SHA-256 values. I checked each one both from `git show 11d4bc3…:<path>` and from the worktree. There are no mismatches. The worktree differs from the prepared commit only by the review-assignment bundles (`git diff --stat 11d4bc3 09c3a6b`).

## Checks run (offline)

- `make check`: 143 tests passed ("OK"), and `python3 -m generalship check` exited 0.
- `python3 -m generalship estimate-check --ledger data/estimates/side-strength-v2.json` exited 0. It reported 305 in scope and 79 out of scope, with side grades A/B/C/D of 184/60/114/252. Fit-eligible row sets are 61/83/130, and 20 rows are excluded as `post_start_information`.
- I did not modify any primary artifact. The only file written is this review.

## Scope actually inspected

- **Rules.** I read AGENTS.md; `docs/strength-estimates.md` (all sections, with §§3–5 as the rules); tier-2 `docs/feature-admission-reported-strength.md` §§1–3 and the start of §4; `docs/ledgers-v2.md`; `docs/research/ledgers-v2.md`; the owner decision JSON; the v1 ledger memo; the ledger's `extractor_policies`; `generalship/estimates.py`; and `generalship/estimates_v2.py`.
- **Entries.** I reviewed all 27 assigned engagements (VA047, VA053, VA054, VA052, VA056, VA059, VA062, VA099, VA098, VA063, VA065, VA113, VA067, VA068, VA069, VA070, VA071, VA072, VA073, VA075, VA074, VA077, VA078, VA079, VA080, VA083, VA084). For each I checked both sides: every input, its estimate, null reason, inventory and rationale.
- **Dossier claims and frozen rows.** For each engagement I read every `strength` claim and each of its citation quotes in `data/evidence/VA0xx.json`. I also read the frozen `cwsac_battles.csv` row (forces text and description) and both `cwsac_forces.csv` rows.
- **Raw source context around cited passages:**
  - `nps-va047-v1` and `nps-va053-v1` (full pages);
  - the Sheridan, Wild and Butler selections (overland-v1);
  - the Humphreys overland and Bermuda Hundred selections;
  - the Humphreys Petersburg selections, at the VA053/054/062/063/072/073/079 passages;
  - the Wilson South Side raid selection;
  - the Hancock Deep Bottom selection;
  - the Hagood Port Walthall selection.
- **Livermore.**
  - I read `livermore-transcription-v2` sections p113–p118 and p128–p134.
  - I compared these page images against the transcription and the ledger values: p114, p115, p116, p117, p118, p128, p131 and p134.
  - I did not open the images for p113, p129, p130 or p133. The figures from those pages that I relied on are either class C inputs that do not set a point, or are confirmed by an adjacent image: the p133 total 34,517 equals the frozen CWSAC value.
- **Not inspected.** I did not inspect the 91 carried-forward v1 entries (out of scope), entries in other batches, or any source not cited by these dossiers.

## Required corrections

### R1: the 39,000 NPS Union "Forces Engaged" cell is coded inconsistently between VA047 and VA053

- **VA047 current coding.** `us-nps` (`nps-va047-v1`, "Forces Engaged :: 39000 total (US 39000; CS 0;)") is coded `other_engagement`, so the input is unusable. The note's reasoning is: "the VA053 page shows the same 39,000, so it is read as an army or campaign figure".
- **VA053 current coding.** The identical cell `us-nps` ("57000 total (US 39000; CS 18000;)") is coded class A for Proctor's Creek.
- **Why this is a coding error.** The two codings cannot both follow from the same evidence.
  - Tier-2 §3 item 2 applies `other_engagement` only to a figure that *is* for another action or for the campaign as a whole. A figure whose link to this engagement "is uncertain" is blocked instead. §3 item 1 says the same when the passages "do not settle" scope.
  - No cited passage states that 39,000 is a campaign figure. The NPS table itself assigns it to each engagement.
  - The doubt comes from inference: the same value appears on both pages, and the pages' own descriptions contradict the cell. At VA047 the description says "a Union division drove Hagood's and Johnson's brigades". At VA053 it says "to confront Butler's 30,000". Humphreys p.149 (cited in VA053) places "Ames … about 5,000 … Hinks with his division of 5,000 at City Point, and about 3,000 … in the Bermuda Hundred intrenchments" away from the Drewry's Bluff fight.
  - That is the "uncertain" case, and the ledger codes such cases `scope_unresolved` elsewhere:
    - VA004 `us-nps`: "equals the description's whole-army figure, while the action was Tyler's reconnaissance, so whether the army is this record's force is unresolved";
    - NM001 `us-nps-cell`: a cell disputed by the same page's description.

**Exact changes.** I recomputed these with the unchanged engine, in memory only.

1. **VA047, US, input `us-nps`.**
   - Set `codes` from `["derivation_unknown", "other_engagement"]` to `["derivation_unknown", "scope_unresolved"]`, and `class` from `unusable` to `C`.
   - Update the note, for example: "live NPS forces-engaged cell for this record; the same page's description names a division as the engaged force and the same 39,000 appears on the VA053 page, so whether it is this engagement's force is unresolved (as VA004)".
   - The US estimate becomes:
     - grade `C`, point 39,000, low 27,300, high 50,700, `point_basis` `reported_engaged`, method `rule3_median`;
     - labels `applicability_unresolved`, `compiled_dependence`, `derivation_unknown`, `single_input`, `whole_engagement_leakage`;
     - point and range groups `["us-nps"]`.
   - Remove the US `null_reason` and update the rationale.
   - The Confederate side stays D, so `nested` is unchanged (`sets: []`, row incomplete).
   - Leave `us-desc` (33,000) as `other_engagement`. The description itself gives it as the army "disembarked … on May 5" and names the engaged force separately ("a Union division"). This matches how this batch treats army-wide figures (VA070, VA071, VA072, VA083, VA084 "army-wide; not entered").
2. **VA053, US, input `us-nps`.**
   - Set `codes` from `["derivation_unknown"]` to `["derivation_unknown", "scope_unresolved"]`, and `class` from `A` to `C`.
   - The note should record the same reason and cite the page's "Butler's 30,000" and Humphreys p.149.
   - The US estimate stays grade `A`, point 30,000, low 28,500, high 40,950 (the `us-nps` candidate still enters the rule 5 hull). The labels gain `applicability_unresolved`, giving `applicability_unresolved`, `compiled_dependence`, `derivation_unknown`, `whole_engagement_leakage`.
   - `nested` is unchanged (set1_A, set2_AB, set3_ABC).
   - The Confederate side is unchanged.

**If the primary prefers the opposite reading,** that 39,000 is established as a campaign-level cell, then VA053 `us-nps` must also become `other_engagement`. The VA053 US range would then shrink to 28,500–31,500, with the point unchanged at 30,000 and without `applicability_unresolved`. VA004 and NM001, outside this batch, would then need to be re-examined for consistency. Either way, the two entries in this batch must not code one cell two ways.

**Consequence for this batch.** Only one side changes grade: VA047 US moves from D to C. No fit row set changes. The mechanically resulting point, 39,000 for a division-level action, is what the declared rules give an `applicability_unresolved` candidate. It is not a historical judgement.

## Advisories (no correction required)

- **A1: VA071 interval.** Livermore heads the entry "DEEP BOTTOM, AUGUST 14-19, 1864", while the frozen interval is August 13–20.
  - VA062 codes a similar mismatch as `partial_interval`: Livermore's June 1–3 against a frozen May 31–June 12.
  - Not coding it at VA071 is defensible. The frozen description has the same II Corps, X Corps and Gregg's division crossing on the night of August 13–14 and withdrawing on the 20th, and Livermore's components are those formations.
  - Record the reason in the `us-lv-eff`, `us-lv-pfd` and `cs-lv` notes.
  - Coding it `interval_unresolved` would add only `applicability_unresolved`. Both sides would stay C through row 3, and the row stays excluded.
- **A2: VA054 `us-smith`.** "very nearly 16,000 infantry" is a cap on one part. The ledger practice for such caps is `one_sided_bound` with `bound: null`; VA062 `cs-hoke` ("a little less than 6,000") is an example. Recoding VA054 would not change the estimate: the side stays D and the residual class is C anyway.
- **A3: VA063 inventory.** The cited Humphreys quote also carries a rejected figure: "The Second Corps had 20,000 enlisted men, not 28,000, as has been stated." The 28,000 is not listed. Add it with a reason: an unattributed Second Corps figure that Humphreys rejects, and a part of the force. This has no effect on the estimate.
- **A4: VA067 and VA068, US.** Wilson's "about 5,500 cavalry and twelve guns", from the departure on June 22, is in the same Wilson selection these dossiers cite, and VA113 uses it as class C. It is not among the VA067 or VA068 dossier citations, though. Using it on June 28–29, after Staunton River Bridge, would borrow a figure across engagements (design §8). Grade D is consistent. The null reasons could mention that the figure was considered.
- **A5: VA056 inventory wording.** Wild's "I estimated them at … my own, and probably triple" is a multiple of the defenders' own strength, not a count, and its first term is garbled. Neither reading yields an input, so "unreadable_value, not entered" gives the right result. A more accurate reason would be "a multiple of the Union garrison, not a count; first term garbled".
- **A6: VA083 Confederate result (a declared-rule consequence, not an error).**
  - Rule 2 groups the frozen 13,835 with Livermore's identical effectives line. p.134 note 1 makes that line `scope_unresolved`: the right wing "probably requires that more should be included, but the Records do not show the constitution of this right wing". I confirmed this reading from the image.
  - The group becomes C with basis `unknown`, so the basis order lets Livermore's present-for-duty 14,877 set the point: C 14,880 (9,680–19,340).
  - The coding is correct. The rationale already states the mechanism.
- **A7: VA072 Confederate.** Grade D is supported. Livermore's line "Add losses below and August 25 2,339" includes August 25 losses from VA073, a later engagement, which I confirmed on the image. Humphreys p.277 adds "part of Hoke's division with Lee's cavalry" to Hill's corps. The input is therefore bound-only (`partial_scope`, `post_engagement_state`, `not_prior`), as coded.

## Confirmations (inspected, no finding)

- **Values checked against the page images.** Every Livermore value that sets a point, or a bound that is applied, matches the page image and is attributed to the correct side:
  - VA062 107,907;
  - VA063 63,797 / 73,368 / 78,891 and Confederate 41,499;
  - VA070 20,708 / 16,910 and Confederate 12,331 / 11,466;
  - VA071 30,080 / 27,974 and Confederate 20,008;
  - VA072 20,289 / 14,787 / 681;
  - VA075 19,639 (p.128);
  - VA079 Confederate 20,324;
  - VA083 Confederate 14,877 / 13,835.
- **Loss timing and post-start state.** These codes are correct in every case: VA053, VA063, VA070, VA071, VA072, VA075 and VA079 (Union). Each loss line includes the start date or later days, or the return is dated after the start.
- **Frozen CWSAC rows.** VA053, VA062, VA063, VA098 and VA083 are grade A as expected. VA098's Confederate "2,500" is description text with no strength bounds and is correctly quoted from the cell. The CWSAC and NPS reproductions are linked, and unlinked NPS narrative restatements follow the v1 policy.
- **Grade D sides.** VA054, VA059, VA065, VA067, VA068, VA069, VA073, VA074, VA077, VA078, VA080, VA084 and VA099 (both sides), plus VA052 CS, VA113 CS and VA072 CS: each recorded reason is accurate. The inspected citations carry only formations, parts, post-start figures, army-wide figures or opponent estimates of parts. No usable figure was missed, apart from R1 (VA047 US).
- **Point-setting C and B sides.** The C and B sides are coded correctly and reproduce under the engine:
  - C from `engagement_link_unknown`: VA052 US (Sheridan's "about 10 000" at the campaign's opening on May 4) and VA113 US (Wilson's departure strength);
  - B from `basis_unknown`: VA056 (Butler's "force of 1,800 men" and the frozen description's "about 1,800" and "about 3,000").
- **Inventories.** Every dossier strength claim, every figure in its citations (except A3) and every frozen force cell is referenced by an input or has a reason, and the reasons are accurate. For the Livermore entries on pp.113–118 and 128–134, each unentered line is accounted for.
