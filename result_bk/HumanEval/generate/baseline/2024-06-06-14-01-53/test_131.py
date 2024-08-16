from code_131 import digits

import unittest
from your_module import digits

class TestDigitsFunction(unittest.TestCase):

    def test_all_even_digits(self):
        self.assertEqual(digits(4), 0)

    def test_one_odd_digit(self):
        self.assertEqual(digits(1), 1)

    def test_multiple_odd_digits(self):
        self.assertEqual(digits(235), 15)

    def test_no_odd_digits(self):
        self.assertEqual(digits(2468), 0)

if __name__ == '__main__':
    unittest.main()
