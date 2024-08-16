from code_143 import words_in_sentence

import unittest
from your_module import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    def test_example1(self):
        sentence = "This is a test"
        self.assertEqual(words_in_sentence(sentence), "is")

    def test_example2(self):
        sentence = "lets go for swimming"
        self.assertEqual(words_in_sentence(sentence), "go for")

    def test_empty_sentence(self):
        sentence = ""
        self.assertEqual(words_in_sentence(sentence), "")

    def test_all_prime_length_words(self):
        sentence = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        self.assertEqual(words_in_sentence(sentence), "a b c d e f g h i j k l m n o p q r s t u v w x y z")

    def test_no_prime_length_words(self):
        sentence = "no prime length words here"
        self.assertEqual(words_in_sentence(sentence), "")

if __name__ == '__main__':
    unittest.main()
