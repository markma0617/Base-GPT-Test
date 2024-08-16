from code_60 import sum_to_n

import unittest
from your_module import sum_to_n

class TestSumToN(unittest.TestCase):

    def test_sum_to_n_30(self):
        self.assertEqual(sum_to_n(30), 465)

    def test_sum_to_n_100(self):
        self.assertEqual(sum_to_n(100), 5050)

    def test_sum_to_n_5(self):
        self.assertEqual(sum_to_n(5), 15)

    def test_sum_to_n_10(self):
        self.assertEqual(sum_to_n(10), 55)

    def test_sum_to_n_1(self):
        self.assertEqual(sum_to_n(1), 1)

if __name__ == '__main__':
    unittest.main()
