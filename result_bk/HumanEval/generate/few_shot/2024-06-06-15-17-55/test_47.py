from code_47 import median

def test():
    assert median([3, 1, 2, 4, 5]) == 3
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([7, 3, 1, 4]) == 3.5
    assert median([9, 2, 5, 8, 4]) == 5
    assert median([5, 5, 5, 5, 5, 5]) == 5
