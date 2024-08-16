from code_37 import sort_even

def test():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([10, 9, 8, 7, 6]) == [6, 9, 8, 7, 10]
    assert sort_even([2, 1, 4, 3, 6, 5]) == [2, 1, 4, 3, 6, 5]
    assert sort_even([100, 50, 200, 150]) == [50, 100, 150, 200]
