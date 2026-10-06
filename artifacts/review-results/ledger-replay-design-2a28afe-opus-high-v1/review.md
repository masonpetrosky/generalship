# Separate review: frozen-ledger replay design (`docs/ledger-replay.md`)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, fresh-context
  subagent, working only from the assignment and the repository.
- **Date:** 2026-10-06.
- **Commits:** prepared commit `2a28afe5f90d6dc2a377bcf4d549b6657a4d387f`. The worktree HEAD is
  `19e0d76bc588d94733e7f182e0e47a7fbe32403c`, which adds only `assignment.md` and `inputs.json`
  (`git diff --stat 2a28afe HEAD`).
- **Inputs:** I checked all 35 `inputs.json` paths. Each file's SHA-256 matched both the copy at
  `2a28afe` and the working copy (0 mismatches). Assignment `assignment.md` has SHA-256 `51a41c57…f2da35`
  and `inputs.json` has `e3a66f32…f35da`. The design under review is `docs/ledger-replay.md`, `45814d76…a1fca3`.
- **Outcome:** **the design is sound, but 8 corrections are required.** I found no way for a view to
  show bytes other than the bound bytes. I found no frozen file, feature admission or model input
  that the design changes. The required corrections fix one overbroad factual claim and one wrong
  figure. They also tighten fail-closed behaviour and conflict wording, fix the run order, complete
  the installation steps and the test plan, and add a disclosure about the wider set of ledgers that
  replay will accept.

This is an AI design review. It is not owner acceptance or human adjudication. It authorizes no
implementation, installation or run.

## Coverage actually inspected

- **Design:** all of `docs/ledger-replay.md` (180 lines).
- **Code, read in full:**
  - `generalship/estimates.py`: `check` and its header.
  - `generalship/estimates_v2.py`.
  - `generalship/command.py`.
  - `generalship/sources.py`.
  - `generalship/cli.py`.
  - `generalship/evidence.py`: `citation_text` and the supersedes check at lines 164–181.
  - `generalship/imputation.py`: lines 1–60 and 129–306.
- **Code, read in part:**
  - `generalship/ratings.py`: `RUNS`, `authorize` and `rate`. I grepped `rate` for every root read.
  - `generalship/ratings_v3.py`: `authorize`, `base_rows` and `rate3` lines 258–317.
  - `generalship/estimate_eval.py`: `RUNS`, `authorize` and `evaluate_estimates`.
  - `generalship/dataset.py`: its root reads.
- **Repository-wide greps:**
  - every caller of `estimates.check`, `estimates_v2.check`, `command.check`, `impute` and `build`
    in `generalship/`, `tests/` and `scripts/`;
  - every write or file operation in the checker modules;
  - every record that binds MS009's v1 hash or a `generalship/*.py` path.
- **Tests:**
  - read in full: `tests/test_command.py`, `test_ledgers_v2.py` and `test_workflow.py`;
  - read the ledger section of `test_estimates.py`;
  - read the replay section and imports of `test_imputation.py`;
  - read only the imports of `test_ratings.py` and `test_estimate_eval.py`.
- **Records:**
  - the dossier bindings of all four ledgers (`bindings` blocks);
  - all five authorization records (their bound paths and `code_commit`);
  - the bindings of `artifacts/strength-imputation-v1.json`;
  - Champion Hill's `correction.json`, and the `supersedes` link and `battle_id` of `staged-MS009.json`;
  - `Makefile`;
  - the evidence contract's archive passage (lines 82–98);
  - the roadmap's 2026-10-06 follow-up (lines 45–59) and its deferred implementation choices
    (lines 678–689);
  - `AGENTS.md`.
