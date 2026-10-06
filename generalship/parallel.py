"""Deterministic parallel map over independent model fits, standard library only.

Results come back in input order, and each task runs the same code it would run serially, so
outputs are identical whatever the worker count. Set GENERALSHIP_WORKERS=1 to run serially.
"""

from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import os

_SHARED = None


def workers():
    value = os.environ.get('GENERALSHIP_WORKERS')
    return max(1, int(value)) if value else (os.cpu_count() or 1)


def _init(shared):
    global _SHARED
    _SHARED = shared


def _run(task):
    fn, item = task
    return fn(item, _SHARED)


def pmap(fn, items, shared=None, n=None):
    """[fn(x, shared) for x in items], spread over processes.

    fn must be a module-level function. `shared` is sent once to each worker rather than with
    every task.
    """
    items = list(items)
    n = workers() if n is None else n
    if n <= 1 or len(items) <= 1:
        return [fn(x, shared) for x in items]
    with ProcessPoolExecutor(max_workers=min(n, len(items)), mp_context=multiprocessing.get_context('spawn'),
                             initializer=_init, initargs=(shared,)) as pool:
        return list(pool.map(_run, [(fn, x) for x in items]))
