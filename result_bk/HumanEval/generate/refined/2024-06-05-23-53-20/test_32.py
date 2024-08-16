from code_32 import poly

def test():
    assert poly([1, 2], 0) == 1
    assert poly([1, 2, 3], 1) == 6
    assert round(find_zero([1, 2]), 2) == -0.5
