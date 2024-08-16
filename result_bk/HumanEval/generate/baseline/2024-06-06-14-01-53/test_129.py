from code_129 import minPath

import unittest
from solution import minPath

class TestMinPath(unittest.TestCase):

    def test_example1(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 3
        expected = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected)

    def test_example2(self):
        grid = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
        k = 1
        expected = [1]
        self.assertEqual(minPath(grid, k), expected)

if __name__ == '__main__':
    unittest.main()
