from code_116 import sort_array

def test():
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    assert sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    assert sort_array([10, 7, 14, 6, 9]) == [6, 7, 9, 10, 14]
    assert sort_array([0, 1, 2, 3, 15]) == [0, 1, 2, 3, 15]
