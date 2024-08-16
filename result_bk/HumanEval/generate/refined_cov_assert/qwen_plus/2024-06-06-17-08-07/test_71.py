from code_71 import triangle_area

def test():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(5, 7, 9) == 17.32
    assert triangle_area(1, 1, 1) == 0.41
    assert triangle_area(9, 12, 15) == 59.99
    assert triangle_area(2, 3, 4) == 3.99
    assert triangle_area(10, 10, 10) == 43.30
    assert triangle_area(1.5, 2.5, 3.5) == 1.77
    assert triangle_area(4.5, 5.5, 6.5) == 12.09
    assert triangle_area(0.1, 0.2, 0.3) == -1
