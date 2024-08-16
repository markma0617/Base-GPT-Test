from code_139 import special_factorial

import unittest
from your_module import special_factorial

class TestSpecialFactorial(unittest.TestCase):

    def test_special_factorial_with_4(self):
        self.assertEqual(special_factorial(4), 288)

    def test_special_factorial_with_0(self):
        self.assertEqual(special_factorial(0), 1)

    def test_special_factorial_with_negative_number(self):
        with self.assertRaises(ValueError):
            special_factorial(-1)

    def test_special_factorial_with_large_number(self):
        self.assertEqual(special_factorial(10), 6652800365)

if __name__ == '__main__':
    unittest.main()
