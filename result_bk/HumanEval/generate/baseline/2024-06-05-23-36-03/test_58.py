from code_58 import common

import unittest

def test_common(self):
    self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
    self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

TestGenerated = type('TestGenerated', (unittest.TestCase,), {'test_common': test_common})
