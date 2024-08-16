from code_5 import intersperse

def test():
    assert intersperse([], 4) == []
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert intersperse([5, 6, 7, 8], 9) == [5, 9, 6, 9, 7, 9, 8]
