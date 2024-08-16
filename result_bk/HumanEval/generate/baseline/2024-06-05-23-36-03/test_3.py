from code_3 import below_zero

import unittest
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False

class TestBelowZero(unittest.TestCase):

    def test_below_zero_positive(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_below_zero_negative(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))

if __name__ == '__main__':
    unittest.main()
