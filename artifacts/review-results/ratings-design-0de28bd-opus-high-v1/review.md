# Separate design review: commander residual ratings v1

## Reviewer record

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), `high` reasoning effort, as the assignment
  specifies. A fresh-context subagent; the author's conversation was not an input.
- **Date:** 2026-09-25.
- **Prepared commit reviewed:** `0de28bd7cdf595b49a8aa80e170650ad82d72a20`, against the previous
  commit `f5fed2e6e971cc37a0610a38b10ed0bad4e300d6`. The bundle commit is
  `33247f084202e38d8d3f4cb5fb49c49294009dd0`; the worktree was checked out there with no local
  changes.
- **Assignment:** `assignment.md`, sha256
  `990339839d912dcaa19d9a003292ab8ee901bc072cae379bd02b7f725ac5e5a9` (verified).
- **Input manifest:** `inputs.json`, sha256
  `4e5b7cac1bfa6c8189bae7edff7e3f027a29c51fa76c336721dcd792fb80eb1c` (verified).
- **Input hashes:** all 22 bound paths match their manifest hashes, both via
  `git show 0de28bd:<path>` and in the worktree. **No mismatches.**
- **Read but not bound by the manifest:** the assignment names three files that `inputs.json`
  does not bind. I hashed them at `0de28bd`:
  - `docs/strength-estimates.md`: `795212ad5a3291a6630911fd5671c9f85a52b19c1d05045c091db1de96164ba3`
  - `artifacts/estimate-evaluation.json`: `d02fa45ce7b876940393deb104725fc856ffbc11fb8929f564beb43a94a59886`
  - `generalship/baseline.py`: `731d9ad96dc85ca8f69bd7689e7ec64d9a1917b1a4b9d45c9c55b37348d42179`

  I also read `data/estimates/side-strength-v1.json`, which is not bound either, to get the
  37 rows' strength points and the set of 91 records.

### Scope actually inspected

- **Read in full:**
  - `docs/commander-ratings.md`, the object of review (230 lines);
  - `docs/methodology.md`;
  - `docs/strength-estimates.md`;
  - `docs/research/estimate-evaluation-v1.md`;
  - `generalship/baseline.py`;
  - the `0de28bd` diff (the design, the confirmation record, the receipt line and the memo
    sentence).
- **Read in part:** `docs/roadmap.md`: the current priority (lines 1–250), the next priority
  (lines 405–427) and Milestones 0–4 with the deferred choices (lines 431–620).
- **`artifacts/estimate-evaluation.json`:** its structure, the counts for `set3_ABC` (37 rows,
  19 campaigns, 25 Union wins), all 37 of its predictions, and the fold slopes and intercepts.
- **`data/raw/cwsac_commanders.csv`:** every listing for the 37 A–C rows.
- **`data/raw/cwsac_battles.csv`:** names, intervals and descriptions for VA032–VA034 and
  MS004–MS006, plus a scan of interval containment across the 91 in-scope records.
- **Dossier `responsibility` claims:** those in PA002, VA016, VA102, TN001, AR006, MS001, GA003,
  MS006 and TN003. I checked the claim values and up to three citations each against the stored
  quotes. I did not open the underlying source texts.
- **Hash-verified but not read:** README, `docs/evidence-contract.md`, `docs/sources.md`,
  `generalship/cli.py`, `tests/test_evidence.py`, the admission files, the receipt, the cohort,
  `data/sources.json` and `cwsac_forces.csv`.
- **Not run:** `make check`, which is not useful for a documentation-only design. No build,
  packet or evaluation command was run. I did **not** fit the proposed commander model to real
  outcomes, because doing so would preview results before the design is fixed.

The only computations were these:

- a sum over the 37 rows' force ratios, which uses no outcomes;
- a commander–opponent graph built from the CWSAC listings as a stand-in for the ledger, which
  does not exist yet (see R4).

No network, no new research and no agents were used.

## Outcome: **corrections required**

