# Primary assessment of the initial implementation review

The [actual review](review.md) and [structured result](review-result.json) report
three P2 corrections against immutable commit
`7b41de14011dbb7150a4b4ea2a30e570a0421e33`. The primary accepts all three findings.
They identify structural validator gaps, not changes to historical evidence.
The original response remains unchanged; it does not claim acceptance of the
later working-tree fixes.

| Finding | Primary disposition and implementation |
| --- | --- |
| ADM-IMPL-R1 | Accepted. The primary supplied and the reviewer independently reproduced the same-quantity/different-members counterexample. Each observation reference now has one leaf per candidate; shared DAG-node reuse remains valid. |
| ADM-IMPL-R2 | Accepted. The reviewer reproduced compatible opposing sides being split across partial scenarios. Applicable candidates with a compatible counterpart on an eligible engagement now require a coherent joint assignment. Missing/inapplicable sides and outcome/grain exclusions remain supported. |
| ADM-IMPL-R3 | Accepted. The reviewer demonstrated that the accepted ISO week-date literal sorts incorrectly as text. The primary confirmed the raw-string comparison and added calendar-date comparisons, preserving the source literal. Week/basic-format regressions cover false acceptance and false exclusion. |

All three corrections are implemented in
`1264e217fc1e952b2115a316313f9dfeea4869ec`. The primary inspected each proposed
correction and ran the targeted regressions and full **82-test** suite, then
`make reproduce`. Valid synthetic sum/subtraction and reviewed-manifest replay
still pass; the three counterexamples no longer permit a verified audit.

The [focused follow-up](../admission-implementation-1264e21-followup-v1/review.md)
is recorded separately against the fixed commit. Consult its actual verdict
and final primary assessment for closure; this initial response's
`corrections_needed` verdict and open finding records are intentionally preserved.

The historical default ledger is unchanged except for validator code hashes:
40/40 quantities, 18 blocked, 22 excluded, zero complete or promoted rows across
127 engagements / 36 campaign groups. Original source/dossier/cohort/packet bytes
and numerical baseline outputs remain identical to the pre-task commit.
No historical fact, source dispute, commander effect or real feature admission
was approved by this review. Declared mappings and review identities still
require substantive inspection; hashes cannot establish their truth or sincerity.
