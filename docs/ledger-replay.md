# Replaying frozen ledgers against the dossiers they bind

**Status: accepted by the owner on 2026-10-06 ("Yes") and implemented in `generalship/replay.py`.**
The owner asked for a design that lets corrections to ledger-bound dossiers be installed while the
frozen ledgers keep replaying, and chose this approach ("Sure, do whatever you recommend"). A
separate Claude Opus 5.5 `high` [review](../artifacts/review-results/ledger-replay-design-2a28afe-opus-high-v1/review.md)
found the design sound and required eight corrections, all applied here. This document changes no
ledger, authorization, bound document, bound code or model input.

## 1. Problem

Four frozen ledgers bind dossiers by path and SHA-256: `data/estimates/side-strength-v1.json` and
`data/command/responsibility-v1.json` (91 dossiers each) and their v2 successors (305 each).
Replay requires `digest(root / path) == sha256` for every in-scope dossier. Rating runs 1 to 3 and
both estimate-layer evaluations replay their ledgers before fitting, and their authorization
records bind the ledgers' own hashes.

The checker code is frozen as well. `side-strength-v1` binds `generalship/estimates.py`;
`side-strength-v2` binds `generalship/estimates_v2.py` and, as its engine, `estimates.py`.
`generalship/imputation.py` is bound by the grade E output, `artifacts/strength-imputation-v1.json`,
which run 3's authorization binds. The strength checkers cannot be taught to read an archive
without breaking those bindings. The command checker, `generalship/command.py`, is bound by no
ledger, output or authorization. It stays unchanged nonetheless, because frozen `imputation.impute`
calls it. Changing its behaviour would change what that frozen replay checks, and one mechanism
serves all four ledgers.

Correcting a ledger-bound dossier therefore breaks replay. The first case is Champion Hill (MS009).
Its separate review on 2026-10-06 found five extraction errors, but installing the corrected dossier
made five tests fail with `Dossier binding: MS009`, so the correction is staged in its
[review record](../artifacts/review-results/champion-hill-fb00e7d-opus-high-v1/correction.json).
Without a replay design, a correction to any of the 305 bound dossiers would meet the same block.

## 2. Requirements

1. **No frozen bytes change.** Ledgers, authorizations, bound documents, bound code, cohorts,
   registries, the grade E output and committed run outputs stay byte-identical.
2. **Full replay.** Each frozen ledger is checked by its own unchanged checker, not by a hash
   comparison or a stored result.
3. **Exact bound bytes.** Every dossier path a ledger binds is presented with the bytes the ledger
   bound. Those bytes come only from the live file, when its hash matches, or from an archive
   reached through the live dossier's `supersedes` chain, with each link verified by SHA-256 and
   battle ID.
4. **Fail closed.** A binding whose bytes cannot be reached this way is left as it is, so the
   checker reports `Dossier binding` exactly as it does today.
5. **No change when nothing changed.** If every bound dossier is live, callers get the real root
   and behaviour is identical to today.
6. **Live tree untouched.** No replay writes to the repository.
7. **Offline and standard library only,** with no dependence on git history.

## 3. Design

A new module, `generalship/replay.py`, provides two functions. Only unfrozen callers use them.

### 3.1 Resolving a binding

`bound_dossier(root, binding)` returns the path that holds the bytes a dossier binding names, or
`None`:

1. If the live file at `binding['path']` hashes to `binding['sha256']`, return it.
2. Otherwise read the live dossier and follow its `supersedes` links. For each link, the
   archive's resolved path must lie inside the root's `data/evidence/history/`. It must not repeat,
   must hash to the link's `sha256` and must carry the live dossier's `battle_id`. If the link's
   `sha256` equals the binding's, return the archive.
3. If the chain ends, or any check fails, return `None`. A missing or unreadable file, invalid
   JSON, a missing field or a path that escapes the root counts as a failed check. The resolver
   never raises for these cases, so the frozen checker reports `Dossier binding` itself.

The evidence contract already requires a corrected dossier to archive its predecessor byte for
byte and to link it by hash, and `generalship check` validates the first link. The resolver
re-verifies every link it uses, so a chain is trusted only as far as its hashes hold.

### 3.2 The bound view

`bound_view(root, *ledgers)` is a context manager. Each ledger is a path relative to the root or
an in-memory ledger, as the tamper tests pass.

