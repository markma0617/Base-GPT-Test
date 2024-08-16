from code_38 import decode_cyclic
from code_38 import encode_cyclic

import unittest
from your_module import encode_cyclic

class TestEncodeCyclic(unittest.TestCase):

    def test_encode_cyclic_empty_string(self):
        self.assertEqual(encode_cyclic(""), "")

    def test_encode_cyclic_single_group(self):
        self.assertEqual(encode_cyclic("abc"), "bca")

    def test_encode_cyclic_multiple_groups(self):
        self.assertEqual(encode_cyclic("abcdefghijk"), "bcadefghijk")

    def test_encode_cyclic_group_with_two_characters(self):
        self.assertEqual(encode_cyclic("ab"), "ab")

    def test_encode_cyclic_group_with_one_character(self):
        self.assertEqual(encode_cyclic("a"), "a")

if __name__ == '__main__':
    unittest.main()
