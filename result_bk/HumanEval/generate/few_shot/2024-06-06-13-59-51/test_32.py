from code_32 import find_zer
from code_32 import pol

def test():
    assert round(find_zero([1, 2]), 2) == -0.5
    assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0
