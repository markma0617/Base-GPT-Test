from code_70 import strange_sort_list

import unittest

def test_strange_sort_list(self):
    self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
    self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
    self.assertEqual(strange_sort_list([]), [])
    self.assertEqual(strange_sort_list([4, 3, 2, 1]), [1, 4, 2, 3])
    self.assertEqual(strange_sort_list([10, 20, 30, 40]), [10, 40, 20, 30])

test_func = test_strange_sort_list
