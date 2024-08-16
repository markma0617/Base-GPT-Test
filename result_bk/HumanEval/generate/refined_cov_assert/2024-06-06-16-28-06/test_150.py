from code_150 import x_or_y

def test():   
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(1, 10, 20) == 20
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(3, 10, 20) == 20
    assert x_or_y(4, 10, 20) == 20
    assert x_or_y(5, 10, 20) == 10
    assert x_or_y(6, 10, 20) == 20
    assert x_or_y(7, 10, 20) == 20
    assert x_or_y(8, 10, 20) == 20
