from code_33 import sort_third

def test():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert sort_third([10, 11, 7, 8, 9, 6, 5, 3, 4]) == [3, 11, 7, 8, 9, 6, 5, 10, 4]
