from code_43 import pairs_sum_to_zero

import unittest

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

class TestPairsSumToZero(unittest.TestCase):

    def test_pairs_sum_to_zero_positive(self):
        self.assertTrue(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))

    def test_pairs_sum_to_zero_negative(self):
        self.assertFalse(pairs_sum_to_zero([1, 3, 5, 0]))
        self.assertFalse(pairs_sum_to_zero([1, 3, -2, 1]))
        self.assertFalse(pairs_sum_to_zero([1, 2, 3, 7]))
        self.assertFalse(pairs_sum_to_zero([1]))

if __name__ == '__main__':
    unittest.main()
