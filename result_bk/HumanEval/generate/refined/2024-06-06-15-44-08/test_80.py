from code_80 import is_happy

def test():
    assert is_happy('a') == False
    assert is_happy('aa') == False
    assert is_happy('abcd') == True
