from code_61 import correct_bracketing

import unittest
from your_module import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_single_opening_bracket(self):
        self.assertFalse(correct_bracketing("("))

    def test_single_closing_bracket(self):
        self.assertFalse(correct_bracketing(")"))

    def test_correct_bracketing(self):
        self.assertTrue(correct_bracketing("()"))
        self.assertTrue(correct_bracketing("(()())"))
        self.assertTrue(correct_bracketing("(())"))
        self.assertTrue(correct_bracketing("((()))"))

    def test_incorrect_bracketing(self):
        self.assertFalse(correct_bracketing(")("))
        self.assertFalse(correct_bracketing("())"))
        self.assertFalse(correct_bracketing("((()"))

if __name__ == '__main__':
    unittest.main()
