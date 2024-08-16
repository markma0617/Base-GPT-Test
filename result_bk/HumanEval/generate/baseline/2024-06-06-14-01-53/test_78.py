from code_78 import hex_key

import unittest
from solution import hex_key

class TestHexKey(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(hex_key(""), 0)

    def test_single_prime_digit(self):
        self.assertEqual(hex_key("B"), 1)

    def test_multiple_prime_digits(self):
        self.assertEqual(hex_key("1077E"), 2)
        self.assertEqual(hex_key("ABED1A33"), 4)
        self.assertEqual(hex_key("123456789ABCDEF0"), 6)

    def test_no_prime_digits(self):
        self.assertEqual(hex_key("CDEF"), 0)
        self.assertEqual(hex_key("2020"), 2)

if __name__ == '__main__':
    unittest.main()
