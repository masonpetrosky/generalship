"""Replay frozen ledgers against the dossier versions they bind (docs/ledger-replay.md).

A frozen ledger binds each dossier by path and SHA-256, and the strength ledgers also bind their
own checker code, so a corrected dossier cannot simply replace the bound file. `bound_view`
presents the bound bytes instead: a temporary hard-linked mirror of the repository in which each
bound dossier path holds the archived version the ledger bound, reached through the live
dossier's hash-verified `supersedes` chain. Callers pass the view as `root` to the unchanged
checkers. Nothing here admits a feature or changes a model input.
"""

from contextlib import contextmanager
import os
from pathlib import Path
import shutil
import tempfile

from .sources import digest, read_json, safe_path

HISTORY = 'data/evidence/history'
SKIPPED_DIRS = {'.git', '__pycache__'}


class ReplayError(ValueError):
    pass


def bound_dossier(root, binding):
    """The path holding the bytes a dossier binding names, or None (design §3.1).

    That is the live file if its hash matches, or an archive reached from it through hash-verified
    `supersedes` links inside `data/evidence/history/`. Every failure returns None, never raises,
    so the frozen checker reports `Dossier binding` itself.
    """
    root = Path(root)
    try:
        live = safe_path(root, binding['path'])
        if digest(live) == binding['sha256']:
            return live
        current = read_json(live)
        battle = current['battle_id']
        history = (root / HISTORY).resolve()
        seen = set()
        while current.get('supersedes'):
            link = current['supersedes']
            archive = safe_path(root, link['path'])
            if not archive.is_relative_to(history) or archive in seen:
                return None
            seen.add(archive)
            if digest(archive) != link['sha256']:
                return None
            current = read_json(archive)
            if current.get('battle_id') != battle:
                return None
            if link['sha256'] == binding['sha256']:
                return archive
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        return None
    return None


def _dossier_bindings(root, ledger):
    """A ledger's dossier bindings; a ledger is a path relative to root or an in-memory ledger."""
    try:
        if isinstance(ledger, str):
            ledger = read_json(safe_path(root, ledger))
        bindings = ledger['bindings']['dossiers']
        return list(bindings.values()) if isinstance(bindings, dict) else []
    except (OSError, ValueError, KeyError, TypeError):
        return []  # an unreadable ledger fails in its checker


def substitutions(root, *ledgers):
    """{bound path: (sha256, archive path)} for bindings whose live file differs but whose bound bytes
    are reachable (design §3.2). Two ledgers binding one path to different reachable hashes, a live
    match included, raise ReplayError; an unreachable binding never conflicts."""
    root = Path(root)
    found = {}
    for ledger in ledgers:
        for binding in _dossier_bindings(root, ledger):
            source = bound_dossier(root, binding)
            if source is None:
                continue
            path, sha = binding['path'], binding['sha256']
            if path in found and found[path][0] != sha:
                raise ReplayError(f'Ledgers bind {path} to different reachable versions; replay them in separate views')
            found[path] = (sha, source)
    return {path: (sha, source) for path, (sha, source) in found.items() if source != safe_path(root, path)}


def repository_text(text, view, root):
    """Name repository paths, not a temporary view's, in a message from a replay. The resolved
    form is replaced first because the unresolved one can be its suffix (/var within /private/var)."""
    for v, r in ((Path(view).resolve(), Path(root).resolve()), (Path(view), Path(root))):
        text = text.replace(str(v), str(r))
    return text


def _report_repository_paths(exc, view, root):
    """Rewrite an exception leaving a view so that it names repository paths."""
    if isinstance(exc, OSError):
        for attr in ('filename', 'filename2'):
            if isinstance(getattr(exc, attr), str):
                setattr(exc, attr, repository_text(getattr(exc, attr), view, root))
    elif exc.args and isinstance(exc.args[0], str):
        exc.args = (repository_text(exc.args[0], view, root),) + exc.args[1:]


def _mirror(root, view):
    """Hard-link every regular file under root into view, copying where linking fails."""
    skip = {view.resolve()}
    for dirpath, dirnames, filenames in os.walk(root):
        here = Path(dirpath)
        dirnames[:] = [d for d in dirnames if d not in SKIPPED_DIRS and (here / d).resolve() not in skip]
        target_dir = view / here.relative_to(root)
        target_dir.mkdir(parents=True, exist_ok=True)
        for name in filenames:
            source = here / name
            if source.is_symlink():
                continue  # safe_path rejects symlinks; the repository holds none
            try:
                os.link(source, target_dir / name)
            except OSError:
                shutil.copy2(source, target_dir / name)


@contextmanager
def bound_view(root, *ledgers):
    """Yield a root in which every reachable dossier binding of the given ledgers has its bound bytes.

    With nothing to substitute this is `root` itself, left in place. Otherwise it is a temporary
    hard-linked mirror of the repository, removed on exit. Code given a view must only read it:
    a write, chmod, utime or extended attribute on a linked file changes the live file.
    """
    root = Path(root)
    subs = substitutions(root, *ledgers)
    if not subs:
        yield root
        return
    view = Path(tempfile.mkdtemp(prefix='generalship-replay-'))
    try:
        _mirror(root.resolve(), view)
        for path, (sha, source) in subs.items():
            target = view / path
            target.unlink()  # never write through a hard link
            shutil.copyfile(source, target)
            if digest(target) != sha:
                raise ReplayError(f'Substituted bytes do not match the binding: {path}')
        yield view
    except Exception as exc:
        _report_repository_paths(exc, view, root)
        raise
    finally:
        shutil.rmtree(view, ignore_errors=True)
