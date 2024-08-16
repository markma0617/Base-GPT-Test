from code_88 import sort_array

import unittest

def test_sort_array(self):
    self.assertEqual(sort_array([]), [])
    self.assertEqual(sort_array([5]), [5])
    self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])
    self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

# Add this function to a test class and run the test
# For example:
# class TestSortArray(unittest.TestCase):
#     test_sort_array = test_sort_array

# if __name__ == '__main__':
#     unittest.main()