1. Collect the dossier bindings of all the given ledgers and resolve each one. A *substitution* is
   a binding whose live file differs but whose bound bytes are reachable.
2. If two of the given ledgers bind one path to different hashes that both resolve, raise
   `ReplayError`. A hash that matches the live file counts as resolving. A caller that needs both
   replays them in separate views. A binding that does not resolve never causes a conflict. It
   fails in the checker.
3. If there are no substitutions, yield `root` itself.
4. Otherwise make a temporary directory and mirror every regular file of the repository except
   those under `.git/` and `__pycache__/`, using hard links, or a byte copy if linking fails (for
   example across filesystems). For each substitution, delete the linked file in the view and write
   the archive's bytes as a new file, so that nothing is written through a link, then check that it
   hashes to the bound value. Yield the view, and remove it on exit, including after an error.

Hard links are needed for two reasons. `safe_path` resolves symlinks and rejects paths outside the
root, and each replay re-hashes every one of the 1,601 source registry entries (1,555 distinct
files, about 345 MB). A probe on 2026-10-06
mirrored the repository's 3,356 files in 0.72 s and removed them in 0.12 s. The repository holds no
symlinks, and the temporary directory is on the same volume.

The view is read-only by contract. The checkers and `imputation.impute` contain no writes, and
callers write their outputs under the real root. Python still imports the package from the real
repository: the view's `generalship/*.py` files exist only so that the bound-code hashes can be
checked, and they are links to the same bytes.

### 3.3 Where views are used

Each unfrozen caller wraps its existing replay call.

| Caller | Replays | Change |
| --- | --- | --- |
| `cli.run_build` (`make check`, `make reproduce`) | all four ledgers | one view for all four, or one per ledger if their bound versions conflict; failures stay non-fatal (`stale_or_invalid`) |
| `cli` `estimate-check`, `command-check` | the named ledger | a view of that ledger |
| `cli` `strength-imputation` | v2 strength and command, inside frozen `imputation.impute` | `build_imputation(view)`; the output is written under the real root |
| `ratings.rate` (runs 1 and 2) | the run's two ledgers | one view of both, around the two checks |
| `ratings_v3.rate3` (run 3) | v2 strength and command | one view of both, around the two checks |
| `estimate_eval.evaluate_estimates` | the run's ledger | a view around the check |
| `tests/test_estimates.py`, `test_command.py`, `test_ledgers_v2.py` | committed ledgers and tamper copies | views built from the ledger under test, reused within a test class |

After replay, the runs read ledgers, registries, cohorts and CWSAC tables but no dossier, so only
the replay calls need a view. `ratings_v3` rebuilds the grade E output with `verify=False`, which
replays nothing and reads no dossier.

### 3.4 What does not change

Ledger formats, the archive rules, authorization records and every bound file stay as they are. A
frozen ledger keeps describing the evidence it was built from. A corrected dossier enters a model
only through a new versioned ledger with its own review and owner authorization. Future ledgers
keep binding live paths, and later corrections use the same mechanism.

Only dossiers are covered. Sources, documents, code and cohorts are never revised in place, so a
change to one of them still fails replay, as intended.

## 4. First use: installing Champion Hill's correction

After the mechanism is implemented and passes with MS009 unchanged, where every view is a no-op:

1. Copy the live `data/evidence/MS009.json` (`f1d093f1…`) to
   `data/evidence/history/MS009.v1.json`, which the staged file's `supersedes` link names, and
   install `staged-MS009.json` (`42d44bef…`).
2. Run `make check`. The four committed-ledger replays and the tamper tests must pass through views,
   and `run_build` must report no stale ledger.
3. Reproduce the authorized local runs under their existing authorizations, in dependency order:
   `make estimate-evaluation`, then `make commander-ratings` (run 1 reads
   `artifacts/estimate-evaluation.json`), then `make commander-ratings-v2` (which runs
   `estimate-evaluation-v2` first), then `make strength-imputation`, then `make commander-ratings-v3`
   (which reads the run 2 and grade E outputs). Every committed output must stay byte-identical.
   Check this with `git status --porcelain artifacts/` and record the hashes. The runs execute at a
   later code commit than their authorizations' `code_commit`, so byte-identical outputs are the
   evidence of equivalence.
