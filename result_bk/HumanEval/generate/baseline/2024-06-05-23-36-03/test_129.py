from code_129 import minPath

import unittest
from your_module import minPath

class TestMinPath(unittest.TestCase):

    def test_min_path_example1(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 3
        expected_output = [1, 2, 1]
        self.assertEqual(minPath(grid, k), expected_output)

    def test_min_path_example2(self):
        grid = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
        k = 1
        expected_output = [1]
        self.assertEqual(minPath(grid, k), expected_output)

if __name__ == '__main__':
    unittest.main()
