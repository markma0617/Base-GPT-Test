from code_57 import monotonic

def test():
    assert monotonic([1, 2, 4, 20]) == True
    assert monotonic([1, 20, 4, 10]) == False
    assert monotonic([4, 1, 0, -10]) == True
    assert monotonic([1, 1, 1, 1]) == True
    assert monotonic([1, 1, 2, 3]) == True
    assert monotonic([3, 2, 1, 0]) == True
    assert monotonic([1, 3, 2, 0]) == False
