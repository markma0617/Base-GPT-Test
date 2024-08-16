from code_37 import sort_even

def test():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([2, 1, 4, 3, 6, 5]) == [1, 6, 2, 3, 4, 5]
    assert sort_even([9, 4, 7, 2]) == [2, 4, 7, 9]
