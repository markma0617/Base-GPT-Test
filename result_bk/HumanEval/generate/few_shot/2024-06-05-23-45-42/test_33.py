from code_33 import sort_third

def test():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert sort_third([7, 1, 3, 9, 2, 6, 5, 8, 4]) == [3, 1, 5, 9, 2, 6, 4, 8, 7]
    assert sort_third([10, 15, 20, 25, 30, 35, 40, 45]) == [20, 15, 40, 25, 30, 35, 10, 45]
