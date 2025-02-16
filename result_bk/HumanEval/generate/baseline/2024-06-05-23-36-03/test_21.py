from code_21 import rescale_to_unit

import unittest
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]


class TestRescaleToUnit(unittest.TestCase):

    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

    def test_rescale_to_unit_with_zeros(self):
        self.assertEqual(rescale_to_unit([0.0, 0.0, 0.0, 0.0]), [0.0, 0.0, 0.0, 0.0])

    def test_rescale_to_unit_with_negative_numbers(self):
        self.assertEqual(rescale_to_unit([-5.0, -3.0, -1.0, 0.0, 2.0]), [0.0, 0.2, 0.4, 0.5, 1.0])


if __name__ == '__main__':
    unittest.main()
