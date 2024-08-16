from code_79 import decimal_to_binary

import unittest
from your_module import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_decimal_to_binary_1(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")

    def test_decimal_to_binary_2(self):
        self.assertEqual(decimal_to_binary(32), "db100000db")

if __name__ == '__main__':
    unittest.main()
