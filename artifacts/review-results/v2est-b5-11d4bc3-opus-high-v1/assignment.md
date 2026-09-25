# Best-estimate strength ledger v2: separate review, batch 5 of 8

Review prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` against `96110cf`. Sibling inputs.json binds
25 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 11d4bc3168b83917a8efc233bf8d0bdc9ccbf372:<path>` first. Other review bundles may be committed after the prepared
commit; they are out of scope.

Read AGENTS.md, the accepted design `docs/strength-estimates.md` (its §§3–5 are the rules), the
tier-2 design `docs/feature-admission-reported-strength.md` (its §3 codes), the addendum
`docs/ledgers-v2.md`, the owner's source decision `data/estimates/owner-decision-v2-sources-2026-09-25.json`,
the v1 ledger memo `docs/research/strength-estimates-ledger-v1.md`, the ledger
`data/estimates/side-strength-v2.json` (including its `extractor_policies`),
`generalship/estimates.py` and `generalship/estimates_v2.py`. The 91 v1 entries are carried forward
unchanged and are out of scope.

Scope: the ledger entries for these 27 engagements: VA047, VA053, VA054, VA052, VA056, VA059, VA062, VA099, VA098, VA063, VA065, VA113, VA067, VA068, VA069, VA070, VA071, VA072, VA073, VA075, VA074, VA077, VA078, VA079, VA080, VA083, VA084.

For each engagement and side:

1. **Passages and values.** Open the cited passage (dossier citation, frozen CSV cell, or the
   `livermore-transcription-v2` section; for Livermore, also look at the registered page image
   `data/raw/strength-v2/livermore-p{N}.jpg` or `data/raw/reported-strength-v1/livermore-p{N}.jpg`
   when a figure matters) and confirm the printed value, bounds and `printed_text` are read
   correctly and attributed to the right side.
2. **Coding.** Check each input's tier-2 codes, basis, `loss_timing`, `bound` and any
   `reproduction_of` against the passage and the extractor policies. Flag mis-coding that
   changes a class, grade, point, range or label, especially: role (own report, compiled,
   opponent or hearsay), whole-side versus partial scope (Livermore campaign aggregates and
   day-only entries), engagement match and state time, losses of this or later engagements,
   and basis.
3. **Inventory completeness.** Check that every strength claim and typed quantity in the bound
   dossier, every frozen CWSAC force figure and every figure in a matching Livermore entry is
   either an input or recorded with a reason, and that the reasons are accurate. Report any
   figure that should have been an input.
4. **Grade D sides.** Confirm the recorded reason, and that no usable figure was missed in the
   inspected sources.
5. **Results.** Note any estimate that is implausible given its inputs, as evidence of a coding
   error, not as a historical judgement.

Do not re-derive the rules; judge the inputs against them. Do not propose new sources.

Run `make check` and `python3 -m generalship estimate-check --ledger data/estimates/side-strength-v2.json`
offline. Do not run build or packet commands and do not modify primary artifacts. No network,
new research or agents.

Write only `artifacts/review-results/v2est-b5-11d4bc3-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (engagement, side, field or input ID, new
value, with the quote that supports it), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication, feature admission or authorization of any fit.
