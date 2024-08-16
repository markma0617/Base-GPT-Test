from code_5 import intersperse
def test():   
    assert intersperse([], 4) == []
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert intersperse([1, 1, 1], 0) == [1, 0, 1, 0, 1]
    assert intersperse([5, 3, 9, 7], 2) == [5, 2, 3, 2, 9, 2, 7]
    assert intersperse([0, 0, 0, 0], -1) == [0, -1, 0, -1, 0, -1, 0]