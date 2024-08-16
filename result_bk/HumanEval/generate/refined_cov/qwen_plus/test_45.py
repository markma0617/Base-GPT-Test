from code_45 import triangle_area
def test():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 20.0
    assert triangle_area(2.5, 6.2) == 7.75
    # Additional test case for a edge scenario
    assert triangle_area(0, 10) == 0.0
    assert triangle_area(1e-9, 1e-9) == 5e-19