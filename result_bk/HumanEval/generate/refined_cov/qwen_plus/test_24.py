from code_24 import largest_divisor

def test():
    assert largest_divisor(15) == 5
    assert largest_divisor(20) == 10
    assert largest_divisor(7) == 7
    assert largest_divisor(1) == 1
    assert largest_divisor(0) == 0
