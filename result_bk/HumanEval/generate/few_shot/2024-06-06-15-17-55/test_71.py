from code_71 import triangle_area

def test():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(5, 12, 13) == 30.0
    assert triangle_area(7, 24, 25) == 84.0
    assert triangle_area(8, 15, 17) == 60.0
