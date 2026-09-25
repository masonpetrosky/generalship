# Primary assessment: commander rating model and first run

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `14c8c3bfe3ce4e9c9de36a24b7f937ccb36c998f`. Its
SHA-256 is `3603b49e00ed03790c3fa2ccc5beffb100624e9d9b13f8c33d671822c786a961`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `497eb12a8b6f52d4a69762d0b57e29b62df5722f`; see [dispatch.json](dispatch.json).

The reviewer reproduced the outputs byte for byte and recomputed the verdict with an independent
implementation, which matched. The primary checked each finding against the JSON and applied all
required findings.

The outputs were regenerated under the existing authorization, which binds the ledgers and
registry, not the code. The verdict, modes and rank intervals are unchanged; the SDs moved by at
most 4e-9 (SHA-256 `18bfa5f220ded00bb4baa8984ed984404f204095412abff9bfeb4b7d8e884aba`).

## Required findings

- **F1** (accepted applied): Memo rank-interval sentence corrected (Jackson 1-4).
- **F2** (accepted applied): Battle-weighted difference 0.0004; campaign-weighted gap 0.0118 stated; "negligible" removed.
- **F3** (accepted applied): Single-campaign commanders: own theta never used, but rows inform other parameters.
- **F4** (accepted applied): unranked_in_view reported for Milroy, Bragg and Ewell.
- **F5** (accepted applied): Outcome-only views reported with differences in the memo and stored per commander (theta_mode_minus_primary).
- **F6** (accepted applied): out_of_model_reasons and dropped_as_nested_in_outcome_only_91 added to the outputs.
- **F7** (accepted applied): Coverage "necessary but may not be sufficient" in memo and roadmap.

## Advisories

- **A1** (accepted applied): No-signal sentence clarified.
- **A2** (accepted applied): Report adds the temporal split, effective commanders, unranked views, 95% intervals and SD ratio; campaigns-better formatted.
- **A3** (accepted applied): Closing sentence corrected.
- **A4** (accepted applied): Covariance recomputed at the final iterate (SD change at most 4e-9).
- **A5** (accepted applied): Raw-residual input hash recorded in the output.
- **A6** (accepted applied): Sparser-eras claim marked untested.
- **A7** (not adopted): Bundle binding gap noted; the reviewer recorded the hashes.

This AI review is a separate analysis. It is not historical adjudication, and it does not make the
diagnostic a ranking of generals.