- **Probes:**
  - **`make check`:** 151 tests OK and `generalship check` passed. The tree stayed clean.
  - **Replay probe:** I ran it in a temporary directory outside the repository with
    `/tmp/lrprobe-scripts/probe.py`. The probe hard-linked the repository's 3,358 files into mirror
    A in 0.87 s. It simulated the MS009 installation inside A only, by unlinking each file before
    writing it.
    - Against A, all four checkers raised `Dossier binding: MS009`.
    - It then built view B from A, substituting the v1 bytes (`f1d093f1…`). Against B, all four
      checkers passed: s1 0.4 s, s2 0.7 s, c1 0.9 s and c2 2.3 s. The view took 0.76 s to build.
    - `safe_path` accepted B under the symlinked `/var` temporary root.
    - The repository's MS009 was byte-identical afterwards.
- **Not done:** I ran no build, rating, evaluation, imputation or packet command, so the four run
  callers were not exercised under a view. I did no source research.

## Fact checks (with evidence)

| Design claim | Finding | Evidence |
| --- | --- | --- |
| The v1 ledgers bind 91 dossiers and the v2 ledgers 305, all at `data/evidence/<id>.json` | Correct. All four bind MS009 at `f1d093f1…`. Every binding in every ledger matches the live file today. Shared battles have identical hashes across ledgers. | ledger `bindings.dossiers` |
| `side-strength-v1` binds `estimates.py`. `side-strength-v2` binds `estimates_v2.py` (`script`) and `estimates.py` (`engine`). | Correct. v1 also binds `design` and `cohort`. v2 also binds `design`, `addendum`, `cohort` and `owner_decision`. Both bind `cited_sources`. | `estimates.py:290-292`, `estimates_v2.py:25-27` |
| The command ledgers' bindings | v1 binds `design`, `cohort` and `registry`. v2 binds those plus `addendum`. **Neither binds any code.** | `command.py:93-96` |
| The grade E output binds `imputation.py`, and run 3's authorization binds that output | Correct. The output also binds the design, both v2 ledgers, the campaigns CSV and the battles CSV. `rate3` enforces this binding through `build_imputation(root, verify=False) != stored`, which compares the rebuilt `bindings` including the hash of `imputation.py`. | `imputation.py:301-306`; `ratings_v3.py:12-13,35-47,264-266`; `rating-authorization-v3.json` |
| No record binds `command.py`, `cli.py`, `ratings.py`, `ratings_v3.py`, `estimate_eval.py`, `evidence.py` or `sources.py` against a replay | Correct, except that the hashes in `shiloh-opening-v2-check.json` and the review inventories are records, not replayed bindings. The authorizations' `code_commit` fields are documentary. | grep; authorization records |
| `safe_path` resolves symlinks and rejects escapes | Correct. It compares `(root/rel).resolve()` with `root.resolve()`, so a symlinked view would fail with `Path escapes project`. | `sources.py:24-28` |
| `digest` | Gives the SHA-256 of `read_bytes()` and follows the path it is given. | `sources.py:11-12` |
| `verify_sources` re-hashes every source | Correct, and it also validates metadata. **The design's "1,601 … (332 MB)" is wrong.** There are 1,601 registry entries but 1,555 distinct files, which total 345.2 MB (329.2 MiB). Counting duplicate entries gives 360.3 MB. Neither figure is 332 MB. | `sources.py:136-143`; `data/sources.json` |
| The checkers and `impute` contain no writes | Correct. The only write helpers are `write_json` and `fetch_sources` in `sources.py`, and no checker or `impute` calls them. | grep of the checker modules |
| `generalship check` validates the first `supersedes` link | Correct. It does this for live dossiers only, because `validate_all` globs `data/evidence/*.json` without recursing. All 305 live dossiers carry `supersedes`, and 12 have chains longer than one link. | `evidence.py:164-181` |
| The staged MS009 links to `data/evidence/history/MS009.v1.json` at `f1d093f1…` | Correct. No archive `MS009.v1.json` exists yet, and the staged file's `battle_id` is `MS009`. | `staged-MS009.json` |

## Call graph (§3.3)

The table lists every production path that replays a frozen ledger:

