from code_5 import intersperse

def test():
    assert intersperse([], 4) == []
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert intersperse([1, 1, 1], 0) == [1, 0, 1, 0, 1]
    assert intersperse([5, 3, 9], 7) == [5, 7, 3, 7, 9]
    assert intersperse([0, 0, 0], 2) == [0, 2, 0, 2, 0]
    assert intersperse([10, 20, 30, 40], 50) == [10, 50, 20, 50, 30, 50, 40]
    assert intersperse([1, 2], -1) == [1, -1, 2]
    assert intersperse([3, 6, 9], -3) == [3, -3, 6, -3, 9]
    assert intersperse([100], 0) == [100]
    assert intersperse([42, 3.14, -1], 99) == [42, 99, 3.14, 99, -1]
