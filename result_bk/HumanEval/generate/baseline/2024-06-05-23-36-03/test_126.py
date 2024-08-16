from code_126 import is_sorted

import unittest
from your_script import is_sorted

class TestIsSorted(unittest.TestCase):

    def test_sorted_list(self):
        self.assertTrue(is_sorted([5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6, 7]))
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))

    def test_unsorted_list(self):
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5, 6, 7]))
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()
