from code_39 import is_prime
from code_39 import prime_fib

import unittest
from your_module import prime_fib

class TestPrimeFib(unittest.TestCase):

    def test_prime_fib(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)

if __name__ == '__main__':
    unittest.main()
