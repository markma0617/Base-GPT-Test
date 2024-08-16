from code_61 import correct_bracketing

import unittest
from your_module import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_single_open_bracket(self):
        self.assertFalse(correct_bracketing("("))

    def test_correct_bracketing(self):
        self.assertTrue(correct_bracketing("()"))
        self.assertTrue(correct_bracketing("(()())"))

    def test_mismatched_brackets(self):
        self.assertFalse(correct_bracketing(")("))
        self.assertFalse(correct_bracketing("()("))
        self.assertFalse(correct_bracketing("())"))

if __name__ == '__main__':
    unittest.main()
