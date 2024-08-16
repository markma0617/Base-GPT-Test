from code_101 import words_string

import unittest

def words_string(s):
    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()

class TestWordsString(unittest.TestCase):

    def test_words_string_commas(self):
        self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"])

    def test_words_string_spaces(self):
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"])

    def test_words_string_empty(self):
        self.assertEqual(words_string(""), [])
