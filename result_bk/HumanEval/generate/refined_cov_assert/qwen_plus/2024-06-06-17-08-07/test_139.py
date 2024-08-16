from code_139 import special_factorial

def test():
    assert special_factorial(0) == 1
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 7680
    assert special_factorial(6) == 345600
    assert special_factorial(7) == 20736000
    assert special_factorial(8) == 1866240000
    assert special_factorial(9) == 232252800000
