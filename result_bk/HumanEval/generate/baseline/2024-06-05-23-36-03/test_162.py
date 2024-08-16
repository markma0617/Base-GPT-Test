from code_162 import string_to_md5

import unittest
import hashlib

def string_to_md5(text):
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

class TestStringToMD5(unittest.TestCase):

    def test_string_to_md5_non_empty_string(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_string_to_md5_empty_string(self):
        self.assertIsNone(string_to_md5(''))

if __name__ == '__main__':
    unittest.main()
