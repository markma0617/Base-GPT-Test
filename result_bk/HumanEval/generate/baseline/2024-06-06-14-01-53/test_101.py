from code_101 import words_string

import unittest
from your_module import words_string

class TestWordsString(unittest.TestCase):
    
    def test_words_string_with_commas(self):
        self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"])
    
    def test_words_string_with_spaces(self):
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"])

    def test_words_string_empty_input(self):
        self.assertEqual(words_string(""), [])
    
    def test_words_string_single_word(self):
        self.assertEqual(words_string("Hello"), ["Hello"])

if __name__ == '__main__':
    unittest.main()
