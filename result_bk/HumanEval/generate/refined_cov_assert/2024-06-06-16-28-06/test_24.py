from code_24 import largest_divisor

def test():
    assert largest_divisor(15) == 5
    assert largest_divisor(17) == 1
    assert largest_divisor(20) == 10
    assert largest_divisor(1) == 1
    assert largest_divisor(0) == 0
    assert largest_divisor(100) == 50
    assert largest_divisor(33) == 11
    assert largest_divisor(49) == 7
    assert largest_divisor(36) == 18
    assert largest_divisor(63) == 21
