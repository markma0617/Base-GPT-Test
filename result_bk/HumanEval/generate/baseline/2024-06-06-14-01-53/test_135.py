from code_135 import can_arrange

import unittest

def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    ind = -1
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            ind = i
        i += 1
    return ind

class TestCanArrange(unittest.TestCase):

    def test_can_arrange_example1(self):
        self.assertEqual(can_arrange([1, 2, 4, 3, 5]), 3)

    def test_can_arrange_example2(self):
        self.assertEqual(can_arrange([1, 2, 3]), -1)

    def test_can_arrange_empty(self):
        self.assertEqual(can_arrange([]), -1)

    def test_can_arrange_single_element(self):
        self.assertEqual(can_arrange([5]), -1)

if __name__ == '__main__':
    unittest.main()
