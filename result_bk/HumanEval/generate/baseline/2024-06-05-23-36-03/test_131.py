from code_131 import digits

import unittest

def test():
    class TestDigits(unittest.TestCase):
        def test_all_even_digits(self):
            self.assertEqual(digits(4), 0)

        def test_no_odd_digits(self):
            self.assertEqual(digits(2468), 0)

        def test_single_odd_digit(self):
            self.assertEqual(digits(1), 1)

        def test_multiple_odd_digits(self):
            self.assertEqual(digits(235), 15)

    return TestDigits
