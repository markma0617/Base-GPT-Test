from code_126 import is_sorted

import unittest

def test():
    class TestIsSorted(unittest.TestCase):
        def test_sorted_list(self):
            self.assertTrue(is_sorted([5]))
            self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
            self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
            self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6]))
            self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6, 7]))
            self.assertFalse(is_sorted([1, 3, 2, 4, 5, 6, 7]))
            self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))
            self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

    return TestIsSorted
