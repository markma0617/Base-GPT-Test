from code_37 import sort_even

def test():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([2, 1, 4, 3]) == [1, 2, 3, 4]
    assert sort_even([10, 20, 30, 40, 50, 60]) == [10, 60, 20, 50, 30, 40]
    assert sort_even([7, 4, 3, 8, 2, 5, 1, 6]) == [1, 8, 2, 6, 3, 5, 4, 7]
    assert sort_even([3, 2, 1]) == [1, 2, 3]
    assert sort_even([100, 200, 300, 400]) == [100, 400, 200, 300]
    assert sort_even([11, 12, 13, 14, 15, 16, 17]) == [11, 16, 12, 15, 13, 14, 17]
    assert sort_even([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert sort_even([2, 3, 1, 4]) == [1, 2, 3, 4]
