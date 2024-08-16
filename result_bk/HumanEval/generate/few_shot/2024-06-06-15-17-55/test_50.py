from code_50 import decode_shift
from code_50 import encode_shift

def test():
    assert triangle(5, 5, 5) == "Equilateral triangle"
    assert triangle(5, 5, 4) == "Isosceles triangle"
    assert triangle(3, 4, 5) == "Scalene triangle"
