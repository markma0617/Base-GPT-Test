from code_40 import triples_sum_to_zero

import unittest

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

class TestTripleSumToZero(unittest.TestCase):
    def test_case1(self):
        self.assertFalse(triples_sum_to_zero([1, 3, 5, 0]))
    
    def test_case2(self):
        self.assertTrue(triples_sum_to_zero([1, 3, -2, 1]))
    
    def test_case3(self):
        self.assertFalse(triples_sum_to_zero([1, 2, 3, 7]))
    
    def test_case4(self):
        self.assertTrue(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))
    
    def test_case5(self):
        self.assertFalse(triples_sum_to_zero([1]))

if __name__ == '__main__':
    unittest.main()
