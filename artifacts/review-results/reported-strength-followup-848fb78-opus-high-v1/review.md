# Focused follow-up design review: `reported_side_strength_v1` (corrected design v1)

## Record

| Field | Value |
| --- | --- |
| Reviewer | Claude agent, fresh-context subagent (not a fork of the author's conversation) |
| Model / effort | `claude-opus-5-5` (Claude Opus 5.5), reasoning effort `high` |
| Date | 2026-09-25 |
| Prepared commit reviewed | `848fb7889471d46771ca0f85fa5462d11b3d4dad` |
| Previous commit | `efeefb98374f470db0b59f70dd8d47a9992d2640` |
| Bundle commit (worktree HEAD) | `ed3fcae6379b9a49b48b061ab145a2ec4771d5cf`. It adds only this directory's `assignment.md` and `inputs.json` over `848fb78`. |
| `assignment.md` sha256 | `39dc8991222e1811f94108d4425163d8a90cad0ec38e48134fc66416e1d20f94` (verified) |
| `inputs.json` sha256 (input manifest) | `34f2a7f1e950c64285ad21883054dadcff3799984ff70a3ee4abf1508e23f10a` (verified) |
| Input hashes | All 23 paths in `inputs.json` match `git show 848fb78:<path>`, and the worktree bytes are identical. **No mismatch.** |
| First review checked | `artifacts/review-results/reported-strength-design-e335b75-opus-high-v1/review.md`, sha256 `b8526a63adbbecea04bed34fbbdf9b7f6fa514d4a00e8064f016a6fdcf165e50` |
| Outcome | **Corrections required**: N1–N4. Advisories B1–B7. |

The assignment named four more files that `inputs.json` does not bind. I read them at the
worktree HEAD, and none changed in `efeefb9..ed3fcae`:

- `docs/feature-admission.md`: `b858b7a27f3617408779c928ea545da814b31229ff2c40caf64927773f320c99`. This equals `CONTRACT_SHA256` in `admission.py`, so the contract text is unchanged.
- `docs/admission-validator.md`: `3aa7c1dfe192b13e10399030bd1f627ed73f9cec21382d9ed0a5e3eed0620e6c`
- `generalship/admission.py`: `55927091b8f7fa4e6a1eaef8a3b57d54de341aff01dfc666eda678a360941993`
- `generalship/baseline.py`: `f69156139eeb674e7a720a798bb235ddbec295944f048d83a68ba1593f53ceee`

I also read `generalship/evidence.py` (`cf52c44b86956201cb6fa8c1a9c3cec85047ada71366f656330c551b536dee69`)
for the quantity schema.

This is an AI design review. It is a separate analysis. It is not human historical
adjudication, feature admission, approval of any candidate or proof of source
independence. It changes no evidence, no model input and no file other than this one.

## Scope actually inspected

- **Read in full:**
  - `docs/feature-admission-reported-strength.md` at `848fb78`.
  - The `efeefb9..848fb78` diffs of that design and of `docs/roadmap.md`.
  - The first review (`review.md`), `correction.json` and `primary-assessment.md`.
  - `docs/feature-admission.md` (the contract).
  - AGENTS.md.
- **Read in part:**
  - `generalship/admission.py`: constants, `_mapping`, `_profile`, the observation and transform branches of `_candidate`, and `_scenarios`.
  - `generalship/baseline.py`: `advantage`, `feature`, `scores` and `evaluate`.
  - `generalship/evidence.py`: `QUANTITY_BASES`, `ESTIMATION_STATUSES` and quantity validation.
  - README "Research direction" (lines 74–80).
  - Roadmap lines 1–20 and 370–405.
  - Searched `README.md`, `docs/roadmap.md`, `docs/methodology.md` and `docs/admission-validator.md` for stale tier-2 counts and wording.
- **Recomputed from data:**
  - The pilot counts are 127 engagements and 91 decisive, non-aggregate records. VA024 is the only aggregate operation, and it has no strengths. Of the 91, 23 have both sides, 5 one side and 63 none.
  - The unknown-opening claims are 113 `opening-personnel-unknown`, 9 `opening-populations-unknown` and 2 `matched-opening-strengths-unknown`. Together they cover 124 distinct dossiers.
  - 126 dossiers use schema v1. Only TN003 uses schema v3 or has quantities.
  - The campaign-weighted Brier is 0.2765271817053925 in `artifacts/baseline.json`.
  - The frozen TN003 record is dated 1862-04-06 to 04-07. Its US description reads "Army of the Tennessee and Army of the Ohio (65,085)".
  - In TN003, `buell-divisions-arrive` and `crittenden-arrival-phases` are `supported`. They report Buell's divisions arriving in the night of April 6 and on April 7.
  - First-pass strength claims that cite `arnold-cwsac-forces` carry phase `unresolved` (10 claims).
  - The registry has several NPS/CWSAC source IDs, including paired `-html` and text representations.
- **Hash-verified only:**
  - `artifacts/admission-check.json` and `data/admission/shiloh-opening-v{1,2}.json`.
  - `data/raw/cwsac_commanders.csv`, `docs/sources.md`, `docs/evidence-contract.md` and `docs/methodology.md` (beyond the search).
  - `generalship/cli.py`, `tests/test_evidence.py` and `dispatch.json`.
- **Not inspected:** any historical source passage. The design cites none, and I did no new research.
- **`make check`:** run offline. 82 tests passed (`OK`). `generalship check` exited 0 with `artifacts_written: false`, admission statuses 18 blocked and 22 excluded, and 0 promoted rows. The worktree was clean afterwards. I ran no build, reproduce or packet command.

## Status of R1–R9

| ID | Status | Notes |
| --- | --- | --- |
| R1 | **Fully applied** | Both texts are verbatim: the status paragraph (lines 3–7) and the §2 "Relationship to contract §4" block (lines 72–89). §3 item 5's last bullet now points to the §2 relaxation, which is consistent. |
| R2 | **Fully applied** | §3 item 2 (lines 109–124) and the §2 source-availability paragraph (lines 62–64) are verbatim. The primary added a Shiloh example: the US figure "combines the Army of the Ohio, which arrived during the engagement". The frozen row description and the TN003 claims above support it. It cites no claim ID; see B7. |
| R3 | **Fully applied** | §3 item 1 is verbatim. |
| R4 | **Fully applied as specified** | §3 item 3 is verbatim. Combined with R5, it creates a pair-class overlap (N1) and a basis inconsistency (N2). |
| R5 | **Applied, with a defect in the specified text** | The §4 pairing, ranking and scenario rules are verbatim. The primary added a pre-extraction rule for compatibility constraints and the A5/A6 sentences, which is acceptable. The class definitions and within-class tiebreak are not deterministic (N1). The unknown-basis clause conflicts with §3 and the schema (N2). The defects are in the first review's replacement text; applying it faithfully carried them in. |
| R6 | **Fully applied, with an equivalent variant** | The §2 uncertainty row and §6 are verbatim. One sentence moved: "Predictions are named as diagnostics, never win probabilities" left the Labels bullet. It is replaced in the Model bullet by the A4 text ("named as diagnostics …, not `p_union_win`"), which is equivalent. The §6 bounds and evaluability rules match `baseline.py`: midpoint, four-endpoint sensitivity, ≥ 6 rows from ≥ 3 campaigns, both classes, and a Laplace training prior. |
| R7 | **Applied, incomplete** | §8 is verbatim. The list of profile-specific gate changes omits the opening profile's contact-boundary time checks, which conflict with §3 item 2 (N3). The `estimation_status: unknown` label is never named or reported (N4). |
| R8 | **Fully applied** | §7 is verbatim. See B1 on the trigger wording for a further family and B2 on `compiled_first` degeneracy. |
| R9 | **Fully applied** | Roadmap lines 3–8 are verbatim. The "Next priority" paragraph (lines 386–398) now reads 124, uses the A2 wording and says 91 engagements. It agrees with README line 76. |

## Advisories from the first review

- **A1: adopted.** §1 and roadmap line 387 give "at least 124"; I recomputed 113 + 9 + 2 = 124 distinct dossiers.
- **A2: adopted** in §1 and in the roadmap.
- **A3: adopted** in §3 item 5.
- **A4: adopted** in §6. The name is given only "for example"; see B6.
- **A6: adopted** in §4.
- **A5: disposition "no change" is acceptable.** A5 required only that any other tiebreak be fixed before extraction and recorded. The source-ID tiebreak is kept and labelled "arbitrary but outcome-blind", and the Revision paragraph and `correction.json` record that choice. As written, though, the tiebreak key is ambiguous (N1). B2 notes a consequence of the kept tiebreak for `compiled_first`.

## Required corrections

### N1. Pair classes overlap, and the within-class order is not a complete key

**Evidence.**

- §3 item 3 (from R4): "A compiled figure whose cited basis is visibly one side's report … takes that underlying role."
- §4 defines classes by source and role at once: "(a) both sides from one compiled source; (b) both sides' own reports".
  - A pair drawn from one compilation whose figures visibly rest on each side's return, such as a numbers-and-losses table citing returns, meets both (a) and (b).
  - Order A puts (a) first and Order B puts (b) first, so the pair's place in `compiled_first` and `reports_first` is undefined.
- "One compiled source" is undefined.
  - The registry holds several NPS/CWSAC IDs, such as `arnold-cwsac-forces`, `nps-tn001-river-v1` and `nps-tn001-river-v1-html`.
  - Some of these are representations of one document; others are different documents of one family.
  - `admission.py` already computes `same_document_key` from `facsimile_source_id`.
- "Pairs are ordered by source ID, then quantity ID": a pair has two source IDs and two quantity IDs, and the design does not say which side's ID comes first.
- §8 adds a `source_role` field but gives it no vocabulary.
- These choices are left to the implementer or extractor after the design is accepted. §4's own rule requires them to be "Fixed now, before any values are extracted or scored."

**Replace the "Pair ranking" bullet of §4** with:

> - **Pair ranking.** Fixed now, before any values are extracted or scored.
>   - Each applicable observation has one recorded `source_role` under §3 item 3:
>     `own_report` (the side's own report or return, including a compiled figure whose
>     cited basis is visibly that side's report) or `compiled_total` (any other admissible
>     compiled or secondary total).
>   - Two observations come from one compiled document when their cited sources have the
>     same `same_document_key`. Registry aliases and transcript/facsimile pairs are one
>     document (contract §5). Other documents in one source family are different
>     documents.
>   - Pair classes are: (a) both sides `compiled_total` from one compiled document; (b) both
>     sides `own_report`; (c) any other combination. Each pair belongs to exactly one class.
>   - Within a class, pairs are ordered by the tuple (US source ID, Confederate source ID,
>     US quantity ID, Confederate quantity ID), compared element by element in ascending
>     code-point order. This tiebreak is arbitrary but outcome-blind.
>   - Order A is (a), (b), (c). Order B is (b), (a), (c).

**In §8 "Mappings and codes"**, replace "adds `source_role` and the §3 codes:" with:

> adds `source_role` (`own_report` or `compiled_total`, §4) and the §3 codes:

### N2. Unknown basis is admitted in §4 but has no status in §3 and cannot be typed

**Evidence.**

- §4 (from R5): "Every other pair is a mixed-basis pair, including one with an unknown basis on either side."
- §3 item 3 (from R4) blocks only "A secondary total with neither a stated nor a table-level basis" as `basis_unknown`. An own-side report with no stated basis has no status.
- §2 Population lists only four bases: `reported_engaged`, `reported_effective`, `reported_present` and `present_for_duty`.
- §4 says a basis "is read from the cited passage or the table's stated definition".
- `evidence.py` `QUANTITY_BASES` has no unknown value, and every schema v3 quantity must carry one of its five bases.

An own report with an unstated basis therefore cannot be typed without inventing a basis. Its status and pairing would be decided at extraction.

**Replace, in §3 item 3,** the bullet "A secondary total with neither a stated nor a table-level basis is `blocked: basis_unknown`." with:

> - A figure whose population basis is given neither by the cited passage nor by the
>   table's stated definition is `blocked: basis_unknown`, whatever its role. A basis is
>   never inferred from the role or the source.

**Replace, in §4 "Basis pairing,"** the sentences "A same-basis pair has identical basis values. Every other pair is a mixed-basis pair, including one with an unknown basis on either side." with:

> A same-basis pair has identical basis values. Every other pair is a mixed-basis pair.
> An observation with no established basis is `blocked: basis_unknown` (§3 item 3) and
> forms no pair.

The primary could instead keep unknown-basis own reports in `mixed_basis_k`. That would
need a reviewed schema v3 `unknown` basis value named in §8, an explicit §3 status and a
§6 count. Either choice must be fixed before extraction.

### N3. §8 leaves the opening profile's contact-boundary time checks in place, contradicting §3 item 2

**Evidence.**

- §8 says contract v1 needs no text change "if the following items are implemented". Its gate-change list covers only basis, the `participation` derivation, unknown derivation and unknown estimation status.
- In `admission.py` `_candidate`:
  - mapping `time == 'after'` gives `excluded: post_boundary_dependency`;
  - a quantity period that starts after the boundary day gives `excluded: observed_state_after_boundary`;
  - a period that ends after it gives `blocked: state_interval_crosses_boundary`;
  - a null start without mapping citations gives `blocked: state_time_unestablished`.
- A whole-engagement engaged figure for a multi-day record, such as TN003 on 1862-04-06/07, spans the start date. Reusing those checks would block it.
- A state date after the start would get opening-profile codes instead of §3 item 2's `post_engagement_state`, `partial_interval`, `interval_unresolved` and `engagement_link_unknown`.
- §2 says participation within the interval is accepted, so the two texts contradict each other.

**Insert in §8, after "Neither of the last two is blocked.":**

> The opening profile's contact-boundary time checks do not apply under this profile.
> These are the `before`/`at_boundary`/`after` time relation, `post_boundary_dependency`,
> `observed_state_after_boundary`, `state_interval_crosses_boundary` and
> `state_time_unestablished`. §3 item 2's engagement-interval codes replace them:
>
> - A quantity whose period is the frozen engagement interval meets state time.
> - A state date before the start date is allowed only when §3 item 2's engagement link
>   holds.
> - A state date after the start date is `excluded: post_engagement_state`.
> - A period the source limits to part of the interval is `excluded: partial_interval`, or
>   `blocked: interval_unresolved` when unclear.
> - An unestablished state date is `blocked: engagement_link_unknown`.
> - The `post_state` derivation stays excluded, as `post_engagement_state`.

### N4. The `estimation_status: unknown` label is referenced but never named, declared or reported

**Evidence.**

- §8 (from R7): "`estimation_status: unknown` is retained and labelled … Neither of the last two is blocked."
- No label name appears in §3, in §8's code list or in §6.
- §6 counts rows that rest on `derivation_unknown`, mixed-basis or own-report observations, but not rows that rest on unknown estimation provenance.
- Under the opening profile this condition is `blocked: estimation_provenance_unknown` (`admission.py`). Here it is relaxed without a declared label or a reported count, which makes §3, §6 and §8 inconsistent.

**Append to §3 item 4:**

> - A quantity with `estimation_status: unknown` is retained and labelled
>   `estimation_status_unknown`. It is not blocked under this profile (§8). The opening
>   profile's `estimation_provenance_unknown` block is unchanged.

**In §8 "Mappings and codes,"** replace "`unreadable_value`, `derived_from_losses`, `derivation_unknown`, `one_sided_bound`." with:

> `unreadable_value`, `derived_from_losses`, `derivation_unknown`,
> `estimation_status_unknown`, `one_sided_bound`.

**In §8 "Profile-specific gate changes,"** replace "`estimation_status: unknown` is retained and labelled." with:

> `estimation_status: unknown` gives the `estimation_status_unknown` label.

**In §6 "Each report gives,"** replace the bullet "the number of rows resting on `derivation_unknown`, mixed-basis or own-report observations." with:

> - the number of rows resting on `derivation_unknown`, `estimation_status_unknown`,
>   mixed-basis or own-report observations, each counted separately.

## Advisories (not required)

- **B1. Trigger for a further family (§7).**
  - "An engagement that still lacks an applicable figure for each side" can be misread.
  - Applicability is final only after evidence-use review, so this trigger rests on the extractor's provisional §3 coding.
  - Suggested text: "Add at most one further family for an engagement where, after the first-pass citations and the compiled family, at least one side has no figure that the extractor's provisional §3 coding leaves neither `excluded` nor `blocked`. This coding triggers research only and approves nothing."
- **B2. `compiled_first` on common rows.**
  - Under the kept source-ID tiebreak, a pair from `arnold-cwsac-forces` sorts before most IDs a new compiled family would get.
  - `compiled_first` then reproduces the frozen CWSAC values on common rows, and its common-row comparison is trivially identical. The Livermore comparison would appear only in `alternate_2`.
  - This is outcome-blind and not an error. However, the new family's source ID decides the order, and nothing fixes that ID yet.
  - Suggestions:
    - fix the Livermore source ID in the registry before any extraction;
    - state that R8's anti-degeneracy aim holds through `alternate_k`, not `compiled_first`;
    - report a common-row scenario whose tier-2 values equal the frozen values as "identical by construction".
- **B3. Remaining opening-path exclusions.**
  - `_candidate` excludes both `reported_reinforcements` and claims with `phase: post_outcome` under the single code `participation_or_post_outcome_observation`.
  - §8 lifts the exclusion only for `reported_engaged`.
  - Suggestion: state that a `reported_reinforcements` quantity is `excluded: partial_scope` (§3 item 1), and state whether a `post_outcome` strength claim stays excluded. First-pass CWSAC strength claims are tagged `unresolved`, so this does not affect the frozen figures.
- **B4. Status and scope wording.**
  - The status line still reads "a proposal awaiting separate review", although the first review is complete. Consider "revised after the first separate review; awaiting the focused follow-up".
  - "Under that contract's §§3, 5 and 6" omits §1 (declaration before fitting, one observation per engagement, the CS→Confederate mapping) and §7 (coverage ledger, evaluation), which the design also relies on unchanged. Consider "§§1, 3, 5, 6 and 7".
- **B5. Row contents (§8).** "Rows carry the profile ID and both bases." §6's counts also need each side's `source_role`, source ID and the derivation and estimation labels on the row. Consider "Rows carry the profile ID and, per side, source ID, `source_role`, basis and labels."
- **B6. Diagnostic output name (§6).** "For example, `diagnostic_union_score`" leaves the name open. Fix it before implementation so that output naming is not decided later.
- **B7. Records.**
  - The §2 Shiloh sentence could cite TN003 `buell-divisions-arrive` and `crittenden-arrival-phases`.
  - `correction.json` uses the key `independent_followup_review`. Per AGENTS.md, an AI follow-up is a separate review, not independent corroboration. A future record could use `separate_followup_review` and leave this immutable record unchanged.

## Findings list

Required: N1, N2, N3, N4. Advisory: B1, B2, B3, B4, B5, B6, B7.
