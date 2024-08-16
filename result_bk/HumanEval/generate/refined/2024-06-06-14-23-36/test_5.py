from code_5 import intersperse
def test():
    assert intersperse([], 4) == []
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert intersperse([5, 10, 15, 20], 7) == [5, 7, 10, 7, 15, 7, 20]