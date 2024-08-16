from code_84 import solve

import unittest
from solution import solve

class TestSolve(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(solve(1000), "1")

    def test_example2(self):
        self.assertEqual(solve(150), "110")

    def test_example3(self):
        self.assertEqual(solve(147), "1100")

    def test_zero_input(self):
        self.assertEqual(solve(0), "0")

    def test_max_input(self):
        self.assertEqual(solve(10000), "1000")

if __name__ == '__main__':
    unittest.main()
