from code_93 import encode

import unittest

def test():
    class TestEncodeFunction(unittest.TestCase):

        def test_encode(self):
            self.assertEqual(encode('test'), 'TGST')

        def test_encode_with_spaces(self):
            self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

    return TestEncodeFunction
