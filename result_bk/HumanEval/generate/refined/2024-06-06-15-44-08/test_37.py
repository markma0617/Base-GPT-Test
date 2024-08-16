from code_37 import sort_even

def test():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([4, 1, 3, 2, 5]) == [2, 1, 4, 3, 5]
