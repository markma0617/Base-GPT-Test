from code_38 import decode_cyclic
from code_38 import encode_cyclic

import unittest
from your_module import encode_cyclic, decode_cyclic

class TestEncodeCyclic(unittest.TestCase):

    def test_encode_cyclic(self):
        self.assertEqual(encode_cyclic("abcdef"), "bcdaef")
        self.assertEqual(encode_cyclic("hello"), "elhol")
        self.assertEqual(encode_cyclic("123456789"), "234156879")

    def test_decode_cyclic(self):
        self.assertEqual(decode_cyclic("abcdef"), "abcdef")
        self.assertEqual(decode_cyclic("hello"), "hello")
        self.assertEqual(decode_cyclic("123456789"), "123456789")

if __name__ == '__main__':
    unittest.main()
