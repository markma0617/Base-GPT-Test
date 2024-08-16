from code_34 import unique

def test():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert unique([1, 2, 2, 3, 4, 4, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert unique([]) == []
