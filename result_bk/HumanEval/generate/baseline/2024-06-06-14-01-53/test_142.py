from code_142 import sum_squares

import unittest

def test():
    class TestSumSquares(unittest.TestCase):

        def test_example1(self):
            self.assertEqual(sum_squares([1, 2, 3]), 6)

        def test_example2(self):
            self.assertEqual(sum_squares([]), 0)

        def test_example3(self):
            self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)

        def test_any_case(self):
            self.assertEqual(sum_squares([3, 2, 1, 4, 5]), 101)  # 9 + 2 + 1 + 64 + 25 = 101

    return TestSumSquares
