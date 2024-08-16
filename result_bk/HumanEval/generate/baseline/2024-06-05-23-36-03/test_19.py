from code_19 import sort_numbers

import unittest
from your_module import sort_numbers

class TestSortNumbers(unittest.TestCase):

    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')
        self.assertEqual(sort_numbers('nine eight seven'), 'nine eight seven')
        self.assertEqual(sort_numbers('two four six'), 'two four six')

if __name__ == '__main__':
    unittest.main()
