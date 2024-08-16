from code_82 import prime_length

import unittest
from your_module import prime_length

class TestPrimeLength(unittest.TestCase):

    def test_prime_length_empty_string(self):
        self.assertFalse(prime_length(''))

    def test_prime_length_single_char_string(self):
        self.assertFalse(prime_length('a'))

    def test_prime_length_prime_length_strings(self):
        self.assertTrue(prime_length('Hello'))
        self.assertTrue(prime_length('abcdcba'))
        self.assertTrue(prime_length('kittens'))

    def test_prime_length_non_prime_length_strings(self):
        self.assertFalse(prime_length('orange'))

if __name__ == '__main__':
    unittest.main()
