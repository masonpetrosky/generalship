# Focused follow-up review: commander residual ratings design (revision `a5a1cd1`)

## Reviewer record

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), `high` reasoning effort. This is a
  fresh-context subagent; the primary's conversation was not an input.
- **Date:** 2026-09-25.
- **Commits:**
  - prepared commit reviewed: `a5a1cd1e7d49e031f6f46dac9f4a47f8be7f84f7`;
  - previous commit: `0de28bd7cdf595b49a8aa80e170650ad82d72a20`;
  - bundle commit: `56a0f193e04603df7862f21f627988e51765f480`. The worktree was at that
    commit with no local changes.
- **Assignment:** `assignment.md`, sha256
  `00bfebfc025a388ae9f18054f8fb631a52687a42933866168403324745129ab7` (verified).
- **Input manifest:** `inputs.json`, sha256
  `ada03436d394a8f45817404cd8f838891a0fc8b88c0c70a085100d98b566a592` (verified).
- **Input hashes:** I checked all 26 bound paths with `git show a5a1cd1:<path>` and in the
  worktree. All match. **No mismatches.**
- **Read but not bound by the manifest.** I hashed these at `a5a1cd1`; each file is identical at
  `0de28bd`.
  - `artifacts/estimate-evaluation.json`: `d02fa45ce7b876940393deb104725fc856ffbc11fb8929f564beb43a94a59886`.
    This is the same hash that the first review recorded. I used it for the 37 `set3_ABC`
    battle IDs.
  - `data/estimates/evaluation-authorization-v1-confirmation.json`:
    `7dc9a635544550a1101ad2cf75c5fdd73a9de7e91ba708c0fdc7727796afa385`. I read it in full.
  - `data/estimates/side-strength-v1.json`:
    `0656b03cbdaa088849dc3795f9c6a9e9d6762be10f53f28e4285be46f7fcde89`. I looked only at its
    top-level keys.

### Scope actually inspected

- **Read in full:**
  - the revised `docs/commander-ratings.md` (371 lines);
  - `git diff 0de28bd a5a1cd1 -- docs/commander-ratings.md`;
  - the first review (`review.md`);
  - `correction.json` and `primary-assessment.md`;
  - `data/command/owner-decision-2026-09-25.json`;
  - the evaluation confirmation record.
- **Computed from frozen inputs, without using outcomes:**
  - The 91 decisive, non-aggregate records in `artifacts/battles.json`.
  - Every same-campaign pair among them where one record's interval lies inside the other's.
    There are 9 pairs, the same set the first review found. No two records share an identical
    interval.
  - Which of those records are among the 37 primary rows.
  - Every side among the 91 whose `cwsac_commanders.csv` listings differ in `navy`.
  - Every side of the 37 primary rows with more than one listing.
  - The set of rank strings used in the listings for the 91 records.
- **Hash-verified but not read:**
  - `README.md`, `docs/methodology.md`, `docs/roadmap.md`, `docs/evidence-contract.md` and
    `docs/sources.md`;
  - `generalship/cli.py` and `tests/test_evidence.py`;
  - the admission files, `artifacts/baseline.json` and `artifacts/admission-check.json`;
  - `data/pilot/cohort.json`, `data/sources.json`, `cwsac_battles.csv` and `cwsac_forces.csv`.
- **Not opened:** no dossier and no source text.
- **Not run:** no build, packet, evaluation or check command, and no model fit.
- **Other tools:** no network, no new research and no agents.

## Outcome: **corrections required**

### Question 1: were R1–R9 and A1–A7 applied faithfully?

Yes, in substance. Every required correction and advisory from the first review appears in the
revised text, mostly word for word. There are two justified adaptations:

- §8 says "no temporal verdict" where R8 said "no temporal check", because A5 adds a descriptive
  temporal split.
- The robustness-view list is wider than R7's, because A1 and A2 add views.

One change goes beyond what was requested, and it removes a limit (F8). Two applied texts have
gaps once they are read as mechanical rules: A1 (F1) and R3 (F2).

### Question 2: new contradictions or rules that cannot be checked

Six findings:

- the alternative-candidate view does not say how grade D sides are handled (F1);
- the scope of the nesting rule against the 37 primary rows (F2);
- the verdict's "both weightings" (F3);
- `view_sensitive` when a commander is unranked in a view (F4);
- rule 5 when one service has several listings (F5);
- rule 2 when a passage contradicts the listing (F6).

