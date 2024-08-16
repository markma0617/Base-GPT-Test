from code_116 import sort_array

import unittest

def test():
    class TestSortArray(unittest.TestCase):
        def test_sort_array(self):
            self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
            self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])
            self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])

    return TestSortArray('test_sort_array')
