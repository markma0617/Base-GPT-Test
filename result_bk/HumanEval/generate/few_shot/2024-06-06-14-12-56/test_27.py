from code_27 import flip_case
def test():
    assert triangle(5, 5, 5) == "Equilateral triangle"
    assert triangle(5, 5, 6) == "Isosceles triangle"
    assert triangle(3, 4, 5) == "Scalene triangle"
    assert triangle(3, 3, 7) == "Isosceles triangle"