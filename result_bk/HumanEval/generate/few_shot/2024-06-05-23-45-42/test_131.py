from code_131 import digits

def test():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(2468) == 0
    assert digits(97531) == 45
