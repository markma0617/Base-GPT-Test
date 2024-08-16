from code_120 import maximum

import unittest

def test_maximum(self):
    self.assertEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])
    self.assertEqual(maximum([4, -4, 4], 2), [4, 4])
    self.assertEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])
    self.assertEqual(maximum([1, 2, 3, 4, 5], 0), [])
    self.assertEqual(maximum([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
    self.assertEqual(maximum([5, 4, 3, 2, 1], 3), [3, 4, 5])

unittest.TestCase.test_maximum = test_maximum
