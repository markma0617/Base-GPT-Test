from code_11 import string_xor

import unittest
from your_module import string_xor

class TestStringXor(unittest.TestCase):

    def test_string_xor(self):
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1010', '1100'), '0110')
        self.assertEqual(string_xor('1111', '1111'), '0000')
        self.assertEqual(string_xor('010101', '101010'), '111111')

if __name__ == '__main__':
    unittest.main()
