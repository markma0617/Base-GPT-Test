from code_52 import below_threshold

def test():
    assert below_threshold([1, 2, 4, 10], 100) == True
    assert below_threshold([1, 20, 4, 10], 5) == False
    assert below_threshold([0, 0, 0, 0], 1) == True
    assert below_threshold([1, 2, 3, 4], 5) == True
    assert below_threshold([10, 20, 30, 40], 5) == False
    assert below_threshold([1, 1, 1, 1], 0) == False
    assert below_threshold([], 10) == True
    assert below_threshold([5], 10) == True
    assert below_threshold([15], 10) == False
    assert below_threshold([-5, -10, -15], -3) == False
