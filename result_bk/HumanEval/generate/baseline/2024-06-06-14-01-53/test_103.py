from code_103 import rounded_avg

import unittest
from your_script import rounded_avg

class TestRoundedAvg(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")

    def test_example_2(self):
        self.assertEqual(rounded_avg(7, 5), -1)

    def test_example_3(self):
        self.assertEqual(rounded_avg(10, 20), "0b1111")

    def test_example_4(self):
        self.assertEqual(rounded_avg(20, 33), "0b11010")

    def test_negative_case(self):
        self.assertEqual(rounded_avg(100, 50), -1)

if __name__ == '__main__':
    unittest.main()
