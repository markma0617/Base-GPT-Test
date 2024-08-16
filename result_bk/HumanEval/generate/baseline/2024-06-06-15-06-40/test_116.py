from code_116 import sort_array

import unittest
from solution import sort_array

class TestSortArray(unittest.TestCase):

    def test_sort_array(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])

    def test_sort_array_negative(self):
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])

    def test_sort_array_with_zero(self):
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
