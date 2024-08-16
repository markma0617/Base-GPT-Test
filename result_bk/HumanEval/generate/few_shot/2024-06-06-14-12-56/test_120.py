from code_120 import maximum
def test():
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    assert maximum([5, 4, 3, 2, 1], 0) == []
    assert maximum([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert maximum([1, 2, 3, 4, 5], 2) == [4, 5]
    assert maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]