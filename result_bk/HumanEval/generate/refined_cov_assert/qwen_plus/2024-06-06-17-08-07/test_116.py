from code_116 import sort_array

def test():
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    assert sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    assert sort_array([10, 7, 8, 9, 6]) == [6, 7, 8, 9, 10]
    assert sort_array([12, 11, 13, 14, 10]) == [10, 11, 12, 13, 14]
    assert sort_array([15, 13, 14, 12, 11]) == [11, 12, 13, 14, 15]
    assert sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sort_array([16, 17, 18, 19, 20, 21]) == [16, 17, 18, 19, 20, 21]
    assert sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert sort_array([24, 25, 26, 27, 28, 29, 30, 31]) == [24, 25, 26, 27, 28, 29, 30, 31]
