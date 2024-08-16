from code_32 import find_zero
from code_32 import poly

def test():
    assert round(find_zero([1, 2]), 2) == -0.5
    assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0
    assert round(find_zero([2, -5, 4]), 2) == -1.0
    assert round(find_zero([1, 0, 0, -1]), 2) == 1.0
