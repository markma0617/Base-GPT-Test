from code_142 import sum_squares

import unittest
from your_module import sum_squares

class TestSumSquares(unittest.TestCase):
    
    def test_case1(self):
        self.assertEqual(sum_squares([1, 2, 3]), 6)
    
    def test_case2(self):
        self.assertEqual(sum_squares([]), 0)
    
    def test_case3(self):
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)

if __name__ == '__main__':
    unittest.main()
