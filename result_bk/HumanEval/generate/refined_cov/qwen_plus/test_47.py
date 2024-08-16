from code_47 import median

def test():
    assert median([3, 1, 2, 4, 5]) == 3
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 2, 3, 4]) == 2.5
    assert median([1.5, 2.5, 3.5]) == 2.5
    assert median([10, 20, 30, 40, 50, 60]) == 35
