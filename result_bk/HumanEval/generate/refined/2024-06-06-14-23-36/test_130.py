from code_130 import tri
def test():
    assert tri(3) == [1, 3, 2, 8]
    assert tri(5) == [1, 3, 2, 8, 3, 13]
    assert tri(0) == [1]