from code_62 import derivative

def test():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([0, 1, 0, 1]) == [1, 0, 1]
    assert derivative([4, 0, 0, 0, 5]) == [0, 0, 0, 5]
    assert derivative([1, -2, 3, -4, 5]) == [-2, 6, -12, 20]
    assert derivative([0, 0, 0, 0, 0, 1]) == [0, 0, 0, 0, 1]
    assert derivative([1, 1, 1, 1, 1]) == [1, 4, 6, 4, 1]
    assert derivative([0, 1, -2, 3, -4]) == [1, -6, 12, -20]
    assert derivative([2, -3, 4, -5, 6]) == [-3, 12, -20, 30]
    assert derivative([1e-9, 1, 1e-9, 1, 1e-9]) == [0, 1, 0, 1, 0]
