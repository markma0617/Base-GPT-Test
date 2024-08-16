from code_162 import string_to_md5

import unittest
import hashlib

def test_string_to_md5():
    class TestStringToMd5(unittest.TestCase):

        def test_non_empty_string(self):
            self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

        def test_empty_string(self):
            self.assertIsNone(string_to_md5(''))

    return TestStringToMd5
