from code_88 import sort_array

def test():
    assert sort_array([]) == []
    assert sort_array([5]) == [5]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([0, 1]) == [1, 0]
    assert sort_array([1, 3, 5]) == [5, 3, 1]
    assert sort_array([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    assert sort_array([9, 9, 9, 9]) == [9, 9, 9, 9]
    assert sort_array([7, 8, 9, 10]) == [10, 9, 8, 7]
    assert sort_array([4, 6, 8, 10, 12, 14]) == [14, 12, 10, 8, 6, 4]
