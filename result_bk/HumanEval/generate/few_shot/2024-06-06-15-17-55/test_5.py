from code_5 import intersperse

def test():
    assert intersperse([], 4) == []
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
