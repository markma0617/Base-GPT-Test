from code_150 import x_or_y
def test():
    assert x_or_y(1, 34, 12) == 12
    assert x_or_y(2, 34, 12) == 34
    assert x_or_y(7, 34, 12) == 34