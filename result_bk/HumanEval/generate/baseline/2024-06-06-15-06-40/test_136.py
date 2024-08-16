from code_136 import largest_smallest_integers

import unittest

def test():
    class TestLargestSmallestIntegers(unittest.TestCase):

        def test_case1(self):
            self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

        def test_case2(self):
            self.assertEqual(largest_smallest_integers([]), (None, None))

        def test_case3(self):
            self.assertEqual(largest_smallest_integers([0]), (None, None))

        def test_case4(self):
            self.assertEqual(largest_smallest_integers([-2, -4, -1, -3, -5, -7]), (-1, None))

        def test_case5(self):
            self.assertEqual(largest_smallest_integers([2, 4, 1, -3, -5, 7]), (-5, 1))

    return TestLargestSmallestIntegers
