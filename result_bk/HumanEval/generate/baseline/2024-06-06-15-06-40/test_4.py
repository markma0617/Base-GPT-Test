from code_4 import mean_absolute_deviation

import unittest
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mean_absolute_deviation(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0, places=7)

    def test_mean_absolute_deviation_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_mean_absolute_deviation_single_element(self):
        self.assertEqual(mean_absolute_deviation([5.0]), 0.0)


if __name__ == '__main__':
    unittest.main()
