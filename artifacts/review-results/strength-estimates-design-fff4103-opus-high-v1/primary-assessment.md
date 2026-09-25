# Primary assessment: best-estimate side-strength design review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`fff4103efea08571af006b4e1c4cc8b171f502e4`. Its SHA-256 is `4b219ea37f619c4c824e5355463e1ce15db713952e57a724145d1850825e397b`. The reviewer ran as a fresh headless session with the
`evidence-reviewer` definition in a detached worktree of the bundle commit; see
[dispatch.json](dispatch.json). It reported ten required findings and seven advisories.

The primary checked each finding against the repository:

- the evidence contract's rule that people present never become people engaged (R1);
- tier-2 §3 codes and §6 one-sided bounds (R2, R3);
- the Livermore/CWSAC identities in the scoping memo (R5);
- contract §7 and AGENTS.md on enriched predictors (R8).

Each correction was applied with the reviewer's replacement text. Dispositions:

- **R1**: §1 target restated on one recorded basis with point_basis.
- **R2**: §3 replaced with the ordered, exhaustive classification table.
- **R3**: §4 replaced with exact-rational, fully specified rules.
- **R4**: resolved by §4 rule 6.
- **R5**: resolved by §4 rule 2.
- **R6**: resolved by §4 rule 4's disclaimer and §6 refit.
- **R7**: §5 label table replaced.
- **R8**: §6 replaced: no fit without an explicit owner authorization naming the reviewed ledger hash.
- **R9**: §7 ledger, inventory, checker and review bullets replaced.
- **R10**: §2 source scope and roadmap paragraph updated.
- **A1**: interpretation of 'each' recorded; README says decisive, non-aggregate.
- **A2**: officer phrase dropped with R1.
- **A3**: upper-middle median refit added to §6.
- **A4**: §4 rule 3 records the deliberate preference.
- **A5**: §2 blinding sentence.
- **A6**: endpoint_refit_* naming.
- **A7**: registered Livermore IDs named in §5.

A focused follow-up review of the corrected design follows. This is a design review only;
no estimate, dossier, source or model input changed. AI review is not historical
adjudication or approval of any estimate.
