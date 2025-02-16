from code_75 import is_multiply_prime

import unittest

def is_multiply_prime(a):
    def is_prime(n):
        for j in range(2,n):
            if n%j == 0:
                return False
        return True

    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(2*3*5))
        self.assertFalse(is_multiply_prime(10))
        self.assertFalse(is_multiply_prime(17))
        self.assertTrue(is_multiply_prime(2*19*23))

if __name__ == '__main__':
    unittest.main()
