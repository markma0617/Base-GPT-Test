from code_150 import x_or_y

def test():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(0, 3, 6) == 6
    assert x_or_y(-1, 99, 88) == 88
    assert x_or_y(11, "prime", "not_prime") == "prime"
    assert x_or_y(12, "x", "y") == "y"
    assert x_or_y(97, True, False) == True
    assert x_or_y(6, "a", "b") == "b"
    assert x_or_y(42, 4, 2) == 2
