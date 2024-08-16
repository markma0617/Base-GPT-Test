from code_75 import is_multiply_prime

import unittest

def is_multiply_prime(a):
    def is_prime(n):
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(2, 101):
            if not is_prime(j):
                continue
            for k in range(2, 101):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False

class TestIsMultiplyPrime(unittest.TestCase):
    def test_example(self):
        self.assertTrue(is_multiply_prime(30))

    def test_not_multiply_prime(self):
        self.assertFalse(is_multiply_prime(20))

    def test_larger_number(self):
        self.assertTrue(is_multiply_prime(77))

    def test_prime_number(self):
        self.assertFalse(is_multiply_prime(13))

if __name__ == '__main__':
    unittest.main()
