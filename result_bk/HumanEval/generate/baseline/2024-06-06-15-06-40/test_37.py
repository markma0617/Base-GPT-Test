from code_37 import sort_even

import unittest
from your_module import sort_even

class TestSortEven(unittest.TestCase):

    def test_sort_even_example1(self):
        input_list = [1, 2, 3]
        expected_output = [1, 2, 3]
        self.assertEqual(sort_even(input_list), expected_output)

    def test_sort_even_example2(self):
        input_list = [5, 6, 3, 4]
        expected_output = [3, 6, 5, 4]
        self.assertEqual(sort_even(input_list), expected_output)

    def test_sort_even_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(sort_even(input_list), expected_output)

    def test_sort_even_single_element_list(self):
        input_list = [7]
        expected_output = [7]
        self.assertEqual(sort_even(input_list), expected_output)

    def test_sort_even_duplicate_elements(self):
        input_list = [4, 4, 2, 2, 3, 3]
        expected_output = [2, 2, 3, 3, 4, 4]
        self.assertEqual(sort_even(input_list), expected_output)

if __name__ == '__main__':
    unittest.main()
