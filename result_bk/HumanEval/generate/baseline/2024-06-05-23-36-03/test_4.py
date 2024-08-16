from code_4 import mean_absolute_deviation

import unittest
from my_module import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mean_absolute_deviation(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

if __name__ == '__main__':
    unittest.main()
