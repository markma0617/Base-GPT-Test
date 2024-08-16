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

        def test_no_elements_with_at_most_two_digits(self):
            arr = [111, 222, 333, 444]
            k = 4
            self.assertEqual(add_elements(arr, k), 0)

        def test_all_elements_with_at_most_two_digits(self):
            arr = [11, 22, 33, 44]
            k = 4
            self.assertEqual(add_elements(arr, k), 110)

        def test_some_elements_with_at_most_two_digits(self):
            arr = [111, 22, 333, 44]
            k = 4
            self.assertEqual(add_elements(arr, k), 66)

    return TestAddElements
