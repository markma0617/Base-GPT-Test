from code_120 import maximum

def test():   
    assert maximum([1, 3, 4, 2, 5], 3) == [3, 4, 5]
    assert maximum([5, 4, 3, 2, 1], 2) == [4, 5]
    assert maximum([-1, -2, -4, -3, -5], 1) == [-1]
