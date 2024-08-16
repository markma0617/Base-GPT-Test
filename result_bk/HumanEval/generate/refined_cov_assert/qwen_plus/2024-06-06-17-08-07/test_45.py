from code_45 import triangle_area

def test():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 25.0
    assert triangle_area(2.5, 6) == 7.5
    assert triangle_area(0, 10) == 0
    assert triangle_area(1, 0) == 0
    assert triangle_area(-1, 2) == None  # Testing negative side length
    assert triangle_area(4, -3) == None  # Testing negative height
    assert triangle_area(0.5, 0.8) == 0.2
    assert triangle_area(1.234, 5.678) == 3.5208
    assert triangle_area(9.876, 5.432) == 26.612
