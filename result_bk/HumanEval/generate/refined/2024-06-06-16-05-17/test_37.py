from code_37 import sort_even

def test():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([2, 6, 1, 4, 3, 8, 5, 7]) == [1, 6, 3, 4, 5, 8, 2, 7]
