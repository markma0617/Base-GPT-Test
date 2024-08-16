from code_71 import triangle_area

def test():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(5, 7, 9) == 17.48
    assert triangle_area(10, 10, 10) == 43.30
    assert triangle_area(2.5, 3.5, 4.5) == 6.00
