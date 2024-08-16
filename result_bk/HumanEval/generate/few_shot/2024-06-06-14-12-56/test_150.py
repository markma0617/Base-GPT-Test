from code_150 import x_or_y

def test():
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(1, 100, 200) == 200
    assert x_or_y(17, 3, 10) == 3
    assert x_or_y(29, 0, 1) == 0
