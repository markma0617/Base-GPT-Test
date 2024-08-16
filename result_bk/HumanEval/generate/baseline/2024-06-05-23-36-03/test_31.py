from code_31 import is_prime

import unittest
from your_module import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))

if __name__ == '__main__':
    unittest.main()
