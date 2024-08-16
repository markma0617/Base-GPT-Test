from code_120 import maximum

import unittest

def test():
    class TestMaximum(unittest.TestCase):

        def test_example1(self):
            arr = [-3, -4, 5]
            k = 3
            expected = [-4, -3, 5]
            self.assertEqual(maximum(arr, k), expected)

        def test_example2(self):
            arr = [4, -4, 4]
            k = 2
            expected = [4, 4]
            self.assertEqual(maximum(arr, k), expected)

        def test_example3(self):
            arr = [-3, 2, 1, 2, -1, -2, 1]
            k = 1
            expected = [2]
            self.assertEqual(maximum(arr, k), expected)

    return TestMaximum