The design is a careful, honest diagnostic proposal. It keeps residuals, execution effects and
campaign contribution apart, never splits credit among listed commanders, fixes τ and the
held-out reading in advance, and states its selection and truncation limits. It still needs
nine corrections before the ledger is built. The attribution target is ambiguous exactly where
the cohort needs it (R1, R2). One view double counts nested records (R3). Cross-side and
cross-component comparisons are identified only by the prior (R4). Several statements overstate
what the model conditions on or what escapes prior dominance (R5). The held-out test and
`view_sensitive` are not specified enough to be read mechanically (R6, R7). The limits (R8) and
the provenance of the delegated design choices (R9) are incomplete.

This is an AI design review. It is not historical adjudication, feature admission or
authorization of any fit.

## Required corrections

### R1. The target conflates formal and field command, and "start of interval" is not defined for date-only records (§2)

**Evidence.**

- Every frozen interval is a date range, and every inspected dossier has
  `tactical_replacement_at: null`. The "start of the record's interval" therefore has no clock
  time, and there is no registered clock anchor to supply one.
- **VA102 (McDowell, 1862-05-08).** Allan's passage reads "with the approval of Gen. Schenck,
  who, as senior, now com-" / "manded". "Now" implies that Schenck took command on or near the
  start date. Read literally, "at the start of the interval" could give Milroy (the commander at
  the start) plus a `command_changed` label, or Schenck. The rules do not say which.
- **MS001 (Iuka).** The NPS passage says Grant "ordered Ord to await the sound of fighting
  between Rosecrans and Price". CWSAC lists only Rosecrans. The phrase "exercising overall command
  of that side's forces engaged" does not say whether a superior directing the operation from
  within the theater (Grant) or the listed field commander (Rosecrans) is meant.
- **TN003 (Shiloh).** Halleck's order reads "he will exercise his separate command, unless the
  enemy should attack you. In that case you are authorized to take the general command." Command
  here is conditional authority, not simply on-field presence.

The methodology's replacement time is "at the start of the engagement". That is the right
anchor in principle. It needs a checkable definition.

**Replace §2 lines 41–46 (from "**Target.**" through "…replacement time for a battle.") with:**

> **Target.** For each of the 91 decisive, non-aggregate engagements and each side, name:
>
> > the officer who held command of that side's engaged forces, as the field commander directing
> > the operation, when the record's fighting began (the **responsible commander**).
>
> - *Command* means command authority over the engaged forces, whether or not the officer was on
>   the part of the field where fighting began. A departmental or national superior who was not
>   directing this operation in the field is excluded.
> - *When the fighting began* means the side's first combat within the frozen interval, which
>   matches the methodology's replacement "at the start of the engagement". Frozen intervals are
>   dates. A change of command on the start date before the first combat is therefore not a
>   command change under rule 4: the officer in command at first combat is used.
> - If an inspected passage shows a superior other than the listed commander directing the
>   operation from within the theater (for example, MS001, where the NPS description has Grant
>   ordering Ord "to await the sound of fighting between Rosecrans and Price"), the listing
>   still decides under rules 2–3. The side is labelled `superior_directing`, naming that
>   officer, and §6 adds a view that uses the named superior instead.

**Also add to §6:** "**Superior directing.** Sides labelled `superior_directing` use the named
superior."

### R2. Rule 3's rank fallback has no tie or cross-service rule, the rule order is unstated, and the grade table conflicts with rule 3 (§2)

**Evidence** (CWSAC listings for the 37 primary rows):

- **Rank ties:**
  - TN003 US: Grant and Buell, both "Major General";
  - TN003 CS: Johnston and Beauregard, both "General";
  - VA102 US: Milroy and Schenck, both "Brigadier General";
  - GA003 CS: Hindman and Breckinridge, both "Major General".
