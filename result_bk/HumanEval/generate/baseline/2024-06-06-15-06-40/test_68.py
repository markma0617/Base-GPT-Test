from code_68 import pluck

import unittest
from your_script import pluck

class TestPluck(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])

    def test_example2(self):
        self.assertEqual(pluck([1, 2, 3]), [2, 1])

    def test_example3(self):
        self.assertEqual(pluck([]), [])

    def test_example4(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_no_even_values(self):
        self.assertEqual(pluck([1, 3, 5, 7]), [])

    def test_multiple_smallest_even_values(self):
        self.assertEqual(pluck([2, 4, 2, 4]), [2, 0])

    def test_larger_input(self):
        self.assertEqual(pluck([7, 3, 7, 3, 5, 1, 2, 4, 2, 4]), [2, 6])

if __name__ == '__main__':
    unittest.main()