### Question 3: does the decision record match the status paragraph?

Mostly. Two statements go beyond the record (F7).

This is an AI follow-up review. It is not historical adjudication, feature admission or
authorization of any fit.

## Required corrections

### F1. The alternative-candidate view is undefined for grade D sides and for sides with several candidates (§6; A1)

**Evidence.**

- The view reads: "Each `responsibility_unresolved` or `joint_command` side is assigned to its
  other recorded candidate."
- A grade D side has no chosen commander, so it has no "other" candidate. This covers rule 3(c)
  ties and rule 5 when nothing is shown.
- On the 37 primary rows, the tied listings are:
  - TN003 US: Grant and Buell;
  - TN003 CS: Johnston and Beauregard;
  - VA102 US: Milroy and Schenck;
  - GA003 CS: Hindman and Breckinridge;
  - GA004 US: Rosecrans and Thomas, both "Major General".
- A side can also have more than one other candidate, for example VA012 CS among the 91, which
  has four listings.
- §2 says "A grade D side contributes no commander term". It does not say whether this view gives
  such a side a term.

**Replace the "Alternative candidates" bullet in §6 with:**

> - **Alternative candidates.** One refit for each side with recorded candidates and for each of
>   those candidates other than the primary choice. For a grade D side, every recorded candidate
>   counts. Each refit changes only that side, which gets that candidate's commander term. Every
>   other side stays as in the primary attribution.

### F2. The nesting rule does not say which views it acts on, and it could be read as removing primary rows (§2 rule 7, §3; R3)

**Evidence.** Rule 7 says: "No view gives one commander both records of a `nested` pair: the
containing record is used, and the contained one is listed as nested." This can be read in two
ways:

- as dropping the contained record even when the containing record is not in the view;
- as dropping it only when the same commander appears on both records.

The first reading shrinks the 37 rows. Four contained records are primary rows: MD002 (inside
WV010), MS006 (inside MS005), LA011 and AR008 (both inside MS011). Their containing records are
not primary rows. VA032 is a primary row, but the records it contains, VA033 and VA034, are not.
Dropping any of these contradicts two statements:

- §5: "the 37 primary rows only";
- §3: the primary rows are "the same rows as the evaluation's A–C set".

The second reading, which depends on the commander, still counts the row's outcome twice
through α and β.

§3 also lists "nested" as a reason a battle is out of the model. Under the correct reading, that
never happens on the primary rows.

**Replace the last two sub-bullets of rule 7 with:**

> - In any view whose rows include both records of a `nested` pair, the contained record's row is
>   dropped and listed as nested, whoever the commanders are. A view that includes only one
>   record of the pair keeps it.
> - For `nesting_unresolved` pairs, every view whose rows include both records is reported with
>   and without the contained record.
> - No pair has both records among the 37 primary rows. MD002, MS006, LA011 and AR008 are primary
>   rows, but their containing records (WV010, MS005 and MS011) are not. VA032 is a primary row,
>   but VA033 and VA034 are not. Rule 7 therefore does not change the primary rows or the §5
>   verdict. It acts on outcome-only view (ii).

**In §3, replace** "why the others are out (strength grade D, post-start, nested, or
unattributed)." **with:** "why the others are out (strength grade D, post-start, or
unattributed), and which are dropped as nested in outcome-only view (ii)."

### F3. "No improvement under both weightings" can be read two ways (§5; R6)

**Evidence.**

- "If there is no improvement under both weightings" can mean either:
  - that neither weighting improves; or
  - that the model does not improve under both.
- If the model improves under one weighting and not the other, the two readings give opposite
  presentations. Under one there is an ordered ranking; under the other there is none, and the
  results are labelled `no_heldout_signal`.
- The wording was ambiguous before this revision. It now decides what gets published, so it has
  to be read mechanically.

**Add to §5, after "Verdict metric":**

> - **Improvement.** The commander model improves only if its held-out log loss is strictly lower
>   than the strength-only model's under both the battle weighting and the campaign weighting. A
>   reduction under one weighting only, or a tie, is no improvement. Both values are reported.

**And replace** "**If there is no improvement** under both weightings:" **with** "**If there is no
improvement:**".

