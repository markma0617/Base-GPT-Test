from code_99 import closest_integer

import unittest
from closest_integer import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_integer_value(self):
        self.assertEqual(closest_integer("10"), 10)

    def test_decimal_value(self):
        self.assertEqual(closest_integer("15.3"), 15)

    def test_rounding_away_from_zero_positive(self):
        self.assertEqual(closest_integer("14.5"), 15)

    def test_rounding_away_from_zero_negative(self):
        self.assertEqual(closest_integer("-14.5"), -15)

if __name__ == '__main__':
    unittest.main()
