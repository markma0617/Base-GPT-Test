from code_60 import sum_to_n

def test():
    assert triangle(5, 5, 5) == "Equilateral triangle"
    assert triangle(5, 5, 4) == "Isosceles triangle"
    assert triangle(3, 4, 5) == "Scalene triangle"
