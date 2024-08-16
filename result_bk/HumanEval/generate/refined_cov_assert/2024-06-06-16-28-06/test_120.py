from code_120 import maximum

def test():
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    assert maximum([0, 0, 0, 0, 0], 3) == [0, 0, 0]
    assert maximum([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == [5, 6, 7, 8, 9]
    assert maximum([9, 8, 7, 6, 5, 4, 3, 2, 1], 4) == [6, 7, 8, 9]
    assert maximum([0], 0) == []
    assert maximum([-5, -4, -3, -2, -1], 3) == [-3, -2, -1]
    assert maximum([0, 0, 0, 0, 0], 0) == []
    assert maximum([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
