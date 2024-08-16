from code_99 import closest_integer

import unittest
from closest_integer import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_integer_input(self):
        self.assertEqual(closest_integer("10"), 10)
    
    def test_decimal_input_round_up(self):
        self.assertEqual(closest_integer("15.3"), 15)

    def test_decimal_input_round_down(self):
        self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_decimal_input_round_down(self):
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_integer_zero_input(self):
        self.assertEqual(closest_integer("0"), 0)

if __name__ == '__main__':
    unittest.main()
