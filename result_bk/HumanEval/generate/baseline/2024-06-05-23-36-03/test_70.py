from code_70 import strange_sort_list

import unittest

def test_strange_sort_list(self):
    self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
    self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
    self.assertEqual(strange_sort_list([]), [])
