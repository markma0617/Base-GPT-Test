from code_53 import add
def test():
    assert triangle(4, 4, 4) == "Equilateral triangle"
    assert triangle(4, 4, 5) == "Isosceles triangle"
    assert triangle(3, 4, 5) == "Scalene triangle"