4. Run `make reproduce`. Record the installation in a new file beside the review record, leaving
   the review bundle's files unchanged. Update `docs/evidence-contract.md` to say that an archive
   reachable from a frozen ledger's binding is permanent and that frozen ledgers replay through
   the archive chain. Update the roadmap, research log, methodology and sources notes. MS009 has
   no prepared packet to update.

## 5. Tests

- **Resolution:** a live match; one- and two-link archive chains. Each of the following returns
  `None` without raising: a broken archive hash, a wrong battle ID, a repeated path, a path outside
  `history/` (including through `..`), a path escaping the root, a missing archive, a missing live
  file and invalid JSON.
- **View:** no substitutions yields the real root and leaves it in place on exit, including after
  an error. A substitution presents the bound bytes. The live file and the live tree are unchanged
  afterwards. The directory is removed on exit and on error. Two kinds of conflicting bindings
  raise `ReplayError`: two archives, and one live match against one archive.
- **Fail closed:** an unreachable binding is not substituted, and the frozen checker still raises
  `Dossier binding`.
- **Integration:** the committed v1 and v2 ledgers replay through views, and every existing tamper
  test still raises its expected message. Before MS009 is installed, a test simulates the
  installation in a temporary hard-linked mirror, unlinking before every write. It asserts that
  all four frozen checkers raise `Dossier binding: MS009` on the mirror and pass through a view of
  it, and that the repository is unchanged.

Unit tests use small synthetic trees in temporary directories; integration tests use the
repository. A view shared across a test class is released with `addClassCleanup`. Model jobs are
not tests, so the views in the four run callers are verified only by the reproduction in section 4,
step 3; the implementation record should state this limit.

## 6. Risks and limits

- **Wider acceptance.** A view accepts any dossier version reachable from the live chain, where
  replay today accepts only the live file. A ledger edited to bind an archived predecessor, and
  made consistent with it, therefore passes through a view but fails today. Replay also stops
  depending on the live dossier's content, which `generalship check` still validates. The views
  do not authenticate the ledger. The rating and evaluation runs anchor their ledgers through the
  authorizations' hashes, while `run_build`, `estimate-check`, `command-check` and the tests replay
  whatever ledger file is present.
- **Writes through hard links.** Code that wrote into a view would write into the live file. This
  is mitigated by the read-only contract, by never writing to a linked path during substitution and
  by tests on the live tree; the checkers contain no writes. Metadata changes carry the same risk:
  `chmod`, `utime` or extended attributes applied to a view file change the live file, so they are
  never applied to a view.
- **Disk and time.** About 0.8 s per view with hard links; if linking fails, a byte copy of about
  500 MB.
- **Archive deletion.** Deleting an archive that a frozen ledger reaches breaks its replay, as it
  should. The evidence contract should state that such archives are permanent.
- **Stale citations are expected.** After installation, the frozen ledgers still cite MS009's v1
  claims. That is their record, not an error, and the roadmap should say so.

## 7. Alternatives considered

- **Replay from git history**, rebuilding the tree at each ledger's commit. This is exact, but it
  needs git and full history at test time, fails in a source archive or shallow clone, is slower
  and ignores the existing archive contract.
- **Keep bound bytes at the live path** and put corrections elsewhere. Replay would not change, but
  "the dossier" would mean different things for different battles, and every reader would need a
  redirect.
- **Verify frozen ledgers by hash only.** This is cheap, but it drops the full replay the project
  relies on.
- **Teach the checkers about archives.** This is impossible for the strength checkers without
  breaking their ledgers' bindings of their own code. For the unbound command checker, it would
  change the replay that frozen `imputation.impute` performs and split the mechanism.

## 8. Review and acceptance

A separate Claude Opus 5.5 `high` review checked this design against the code and records it names,
under AGENTS.md. It found no way for a view to present bytes other than the bound bytes, confirmed
the call graph, and reproduced the failure and the fix in a temporary mirror. Its eight required
corrections and four of its seven advisory notes are applied; see the
[primary assessment](../artifacts/review-results/ledger-replay-design-2a28afe-opus-high-v1/primary-assessment.md).
The owner accepted the design for implementation on 2026-10-06. Acceptance does not admit a
feature, change a frozen input or authorize a run.
