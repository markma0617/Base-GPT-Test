from code_144 import simplify
def test():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("3/4", "2/3") == False
    assert simplify("5/8", "8/5") == True
    assert simplify("2/3", "3/2") == False
    assert simplify("4/7", "7/4") == True
    assert simplify("5/9", "9/5") == False
    assert simplify("1/3", "3/1") == True
    assert simplify("3/5", "5/3") == False