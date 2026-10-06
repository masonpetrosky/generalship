# Primary assessment: Antietam (MD003)

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`fb00e7da75b1a21d10033f2dde39379c45949ce0`. Its SHA-256 is
`8e0b3a8d1388107618c44b3d25947add7cf87ea0b3bab120a88310d6ae2bb90f`. The reviewer ran as a fresh
headless session (`146fc84f-ef3c-486f-ba33-d01d8f00599d`) with the `evidence-reviewer` definition
in a detached worktree of bundle commit `379da81`; see [dispatch.json](dispatch.json). The parent
session's effort and session variables were removed, so it ran at `high` effort; the run reports
only `claude-opus-5-5`, no subagents and no permission denials. It verified all 22 bound input
hashes and inspected the whole dossier (9 claims, 5 citation occurrences, 5 null unknowns), the
NPS snapshot and the MD003 rows of the three CWSAC tables. It reported three required findings and
six advisory notes.

**All three required findings are accepted and closed by primary verification.** R1 adds the
frozen `results_text` ("Inconclusive (Union strategic victory.)") and keeps the strategic label
separate from the tactical result; the frozen value Inconclusive is retained. R2 replaces the
terrain unknown with `named-terrain` (Miller's cornfield, the Dunker Church, the Sunken Road and
the stone bridge). R3 replaces the responsibility unknown with `army-command-decisions`; the
primary added one citation, the CWSAC commanders rank cell ("General") that its rationale relies
on. Every quote occurs exactly once in its cell or snapshot, and `generalship check` validates them.

Advisories A1 to A5 are adopted. A1 cites the frozen force text "Armies" so the dossier says a
missing value is not a zero; A2 notes that NPS does not state the population behind
"two-to-one"; A3 states that Lee ordered the withdrawal after dark, following skirmishing
throughout the 18th; A4 adds a disputed `casualty-records` claim (23,100 in CWSAC against 22,700 on
the NPS page), following the reviewed MD002 and WV016 claims; A5 dates the NPS retrieval
(2026-09-20) instead of calling the page live. A6 is not applied.

[correction.json](correction.json) binds the response and both dossier versions. The v1 draft is
archived byte-for-byte as `data/evidence/history/MD003.v1.json` (`3b9432c4…`) and linked by
`supersedes`; the corrected dossier (`c5c2af00…`) carries revision
`antietam-review-correction-2026-10-06`. The two replacement claims take new IDs, since an ID
ending in `-unknown` would mislabel a supported claim; the archive keeps the old IDs. Claims go
from 9 to 10, explicit unknowns from 5 to 3 (logistics, information and objectives) and citations
from 5 to 18.

No frozen ledger binds MD003, which is inconclusive and outside ledger scope, so every ledger,
authorization and run is unchanged. After correction, 151 tests and the offline checks pass, all
four frozen ledgers replay, and `make reproduce` changes only the MD003 rows of the report and
evidence checks, plus the receipt. Accept the bounded first pass for MD003. Present, available and
engaged strengths, the source of the NPS zeros, casualty reconciliation and a second source family
remain open; the dossier rests on the one `nps-cwsac` family. AI review is not historical
adjudication, proof of source independence or feature admission. Zero rows are promoted, and the
baseline is unchanged (Brier 0.2768816348133779 versus 0.25).
