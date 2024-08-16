from code_80 import is_happy

import unittest

def is_happy(s):
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
            return False
    return True

class TestIsHappy(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(is_happy(""))

    def test_single_char_string(self):
        self.assertFalse(is_happy("a"))

    def test_same_chars_string(self):
        self.assertFalse(is_happy("aa"))

    def test_distinct_chars_string(self):
        self.assertTrue(is_happy("abcd"))

    def test_two_consecutive_same_chars(self):
        self.assertFalse(is_happy("aabb"))

    def test_two_consecutive_same_chars_at_boundary(self):
        self.assertFalse(is_happy("adb"))

    def test_two_different_chars(self):
        self.assertFalse(is_happy("xyy"))

if __name__ == '__main__':
    unittest.main()
