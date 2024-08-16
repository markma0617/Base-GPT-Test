from code_62 import derivative

def test():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([0, 1, 2, 3, 4]) == [1, 6, 12]
    assert derivative([4, 0, 0, 0, 5]) == [0, 0, 0, 20]
    assert derivative([1]) == []