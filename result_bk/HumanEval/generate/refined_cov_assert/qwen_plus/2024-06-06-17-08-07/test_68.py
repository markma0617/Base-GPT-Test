from code_68 import pluck

def test():
    assert pluck([]) == []
    assert pluck([1]) == []
    assert pluck([1, 3]) == []
    assert pluck([2, 3]) == [2, 0]
    assert pluck([4, 2, 3]) == [2, 1]
    assert pluck([1, 2, 3]) == [2, 1]
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert pluck([0, 5, 3, 0, 4, 2]) == [0, 0]
    assert pluck([5, 7, 9, 11]) == []
    assert pluck([2, 2, 3, 4]) == [2, 0]