- **Cross-service pairs** (`navy` = 1 against 0):
  - TN001: Foote ("Flag Officer") and Grant ("Brigadier General");
  - AR006: Porter ("Acting Rear Admiral") and McClernand ("Major General").

  In both cases rules 3 and 5 could each apply, and they can give different people. At TN001,
  rule 5 ("the force whose action the frozen record describes") points to Foote: the NPS
  description reads "surrendered to the fleet". Rule 3 has no ordering between army and navy
  ranks.
- **Grade table.** The table gives grade C when "Rules 3–5 decided the choice". Yet under rule 3
  the choice can be settled by a passage that states command, which is grade A's condition.
  VA102's Allan passage is such a case.

**Replace rules 3 and 5 and the grade table with:**

> Rules are applied in this order: 5, then 3, then 2, then 6. Rule 4 is then applied to the
> result.
>
> 3. **Several listed commanders in one service.**
>    - (a) Use the one an inspected passage shows in command of the side's engaged forces when
>      the fighting began.
>    - (b) Otherwise, if one listed officer outranks every other by listed rank, use that officer
>      and label the side `responsibility_unresolved`.
>    - (c) If the highest listed ranks tie (for example, TN003 US, TN003 CS, VA102 and GA003 CS),
>      there is no rank fallback. The side is grade D, labelled `responsibility_unresolved`, with
>      the tied candidates recorded.
> 5. **Several listed commanders in different services** (CWSAC `navy` differs, for example TN001
>    and AR006).
>    - If an inspected passage shows one officer in overall command of both forces, use that
>      officer.
>    - Otherwise, use the listed commander of the force that an inspected passage or the frozen
>      description shows compelling the result (for example, surrender "to the fleet" at TN001),
>      and label the side `joint_command`.
>    - If neither is shown, the side is grade D, labelled `joint_command`, with the candidates
>      recorded.
>
> | Grade | Condition |
> | --- | --- |
> | A | Rule 2 or 3(a): an inspected passage states that the officer commanded the side's engaged forces when the fighting began, and nothing inspected contradicts it. |
> | B | Rule 2 with no passage stating the command, and nothing inspected contradicting the single listing. |
> | C | Rule 3(b) or rule 5 decided the choice, or inspected sources disagree about who commanded. |
> | D | Rule 3(c), rule 5 with nothing shown, or rule 6. |
>
> Labels such as `command_changed` and `superior_directing` do not change the grade.

### R3. The outcome-only view double counts nested records; the design has no nesting rule (§§2, 6, 8)

**Evidence.** Among the 91 in-scope records, nine same-campaign pairs have one interval inside the
other:

| Containing record | Contained record |
| --- | --- |
| MS005 | MS004 |
| MS005 | MS006 |
| MS011 | AR008 |
| MS011 | LA011 |
| VA026 | VA025 |
| VA032 | VA033 |
| VA032 | VA034 |
| VA033 | VA034 |
| WV010 | MD002 |

Interval containment alone does not show nesting. Helena (AR008) is not part of the Vicksburg
siege, for example. But **VA032 (Chancellorsville, 30 April–6 May)** narrates the Sedgwick
operations in its frozen description: "Sedgwick's VI Corps and Gibbon's division remained to
demonstrate…" and "after Union reverses at Salem Church, Hooker recrossed". Its reviewed US
strength point is 114,500. **VA033 (Salem Church, 3–4 May)** lists Lee as the Confederate
commander and has a Confederate result.

In the 91-row outcome-only view, Lee could be credited twice for the same fighting. That breaks
AGENTS.md's no-double-counting rule and the roadmap's precedent that overlapping records are
"not three independent wins". VA033 and VA034 are grade D for strength, so the primary 37 rows
are not affected. The §8 sentence "There is no battle and campaign double counting" does not
cover battle-within-battle nesting.

**Add to §2 as rule 7:**

