from code_68 import pluck

def test():
    assert pluck([4, 2, 3]) == [2, 1]
    assert pluck([1, 2, 3]) == [2, 1]
    assert pluck([]) == []
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert pluck([2, 4, 6, 8]) == [2, 0]
    assert pluck([1, 3, 5, 7]) == []
    assert pluck([0, 1, 0, 1]) == [0, 0]
    assert pluck([2, 4, 6, 8, 2, 4]) == [2, 0]
    assert pluck([1, 2, 3, 4, 5, 6]) == [2, 1]
    assert pluck([9, 5, 3, 7, 1]) == []
