from code_59 import largest_prime_factor

import unittest
from module_name import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

if __name__ == '__main__':
    unittest.main()
