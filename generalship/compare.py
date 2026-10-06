"""Compare a rebuilt output with a committed one: exact structure, floats within a tolerance.

Floating-point results can differ in the last bits across platforms (their maths libraries) and Python
versions (sum() is compensated from 3.12), so a committed output reproduces bit for bit only in the
environment that wrote it. Elsewhere every key, string, integer and boolean must still match exactly,
and every float must agree to a relative 1e-9.
"""

import math

REL, ABS = 1e-9, 1e-12


def differences(a, b, rel=REL, abs_tol=ABS, path='$'):
    """Paths where b fails to reproduce a; empty when it does."""
    if isinstance(a, float) or isinstance(b, float):
        numbers = all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in (a, b))
        return [] if numbers and math.isclose(a, b, rel_tol=rel, abs_tol=abs_tol) else [path]
    if type(a) is not type(b):
        return [path]
    if isinstance(a, dict):
        if a.keys() != b.keys():
            return [f'{path} keys']
        return [d for k in a for d in differences(a[k], b[k], rel, abs_tol, f'{path}.{k}')]
    if isinstance(a, list):
        if len(a) != len(b):
            return [f'{path} length']
        return [d for i, (x, y) in enumerate(zip(a, b)) for d in differences(x, y, rel, abs_tol, f'{path}[{i}]')]
    return [] if a == b else [path]
