from code_99 import closest_integer

import unittest
from closest_integer import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_closest_integer_positive(self):
        self.assertEqual(closest_integer("10"), 10)

    def test_closest_integer_decimal(self):
        self.assertEqual(closest_integer("15.3"), 15)

    def test_closest_integer_negative(self):
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_closest_integer_negative_decimal(self):
        self.assertEqual(closest_integer("-7.8"), -8)

    def test_closest_integer_zero(self):
        self.assertEqual(closest_integer("0"), 0)

if __name__ == '__main__':
    unittest.main()
