from code_103 import rounded_avg

import unittest
from solution import rounded_avg

class TestRoundedAvg(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")

    def test_example2(self):
        self.assertEqual(rounded_avg(7, 5), -1)

    def test_example3(self):
        self.assertEqual(rounded_avg(10, 20), "0b1111")

    def test_example4(self):
        self.assertEqual(rounded_avg(20, 33), "0b11010")

if __name__ == '__main__':
    unittest.main()
