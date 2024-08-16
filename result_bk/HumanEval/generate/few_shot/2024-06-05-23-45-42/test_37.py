from code_37 import sort_even
def test():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([4, 3, 2, 1]) == [2, 3, 1, 4]
    assert sort_even([10, 20, 5, 15, 30, 25]) == [5, 20, 10, 25, 15, 30]
    assert sort_even([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]