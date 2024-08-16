from code_31 import is_prime

import unittest
from your_module import is_prime

class TestIsPrime(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertEqual(is_prime(101), True)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(13441), True)
        self.assertEqual(is_prime(61), True)

    def test_non_prime_numbers(self):
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(1), False)

    def test_edge_cases(self):
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)

if __name__ == '__main__':
    unittest.main()
