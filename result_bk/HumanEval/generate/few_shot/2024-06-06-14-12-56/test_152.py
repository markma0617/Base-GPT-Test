from code_152 import compare

def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(3, 4, 5) == "Scalene triangle"
