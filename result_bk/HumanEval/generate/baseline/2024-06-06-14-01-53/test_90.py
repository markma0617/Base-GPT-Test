from code_90 import next_smallest

import unittest

def test():
    class TestNextSmallest(unittest.TestCase):

        def test_example1(self):
            self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)

        def test_example2(self):
            self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)

        def test_empty_list(self):
            self.assertIsNone(next_smallest([]))

        def test_duplicate_elements(self):
            self.assertIsNone(next_smallest([1, 1]))

    return TestNextSmallest
