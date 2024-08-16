from code_130 import tri

def test():
    assert tri(0) == [1]
    assert tri(1) == [1, 3]
    assert tri(2) == [1, 3, 2]
    assert tri(3) == [1, 3, 2, 8]
    assert tri(4) == [1, 3, 2, 8, 7]
    assert tri(5) == [1, 3, 2, 8, 7, 18]
    assert tri(6) == [1, 3, 2, 8, 7, 18, 26]
    assert tri(7) == [1, 3, 2, 8, 7, 18, 26, 34]
    assert tri(8) == [1, 3, 2, 8, 7, 18, 26, 34, 49]
    assert tri(9) == [1, 3, 2, 8, 7, 18, 26, 34, 49, 52]
