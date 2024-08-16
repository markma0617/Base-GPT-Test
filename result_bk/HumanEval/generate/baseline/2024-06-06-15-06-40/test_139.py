from code_139 import special_factorial

import unittest
from your_module import special_factorial

class TestSpecialFactorial(unittest.TestCase):

    def test_special_factorial(self):
        self.assertEqual(special_factorial(1), 1)
        self.assertEqual(special_factorial(2), 2)
        self.assertEqual(special_factorial(3), 12)
        self.assertEqual(special_factorial(4), 288)
        self.assertEqual(special_factorial(5), 34560)
        self.assertEqual(special_factorial(6), 24883200)

if __name__ == '__main__':
    unittest.main()
