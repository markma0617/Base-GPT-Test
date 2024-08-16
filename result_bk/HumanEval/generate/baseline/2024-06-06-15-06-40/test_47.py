from code_47 import median

import unittest

def test_median(self):
    self.assertEqual(median([3, 1, 2, 4, 5]), 3)
    self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

TestMedian = type('TestMedian', (unittest.TestCase,), {'test_median': test_median})
