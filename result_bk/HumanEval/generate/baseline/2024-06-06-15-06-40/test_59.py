from code_59 import largest_prime_factor

import unittest
from your_module import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_largest_prime_factor_example1(self):
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_largest_prime_factor_example2(self):
        self.assertEqual(largest_prime_factor(2048), 2)

if __name__ == '__main__':
    unittest.main()
