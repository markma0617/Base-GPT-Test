from code_33 import sort_third
def test():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert sort_third([3, 6, 9, 12]) == [3, 6, 9, 12]