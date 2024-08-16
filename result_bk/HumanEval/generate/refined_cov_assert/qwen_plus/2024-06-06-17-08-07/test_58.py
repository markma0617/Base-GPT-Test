from code_58 import common

def test():
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert common([1, 2, 3, 4], [4, 5, 6, 7]) == [4]
    assert common([10, 20, 30, 40], [20, 30, 40, 50, 60]) == [20, 30, 40]
    assert common([1, 2, 3], [3, 4, 5]) == [3]
    assert common([1, 1, 2], [2, 2, 3]) == [2]
    assert common([], []) == []
    assert common([1, 2, 3], []) == []
    assert common([], [1, 2, 3]) == []
    assert common([1, 2, 3], [4, 5, 6]) == []
