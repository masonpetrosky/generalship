# Primary assessment: reported side-strength design follow-up

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`848fb7889471d46771ca0f85fa5462d11b3d4dad`. Its SHA-256 is `1b2675c0637a22008686b9b2b48cff70f204fb48f9b2d1cf8f9b4e50577b3514`. The reviewer ran as a fresh headless session with the
`evidence-reviewer` definition in a detached worktree of the bundle commit; see
[dispatch.json](dispatch.json). It verified all 23 bound input hashes and confirmed that
R1–R9 of the first review are applied. It found four new consistency problems, N1–N4,
which those corrections had introduced, and seven advisories.

The primary checked each finding against the design, `admission.py` and `evidence.py`:

- the `_candidate` time checks (N3);
- the absence of an unknown value in `QUANTITY_BASES` (N2);
- the overlapping pair classes (N1);
- the unnamed estimation label (N4).

Each correction was applied with the reviewer's exact replacement text, choosing the
"block unknown basis" option for N2. Dispositions:

- **N1**: §4 pair ranking and §8 source_role replaced with the specified text.
- **N2**: basis_unknown now blocks any figure without an established basis; unknown-basis pairs removed from §4.
- **N3**: §8 states the opening profile's contact-boundary checks do not apply and lists the replacement interval rules.
- **N4**: estimation_status_unknown named in §3, §8 and counted in §6.
- **B1**: §7 further-family trigger reworded as specified.
- **B2**: Livermore source ID fixed as livermore-numbers-losses-selections-v1; identical-by-construction reporting stated.
- **B3**: §3 item 6 excludes reported_reinforcements as partial_scope and post_outcome strength claims as post_outcome_claim.
- **B4**: status line and contract sections (§§1, 3, 5, 6 and 7) updated.
- **B5**: §8 row contents per side.
- **B6**: diagnostic output name fixed as diagnostic_union_score.
- **B7**: Shiloh event IDs cited; this record uses separate_followup_review.

The design is accepted for implementation. No further design reviewer pass is claimed;
the separate review of the validator implementation will read the design as its
specification. This is a design review only: no evidence, dossier, source, proposal or
model input changed. AI review is not historical adjudication or feature admission.
