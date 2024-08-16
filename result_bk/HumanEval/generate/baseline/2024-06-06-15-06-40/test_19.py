from code_19 import sort_numbers

import unittest
from your_module import sort_numbers

class TestSortNumbers(unittest.TestCase):
    
    def test_sort_numbers_basic(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

    def test_sort_numbers_duplicate(self):
        self.assertEqual(sort_numbers('four four two'), 'four four two')

    def test_sort_numbers_empty(self):
        self.assertEqual(sort_numbers(''), '')

    def test_sort_numbers_invalid_input(self):
        with self.assertRaises(KeyError):
            sort_numbers('invalid input')

if __name__ == '__main__':
    unittest.main()