- **`cli.run_build`:** four checks, at `cli.py:84-108`.
- **CLI `estimate-check` and `command-check`:** `cli.py:210-212,230-231`.
- **CLI `strength-imputation`:** `build_imputation(root)` runs with `verify=True`, which calls both
  v2 checks (`imputation.py:203-205`).
- **`ratings.rate`:** `ratings.py:340-341`.
- **`ratings_v3.rate3`:** `ratings_v3.py:262-263`.
- **`estimate_eval.evaluate_estimates`:** `estimate_eval.py:200`.

Nothing in `scripts/`, `admission.py` or `strength_admission.py` calls a ledger checker.

On the test side, the table names `test_estimates`, `test_command` and `test_ledgers_v2`. The other
tests are as follows:

- **`test_workflow.py`:** reaches the checks through `run_build` on temporary copies, so it is
  covered by the `run_build` row.
- **`test_imputation.py`:** calls only `build(ROOT, verify=False)`, which replays nothing.
- **`test_ratings.py` and `test_estimate_eval.py`:** import only `authorize` and helper functions.

**No caller is missing.**

The claim that the runs read no dossier after replay is **correct**:

- `rate` reads the ledgers, the registry, `build_dataset` (raw CWSAC tables and the cohort) and the
  evaluation output (`ratings.py:342-348,401`).
- `rate3` reads the imputation output, the registry, `base_rows` (ledgers and battles) and the run 2
  output (`ratings_v3.py:52-54,264-299`).
- `evaluate_estimates` reads the ledger and `build_dataset`.
- `side_frame` reads the ledgers, battles and campaigns (`imputation.py:129-149`).
- None of these reads `data/evidence/`.
- `rate3`'s `build_imputation(..., verify=False)` and its three sensitivity `impute(..., verify=False)`
  calls replay nothing.

## Soundness

- **Exact bytes.** The resolver's final condition is a SHA-256 match against the ledger's own binding.
  Substitution then writes a fresh file and re-hashes it. A forged link, archive or dossier can
  therefore change only *whether* bytes are found, not *which* bytes are presented. Doing otherwise
  would need a SHA-256 preimage. Every other file in the view is a hard link to the same inode as
  the live file, so it has identical bytes. My probe reproduced both outcomes, the fail and the
  pass.
- **What replay accepts.** A view accepts a ledger whose dossier binding names any version reachable
  from the live chain. Today replay accepts only the live version. So a ledger edited to bind an
  archived predecessor, and made consistent with it, passes through a view where it fails today.
  Equally, replay no longer depends on the live dossier's content, only on its existence, its
  parseability and its chain.
  - This follows from the purpose of the design and does not breach requirement 3.
  - The ledger itself is anchored by hash only where an authorization binds it: `ratings.authorize`,
    `ratings_v3.authorize` and `estimate_eval.authorize`.
  - `run_build`, `estimate-check`, `command-check` and the tests replay whatever ledger file is
    present.
  - The design does not disclose this (R8).
- **Fail closed.** An unreachable binding is left alone, so the checker's own `digest` comparison
  raises `Dossier binding: <id>` (`estimates.py:313`, `estimates_v2.py:57`, `command.py:131`). The
  design does not say what happens when the live file or an archive is missing or not JSON, or when
  a link escapes the root. In that last case `safe_path` raises `ValueError`. If any of these errors
  escapes the resolver, the reported failure changes from `Dossier binding` to a view error, which
  breaks requirement 4 (R2).
- **Conflicts.** Step 2 is right in substance. The wording "different reachable versions" leaves it
  open whether a live match counts as a version. Suppose one ledger binds the live bytes and another
  an archive, and only substitutions are compared. The view would then substitute the archive, and
  the first ledger would fail falsely (R3). Such a failure is never a false pass.
- **Chain rules.**
  - The history-directory rule must hold for the *resolved* path.
  - The no-repeat rule bounds cycles.
  - Matching battle IDs against the live dossier is adequate, because the final hash decides.
