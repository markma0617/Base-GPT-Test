from code_5 import intersperse
def test():
    assert intersperse([], 4) == []
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert intersperse([5, 10, 15], 0) == [5, 0, 10, 0, 15]
    assert intersperse([1], 8) == [1]
    assert intersperse([4, 5, 6, 7], 1) == [4, 1, 5, 1, 6, 1, 7]
    assert intersperse([9, 10], 9) == [9, 9, 10]
    assert intersperse([2, 2, 2, 2], 2) == [2, 2, 2, 2, 2, 2, 2]
    assert intersperse([0, 0, 0, 0], 5) == [0, 5, 0, 5, 0, 5, 0]
    assert intersperse([3, 7, 9, 1, 5], 6) == [3, 6, 7, 6, 9, 6, 1, 6, 5]
    assert intersperse([5, 5, 5], 0) == [5, 0, 5, 0, 5]