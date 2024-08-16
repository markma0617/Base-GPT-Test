from code_93 import encode

import unittest
from your_module import encode

class TestEncodeFunction(unittest.TestCase):

    def test_encode_example1(self):
        self.assertEqual(encode('test'), 'TGST')

    def test_encode_example2(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()
