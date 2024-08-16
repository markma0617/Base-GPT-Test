from code_120 import maximum

def test():
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    assert maximum([], 5) == []
    assert maximum([1, 2, 3, 4, 5], 0) == []
    assert maximum([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1]
    assert maximum([-1000, -999, 0, 1, 1000], 3) == [1000, 1, 0]
    assert maximum([1] * 1000, 500) == [1] * 500
    assert maximum([-1000] * 1000, 1) == [-1000]
    assert maximum([i % 1000 for i in range(1000)], 750) == sorted([i % 1000 for i in range(750, 1750)])
