from code_68 import pluck

import unittest
from function_file import pluck

class TestPluckFunction(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(pluck([]), [])

    def test_no_even_values(self):
        self.assertEqual(pluck([1, 3, 5]), [])

    def test_single_even_value(self):
        self.assertEqual(pluck([4]), [4, 0])

    def test_multiple_even_values_same_index(self):
        self.assertEqual(pluck([4, 2, 6, 2]), [2, 1])

    def test_multiple_even_values_different_index(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

if __name__ == '__main__':
    unittest.main()
