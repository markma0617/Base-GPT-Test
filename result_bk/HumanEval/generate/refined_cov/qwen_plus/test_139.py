from code_139 import special_factorial

def test():
    assert special_factorial(0) == 1
    assert special_factorial(1) == 1
    assert special_factorial(4) == 288
    assert special_factorial(5) == 77760
    assert special_factorial(7) == 124416000
