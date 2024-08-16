from code_11 import xor
from code_11 import string_xor

import unittest
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

class TestStringXor(unittest.TestCase):

    def test_string_xor_equal_length(self):
        result = string_xor('010', '110')
        self.assertEqual(result, '100')

    def test_string_xor_different_length(self):
        result = string_xor('010', '11')
        self.assertEqual(result, '101')

    def test_string_xor_empty_string(self):
        result = string_xor('', '')
        self.assertEqual(result, '')

    def test_string_xor_one_empty_string(self):
        result = string_xor('010', '')
        self.assertEqual(result, '010')

if __name__ == '__main__':
    unittest.main()
