from code_125 import split_words

import unittest

def split_words(txt):
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',',' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])

class TestSplitWords(unittest.TestCase):
    def test_whitespace_split(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_comma_split(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_no_whitespace_or_comma(self):
        self.assertEqual(split_words("abcdef"), 3)

if __name__ == '__main__':
    unittest.main()
