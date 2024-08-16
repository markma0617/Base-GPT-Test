from code_8 import sum_product

import unittest
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_positive_numbers(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

if __name__ == '__main__':
    unittest.main()
