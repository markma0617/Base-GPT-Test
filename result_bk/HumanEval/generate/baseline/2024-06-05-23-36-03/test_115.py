from code_115 import max_fill

import unittest
from your_module import max_fill

class TestMaxFill(unittest.TestCase):

    def test_example1(self):
        grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 6)

    def test_example2(self):
        grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
        capacity = 2
        self.assertEqual(max_fill(grid, capacity), 5)

    def test_example3(self):
        grid = [[0,0,0], [0,0,0]]
        capacity = 5
        self.assertEqual(max_fill(grid, capacity), 0)

if __name__ == '__main__':
    unittest.main()
