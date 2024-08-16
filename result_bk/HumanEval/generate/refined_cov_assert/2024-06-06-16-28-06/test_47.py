from code_47 import median

def test():
    assert median([3, 1, 2, 4, 5]) == 3
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 2, 3, 4]) == 2.5
    assert median([5, 8, 2, 9, 12]) == 8
    assert median([1, 1, 1, 1, 1]) == 1
    assert median([2, 5, 7, 3, 8]) == 5
    assert median([9, 4, 6, 3, 2, 1, 8]) == 4
    assert median([6, 8, 10, 12, 14, 16]) == 11.0
    assert median([10, 20, 30, 40, 50, 60, 70, 80]) == 45.0
    assert median([5]) == 5
