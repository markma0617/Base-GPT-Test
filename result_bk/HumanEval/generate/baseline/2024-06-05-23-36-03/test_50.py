from code_50 import encode_shift

import unittest
from your_module import encode_shift, decode_shift

class TestStringMethods(unittest.TestCase):

    def test_encode_shift(self):
        self.assertEqual(encode_shift("abc"), "fgh")
        self.assertEqual(encode_shift("xyz"), "cde")
        self.assertEqual(encode_shift("hello"), "mjqqt")
    
    def test_decode_shift(self):
        self.assertEqual(decode_shift("fgh"), "abc")
        self.assertEqual(decode_shift("cde"), "xyz")
        self.assertEqual(decode_shift("mjqqt"), "hello")

if __name__ == '__main__':
    unittest.main()
