from code_117 import select_words

import unittest

def select_words(s, n):
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n:
            result.append(word)
    return result

class TestSelectWords(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])

    def test_example_2(self):
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])

    def test_example_3(self):
        self.assertEqual(select_words("simple white space", 2), [])

    def test_example_4(self):
        self.assertEqual(select_words("Hello world", 4), ["world"])

    def test_example_5(self):
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

if __name__ == '__main__':
    unittest.main()