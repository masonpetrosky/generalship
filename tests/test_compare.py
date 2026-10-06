"""Rebuilt-versus-committed comparison (generalship/compare.py)."""

import unittest

from generalship.compare import differences


class CompareTests(unittest.TestCase):
    def test_floats_may_differ_in_the_last_bits_only(self):
        self.assertEqual(differences({'a': [0.1 + 0.2, 1, 'x']}, {'a': [0.3, 1, 'x']}), [])
        self.assertEqual(differences({'a': 1.0}, {'a': 1.0 + 1e-6}), ['$.a'])

    def test_structure_strings_and_integers_must_match_exactly(self):
        self.assertEqual(differences({'a': 1}, {'a': 2}), ['$.a'])
        self.assertEqual(differences({'a': 1}, {'b': 1}), ['$ keys'])
        self.assertEqual(differences([1, 2], [1]), ['$ length'])
        self.assertEqual(differences({'a': True}, {'a': 1.0}), ['$.a'])
        self.assertEqual(differences('x', 'y'), ['$'])


if __name__ == '__main__':
    unittest.main()
