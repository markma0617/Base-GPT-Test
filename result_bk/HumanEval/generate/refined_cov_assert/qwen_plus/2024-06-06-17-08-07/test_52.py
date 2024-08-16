from code_52 import below_threshold

def test():
    assert below_threshold([1, 2, 3, 4], 5) == True
    assert below_threshold([1, 2, 100, 4], 10) == False
    assert below_threshold([0, 0, 0, 0], 1) == True
    assert below_threshold([10, 20, 30, 40], 50) == True
    assert below_threshold([-1, -2, -3, -4], 0) == True
    assert below_threshold([1.5, 2.7, 3.9, 4.1], 4.0) == False
    assert below_threshold([1, 2, 3, 4, 5], 6) == True
    assert below_threshold([5, 6, 7, 8, 9], 10) == False
    assert below_threshold([], 100) == True
    assert below_threshold([100], 0) == False
