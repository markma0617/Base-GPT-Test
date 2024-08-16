from code_136 import largest_smallest_integers

import unittest

def test():
    class TestLargestSmallestIntegers(unittest.TestCase):

        def test_positive_numbers(self):
            self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

        def test_empty_list(self):
            self.assertEqual(largest_smallest_integers([]), (None, None))

        def test_zero_element_list(self):
            self.assertEqual(largest_smallest_integers([0]), (None, None))

        def test_negative_numbers(self):
            self.assertEqual(largest_smallest_integers([-2, -4, -1, -3, -5, -7]), (-7, None))

        def test_mixed_numbers(self):
            self.assertEqual(largest_smallest_integers([-2, 4, -1, 3, -5, 7]), (-2, 3))

    return TestLargestSmallestIntegers
