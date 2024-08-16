from code_32 import find_zero
from code_32 import poly

def test():
    assert poly([1, 2], 3.0) == 7
    assert poly([1, 2, 3], 4.0) == 27
    assert poly([2, 0, 0, 1], 2.0) == 10
    assert round(find_zero([1, 2]), 2) == -0.5
    assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0