> 7. **Nested records.**
>    - The checker lists every same-campaign pair among the 91 whose frozen interval lies inside
>      another's. For each pair, the ledger records one of three outcomes:
>      - `nested`, when an inspected passage or the frozen description shows that the containing
>        record's fighting or force scope includes the contained record (for example, VA032's
>        description narrates the Sedgwick operations and Salem Church, VA033);
>      - `not_nested`, with a reason;
>      - `nesting_unresolved`.
>    - No view gives one commander both records of a `nested` pair. The containing record is
>      used, and the contained one is listed as nested.
>    - For `nesting_unresolved` pairs, every view that contains both records is reported both with
>      and without the contained record.

**Also add to the §2 checker list:** "that every contained-interval pair has a nesting outcome."

**In §8, replace** "There is no battle and campaign double counting" **with:** "There is no
battle and campaign double counting, and no double counting of nested records (rule 7)".

### R4. Cross-side and cross-component comparisons are identified only by the prior; the rank set is unspecified (§§4, 8)

**Evidence.**

- **Side offset.** In `logit P = α + βx + θ_US − θ_CS`, adding c to every Union θ and
  subtracting c from α leaves every prediction unchanged. The same holds for the Confederate θs
  with +c. The likelihood cannot separate a side-wide difference from α; the Normal(0, 1) and
  Normal(0, τ²) priors decide it. For a uniform shift δ over n commanders of one side, the mode
  puts 4n/(4n + 1) of δ into α when τ = 0.5. With many commanders per side, α therefore takes
  nearly all of any side-wide difference, including a real difference between the two sides'
  average commanders.
- **§8 wording.** §8's "The Union intercept α absorbs side-wide differences only partly" states
  the opposite of this, and a combined cross-side ranking silently assumes that the two sides'
  commander means are equal.
- **Connectivity.** The methodology requires checking "whether commander assignments and army
  context can be distinguished at all; weakly connected schedules may not identify them." The
  design has no connectivity check. As a rough stand-in I built the commander–opponent graph
  from the CWSAC listings: the senior listing, with illustrative choices at the tied and joint
  sides TN003, VA102, TN001, AR006 and GA003. This is not the ledger. On that graph:
  - the 37 rows form **17 components**, and the largest has 8 commanders;
  - Grant, Rosecrans and Burnside, the Union commanders with at least 2 battles, lie in three
    different components;
  - among the Confederate commanders with at least 2 battles, Bragg, Morgan, Jackson and Ewell
    each lie in different components, and only Lee shares a component with a ranked commander
    of the other side (Burnside).

  Within-side rank comparisons between components are therefore driven by α, β and the
  prior's split of each residual between a commander and their opponents, not by shared
  opponents.
- **Rank intervals.** §4 does not say among which commanders ranks are computed, or at what
  interval level.

**Add to §4, after "Commander sides":**

> - **Side offset.** The likelihood cannot separate α from a common shift of one side's θs. The
>   priors give nearly all of a side-wide difference to α, so each side's commanders are
>   effectively centred on zero, and a real difference between the two sides' average commanders
>   is absorbed by α. Ranks are therefore computed **within each side**. A combined list, if one
>   is shown at all, is labelled `cross_side_prior_anchored`.
> - **Connectivity.** The report gives the connected components of the commander–opponent graph
>   on the modelled rows, and each commander's component. Within a component the data inform
>   differences between θs. Between components, only α, β and the prior do. A ranked commander
>   who shares a component with no other ranked commander of the same side is labelled
>   `not_connected`.
> - **Rank set.** Within each side, ranks are computed among the commanders with at least 2
>   modelled battles. The report gives central 80% and 95% rank intervals from the 20,000 draws.

**Replace in §8** "The Union intercept α absorbs side-wide differences only partly." **with:**
"The Union intercept α absorbs nearly all of any side-wide difference, including any real
difference between the two sides' average commanders; ratings are relative to one's own side,
and within-side differences still absorb army, theater and opponent differences."

### R5. The design overstates force-size conditioning and implies that 2 battles escape prior dominance; "posterior mean" is mislabelled (§§1, 4, 7, 8)

**Evidence.**

