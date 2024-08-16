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
        self.assertEqual(below_zero([1, 2, 3]), False)

    def test_below_zero_negative(self):
        self.assertEqual(below_zero([1, 2, -4, 5]), True)

    def test_below_zero_zero_balance(self):
        self.assertEqual(below_zero([0, 0, 0]), False)

    def test_below_zero_empty_list(self):
        self.assertEqual(below_zero([]), False)

    def test_below_zero_single_negative(self):
        self.assertEqual(below_zero([-5]), True)


if __name__ == '__main__':
    unittest.main()
