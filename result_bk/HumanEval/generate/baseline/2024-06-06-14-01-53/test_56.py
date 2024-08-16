from code_56 import correct_bracketing

import unittest

def test_correct_bracketing():
    assert correct_bracketing("<") == False
    assert correct_bracketing("<>") == True
    assert correct_bracketing("<<><>>") == True
    assert correct_bracketing("><<>") == False

if __name__ == '__main__':
    unittest.main()
