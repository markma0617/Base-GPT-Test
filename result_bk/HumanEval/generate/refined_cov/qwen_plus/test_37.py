from code_37 import sort_even

def test():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([10, 9, 8, 7, 6, 5]) == [5, 9, 6, 7, 8, 10]
    assert sort_even([3, 2, 1, 0]) == [0, 2, 1, 3]
    assert sort_even([]) == []
