from code_131 import digits

def test():
    assert digits(1) == 1
    assert digits(4) == 0
    assert digits(235) == 15
    assert digits(2468) == 0
    assert digits(13579) == 105
    assert digits(101010101) == 1
    assert digits(33333333) == 2187
    assert digits(123456789) == 105
    assert digits(246813579) == 105
    assert digits(1111222233334444) == 576
