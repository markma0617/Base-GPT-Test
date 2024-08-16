from code_155 import even_odd_count

import unittest
from your_module import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_even_odd_count_positive(self):
        self.assertEqual(even_odd_count(123), (1, 2))

    def test_even_odd_count_negative(self):
        self.assertEqual(even_odd_count(-12), (1, 1))

    def test_even_odd_count_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))

if __name__ == '__main__':
    unittest.main()
