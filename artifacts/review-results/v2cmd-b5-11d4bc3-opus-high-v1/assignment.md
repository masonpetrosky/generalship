# Command-responsibility ledger v2: separate review, batch 5 of 8

Review prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` against `96110cf`. Sibling inputs.json binds
25 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 11d4bc3168b83917a8efc233bf8d0bdc9ccbf372:<path>` first. Other review bundles may be committed after the prepared
commit; they are out of scope.

Read AGENTS.md, the accepted design `docs/commander-ratings.md` (its §2 gives the target, rules
1–7, grades and checker), the addendum `docs/ledgers-v2.md` (scope, two-sided rule, v2 rank order,
merges), the v1 ledger memo `docs/research/command-responsibility-v1.md`, the ledger
`data/command/responsibility-v2.json`, the registry `data/command/commanders-v2.json` and
`generalship/command.py`. The 91 v1 entries are carried forward unchanged and are out of scope.

**Assigned engagements (27):** VA047, VA053, VA054, VA052, VA056, VA059, VA062, VA099, VA098, VA063, VA065, VA113, VA067, VA068, VA069, VA070, VA071, VA072, VA073, VA075, VA074, VA077, VA078, VA079, VA080, VA083, VA084.

For each assigned engagement and each side, check against the evidence the design allows (the
bound dossier's citations and their sources' sections, the frozen CWSAC battle description and
the CWSAC commander listing):

1. **Choice.** Is the responsible commander the officer who held command of that side's engaged
   forces, as the field commander directing the operation, when the record's fighting began?
   Apply rule order 5, 3, 2, 6, then 4, then 7. Look for passages the ledger missed that state,
   contradict or date the command, and for any misreading of a quoted passage.
2. **Grade and labels.** Does the grade follow the table? Are `command_changed` (with successor),
   `superior_directing` (with superior), `joint_command` and `responsibility_unresolved` applied
   where the passages call for them, and only there? Are candidates complete?
3. **Citations.** Does each cited quote actually support what the rationale says? The checker
   verifies only that quotes occur in their sources.
4. **Echelon and identity.** Is the echelon supported (or `unknown`)? Are the registry merges and
   passage merges (`merge_basis`, `passage_merges`) and passage-only entries that these
   engagements use sound? Flag any identity asserted without a listing field or passage.
5. **Nesting.** For any contained-interval pair involving an assigned engagement, is the outcome
   right?

Run `make check` and `python3 -m generalship command-check --ledger data/command/responsibility-v2.json`
offline. Do not run build, packet or evaluation commands and do not modify primary artifacts. No
network, new research or agents.

Write only `artifacts/review-results/v2cmd-b5-11d4bc3-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (engagement, side, field or input ID, new
value, with the quote that supports it), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication, feature admission or authorization of any fit.
