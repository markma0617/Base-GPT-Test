from code_126 import is_sorted

import unittest

def is_sorted(lst):
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i] += 1
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all(lst[i - 1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False

class TestIsSorted(unittest.TestCase):

    def test_sorted_list(self):
        self.assertTrue(is_sorted([5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6, 7]))
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))
    
    def test_unsorted_list(self):
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5, 6, 7]))
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()
