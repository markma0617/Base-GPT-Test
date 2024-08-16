from code_33 import sort_third
def test():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert sort_third([5, 2, 1, 6, 4, 3, 9, 8, 7]) == [1, 2, 3, 4, 7, 6, 9, 8, 5]
    assert sort_third([1, 1, 1, 4, 3, 3, 7, 6, 6]) == [1, 1, 1, 3, 4, 3, 6, 7, 6]
    assert sort_third([3, 6, 9, 1, 4, 7, 2, 5, 8]) == [1, 6, 3, 2, 4, 7, 5, 8, 9]
    assert sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 8, 7, 1, 5, 4, 9, 2, 6]
    assert sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sort_third([]) == []
    assert sort_third([1, 1, 1]) == [1, 1, 1]
    assert sort_third([2, 3, 1, 5, 4, 6]) == [1, 3, 2, 4, 5, 6]