- **Cleanup.** A tree of hard links is safe to `rmtree`, because unlinking does not touch the live
  inodes. The one hazard is the no-substitution branch, which yields `root` itself and must never
  be removed. The test plan does not check this (R7).
- **Hard links and copy fallback.**
  - Writes are correctly identified as the risk.
  - Metadata changes are a further risk: `chmod`, `utime` or xattrs on a view file change the live
    file (A1). The view cannot be made read-only through permissions.
  - The copy fallback presents identical bytes, and substituted files are always fresh copies.
  - This worktree and the default temporary directory are on the same APFS data volume
    (`/dev/disk3s5`).

## Plan and tests

- **Run order.** §4 step 3 runs `commander-ratings` before `estimate-evaluation`. Run 1, however,
  reads `artifacts/estimate-evaluation.json` as its raw residual input (`ratings.py:25,401,444`). The
  Makefile already orders v2 that way (`commander-ratings-v2: estimate-evaluation-v2`). Run 3 needs
  the run 2 output and the imputation output (`ratings_v3.py:264,299`), and the listed order already
  satisfies that (R5).
- **Missing contract update.** §6 says the evidence contract should make reached archives permanent,
  but §4 step 4 does not update the contract (R6).
- **Simulated installation not tested.** Until installation, every view in the integration tests is a
  no-op. The substitution path would then be tested with the real checkers only after MS009 is
  installed. My probe shows that a temporary-mirror simulation is cheap: about 0.8 s plus a few
  seconds of replay (R7).

## Policy

The design changes no ledger, authorization, bound document, bound code, cohort, registry, grade E
output or run output. It adds `generalship/replay.py` and edits only callers that no record binds.
It admits no feature. A corrected dossier enters a model only through a new ledger with its own
review and authorization (§3.4). This is consistent with AGENTS.md (immutable records, versioned
evidence, no automatic feature admission) and with the evidence contract's archive rule
(lines 86–88). Recording the installation *beside* the review record, rather than in it, keeps the
review bundle immutable.

## Required corrections (exact replacement text)

**R1, §1 final sentence of the second paragraph.** The command checker is not hash-bound.

Replace:

> None of these checkers can be taught to read an archive without breaking those bindings.

with:

> The strength checkers cannot be taught to read an archive without breaking those bindings. The
> command checker, `generalship/command.py`, is bound by no ledger, output or authorization. It
> stays unchanged nonetheless, because frozen `imputation.impute` calls it. Changing its behaviour
> would change what that frozen replay checks, and one mechanism serves all four ledgers.

In §7, replace the last bullet with:

> - **Teach the checkers about archives.** This is impossible for the strength checkers without
>   breaking their ledgers' bindings of their own code. For the unbound command checker, it would
>   change the replay that frozen `imputation.impute` performs and split the mechanism.

**R2, §3.1 steps 2–3.** Errors must fail closed. Replace steps 2 and 3 with:

> 2. Otherwise read the live dossier and follow its `supersedes` links. For each link, the
>    archive's resolved path must lie inside the root's `data/evidence/history/`. It must not repeat,
>    must hash to the link's `sha256` and must carry the live dossier's `battle_id`. If the link's
>    `sha256` equals the binding's, return the archive.
> 3. If the chain ends, or any check fails, return `None`. A missing or unreadable file, invalid
>    JSON, a missing field or a path that escapes the root counts as a failed check. The resolver
>    never raises for these cases, so the frozen checker reports `Dossier binding` itself.

**R3, §3.2 step 2.** Clarify conflicts. Replace with:

> 2. If two of the given ledgers bind one path to different hashes that both resolve, raise
>    `ReplayError`. A hash that matches the live file counts as resolving. A caller that needs both
>    replays them in separate views. A binding that does not resolve never causes a conflict. It
>    fails in the checker.

