from code_32 import find_zero
from code_32 import poly

def test():   
    assert poly([1, 2], -0.5) == 0
    assert round(find_zero([1, 2]), 2) == -0.5
    assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0
