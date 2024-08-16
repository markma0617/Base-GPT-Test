from code_54 import same_chars

import unittest
from your_module_name import same_chars

class TestSameChars(unittest.TestCase):

    def test_same_chars_1(self):
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))

    def test_same_chars_2(self):
        self.assertTrue(same_chars('abcd', 'dddddddabc'))

    def test_same_chars_3(self):
        self.assertTrue(same_chars('dddddddabc', 'abcd'))

    def test_same_chars_4(self):
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))

    def test_same_chars_5(self):
        self.assertFalse(same_chars('abcd', 'dddddddabce'))

    def test_same_chars_6(self):
        self.assertFalse(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))

if __name__ == '__main__':
    unittest.main()
