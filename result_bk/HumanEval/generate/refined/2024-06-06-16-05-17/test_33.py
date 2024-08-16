from code_33 import sort_third
def test():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 2, 1, 4, 5, 6, 9, 8, 7, 10]