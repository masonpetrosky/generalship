# Separate review: best-estimate engine, checker and ledger bindings (`4fd1b51`)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This is a fresh-context
  subagent. The author's conversation was not an input.
- **Date:** 2026-09-25.
- **Commits:** prepared commit `4fd1b512f9e4db0402537bfe577031a6cc6939f6`, previous commit
  `5151b5700f50fc494b167cc7c4d742c8fc17cc13`. The worktree was at bundle commit
  `98212664305094d1ea7a4f02d00c89006edb919b`, which only adds review assignments after `4fd1b51`.
- **Assignment:** `assignment.md`, sha256 `8f701fd4b487f426679f67fa9be7811c03526f5a0f05df01d964cec006d96235`.
  **Input manifest:** `inputs.json`, sha256 `3c3d44031bacf0e03bb86c936b63bd653ee3cb7c887a350425dcfc622490c388`.
- **Hash verification:** I checked all 25 bound inputs against `git show 4fd1b51:<path>`. All
  match, and the worktree copies are byte-identical. There were **no mismatches**.
- **Documents the assignment names but `inputs.json` does not bind:** I read them at the
  worktree commit and hashed them.
  - `docs/strength-estimates.md` (`795212ad…64ba3`, equal to the ledger's design binding)
  - `docs/feature-admission-reported-strength.md` (`0699152d…c48`)
  - `docs/research/reported-strength-scoping-v1.md` (`aa8bb163…a1a3`)
- **Commands run, offline:**
  - `make check`: 107 unit tests OK, and `generalship check` completed.
  - `python3 -m generalship estimate-check`: in_scope 91, out_of_scope 36, grades
    A/B/C/D 62/25/23/72, fit-eligible rows 21/31/40, 6 rows excluded as post-start,
    `fitted: false`, `promoted_rows: 0`.

  I ran no build or packet command, made no network access, did no new research and started
  no agents. My only write is this file.

This AI review is a separate analysis. It is not historical adjudication, independent
corroboration, feature admission or authorization of any fit.

## Coverage actually inspected

- **Full reads:**
  - `generalship/estimates.py` (all 355 lines) and `tests/test_estimates.py`
  - the `cli.py` diff `5151b57..4fd1b51` and `run_build`/`main` at `4fd1b51`
  - design §§1–8
  - tier-2 §3
  - scoping memo findings 1–4
  - the ledger memo
  - `evidence.citation_text`, and `sources.source_metadata_digest` and `verify_sources`
- **Ledger:**
  - Top level: `bindings`, `constants`, `extractor_policies`, `out_of_scope` (all 36) and
    `status`.
  - Inventory shape for every engagement.
  - Scripted scans of all 313 inputs: fields, codes, `loss_timing`, adjustments,
    `reproduction_of`, `printed_text`, printed ranges and bound inputs.
- **Engagement spot checks, input level:** AL001 US; IN001 US; KY005 US; KY009 US; OH002
  Confederate; TN006 both sides; TN015 US; WV010 US.
- **Estimate-level scans:** all 182 sides.
  - opponent-raised highs;
  - equal-value candidates in the compiled lineage that are not linked;
  - CWSAC forces figures against inputs;
  - the 23 baseline rows against the estimates;
  - all 91 memo table rows against the ledger.
- **Not inspected:** I did not check any quote against its passage by reading (the batch
  reviews cover that), the Livermore transcription against its images, or the dossier
  classifications.

## 1. Rules (design §§3–5)

**§3.**
- `class_of` tests row 1, then row 5, then rows 2, 3, 4, 6/7 and 8, in that order.
- Row 3 is `loss_timing == not_prior` or `post_engagement_state`.
- Row 7 treats these as conditions: `basis_unknown`; prior-only losses (either
  `loss_timing` or a `prior_loss` adjustment, counted once); `completed_sum`; and
  `quoted_ratio`.
- Two or more conditions give C, one gives B.

This matches.

**§4 rules 1–9.** Rules 1, 3, 4, 8 and 9 match the text. I worked the required cases with
synthetic inputs, reusing the test helper:

| Case | Result | Per design? |
| --- | --- | --- |
| Group whose members disagree on basis: NPS 1,000 engaged ↔ Livermore 1,000 pfd (compiled link); and reproduction link across bases plus a separate A at 1,100 | Group basis `unknown`, class B through `basis_unknown`. With another A present, the point is 1,100 A and the B group enters the hull as `unknown` (low 950) | Yes (rule 2, §3 row 7) |
| Upper bound 900 on the point basis, residual `scope_unresolved` (C), own A 1,000 | Not applied; no `bound_conflict` | Yes (rule 7, "would be class A or B") |
| Own A 1,000 engaged; opponent 5,000 **pfd** | No effect on high | Yes (rule 5, basis filter) |
| Same, opponent on `unknown` basis | High = 5,000; point unchanged | Yes, but see R1 for labels |
| Two opponents, pfd 10,000 and unknown 20,000 | point_basis pfd; point 7,500; low 5,000; high 20,000 | Yes (rule 4: min and max over pfd ∪ unknown) |
| Two opponents, engaged 10,000 and pfd 20,000 | point 7,500; low 5,000; high 10,000; pfd ignored | Yes |
| Completed sum (KY005 US, WV010 US) | Operands are excluded from grouping; the value is recomputed from the operands; class C (`basis_unknown` + `completed_sum`); `partial_completed` applies | Yes |

- **Rule 2:** the three links are transitive. Membership of the union keeps the most
  restrictive `loss_timing`, a basis that differs across members becomes `unknown`, and a
  bound-only or unusable member makes the whole group so. This matches the design's text.
- **Rule 5:** the hull uses all non-opponent candidates of any class on point_basis or
  `unknown`. Post-start candidates are excluded unless one is used. The margin follows the
  side grade. This matches.

**§5.** One divergence (R1). The other labels match, including `compiled_dependence`
(point only, any group member) and `single_input` (after rule 2).

## 2. Checker (design §7)

**Enforced:**
- **Coverage:** 91 + 36 against the cohort, with a reason for each out-of-scope record.
- **Bindings:** design, script, cohort and every in-scope dossier. The raw files of every
  registered source are verified. The metadata and raw hashes of every cited source are
  bound, and every quoted input must use a bound source.
- **Passages:** the quote must occur in its section or CSV cell, and the printed value (or
  `printed_text`) must occur in the quote.
- **Records:** the document key and independence group equal the registry-derived values.
- **Vocabulary and class:** codes, bases and adjustment kinds come from the fixed lists;
  adjustment operands exist; and `class` equals `classify`.
- **Reproduction:** full estimate replay, nested sets, `0 < low ≤ point ≤ high`, and a
  null reason for grade D.
- **Inventory:** the dossier strength claim IDs and quantity IDs are present, and a CWSAC
  key exists wherever `strength_min` is nonempty.

**Not enforced.** None of these gaps is exposed in the current ledger except where noted.
The data scans above are my own, not the checker's.
- A row-5 input may have `bound: null`, which silently disables rule 7. Seven inputs have
  this. None would apply today, because each is off the point basis, has a residual class
  of C or is a sum operand.
- `printed.lower ≤ printed.upper` is not checked.
- The match is a substring test, so 400 passes inside "1,400".
- `printed_text` skips the numeric check; 29 inputs use it. I read all 29 mappings and all
  are consistent, such as "35,- 155" → 35,155.
- A `completed_sum`'s own `printed` value is not compared with its operand sum. It is used
  for grouping and is correct in both uses.
- A sum's basis, codes and `loss_timing` are not required to reflect its operands.
  Synthetic case: an operand with `not_prior` yields a class B sum with no
  `post_start_information`.
- `derived_from_losses` does not force `loss_timing ≠ none`. It is unused in the ledger.
- A dangling `reproduction_of` is not caught.
- Inventory `use` entries are not resolved to input IDs. My scan found all resolvable, and
  every in-scope CWSAC forces figure has a matching `arnold-cwsac-forces` input with the
  same value.
- The Livermore inventory is unchecked (declared B2).
- The ledger's `constants` block is not compared with the code; the code is bound by hash.
- `interval` is not compared with `cwsac_battles.csv`, yet it anchors `loss_timing`.
- The design's §2 source scope (registered at the acceptance commit) is not enforced (A1).
- Livermore inputs are not barred from citing the OCR or image IDs. None do.

## 3. The two implementation choices

- **Cited-source binding.** This is weaker than §7's "source registry snapshot" but
  sufficient for replay:
  - every quoted input must use a bound source;
  - the metadata digest covers `independence_group` and `facsimile_source_id`, so the
    compiled links and document keys are fixed;
  - `verify_sources` still hashes every raw file;
  - no bound source is uncited.

  **Loophole:** the checker cannot tell whether a cited source existed at the design's
  acceptance commit (design §2). `livermore-transcription-v1` was absent from the registry
  at `5151b57` and added at `4fd1b51`. It is named explicitly by rule 2 and transcribes
  images that were already registered, so I treat it as within the design's intent. A
  genuinely new source would pass the same way. See A1.
- **Unlinked NPS narrative restatements.** These are consistent with the letter of rule 2:
  - link 1 requires the same basis;
  - "figures from one document on different bases … stay separate";
  - link 2 applies only when a reproduction is recorded.

  They cannot set a point above the A figure they restate, and they do not move the range
  (equal value). **Loophole:** the unlinked restatement counts as a second candidate for
  `single_input`. The label is therefore missing on IN001 US, OH002 Confederate and TN015
  US, each of which rests on one NPS/CWSAC lineage figure (400). Only reporting is
  affected; the §6 refit labels, grades and sets are not (A2).

  The memo's general statement is also inaccurate: the same-basis restatements KY009
  `us-nps-desc` and TN006 `cs-nps-desc` *are* recorded as reproductions (R3).

## 4. Build wiring

This is sound as wired.
- A stale ledger fails through a design, script, cohort, dossier or cited-source hash
  mismatch. Each raises `EstimateError(ValueError)` before any passage lookup, and
  `run_build` catches it.
- `make check` runs `test_committed_ledger_reproduces` first, so the gate holds. Only a
  malformed ledger (`StopIteration`, `IndexError`, `TypeError`) crashes the build, which
  is loud failure.
- **Limit:** the stale status appears only in the stdout summary. `receipt.json` records
  the ledger's hash but not whether it replayed. Running `generalship check` alone passes
  with a stale ledger (A5).

## 5. Ledger-level facts

I recomputed these from the ledger:
- side grades 62/25/23/72;
- fit-eligible rows 21/31/40;
- 22 of 23 baseline rows are common, and VA017 is excluded;
- 18 new rows;
- 6 post-start exclusions: MD002, MS003, MS011, TN024, VA017 and WV010;
- the new grade-B baseline rows are VA016 (both sides), VA022 (both sides) and PA002 US;
- VA032 is C/C.

All 91 memo table cells equal the ledger values.

**Misstatement:** **45** engagements have a non-null estimate for both sides, not 40. Forty
are fit-eligible, and five more are post-start exclusions (R2).

## Required corrections

These are fixes to the engine and the documents; no ledger input changes. After R1, the
ledger's derived `estimate` blocks and its `script` binding must be regenerated.

**R1 — the engine omits §5 labels for an opponent candidate that sets `high` under rule 5.**
- **Design §5:** `post_start_information`, `applicability_unresolved` and
  `derivation_unknown` apply to "any candidate used for the point or range". `single_input`
  requires that exactly one candidate "enters the side's point and range under §4 rule
  4 or 5".
- **The rule:** rule 5 says the opponent candidate "becomes high".
- **The code:** it leaves that candidate out of `rng`/`touched`.
- **Consequence:** an opponent figure with `not_prior` timing could set `high` while the row
  stays fit-eligible, so it bypasses the §6 leakage exclusion. Synthetic case: own 1,000
  engaged plus an opponent at 5,000 (`unknown`, `not_prior`) gives
  `excluded_post_start_information: false`.
- **Fix in `estimate_side`:** replace the opponent-raise loop with:

  ```python
  raised = None
  for c in cands:
      if c['tag'] == 'opponent_or_hearsay' and c['basis'] in {point_basis, 'unknown'} and c['value'] > high:
          high, raised = c['value'], c
  if raised is not None:
      rng = rng + [raised]
  ```

  Add a test for the synthetic case above.
- **Regenerated estimate changes,** computed in memory. No point, range, grade or
  nested-set membership changes.
  - AL001 US: remove `single_input`; `range_groups` becomes `["us-jp-est","us-nps"]`.
  - NC007 Confederate: remove `single_input`; `range_groups` becomes
    `["cs-foster-est","cs-smith-evans"]`.
  - TN002 Confederate: remove `single_input`; `range_groups` becomes
    `["cs-lv-grant","cs-pillow"]`.
  - TN019 Confederate: add `applicability_unresolved`, from `cs-foster-est`'s recorded
    `engagement_link_unknown`; remove `single_input`; `range_groups` becomes
    `["cs-cw","cs-foster-est"]`.
  - WV012 Confederate: remove `single_input`; `range_groups` becomes
    `["cs-averell-est","cs-echols"]`.
  - AR006, AR008 and IN001 Confederate: the opponent ID (`cs-sherman`, `cs-union-est`,
    `cs-burnside`) is added to `range_groups` only.
  - Label totals: `single_input` goes from 75 to 70 and `applicability_unresolved` from
    15 to 16.
- **If the owner prefers the narrower reading** (an opponent that sets high is not "used"),
  that is a design revision. Amend the §5 text instead of the code.

**R2 — count wording.**
- Memo lines 30–31. Replace "At the widest grade set, 40 decisive engagements have an
  estimate for both sides, against 23 frozen rows." with "45 decisive engagements have an
  estimate for both sides; 40 of them are fit-eligible at grades A–C (5 are excluded as
  `post_start_information`), against 23 frozen rows."
- README lines 81–82. Replace "gives 40 decisive engagements an estimate for both sides
  (21 at grade A)" with "gives 45 decisive engagements an estimate for both sides, 40 of
  them fit-eligible (21 with both sides at grade A)".

**R3 — memo lines 69–71.** Replace "NPS narrative restatements of a frozen figure ("about 400
Home Guards") are not recorded as reproductions." with "NPS narrative restatements whose
basis is unstated (IN001 US, OH002 Confederate, TN015 US) are not recorded as
reproductions; same-basis restatements (KY009 US `us-nps-desc`, TN006 Confederate
`cs-nps-desc`) are linked." Keep the rest of the bullet, and add: "The unlinked restatement
counts as a second candidate, so those three sides lack `single_input`."

## Advisories

- **A1.** Record `livermore-transcription-v1` as a declared exception to design §2. It is
  named by rule 2 and derived from registered images. Also consider binding the ID list of
  the registry at acceptance, so that the checker can enforce §2.
- **A2.** Owner decision on `single_input` for unlinked same-lineage restatements. Either
  accept and report the three sides, or count equal-value candidates in one lineage once for
  that label (a design revision).
- **A3.** Add these checker assertions (all cheap and currently satisfied):
  - a row-5 input needs `bound` ∈ {`upper`, `lower`};
  - `lower ≤ upper`;
  - a sum's `printed` equals its operand sum, and its basis equals its operands';
  - `derived_from_losses` ⇒ `loss_timing ≠ none`;
  - `reproduction_of` resolves;
  - inventory `use` IDs resolve;
  - no inputs cite `livermore-ocr-v1` or the image IDs;
  - `interval` equals the frozen dates;
  - the `constants` block equals the code.
- **A4.** `test_same_document_different_basis_stay_separate` does not discriminate. A merged
  group also gives point_groups plus range_groups = 2, which I verified by simulation.
  Assert grade A and point_basis `reported_engaged` instead. Also add tests for:
  - `floor_applied`;
  - lower bounds and conflicts;
  - a residual-C bound;
  - post-start hull inclusion;
  - `basis_mixed`;
  - `nested_sets`;
  - checker tamper cases.
- **A5.** Record the estimate-check status (or the stale flag) in `receipt.json`.
- **A6.** Unused paths: `quoted_ratio` assumes a percentage operand (`/100`). A group's value
  comes from its lowest-source-ID member, which differs from the other members if a member
  has an adjustment. Document both before first use.
- **A7.** `basis_mixed` is never set when one side is grade D. This is harmless for the fits;
  state the interpretation.
- **A8.** Documentation fixes:
  - The memo's "6 excluded" includes WV010, whose Confederate side is grade D; say
    "5 + WV010".
  - Delete the stray memo line 176 `common=22 new=18`.
  - Roadmap "72 of 182 sides blank for lack of any count": 14 of those sides carry bounds or
    unusable figures. Suggest "for lack of a usable candidate value".
- **A9.** The bound design text still reads "Status: proposed", although `5151b57` accepted
  it. Editing the file would break the ledger's design binding, so record the acceptance in
  the memo or a new design version.
- **A10.** The inputs store only the tier-2 failure codes. Source role (own report,
  compiled or opponent) is implicit, so a reviewer must infer it; consider a `role` field.

## Outcome

**Corrections required:** R1 (engine labels), R2 and R3 (memo and README text). Advisories
A1–A10. No unresolved dispute was adjudicated.
