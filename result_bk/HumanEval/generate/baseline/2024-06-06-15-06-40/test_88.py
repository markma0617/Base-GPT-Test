from code_88 import sort_array

import unittest
from your_module import sort_array

class TestSortArray(unittest.TestCase):

    def test_sort_array_empty(self):
        self.assertEqual(sort_array([]), [])

    def test_sort_array_single_element(self):
        self.assertEqual(sort_array([5]), [5])

    def test_sort_array_odd_sum(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_sort_array_even_sum(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

if __name__ == '__main__':
    unittest.main()
