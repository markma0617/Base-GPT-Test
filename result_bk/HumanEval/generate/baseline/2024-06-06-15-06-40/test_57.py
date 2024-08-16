from code_57 import monotonic

import unittest

def test():
    class TestMonotonic(unittest.TestCase):

        def test_increasing(self):
            self.assertTrue(monotonic([1, 2, 4, 20]))

        def test_decreasing(self):
            self.assertTrue(monotonic([4, 1, 0, -10]))

        def test_not_monotonic(self):
            self.assertFalse(monotonic([1, 20, 4, 10]))

    return TestMonotonic
