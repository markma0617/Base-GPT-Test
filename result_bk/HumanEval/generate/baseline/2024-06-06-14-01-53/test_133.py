from code_133 import sum_squares

import unittest
from your_module import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_sum_squares_example1(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)

    def test_sum_squares_example2(self):
        self.assertEqual(sum_squares([1, 4, 9]), 98)

    def test_sum_squares_example3(self):
        self.assertEqual(sum_squares([1, 3, 5, 7]), 84)

    def test_sum_squares_example4(self):
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)

    def test_sum_squares_example5(self):
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)

if __name__ == '__main__':
    unittest.main()
