from code_140 import fix_spaces

import unittest
from your_module import fix_spaces

class TestFixSpaces(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_single_word_with_digit(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")

    def test_single_word_with_leading_space(self):
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")

    def test_single_word_with_multiple_spaces(self):
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

if __name__ == '__main__':
    unittest.main()