- **β shrinkage.** β has a Normal(0, 1) prior (`fit_logistic` minimizes the log loss plus
  ridge/2 × (α² + β²), with ridge 1). On the 37 rows, Σx² = 6.35, computed from the reviewed
  points. At p(1 − p) ≈ 0.22, the data carry about 1.4 units of information on β, against the
  prior's 1, so β is materially shrunk. The A–C fold slopes are 0.67–1.15. Part of the
  force-ratio effect therefore stays in the residual. "Gets no credit for that concentration"
  (§1) overstates the conditioning.
- **Prior dominance.** The prior precision on θ is 1/τ² = 4. Near even odds, each battle adds
  about 0.25 of information, so the ratio of posterior to prior sd is about (1 + k/16)^(−1/2):
  0.94 at k = 2 and 0.87 at k = 5. The §4 sentence justifying the fewer-than-2-battles exclusion
  ("because their rating is almost entirely the prior") also describes commanders with 2–5
  battles.
- **"About a dozen."** On the listing-based stand-in (R4), 8 commanders have at least 2 of the
  37 battles. Alternative tie choices give roughly 8–10.
- **Mode, not mean.** §7 says "posterior mean θ", but §4 computes the mode. Under the Laplace
  approximation the mean equals the mode.
- **Wording.** "One standard deviation of τ" is imprecise: τ *is* the standard deviation.

**Replacements.**

- **§1, the "Force size is conditioned on" bullet:**

  > **Force size is partly conditioned on.** The force-ratio slope β has a Normal(0, 1) prior.
  > On the 37 primary rows the data carry roughly as much information about β as the prior does,
  > so β is shrunk towards zero and part of the force-ratio effect remains in the residual. A
  > commander who wins by concentrating superior numbers gets little, though not necessarily
  > zero, credit for that concentration, because the force ratio may be a commander-created
  > advantage (a mediator). The outcome-only views (§6) show the other side of that choice.
  > Neither view is the true measure.

- **§4, the pooling sentence.** Replace "One standard deviation of τ moves an even battle to about
  62%." with: "A commander effect of one prior standard deviation (τ = 0.5) moves an even battle
  to about 62%; a difference θ_US − θ_CS of one prior standard deviation (about 0.71) moves it to
  about 67%. τ = 0.5 is a declared convention, not an estimate."
- **§4, lines 151–153:**

  > **Commanders with fewer than 2 battles in the model** get no rank position and are listed
  > separately, with their estimate and interval. Every commander's output also gives the ratio of
  > posterior to prior standard deviation. With τ = 0.5, near even odds, this ratio is about
  > 0.94 for 2 battles and 0.87 for 5, so ratings from a handful of battles are still mostly prior.

- **§7:** replace "the posterior mean θ" with "the posterior mode θ (the mean of the Laplace
  approximation), the posterior-to-prior sd ratio".
- **§8, "Few battles":** replace "only about a dozen commanders have two or more battles" with
  "fewer than a dozen commanders are expected to have two or more battles (8 on a provisional
  listing-based attribution; the ledger will give the count)".

### R6. The held-out test needs a fixed verdict configuration, an effective denominator and a rule for what is published if it fails (§5)

**Evidence.**

- **Verdict configuration.** §5 does not say which τ or attribution the verdict uses, although §6
  refits several of each. A verdict could be read off whichever view improves.
- **Who can matter.** Under leave-one-campaign-out, a commander whose modelled battles all fall in
  one campaign is always unseen (θ = 0) in their own fold. On current listings, Jackson's five
  primary rows are all in "Jackson's Valley Campaign". Only held-out rows with a commander seen in
  another campaign can differ from the strength-only model except through α and β. On the
  listing stand-in, the commanders with at least 2 battles in 2 or more campaigns are Lee (5
  campaigns), Rosecrans (3), Bragg (3), Burnside (3), Grant (2), Morgan (2) and Ewell (2).
- **What is published.** §5 says the design tests for signal "before anything is ranked", but a
  failed test only changes the presentation ("descriptive, heavily pooled residual summaries").
  It is not stated whether rank positions are still published.
