from code_131 import digits

def test():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(678) == 7
    assert digits(9119) == 99
    assert digits(1242) == 0
    assert digits(55555) == 625
    assert digits(2468) == 0
    assert digits(13579) == 315
    assert digits(10020) == 0
