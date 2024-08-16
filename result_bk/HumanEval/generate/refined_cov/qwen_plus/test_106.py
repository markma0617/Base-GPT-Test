from code_106 import f

def test():
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(3) == [1, 2, 3]
    assert f(7) == [1, 2, 6, 24, 15, 21, 22]
