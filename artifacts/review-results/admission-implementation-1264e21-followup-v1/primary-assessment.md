# Final primary assessment: offline admission validator

**Accepted within the non-promoting implementation scope.** The
[original review](../admission-implementation-7b41de1-astra-xhigh-v1/review.md)
found three P2 gaps at `7b41de14011dbb7150a4b4ea2a30e570a0421e33`. The
[primary reconciliation](../admission-implementation-7b41de1-astra-xhigh-v1/primary-assessment.md)
accepts those findings. All were fixed in
`1264e217fc1e952b2115a316313f9dfeea4869ec`, and the actual
[focused follow-up](review.md) / [structured result](review-result.json)
accepts the corrections with no unresolved findings.

| Finding | Verified closure |
| --- | --- |
| ADM-IMPL-R1 | A repeated observation reference cannot acquire different membership labels through a second leaf. Shared graph-node reuse, including `(A+B)-B`, still works. |
| ADM-IMPL-R2 | Compatible opposing candidates must appear in a coherent joint assignment on eligible engagements. Genuine missing/inapplicable sides and outcome/grain exclusions retain partial coverage without fabricated rows. |
| ADM-IMPL-R3 | Calendar dates are parsed before comparison. Cross-year ISO week dates cannot bypass the post-boundary gate; valid earlier compact dates pass and source literals remain unchanged. |

The reviewer was `/root/admission_implementation_review`, GPT-6 Astra at `xhigh`.
The initial assignment used fresh context; this follow-up continued that reviewer
with a five-file bounded correction assignment. Both dispatches, actual responses,
input hashes and coverage are retained. The original `corrections_needed` response
and open finding objects are preserved rather than rewritten as an initial pass.

The primary read both responses, checked their hashes against the exact Git
commits, confirmed the fix scope and independently ran all **82 tests** (including
30 admission tests) and `make reproduce`. The reviewer independently passed
30 admission tests and 11 focused synthetic proposal/release probes. It did not
repeat a broad historical or image review. The final source/registry/cohort,
prepared packet and numerical baseline artifacts remain byte-identical to the
pre-task commit. Final status updates change documentation/report prose, not the
accepted admission engine, tests, proposal or frozen snapshot.

The default ledger covers **127 engagements / 36 campaign groups**, with three
available dossiers and all **40/40 Shiloh troop observations** represented:
**18 blocked, 22 excluded, zero eligible candidates, zero complete rows and zero
promoted rows**. The post-fix ledger differs from the initial implementation only
in validator code hashes. Existing source disputes and missing boundary/population
mappings remain unresolved. Baseline coverage remains 23 engagements / 13 groups,
with Brier 0.2768816348133779 versus equal odds 0.25.

Synthetic accepted audits test software behavior only; their review stubs are
explicitly invented and normal commands reject them. No actual historical
evidence-use approval, feature release, model-input installer or enriched fit was
created. Hash checks cannot establish historical entailment, source independence
or reviewer sincerity. AI implementation acceptance does not establish those
claims either.

See [final validation](final-validation.json) for the test/reproduction receipt
and preservation checks. Next prepare a bounded, source-backed opening-boundary
and population-mapping proposal while continuing evidence work by complete
campaign. Real feature admission still requires substantive evidence-use review
of the exact proposal and an immutable release manifest.
