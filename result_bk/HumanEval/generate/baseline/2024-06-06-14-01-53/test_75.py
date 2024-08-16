from code_75 import is_prime
from code_75 import is_multiply_prime

import unittest

def test_is_multiply_prime():
    class TestIsMultiplyPrime(unittest.TestCase):
        def test_example_case(self):
            self.assertEqual(is_multiply_prime(30), True)

        def test_not_multiply_prime(self):
            self.assertEqual(is_multiply_prime(10), False)

        def test_large_number(self):
            self.assertEqual(is_multiply_prime(97), False)

    suite = unittest.TestSuite()
    suite.addTest(TestIsMultiplyPrime('test_example_case'))
    suite.addTest(TestIsMultiplyPrime('test_not_multiply_prime'))
    suite.addTest(TestIsMultiplyPrime('test_large_number'))
    
    return suite
