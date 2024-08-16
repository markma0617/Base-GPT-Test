from code_36 import fizz_buzz

def test():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
    assert fizz_buzz(100) == 4
    assert fizz_buzz(132) == 2
    assert fizz_buzz(143) == 1
    assert fizz_buzz(200) == 3
    assert fizz_buzz(300) == 6
    assert fizz_buzz(1000) == 24
    assert fizz_buzz(10000) == 246
