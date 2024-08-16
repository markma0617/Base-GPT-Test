from code_90 import next_smallest

import unittest

def next_smallest(lst):
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]

class TestNextSmallest(unittest.TestCase):

    def test_next_smallest_example1(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)

    def test_next_smallest_example2(self):
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)

    def test_next_smallest_empty_list(self):
        self.assertIsNone(next_smallest([]))

    def test_next_smallest_no_second_smallest(self):
        self.assertIsNone(next_smallest([1, 1]))

if __name__ == '__main__':
    unittest.main()
