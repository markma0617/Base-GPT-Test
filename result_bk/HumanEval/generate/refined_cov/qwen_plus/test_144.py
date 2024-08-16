from code_144 import simplify

def test():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("3/4", "4/3") == True
    assert simplify("9/10", "5/10") == False
