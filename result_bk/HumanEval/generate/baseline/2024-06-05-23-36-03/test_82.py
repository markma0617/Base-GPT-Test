from code_82 import prime_length

import unittest

def test():
    class TestPrimeLength(unittest.TestCase):
        def test_prime_length(self):
            self.assertEqual(prime_length('Hello'), True)
            self.assertEqual(prime_length('abcdcba'), True)
            self.assertEqual(prime_length('kittens'), True)
            self.assertEqual(prime_length('orange'), False)

    return TestPrimeLength
