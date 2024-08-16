from code_125 import split_words

import unittest
from solution import split_words

class TestSplitWords(unittest.TestCase):

    def test_space_split(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_comma_split(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_no_split(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_no_split_special_characters(self):
        self.assertEqual(split_words("1234#$%"), 2)

    def test_empty_string(self):
        self.assertEqual(split_words(""), 0)

if __name__ == '__main__':
    unittest.main()
