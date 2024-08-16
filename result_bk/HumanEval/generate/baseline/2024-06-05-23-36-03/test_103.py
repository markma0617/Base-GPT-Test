from code_103 import rounded_avg

import unittest
from solution import rounded_avg

class TestRoundedAvg(unittest.TestCase):

    def test_rounded_avg_example1(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")

    def test_rounded_avg_example2(self):
        self.assertEqual(rounded_avg(7, 5), -1)

    def test_rounded_avg_example3(self):
        self.assertEqual(rounded_avg(10, 20), "0b1111")

    def test_rounded_avg_example4(self):
        self.assertEqual(rounded_avg(20, 33), "0b11010")

    def test_rounded_avg_custom1(self):
        self.assertEqual(rounded_avg(5, 9), "0b101")

    def test_rounded_avg_custom2(self):
        self.assertEqual(rounded_avg(1, 1), "0b1")

if __name__ == '__main__':
    unittest.main()
