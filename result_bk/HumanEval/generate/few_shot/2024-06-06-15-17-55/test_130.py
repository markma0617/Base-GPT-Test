from code_130 import tri

def test():
    assert tri(0) == [1]
    assert tri(1) == [1, 3]
    assert tri(2) == [1, 3, 2]
    assert tri(3) == [1, 3, 2, 8]
    assert tri(4) == [1, 3, 2, 8, 4]