The author may choose the other reading instead. The design must then state it explicitly.

### F4. `view_sensitive` does not say what happens when a commander is unranked or absent in a view (§6; R7)

**Evidence.**

- Several robustness views can drop a primary-ranked commander below 2 modelled battles, or
  remove their term altogether:
  - the grade A–B view;
  - excluding the `command_changed` rows;
  - the alternative-candidate and superior-directing refits.
- In such a view the commander has no rank interval, so the non-overlap test cannot be computed.
- "A commander with at least 2 modelled battles" does not say in which view the count is taken.

**Replace the `view_sensitive` paragraph in §6 (up to "…primary 80% rank interval.") with:**

> **`view_sensitive`.** A commander with at least 2 modelled battles in the primary view is
> flagged if, in any robustness view (each refit counted separately):
>
> - they have a term, and their 80% interval lies entirely on the opposite side of zero from
>   their primary posterior mode; or
> - they are ranked in that view, and their 80% rank interval does not overlap their primary 80%
>   rank interval.
>
> If they are not ranked in a view (fewer than 2 modelled battles there, or no term), the report
> labels them `unranked_in_view`, naming that view.

### F5. Rule 5 does not choose among several listings in one service (§2 rule 5; R2 rule order)

**Evidence.**

- VA012 (Drewry's Bluff) CS is one of the 91 records. Its listings are:
  - navy: E. Farrand ("Commander") and S. S. Lee ("Captain");
  - army: William Mahone ("Brigadier General") and John Taylor Wood ("Lieutenant").
- Rule 5 applies first, but "use the listed commander of the force … compelling the result"
  assumes one listing per force.
- Rule 3 is not stated to apply after rule 5.
- The checker cannot verify that "grades follow from the recorded rule" for this side. No such
  side is among the 37 primary rows, but the ledger covers all 91.

**Append to the second bullet of rule 5:**

> If that force has several listed commanders, rule 3 is applied to them. The side is then
> grade C, or grade D if rule 3(c) applies. VA012 CS is such a side.

### F6. Rule 2 does not say whom to use when a passage contradicts the listing (§2 rule 2; A4 and the grade table)

**Evidence.**

- A4 made "contradicts" operational: a passage "names a different officer as commanding the
  side's engaged forces when the fighting began".
- Rule 2 still says only "Use that commander unless an inspected passage contradicts the
  listing".
- The grade table implies grade C ("inspected sources disagree"), but no rule names the chosen
  commander or the candidates. The checker therefore cannot verify the side.
- The officer named in the passage may have no CWSAC string. The registry, however, is defined
  by "every CWSAC name string mapped to them".
- This gap existed before the revision. The operational test now makes it reachable.

**Add as a third sub-bullet of rule 2:**

> - If inspected passages contradict the listing and all name the same other officer, use that
>   officer. Otherwise use the listed commander. Either way, the side is grade C, labelled
>   `responsibility_unresolved`, with the other officers recorded as candidates.

**And in the identity registry, after "every CWSAC name string mapped to them;", add:**

> - for an officer named only in an inspected passage, that citation.

### F7. The status paragraph says more than the decision record supports (status; R9)

**Evidence.**

- **The date of the request.** The record gives one date, `decision_date: "2026-09-25"`, and
  gives no date for `earlier_owner_request`. The status paragraph's "On 2026-09-25 the owner
  asked…" and "Later the same day" are therefore not recorded.
- **"Verbatim."** The record is `recorded_by` the primary agent "from the owner's chat
  messages". A reviewer cannot check whether it is verbatim. It holds one request, one set of
  questions and one reply.
- **"Confirms."** The status paragraph says "The same reply also confirms the evaluation's
  option (a)". The confirmation record's own reading says the reply is "recorded as a general
  acceptance of the recommendations, not a separate statement about option (a)".
- The quoted fragment of the owner's request, the three questions and the reply all match the
  record.

**Replace the first paragraph (from "**Status:" through "…evaluation-authorization-v1-confirmation.json))."):**

> **Status: proposed; revised after a separate design review.** The owner had asked "Are we ready
> to rank the generals in the American civil war, or is there still work to be done?". They were
> then asked three design questions: who gets credit, what unit is scored, and how a rating is
> computed. On 2026-09-25 they answered: "Okay, yeah I'm fine with whatever you recommend." The
> [decision record](../data/command/owner-decision-2026-09-25.json) keeps the request, the
> questions and the reply as the primary agent recorded them from the owner's chat. It does not
> date the earlier request. The choices below are the author's recommendations, which the owner
> delegated; they are not the owner's own words. The same reply is also recorded as confirming
> the evaluation's option (a), as a general acceptance of the recommendations rather than a
> separate statement about it
> ([confirmation](../data/estimates/evaluation-authorization-v1-confirmation.json)).

If the primary has a dated record of the earlier request, it may cite that record and keep the
date instead.

### F8. The revision deleted a limit that R4 did not ask to remove (§8)

**Evidence.**

- R4 asked to replace a single sentence: "The Union intercept α absorbs side-wide differences
  only partly."
- The revision also deleted the next sentence, "Army quality, subordinates and supply stay in the
  residual.", from the "Not causal" bullet.
- The new "Side-relative" bullet mentions army, theater and opponent differences, but no longer
  mentions subordinates or supply.

**Replace the "Not causal" bullet with:**

> - **Not causal.** The rating is not command skill. Commanders are not randomly assigned to
>   armies, theaters, opponents or odds. Army quality, subordinates and supply stay in the
>   residual.

## Advisories (not required)

- **AD1. Rule 5 with a stated overall commander gets grade C.** Rule 5's first bullet is decided
  by a passage showing one officer in overall command. The equivalent passage under rule 3(a) or
  rule 2 earns grade A. The table is consistent, and it is conservative. Either give the rule 5
  passage case grade A or state why it stays at C, because it is excluded from the grade A–B view.
- **AD2. GA004 US is also a tie.** Rosecrans and Thomas are both listed as "Major General".
  - The first review's list of ties, and the primary's assessment that "the rank ties (TN003,
    VA102, GA003) … hold", both omit this side.
  - It may affect the provisional count of "8" commanders with two or more battles. §8 already
    labels that count provisional.
  - Consider rewording the rule 3(c) examples: "(tied listed ranks occur at TN003 on both sides,
    VA102 US, GA003 CS and GA004 US; they reach 3(c) only if 3(a) does not decide them)". As
    written, the examples can read as if these sides are grade D, although the first review noted
    that VA102's Allan passage may settle rule 3(a).
