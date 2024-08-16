from code_120 import maximum

import unittest

def test():
    class TestMaximum(unittest.TestCase):
        def test_example1(self):
            self.assertEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])

        def test_example2(self):
            self.assertEqual(maximum([4, -4, 4], 2), [4, 4])

        def test_example3(self):
            self.assertEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])

    return TestMaximum
