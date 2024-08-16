from code_61 import correct_bracketing

import unittest

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    depth = 0
    for b in brackets:
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

class TestCorrectBracketing(unittest.TestCase):

    def test_single_opening_bracket(self):
        self.assertFalse(correct_bracketing("("))

    def test_balanced_brackets(self):
        self.assertTrue(correct_bracketing("()"))

    def test_multiple_balanced_sets(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_unbalanced_brackets(self):
        self.assertFalse(correct_bracketing(")(()"))

if __name__ == '__main__':
    unittest.main()
