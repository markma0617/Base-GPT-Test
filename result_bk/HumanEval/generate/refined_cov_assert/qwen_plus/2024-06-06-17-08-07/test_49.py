from code_49 import modp

def test():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1
    assert modp(7, 29) == 24
    assert modp(5, 7) == 3
    assert modp(10, 31) == 21
    assert modp(20, 43) == 26
    assert modp(1000, 10007) == 1
