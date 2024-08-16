from code_132 import is_nested

import unittest
from test_function import is_nested

class TestIsNested(unittest.TestCase):

    def test_valid_nested(self):
        self.assertTrue(is_nested('[[]]'))
        self.assertTrue(is_nested('[[][]]'))
        self.assertTrue(is_nested('[[]][['))

    def test_invalid_nested(self):
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))
        self.assertFalse(is_nested('[][]'))
        self.assertFalse(is_nested('[]'))

if __name__ == '__main__':
    unittest.main()
