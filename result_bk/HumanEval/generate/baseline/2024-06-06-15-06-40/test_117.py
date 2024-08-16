from code_117 import select_words

import unittest
from solution import select_words

class TestSelectWords(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(select_words("", 3), [])

    def test_n_consonants_exist(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])
        self.assertEqual(select_words("simple white space", 2), [])
        self.assertEqual(select_words("Hello world", 4), ["world"])
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

if __name__ == '__main__':
    unittest.main()
