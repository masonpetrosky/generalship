# Best-estimate ledger: separate review, batch 4 of 4

Review prepared commit `4fd1b512f9e4db0402537bfe577031a6cc6939f6` against `5151b5700f50fc494b167cc7c4d742c8fc17cc13`. Sibling inputs.json binds
25 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 4fd1b512f9e4db0402537bfe577031a6cc6939f6:<path>` first. Other review bundles may be committed after the prepared
commit; they are out of scope.

Read AGENTS.md, the accepted design `docs/strength-estimates.md` (its §§3–5 are the rules), the
tier-2 design `docs/feature-admission-reported-strength.md` (its §3 codes), the scoping memo
`docs/research/reported-strength-scoping-v1.md`, the ledger memo
`docs/research/strength-estimates-ledger-v1.md`, the ledger `data/estimates/side-strength-v1.json`
(including its `extractor_policies`) and `generalship/estimates.py`.

Scope: the ledger entries for these 21 engagements, in the ledger's date order:
IN001, OH001, OH002, TN018, GA003, GA004, TN019, TN020, VA040, VA042, TN021, TN022, WV012, TN023, TN024, GA005, TN025, TN026, TN027, TN028, TN029.

For each engagement and side:

1. **Passages and values.** Open the cited passage (dossier citation, frozen CSV cell, or the
   `livermore-transcription-v1` section; for Livermore, also look at the registered page image
   `data/raw/reported-strength-v1/livermore-p{N}.jpg` when a figure matters) and confirm the printed
   value, bounds and `printed_text` are read correctly and attributed to the right side.
2. **Coding.** Check each input's tier-2 codes, basis, `loss_timing`, `bound` and any
   `reproduction_of` against the passage and the extractor policies. Flag mis-coding that
   changes a class, grade, point, range or label, especially: role (own report, compiled,
   opponent or hearsay), whole-side versus partial scope, engagement match and state time,
   losses of this or later engagements, and basis.
3. **Inventory completeness.** Check that every strength claim (and, for Shiloh, every typed
   quantity) in the bound dossier, every frozen CWSAC force figure and every figure in a
   matching Livermore entry is either an input or recorded with a reason, and that the reasons
   are accurate. Report any figure that should have been an input.
4. **Grade D sides.** Confirm the recorded reason, and that no usable figure was missed in the
   inspected sources.
5. **Results.** Note any estimate that is implausible given its inputs, as evidence of a coding
   error, not as a historical judgement.

Do not re-derive the rules; judge the inputs against them. Do not propose new sources.

Run `make check` and `python3 -m generalship estimate-check` offline. Do not run build or
packet commands and do not modify primary artifacts. No network, new research or agents.

Write only `artifacts/review-results/est-review-b4-4fd1b51-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you
actually inspected (which engagements, inputs and passages). Give required corrections as exact,
evidence-backed changes to specific ledger inputs (engagement, side, input ID, field, new value),
or say there are none; list advisories separately. A concise review is sufficient. Return the
path and outcome. An AI review is not historical adjudication, feature admission or
authorization of any fit.
