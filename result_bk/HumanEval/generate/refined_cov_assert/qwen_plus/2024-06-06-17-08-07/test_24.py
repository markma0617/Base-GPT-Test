from code_24 import largest_divisor

def test():
    assert largest_divisor(15) == 5
    assert largest_divisor(20) == 10
    assert largest_divisor(7) == 7
    assert largest_divisor(1) == 1
    assert largest_divisor(21) == 7
    assert largest_divisor(99) == 33
    assert largest_divisor(100) == 50
    assert largest_divisor(123456) == 61728
    assert largest_divisor(987654321) == 493827161
    assert largest_divisor(2**31 - 1) == 2**30 - 1
