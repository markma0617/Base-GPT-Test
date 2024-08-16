from code_93 import encode

import unittest
from your_module import encode

class TestEncodeFunction(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()
