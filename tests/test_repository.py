"""Repository-level limits that keep the project pushable and reproducible."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
# GitHub warns on files over 50 MiB and rejects files over 100 MiB; fail well before either.
LIMIT = 45 * 1024 * 1024


class RepositoryLimitTests(unittest.TestCase):
    def test_no_file_approaches_the_github_file_size_limit(self):
        big = sorted((str(p.relative_to(ROOT)), p.stat().st_size)
                     for d in ('artifacts', 'data', 'docs', 'design', 'reviews', 'generalship', 'tests')
                     for p in (ROOT / d).rglob('*') if p.is_file() and p.stat().st_size > LIMIT)
        self.assertEqual(big, [], 'Split or compact these outputs before committing them')
