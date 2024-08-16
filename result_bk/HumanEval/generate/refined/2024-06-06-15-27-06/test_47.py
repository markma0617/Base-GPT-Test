from code_47 import median
def test():
    assert median([3, 1, 2, 4, 5]) == 3
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([2, 3, 5, 7, 11, 13, 17]) == 7
    assert median([1, 3, 5, 7, 9, 11]) == 6.0