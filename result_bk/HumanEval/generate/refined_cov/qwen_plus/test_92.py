from code_92 import any_int

def test():
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True
    assert any_int(3.6, -2.2, 2) == False
    assert any_int(-1, 2, 3) == True
    assert any_int(0, 0, 0) == True
    assert any_int(4, 5, 6) == False
