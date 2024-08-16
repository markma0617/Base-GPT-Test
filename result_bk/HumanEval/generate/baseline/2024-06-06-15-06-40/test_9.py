from code_9 import rolling_max

import unittest
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result


class TestRollingMax(unittest.TestCase):

    def test_rolling_max_example(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

    def test_rolling_max_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_rolling_max_single_element(self):
        self.assertEqual(rolling_max([5]), [5])

    def test_rolling_max_negative_numbers(self):
        self.assertEqual(rolling_max([-5, 2, -3, 8, -1]), [-5, 2, 2, 8, 8])


if __name__ == '__main__':
    unittest.main()
