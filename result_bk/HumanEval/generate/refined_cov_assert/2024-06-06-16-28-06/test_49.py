from code_49 import modp

def test():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1
    assert modp(1, 1) == 0
    assert modp(5, 2) == 0
    assert modp(10, 3) == 1
    assert modp(2, 7) == 4
    assert modp(6, 13) == 8
