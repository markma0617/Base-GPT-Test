from code_150 import x_or_y

import unittest
from your_module import x_or_y

class TestXOrYFunction(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test_non_prime_number(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

    def test_n_equals_1(self):
        self.assertEqual(x_or_y(1, 8, 5), 5)

    def test_n_equals_2(self):
        self.assertEqual(x_or_y(2, 8, 5), 5)

    def test_n_equals_4(self):
        self.assertEqual(x_or_y(4, 8, 5), 5)

if __name__ == '__main__':
    unittest.main()
