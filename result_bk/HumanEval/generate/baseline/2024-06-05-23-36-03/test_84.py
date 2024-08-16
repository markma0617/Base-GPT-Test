from code_84 import solve

import unittest
from your_module import solve

class TestSolveFunction(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(solve(1000), "1")

    def test_case_2(self):
        self.assertEqual(solve(150), "110")

    def test_case_3(self):
        self.assertEqual(solve(147), "1100")

    def test_case_4(self):
        self.assertEqual(solve(0), "0")

    def test_case_5(self):
        self.assertEqual(solve(1111), "100")

if __name__ == '__main__':
    unittest.main()
