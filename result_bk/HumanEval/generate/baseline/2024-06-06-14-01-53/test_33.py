from code_33 import sort_third

import unittest
from your_file_name import sort_third

class TestSortThird(unittest.TestCase):

    def test_sort_third_example1(self):
        result = sort_third([1, 2, 3])
        self.assertEqual(result, [1, 2, 3])

    def test_sort_third_example2(self):
        result = sort_third([5, 6, 3, 4, 8, 9, 2])
        self.assertEqual(result, [2, 6, 3, 4, 8, 9, 5])
        
    def test_sort_third_empty_list(self):
        result = sort_third([])
        self.assertEqual(result, [])
        
    def test_sort_third_single_element_list(self):
        result = sort_third([5])
        self.assertEqual(result, [5])

    def test_sort_third_large_list(self):
        result = sort_third([9, 6, 1, 2, 3, 5, 10, 4, 8, 7])
        self.assertEqual(result, [1, 6, 3, 2, 5, 7, 10, 4, 8, 9])

if __name__ == '__main__':
    unittest.main()
