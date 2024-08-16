from code_47 import median

def test():
    assert median([3, 1, 2, 4, 5]) == 3
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 2, 3, 4]) == 2.5
    assert median([1, 2, 3, 4, 5, 6]) == 3.5
    assert median([1, 2, 3, 4, 5, 6, 7]) == 4
    assert median([]) is None
    assert median([1]) == 1
    assert median([-5, -3, -1, 1, 3, 5]) == 0.0
    assert median([1.5, 2.5, 3.5]) == 2.5
    assert median([1.1, 2.2, 3.3, 4.4, 5.5]) == 3.3
