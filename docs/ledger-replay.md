# Replaying frozen ledgers against the dossiers they bind

**Status: draft for separate review, 2026-10-06.** The owner asked for a design that lets
corrections to ledger-bound dossiers be installed while the frozen ledgers keep replaying, and
chose this approach ("Sure, do whatever you recommend"). This document changes no ledger,
authorization, bound document, bound code or model input. Implementation waits for the separate
review and the owner's acceptance.

## 1. Problem

Four frozen ledgers bind dossiers by path and SHA-256: `data/estimates/side-strength-v1.json` and
`data/command/responsibility-v1.json` (91 dossiers each) and their v2 successors (305 each).
Replay requires `digest(root / path) == sha256` for every in-scope dossier. Rating runs 1 to 3 and
both estimate-layer evaluations replay their ledgers before fitting, and their authorization
records bind the ledgers' own hashes.

The checker code is frozen as well. `side-strength-v1` binds `generalship/estimates.py`;
`side-strength-v2` binds `generalship/estimates_v2.py` and, as its engine, `estimates.py`.
`generalship/imputation.py` is bound by the grade E output, `artifacts/strength-imputation-v1.json`,
which run 3's authorization binds. None of these checkers can be taught to read an archive without
breaking those bindings.

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
2. Otherwise read the live dossier and follow its `supersedes` links. For each link, the archive
   must lie under `data/evidence/history/`, must not repeat, must hash to the link's `sha256` and
   must carry the live dossier's `battle_id`. If the link's `sha256` equals the binding's, return
   the archive.
3. If the chain ends or any check fails, return `None`.

The evidence contract already requires a corrected dossier to archive its predecessor byte for
byte and to link it by hash, and `generalship check` validates the first link. The resolver
re-verifies every link it uses, so a chain is trusted only as far as its hashes hold.

### 3.2 The bound view

`bound_view(root, *ledgers)` is a context manager. Each ledger is a path relative to the root or
an in-memory ledger, as the tamper tests pass.

1. Collect the dossier bindings of all the given ledgers and resolve each one. A *substitution* is
   a binding whose live file differs but whose bound bytes are reachable.
2. If two of the given ledgers bind one path to different reachable versions, raise `ReplayError`.
   A caller that needs both replays them in separate views.
3. If there are no substitutions, yield `root` itself.
4. Otherwise make a temporary directory and mirror every regular file of the repository except
   those under `.git/` and `__pycache__/`, using hard links, or a byte copy if linking fails (for
   example across filesystems). For each substitution, delete the linked file in the view and write
   the archive's bytes as a new file, so that nothing is written through a link, then check that it
   hashes to the bound value. Yield the view, and remove it on exit, including after an error.

Hard links are needed for two reasons. `safe_path` resolves symlinks and rejects paths outside the
root, and each replay re-hashes all 1,601 registered sources (332 MB). A probe on 2026-10-06
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
3. Reproduce the authorized local runs under their existing authorizations: `make
   commander-ratings`, `make estimate-evaluation`, `make commander-ratings-v2` (which runs
   `estimate-evaluation-v2` first), `make strength-imputation` and `make commander-ratings-v3`.
   Every committed output must stay byte-identical.
4. Run `make reproduce`, record the installation beside the review record, and update the roadmap,
   research log, methodology and sources notes. MS009 has no prepared packet to update.

## 5. Tests

- **Resolution:** a live match; one- and two-link archive chains; a broken archive hash, a wrong
  battle ID, a repeated path and a path outside `history/` each return `None`.
- **View:** no substitutions yields the real root; a substitution presents the bound bytes; the live
  file and the live tree are unchanged afterwards; the directory is removed on exit and on error;
  conflicting bindings raise `ReplayError`.
- **Fail closed:** an unreachable binding is not substituted, and the frozen checker still raises
  `Dossier binding`.
- **Integration:** the committed v1 and v2 ledgers replay through views, and every existing tamper
  test still raises its expected message.

Unit tests use small synthetic trees in temporary directories; integration tests use the
repository.

## 6. Risks and limits

- **Writes through hard links.** Code that wrote into a view would write into the live file. This
  is mitigated by the read-only contract, by never writing to a linked path during substitution and
  by tests on the live tree; the checkers contain no writes.
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
- **Teach the checkers about archives.** This is impossible without breaking the strength ledgers'
  bindings of their own code.

## 8. Review and acceptance

A separate Claude Opus 5.5 `high` review checks this design against the code and records it names,
under AGENTS.md. After its findings are reconciled, the owner decides whether to accept it for
implementation. Acceptance does not admit a feature, change a frozen input or authorize a run.