**R4, §3.2 second paragraph.** Correct the figure. Replace "each replay re-hashes all 1,601
registered sources (332 MB)" with:

> each replay re-hashes every one of the 1,601 source registry entries (1,555 distinct files,
> about 345 MB)

**R5, §4 step 3.** Fix the order and say how byte identity is checked. Replace with:

> 3. Reproduce the authorized local runs under their existing authorizations, in dependency order:
>    `make estimate-evaluation`, then `make commander-ratings` (run 1 reads
>    `artifacts/estimate-evaluation.json`), then `make commander-ratings-v2` (which runs
>    `estimate-evaluation-v2` first), then `make strength-imputation`, then `make commander-ratings-v3`
>    (which reads the run 2 and grade E outputs). Every committed output must stay byte-identical.
>    Check this with `git status --porcelain artifacts/` and record the hashes.

**R6, §4 step 4.** Add the contract update. Replace with:

> 4. Run `make reproduce`. Record the installation in a new file beside the review record, leaving
>    the review bundle's files unchanged. Update `docs/evidence-contract.md` to say that an archive
>    reachable from a frozen ledger's binding is permanent and that frozen ledgers replay through
>    the archive chain. Update the roadmap, research log, methodology and sources notes. MS009 has
>    no prepared packet to update.

**R7, §5.** Complete the test plan. Replace the **Resolution**, **View** and **Integration**
bullets with:

> - **Resolution:** a live match; one- and two-link archive chains. Each of the following returns
>   `None` without raising: a broken archive hash, a wrong battle ID, a repeated path, a path outside
>   `history/` (including through `..`), a path escaping the root, a missing archive, a missing live
>   file and invalid JSON.
> - **View:** no substitutions yields the real root and leaves it in place on exit, including after
>   an error. A substitution presents the bound bytes. The live file and the live tree are unchanged
>   afterwards. The directory is removed on exit and on error. Two kinds of conflicting bindings
>   raise `ReplayError`: two archives, and one live match against one archive.
> - **Integration:** the committed v1 and v2 ledgers replay through views, and every existing tamper
>   test still raises its expected message. Before MS009 is installed, a test simulates the
>   installation in a temporary hard-linked mirror, unlinking before every write. It asserts that
>   all four frozen checkers raise `Dossier binding: MS009` on the mirror and pass through a view of
>   it, and that the repository is unchanged.

**R8, §6.** Add the disclosure as a new first bullet:

> - **Wider acceptance.** A view accepts any dossier version reachable from the live chain, where
>   replay today accepts only the live file. A ledger edited to bind an archived predecessor, and
>   made consistent with it, therefore passes through a view but fails today. Replay also stops
>   depending on the live dossier's content, which `generalship check` still validates. The views
>   do not authenticate the ledger. The rating and evaluation runs anchor their ledgers through the
>   authorizations' hashes, while `run_build`, `estimate-check`, `command-check` and the tests replay
>   whatever ledger file is present.

## Advisory notes (not required)

- **A1.** Add to the §6 hard-link bullet that `chmod`, `utime` and xattr changes on a view file
  change the live file. Never apply them to the view.
- **A2.** The resolver could also require the live dossier's `battle_id` to equal the ledger's
  binding key. This is not needed for soundness.
- **A3.** The reproduction runs at a later code commit than the authorizations' `code_commit`.
  Precedent exists: `ratings.py`, `estimate_eval.py` and `ratings_v3.py` changed after their
  authorizations. Record byte-identical outputs as the evidence of equivalence.
- **A4.** `rate` and `rate3` could use one view per check instead of one for both, so they never
  reach the conflict path. That costs about 0.8 s each.
- **A5.** Views shared across a test class should be released with `addClassCleanup`.
- **A6.** Because model jobs are not tests, the views in the four run callers are verified only by
  §4 step 3. State this limit in the implementation record.
- **A7.** The 2026-10-06 probe count of 3,356 files is now 3,358 because of this review's assignment
  files. No action is needed.
