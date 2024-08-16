from code_37 import sort_even

def test():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([1, 3, 2, 4, 5]) == [2, 3, 1, 4, 5]
    assert sort_even([7, 5, 9, 3, 6]) == [3, 5, 7, 9, 6]
    assert sort_even([10, 9, 8, 7, 6, 5]) == [5, 9, 7, 8, 6, 10]
    assert sort_even([]) == []
    assert sort_even([1]) == [1]
    assert sort_even([1, 2, 3, 4, 5, 6, 7]) == [3, 2, 5, 4, 7, 6, 1]
    assert sort_even([2, 4, 6, 8, 10]) == [4, 2, 6, 8, 10]
    assert sort_even([1, 3, 5, 7, 9, 11, 13]) == [3, 1, 5, 7, 9, 11, 13]
