# Primary assessment: reported side-strength design review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`e335b751e354bd2581eec5770b0fba7e200f6c0e`. Its SHA-256 is `b8526a63adbbecea04bed34fbbdf9b7f6fa514d4a00e8064f016a6fdcf165e50`. The reviewer ran as a fresh headless session with the
`evidence-reviewer` definition in a detached worktree of the bundle commit; see
[dispatch.json](dispatch.json). It verified all 19 bound input hashes, read the contract,
validator documentation and baseline in full and `admission.py` in part, and recomputed
every count the design states. It reported nine required findings and six advisories.

The primary checked each finding against the repository before applying it:

- the contract and `admission.py` constraints cited in R1 and R7;
- the five unit-list frozen rows cited in R3;
- the baseline's campaign-weighted Brier (0.2765271817053925) and minimum-row rule cited
  in R6;
- the absence of Livermore from the registry (R8);
- the 113 + 11 unknown-opening claim IDs (A1).

Dispositions:

- **R1**: status paragraph and a §2 'Relationship to contract §4' block declare the tier-2 departures, including the derivation_unknown relaxation.
- **R2**: §3 item 2 adds state-time, post-engagement and partial-interval rules; §2 adds the source-availability weakness.
- **R3**: §3 item 1 defines whole-side scope for side-level table entries and adds scope_unresolved.
- **R4**: §3 item 3 adds basis_unknown, source_role_unresolved and underlying-role rules.
- **R5**: §4 replaced with the complete pair and scenario generation rule.
- **R6**: §2 uncertainty row and §6 replaced with the locked evaluation plan.
- **R7**: §8 replaced with the complete implementation notes.
- **R8**: §7 replaced: Livermore to be pinned before extraction, extraction across all 91, yield not asserted.
- **R9**: roadmap current-priority heading updated.
- **A1**: §1 and roadmap say at least 124 dossiers record opening personnel as unknown.
- **A2**: §1 and roadmap describe a measure that includes the forces-engaged class.
- **A3**: §3 item 5 forbids our own sums of initial and later-arriving forces.
- **A4**: §6 names tier-2 predictions as diagnostics, not p_union_win.
- **A5**: the source-ID tiebreak is kept; §4 notes it is arbitrary but outcome-blind.
- **A6**: §4 says alternate_k counts are reported, not trimmed after extraction.

[correction.json](correction.json) records the dispositions. This is a design review
only: no evidence, dossier, source record, admission proposal or model input changed. A
focused follow-up review of the corrected design is required before implementation. AI
review is not historical adjudication or feature admission.
