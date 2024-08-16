from code_62 import derivative

def test():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([4, 2, 1, 3]) == [2, 2, 9]
    assert derivative([0, 1, 1, 1, 1]) == [1, 2, 3, 4]
    assert derivative([1, 0, 0, 1]) == [0, 0, 3]
    assert derivative([5, 2, 3, 1]) == [2, 6, 3]
    assert derivative([1, 1, 1, 1, 1]) == [1, 2, 3, 4]
    assert derivative([2, 3, 4, 5]) == [3, 8, 15]
    assert derivative([2, 2, 2, 2]) == [2, 4, 6]
    assert derivative([1, 3, 5, 7]) == [3, 10, 21]