- **Positive reading.** Any strict reduction, however small, counts as passing. "Detectable" has
  no criterion.

**Add to §5:**

> - **Verdict configuration.** The verdict uses τ = 0.5, the primary attribution and the 37
>   primary rows only. No sensitivity view is used to reverse or support it.
> - **Effective denominator.** The report counts the held-out rows in which at least one side's
>   commander has a θ estimated from another campaign, and names those commanders. Other held-out
>   rows can differ from the strength-only model only through α and β. Commanders whose modelled
>   battles all fall in one campaign never affect a held-out prediction.
> - **Reading of an improvement.** An improvement is reported with its size and its effective
>   denominator. It is read only as "held-out log loss was lower on these rows". There is no
>   threshold, and it is not evidence of a persistent commander effect.
> - **If there is no improvement** under both weightings, the Markdown report gives no ordered
>   ranking. The JSON keeps θ, the intervals and the rank intervals, each labelled
>   `no_heldout_signal`.

### R7. `view_sensitive` is undefined, the outcome-only view changes two things at once, and "sum of raw residuals" has no model (§§6–7)

**Evidence.**

- **`view_sensitive`.** Most θ sit near zero (R5), so "sign changes" would flag nearly every
  commander. Rank intervals always move somewhat, so "rank interval … changes" has no criterion.
- **Outcome-only view.** It drops β *and* moves from the 37 rows to the 91, so its difference from
  the primary view cannot be read as "the other side of" conditioning on force (§1). It is also a
  different estimand, so letting it set `view_sensitive` mixes robustness with definition.
- **Raw residuals.** "The sum of raw residuals" (§7) does not name the fitted model that supplies
  p, and the sum grows with the number of battles.

**Replace the last line of §6 and the outcome-only bullet with:**

> - **Outcome-only views.** Both have no force-ratio term (β = 0) and are labelled
>   `includes_force_size_advantage`:
>   - (i) on the 37 primary rows, which isolates the effect of dropping the force term;
>   - (ii) on all 91 decisive engagements with attribution, after rule 7, which also changes the
>     rows and is labelled `expanded_rows`.
>
>   These views credit force concentration and every other advantage the commander did not create.
>
> A commander with at least 2 modelled battles is flagged `view_sensitive` if, in any robustness
> view (pooling strength, attribution grades, superior directing, command changes or strength
> endpoints):
>
> - their 80% interval lies entirely on the opposite side of zero from their primary posterior
>   mode; or
> - their 80% rank interval does not overlap their primary 80% rank interval.
>
> The outcome-only views estimate a different quantity. They are reported beside the primary
> ratings with their differences, and do not set `view_sensitive`.

**In §7, replace** "the sum of raw residuals" **with:** "the number of modelled battles and the sum
over them of the outcome minus p, oriented to the commander's side, where p is the held-out
`diagnostic_union_score` of the A–C strength-only fit in `artifacts/estimate-evaluation.json`".
The author may choose a different, stated p, but the design must name one.

### R8. The limits omit non-blind attribution, mixed echelons and the gap to Milestone 3 (§8)

**Evidence.**

- **Blinding.** The strength design recorded that extraction is not blind (its A5). This design's
  rules 2, 3(a) and 5 call for judgments: whether a passage "contradicts" a listing, which passage
  "shows directing", and which force the record "describes". An AI that knows outcomes and
  reputations makes those judgments. For example, at MS006 Greene shows McClernand directing three
  divisions, while CWSAC lists Grant alone.
- **Mixed echelons.** The target mixes army commanders with brigade or detachment commanders under
  one τ. At VA016, Beaver Dam Creek, CWSAC lists Fitz John Porter against Lee.
- **Milestone 3.** Milestone 3's acceptance requires a causal graph, opponent and army context, a
  locked final test set and a temporal check. None is in this design. Roadmap line 26 frames this
  work as a Milestone 3 step.

**Add to §8:**

