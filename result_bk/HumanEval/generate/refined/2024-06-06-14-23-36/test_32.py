from code_32 import find_zero
from code_32 import poly
def test():
    assert poly([1, 2], 0) == 1
    assert poly([1, 2], 1) == 3
    assert poly([1, 2, 3], 2) == 17
    assert find_zero([1, 2]) == -0.5
    assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0
    assert round(find_zero([1, -3, 3, -1]), 2) == 1.0