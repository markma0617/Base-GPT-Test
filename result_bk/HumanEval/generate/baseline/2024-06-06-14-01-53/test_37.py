from code_37 import sort_even

import unittest
from solution import sort_even

class TestSortEven(unittest.TestCase):

    def test_sort_even_with_odd_list(self):
        input_list = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(sort_even(input_list), expected)

    def test_sort_even_with_even_list(self):
        input_list = [5, 6, 3, 4]
        expected = [3, 6, 5, 4]
        self.assertEqual(sort_even(input_list), expected)

if __name__ == '__main__':
    unittest.main()
