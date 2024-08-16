from code_34 import unique

def test():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert unique([1, 2, 2, 3, 3, 3, 4, 4, 4]) == [1, 2, 3, 4]
    assert unique([]) == []
    assert unique([-1, 0, 1, -1, 2, 1]) == [-1, 0, 1, 2]
    assert unique([1.1, 1.2, 1.1, 1.3, 1.2]) == [1.1, 1.2, 1.3]
    assert unique([True, False, True, True, False]) == [False, True]
    assert unique(["a", "b", "b", "c", "c", "c"]) == ["a", "b", "c"]
    assert unique([1+2j, 1+2j, 3+4j, 3+4j]) == [1+2j, 3+4j]
    assert unique([None, None, "a", "b", "b"]) == [None, "a", "b"]
    assert unique(range(10, 20, 2), range(11, 20, 2)) == list(range(10, 20, 2))
