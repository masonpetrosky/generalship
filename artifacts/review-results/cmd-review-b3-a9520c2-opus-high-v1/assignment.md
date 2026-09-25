# Command-responsibility ledger: separate review, batch 3 of 4

Review prepared commit `a9520c2d5628c25b49437f4f54bfc78268a85393` against `16a32116067912a1b5cb380097d75092a2a430b4`. Sibling inputs.json binds
24 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show a9520c2d5628c25b49437f4f54bfc78268a85393:<path>` first. Other review bundles may be committed after the prepared
commit; they are out of scope.

Read AGENTS.md, the accepted design `docs/commander-ratings.md` (its §2 gives the target, rules
1–7, grades and checker), the ledger memo `docs/research/command-responsibility-v1.md`, the
ledger `data/command/responsibility-v1.json`, the registry `data/command/commanders-v1.json` and
`generalship/command.py`.

**Assigned engagements (23):** TN012, TN013, NC010, TN014, TN015, TN016, MS004, MS005, AL001, VA032, MS006, VA033, VA034, MS007, MS008, MS009, MS010, MS011, LA011, VA107, TN017, PA002, AR008.

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
4. **Echelon and identity.** Is the echelon supported (or `unknown`)? Are registry merges and
   passage-only entries sound?
5. **Nesting.** For any contained-interval pair involving an assigned engagement, is the outcome
   right?

Run `make check` and `python3 -m generalship command-check` offline. Do not run build, packet or
evaluation commands and do not modify primary artifacts. No network, new research or agents.

Write only `artifacts/review-results/cmd-review-b3-a9520c2-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (engagement, side, field, new value, with
the quote that supports it), or say there are none; list advisories separately. A concise review
is sufficient. Return the path and outcome. An AI review is not historical adjudication, feature
admission or authorization of any fit.
