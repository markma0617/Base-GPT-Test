from code_8 import sum_product

import unittest
from my_module import sum_product

class TestSumProduct(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_positive_numbers(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))

    def test_mixed_numbers(self):
        self.assertEqual(sum_product([1, -2, 3, -4]), (-2, 24))

if __name__ == '__main__':
    unittest.main()
