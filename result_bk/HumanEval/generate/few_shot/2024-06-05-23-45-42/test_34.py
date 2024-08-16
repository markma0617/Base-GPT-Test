from code_34 import unique
def test():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert unique([]) == []
    assert unique([5, 5, 5, 5, 5]) == [5]
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique([1, 2, 2, 1, 1, 2]) == [1, 2]