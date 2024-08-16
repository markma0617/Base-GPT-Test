from code_132 import is_nested

def test():
    assert is_nested('[[]]') == True
    assert is_nested('[]]]]]]][[[[[]') == False
    assert is_nested('[][]') == False
