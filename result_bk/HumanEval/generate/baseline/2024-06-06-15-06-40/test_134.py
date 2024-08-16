from code_134 import check_if_last_char_is_a_letter

import unittest

def test():
    class TestCheckIfLastCharIsALetter(unittest.TestCase):
        def test_empty_string(self):
            self.assertFalse(check_if_last_char_is_a_letter(""))

        def test_single_letter_word(self):
            self.assertTrue(check_if_last_char_is_a_letter("e"))

        def test_single_letter_word_with_space(self):
            self.assertTrue(check_if_last_char_is_a_letter("e "))

        def test_single_letter_word_in_sentence(self):
            self.assertFalse(check_if_last_char_is_a_letter("apple pie"))

        def test_single_letter_word_in_sentence_with_space(self):
            self.assertTrue(check_if_last_char_is_a_letter("apple pi e"))

    return TestCheckIfLastCharIsALetter
