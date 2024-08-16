from code_5 import intersperse

def test():   
    assert intersperse([], 4) == []
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert intersperse([0], 7) == [0]
    assert intersperse([5, 6, 7, 8], 0) == [5, 0, 6, 0, 7, 0, 8]
    assert intersperse([2, 3], 1) == [2, 1, 3]
