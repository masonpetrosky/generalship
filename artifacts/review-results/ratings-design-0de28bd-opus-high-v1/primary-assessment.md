# Primary assessment: commander residual ratings design review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`0de28bd7cdf595b49a8aa80e170650ad82d72a20`. Its SHA-256 is `1551d14c55c041ca3d8acd899a775d3beeecdf01f2923d03d5bb4805c9466809`. The reviewer ran as a fresh headless session with the
`evidence-reviewer` definition in a detached worktree of bundle commit `33247f084202e38d8d3f4cb5fb49c49294009dd0`; see
[dispatch.json](dispatch.json).

The primary checked each finding against the design, the CWSAC listings and the cited dossier
passages. The rank ties (TN003, VA102, GA003), army/navy pairs (TN001, AR006), the VA032/VA033
nesting and the side-offset identity all hold. Every required finding and every advisory is
accepted and applied in the revised design (SHA-256 `1e74f02c6f4a99c391e2c7a53e96fc1a1962afc044f80affc3860f1e30af42a3`).

## Required findings

- **R1**: Target redefined: field commander with command authority when the side first fought; date-only intervals handled; superior_directing label and view.
- **R2**: Rule order 5, 3, 2, 6 then 4; rank ties give grade D; army/navy pairs under rule 5; grade table aligned with the rules.
- **R3**: Rule 7 for nested records, with checker coverage and the section 8 wording.
- **R4**: Side offset stated; ranks within each side; connectivity components and not_connected label; rank set defined; section 8 corrected.
- **R5**: Force size "partly conditioned on"; posterior-to-prior sd ratio reported; mode, not mean; tau wording; "fewer than a dozen".
- **R6**: Verdict configuration fixed; effective denominator; reading of an improvement; no ordered ranking if there is no improvement.
- **R7**: Outcome-only views split into 37-row and 91-row versions; view_sensitive defined on robustness views only; raw-residual p named.
- **R8**: Limits add non-blind attribution, mixed echelons (echelon recorded) and "not Milestone 3".
- **R9**: Questions and replies recorded verbatim in data/command/owner-decision-2026-09-25.json and cited.

## Advisories

- **A1**: Alternative-candidate and successor views added.
- **A2**: Side-offset view with alpha prior sd 3.
- **A3**: Identical fullname strings on one side presumed one person.
- **A4**: Rule 2 contradiction test made operational.
- **A5**: 1862-to-1863 temporal split reported descriptively.
- **A6**: Unit test against quadrature specified.
- **A7**: Brier reported but not part of the verdict.

A focused follow-up review of the revision is next. This AI review is a separate analysis, not
historical adjudication, feature admission or authorization of any fit.
