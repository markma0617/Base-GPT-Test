from code_138 import is_equal_to_sum_even

def test():
    assert triangle(3, 3, 3) == "Equilateral triangle"
    assert triangle(3, 3, 2) == "Isosceles triangle"
    assert triangle(3, 4, 5) == "Scalene triangle"
