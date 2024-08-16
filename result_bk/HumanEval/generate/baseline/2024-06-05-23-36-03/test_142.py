from code_142 import sum_squares

import unittest

def test():
    class TestSumSquares(unittest.TestCase):

        def test_example_cases(self):
            self.assertEqual(sum_squares([1, 2, 3]), 6)
            self.assertEqual(sum_squares([]), 0)
            self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)

        def test_random_cases(self):
            self.assertEqual(sum_squares([2, 4, 6, 8]), 112)
            self.assertEqual(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]), 378)
            self.assertEqual(sum_squares([0, 0, 0]), 0)
            self.assertEqual(sum_squares([1, 1, 1, 1]), 4)

    return TestSumSquares
