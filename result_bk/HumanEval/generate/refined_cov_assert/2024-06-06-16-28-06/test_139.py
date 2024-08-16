from code_139 import special_factorial

def test():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560
    assert special_factorial(6) == 24883200
    assert special_factorial(7) == 125411328000
    assert special_factorial(8) == 505658474496000
    assert special_factorial(9) == 1608641288704000000
    assert special_factorial(10) == 418455797760000000000