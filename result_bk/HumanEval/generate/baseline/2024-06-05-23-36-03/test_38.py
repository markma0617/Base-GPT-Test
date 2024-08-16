from code_38 import encode_cyclic

import unittest
from your_module import encode_cyclic, decode_cyclic

class TestEncodingDecoding(unittest.TestCase):

    def test_encode_cyclic(self):
        self.assertEqual(encode_cyclic("abcdef"), "bcdefa")
        self.assertEqual(encode_cyclic("abc"), "bca")
        self.assertEqual(encode_cyclic("python"), "yhtonp")

    def test_decode_cyclic(self):
        self.assertEqual(decode_cyclic("bcdefa"), "abcdef")
        self.assertEqual(decode_cyclic("bca"), "abc")
        self.assertEqual(decode_cyclic("yhtonp"), "python")

if __name__ == '__main__':
    unittest.main()