> - **Attribution is not blind.** The ledger's extractor and reviewers are AI systems that may know
>   outcomes and reputations. Rules 2–5 are mechanical where possible, but judging a contradiction
>   (rule 2), choosing a passage (rule 3(a)) and applying rule 5 are judgments. The grade A–B view
>   is the structural check, not proof.
> - **Mixed echelons.** The target names army commanders in some rows and corps, brigade or
>   detachment commanders in others (for example, VA016 lists Fitz John Porter against Lee), all
>   pooled with one τ. The ledger records each responsible commander's echelon, and the report
>   gives it.
> - **Not Milestone 3.** There is no causal graph, no army, opponent or campaign effect, no locked
>   final test set and no temporal check. This exploratory diagnostic does not meet Milestone 3's
>   acceptance.

### R9. The delegated design questions are not preserved (status paragraph)

**Evidence.** The design says the owner "asked for the next step towards ranking generals and
answered the design questions put to them". The only record,
`data/estimates/evaluation-authorization-v1-confirmation.json`, keeps the reply but summarizes the
questions as "[followed by three commander-rating design questions]". It records no request about
ranking generals. AGENTS.md requires preserving what the owner actually decided. The same reply is
also used as the option-(a) confirmation, and the record's own "reading" says so.

**Correction.** Either record the three questions verbatim in a new immutable record and cite it
from the status paragraph, or add this after the owner quote:

> The three design questions are summarised, not preserved verbatim, in the
> [confirmation record](../data/estimates/evaluation-authorization-v1-confirmation.json), which
> also uses the same reply to confirm the evaluation's option (a). The request for a next step
> towards ranking generals is not recorded in the repository.

## Advisories (not required)

- **A1. Alternative-candidate and successor views.** Add a view that assigns each
  `responsibility_unresolved` or `joint_command` side to its other recorded candidate, and one that
  credits the `command_changed` successor (TN003 CS: Beauregard) rather than dropping the row.
  Exclusion alone does not test the choice.
- **A2. Side-offset sensitivity.** Add a refit with α's prior standard deviation set to 3, to show
  how much of each side's results moves between α and the θs (R4).
- **A3. Identity registry.** State that identical `fullname` strings on the same side are presumed
  to be one person unless a passage or listing field shows otherwise, so that "Robert Milroy"
  (VA102, VA107) and "Ulysses S. Grant" (listed as Brigadier General and as Major General) do not
  need a passage to merge.
- **A4. Rule 2 "contradicts".** Give an operational test, for example a passage naming a different
  officer as commanding the engaged forces when the fighting began. Record passages like Greene's
  on MS006 as `superior_directing` or subordinate context, not as contradictions.
- **A5. Temporal check.** Milestone 3 asks for temporal generalization. A 1862-trained,
  1863-predicted split could be reported descriptively beside leave-one-campaign-out, without a
  verdict.
- **A6. Laplace adequacy.** For commanders with 1–2 battles the posterior is close to the Gaussian
  prior, so the Laplace approximation is reasonable. Add a unit test on a synthetic case against
  a brute-force quadrature for one θ.
- **A7. Brier in the verdict.** §5 scores Brier but bases the verdict on log loss alone. Say
  explicitly that Brier is reported and not part of the verdict.

## What is sound

The following choices are consistent with the project's rules:

- one commander per side, never an equal split;
- a per-commander coverage report with reasons for exclusion;
- τ fixed with no hyperparameter search;
- grade-D sides getting no term, and θ = 0 for unseen commanders;
- the strength rows reused unchanged, with post-start rows excluded;
- a pre-stated reading for no improvement, with no significance test;
- a gate on reconciled review and owner hashes;
- outputs kept out of `artifacts/baseline.json`;
- explicit truncation of the 1862–63 frame, with the full-war extension left as an owner decision;
- a "no reputation check" limit.

With τ fixed and Gaussian priors on every parameter, the posterior mode is unique (a strictly
convex objective), so the model is well posed at 37 rows. The problems are what the data can
distinguish (R4, R5), not whether the fit exists.
