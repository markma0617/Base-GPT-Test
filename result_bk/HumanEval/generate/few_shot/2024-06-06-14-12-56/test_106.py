from code_106 import f

def test():
    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(5) == [1, 2, 6, 24, 15]
