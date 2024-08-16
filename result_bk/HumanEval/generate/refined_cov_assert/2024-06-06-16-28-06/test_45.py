from code_45 import triangle_area

def test():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 20.0
    assert triangle_area(8, 6) == 24.0
    assert triangle_area(3, 5) == 7.5
    assert triangle_area(7, 2) == 7.0
    assert triangle_area(4, 10) == 20.0
    assert triangle_area(6, 8) == 24.0
    assert triangle_area(2, 7) == 7.0
    assert triangle_area(0, 0) == 0.0
    assert triangle_area(1, 1) == 0.5
