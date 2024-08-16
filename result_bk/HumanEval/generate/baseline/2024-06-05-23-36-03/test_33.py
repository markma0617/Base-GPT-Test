from code_33 import sort_third

import unittest

def test_sort_third(self):
    self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
    self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

class TestSortThird(unittest.TestCase):
    test_sort_third = test_sort_third

if __name__ == '__main__':
    unittest.main()
