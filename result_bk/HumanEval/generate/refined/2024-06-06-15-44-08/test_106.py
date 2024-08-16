from code_106 import f
def test():
    assert f(1) == [1]
    assert f(2) == [1, 1]
    assert f(5) == [1, 1, 6, 24, 15]