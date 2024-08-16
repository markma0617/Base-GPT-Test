from code_57 import monotonic

def test():
    assert monotonic([1, 2, 4, 20]) == True
    assert monotonic([1, 20, 4, 10]) == False
    assert monotonic([4, 1, 0, -10]) == True
    assert monotonic([1, 1, 1, 1]) == True
    assert monotonic([1]) == True
    assert monotonic([]) == True
    assert monotonic([1, 2, 3, 4, 4, 5, 5, 5]) == True
    assert monotonic([5, 5, 5, 4, 4, 3, 2, 1]) == True
    assert monotonic([5, 5, 5, 4, 4, 3, 2, 2, 1]) == False
    assert monotonic([-10, 0, 1, 4]) == True
