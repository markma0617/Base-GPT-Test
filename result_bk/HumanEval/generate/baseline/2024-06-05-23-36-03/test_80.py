from code_80 import is_happy

import unittest
from your_module import is_happy

class TestIsHappy(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(is_happy(''))

    def test_single_letter(self):
        self.assertFalse(is_happy('a'))

    def test_two_same_letters(self):
        self.assertFalse(is_happy('aa'))

    def test_three_distinct_letters(self):
        self.assertTrue(is_happy('abc'))

    def test_three_letters_with_duplicate(self):
        self.assertFalse(is_happy('abb'))

    def test_three_letters_with_one_duplicate(self):
        self.assertFalse(is_happy('aba'))

    def test_happy_string(self):
        self.assertTrue(is_happy('abcde'))

    def test_happy_string_with_repeating_pattern(self):
        self.assertTrue(is_happy('abcabc'))

if __name__ == '__main__':
    unittest.main()
