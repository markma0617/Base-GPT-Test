from code_144 import simplify

def test():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("2/3", "3/2") == True
    assert simplify("3/4", "4/3") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("5/6", "6/5") == False
    assert simplify("9/10", "10/9") == False
    assert simplify("1/10", "10/1") == True
    assert simplify("3/7", "7/3") == False