- **AD3. Declare the rank order.** Rule 3(b) needs an ordering of the rank strings actually used
  in the listings for the 91 records:
  - army: General, Lieutenant General, Major General, Brigadier General, Colonel, Brevet Colonel,
    Lieutenant Colonel and Lieutenant;
  - navy: Rear Admiral, Acting Rear Admiral, Flag Officer, Captain and Commander.

  Say how "Brevet" and "Acting" ranks are treated, so that the checker can verify 3(b) and 3(c).
- **AD4. The "Effective denominator" sentence is inaccurate.** It says: "Commanders whose modelled
  battles all fall in one campaign never affect a held-out prediction". Their θ is never used for
  their own held-out rows, but in other folds their rows still inform α, β and their opponents'
  θs. Suggested text: "Such commanders' own θ is never used in a held-out prediction (it is 0 in
  their own fold), though their rows still inform α, β and their opponents' θs in other folds."
  The first review's R6 introduced this wording.
- **AD5. Grade D rows in the β = 0 views.** "Its row still counts through α and β" should say
  "through α (and β where the view has a force term)".

## Checked and found consistent

- Rules 2, 3, 5 and 6 have preconditions that do not overlap, so the stated order 5, 3, 2, 6
  never conflicts, apart from the rule 5 case in F5. Rule 4 is applied to the chosen commander,
  and the Target's definition of "first combat" keeps rule 4 consistent with dates alone.
- The grade table follows from the rules, apart from F6 (the contradicted listing) and AD1.
- Grade D sides contribute no commander term in the primary model, in the verdict and in the
  grade A–B view. F1 covers the one view that needs its own rule.
- Within-side ranks, the connectivity labels, the posterior-to-prior sd ratio, the mode wording,
  the no-signal JSON labels and the 1862→1863 split without a verdict are all stated so that they
  can be applied.
- The design's §§5 and 7 and §8's limits no longer disagree with each other.
- The owner decision record's reading matches the design as drafted: battles as the unit, one
  responsible commander per side, and partial pooling with uncertainty.
