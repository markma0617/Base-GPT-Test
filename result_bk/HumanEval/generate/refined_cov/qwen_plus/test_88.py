from code_88 import sort_array

def test():
    assert sort_array([]) == []
    assert sort_array([5]) == [5]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([0, 0, 0]) == [0, 0, 0]
    assert sort_array([1, 1, 1]) == [1, 1, 1]
    assert sort_array([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([0, 1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
