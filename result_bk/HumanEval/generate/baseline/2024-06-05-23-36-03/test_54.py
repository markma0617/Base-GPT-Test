from code_54 import same_chars

import unittest
from your_module import same_chars

class TestSameChars(unittest.TestCase):

    def test_same_chars_same_length_true(self):
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))

    def test_same_chars_same_length_false(self):
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))

    def test_same_chars_different_length_false(self):
        self.assertFalse(same_chars('abcd', 'dddddddabce'))

    def test_same_chars_different_length_false_2(self):
        self.assertFalse(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))

    def test_same_chars_different_length_false_3(self):
        self.assertFalse(same_chars('abcd', 'dddddddabce'))

if __name__ == '__main__':
    unittest.main()
