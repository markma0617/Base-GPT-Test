from code_11 import string_xor

import unittest
from your_module import string_xor

class TestStringXor(unittest.TestCase):

    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('101', '011'), '110')
        self.assertEqual(string_xor('111', '111'), '000')
        self.assertEqual(string_xor('000', '000'), '000')

if __name__ == '__main__':
    unittest.main()
