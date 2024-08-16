from code_125 import split_words

import unittest

def test():
    class TestSplitWords(unittest.TestCase):

        def test_whitespace_split(self):
            self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
            self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

        def test_comma_split(self):
            self.assertEqual(split_words("Hello ,world!"), ["Hello", "world!"])
            self.assertEqual(split_words("Hello,Hello,world !"), ["Hello,Hello,world", "!"])

        def test_no_split(self):
            self.assertEqual(split_words("abcdef"), 3)
            self.assertEqual(split_words("Hello world,!"), ["Hello", "world,!"])

    return TestSplitWords
