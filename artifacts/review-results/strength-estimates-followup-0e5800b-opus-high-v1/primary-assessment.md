# Primary assessment: best-estimate design follow-up

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`0e5800b3a931305bf3762434b2280b61d3322ef0`. Its SHA-256 is `069268e175552907b0b7cb6dc952df45bb27a2081db109f1dceef5f7ff0a014a`. The reviewer ran as a fresh headless session with the
`evidence-reviewer` definition in a detached worktree of the bundle commit; see
[dispatch.json](dispatch.json). It confirmed R1–R10 and found seven defects, S1–S7, that
the first round's replacement text created or carried forward, plus five advisories.

The primary had independently met S1 while trying the rules on Fort Henry: an opponent's
figure for a gun-crew remnant became a whole-side candidate and set the point at 80. Each
finding was checked against the design, the tier-2 design, the registry and
`admission.py`. Dispositions:

- **S1**: classification order row 1, row 5, then 2-4 and 6-8; the primary had met the same defect in trial extraction (an opponent's partial gun-crew figure set a point).
- **S2**: rows 3 and 7 replaced; loss_timing and adjustments fields added; checker consistency bullet replaced.
- **S3**: rule 1 and the ledger and passages bullets replaced.
- **S4**: rule 2 replaced, with one justified variant: Livermore figures are cited from the registered transcription of the page images (livermore-transcription-v1), since images carry no quotable text.
- **S5**: rule 4 opening and the rule 5 opponent cap replaced.
- **S6**: four label rows replaced.
- **S7**: identical-by-construction test made before rounding.
- **B1**: applicability_unresolved extended to point or range.
- **B2**: checker limitation sentence extended.
- **B3**: declared consequences recorded in §5.
- **B4**: roadmap and README status updated.
- **B5**: documented floor of 10 for low, labelled floor_applied.

The design is accepted for building the ledger. This is a design review only: no estimate,
dossier, source or model input changed. AI review is not historical adjudication or
approval of any estimate.
