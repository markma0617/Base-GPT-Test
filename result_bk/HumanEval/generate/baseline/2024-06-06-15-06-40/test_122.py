from code_122 import add_elements

import unittest

def test():
    class TestAddElements(unittest.TestCase):

        def test_example(self):
            arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
            k = 4
            self.assertEqual(add_elements(arr, k), 24)

        def test_empty_array(self):
            arr = []
            k = 0
            self.assertEqual(add_elements(arr, k), 0)

        def test_single_element(self):
            arr = [99]
            k = 1
            self.assertEqual(add_elements(arr, k), 99)

        def test_all_two_digits(self):
            arr = [10, 20, 30, 40, 50]
            k = 5
            self.assertEqual(add_elements(arr, k), 100)

        def test_no_elements_with_two_digits(self):
            arr = [111, 234, 987, 345, 111, 999]
            k = 6
            self.assertEqual(add_elements(arr, k), 0)

    return TestAddElements
