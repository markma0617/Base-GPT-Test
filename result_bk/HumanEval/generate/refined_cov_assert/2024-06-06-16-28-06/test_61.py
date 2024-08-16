from code_61 import correct_bracketing

def test():
    assert correct_bracketing("(") == False
    assert correct_bracketing("()") == True
    assert correct_bracketing("(()())") == True
    assert correct_bracketing(")(()") == False
    assert correct_bracketing(")") == False
    assert correct_bracketing("(()") == False
    assert correct_bracketing("(())") == True
    assert correct_bracketing("())(") == False
    assert correct_bracketing("((()))") == True
    assert correct_bracketing("()(())") == True
