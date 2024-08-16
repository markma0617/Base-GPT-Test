from code_82 import prime_length

import unittest
from test_module import prime_length

class TestPrimeLength(unittest.TestCase):

    def test_prime_length_with_empty_string(self):
        self.assertFalse(prime_length(''))

    def test_prime_length_with_string_length_1(self):
        self.assertFalse(prime_length('a'))

    def test_prime_length_with_prime_length(self):
        self.assertTrue(prime_length('Hello'))
        self.assertTrue(prime_length('abcdcba'))
        self.assertTrue(prime_length('kittens'))

    def test_prime_length_with_non_prime_length(self):
        self.assertFalse(prime_length('orange'))

if __name__ == '__main__':
    unittest.main()
