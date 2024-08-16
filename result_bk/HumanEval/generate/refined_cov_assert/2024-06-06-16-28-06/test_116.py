from code_116 import sort_array

def test():
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    assert sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    assert sort_array([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert sort_array([]) == []
    assert sort_array([8, 4, 2, 1]) == [1, 2, 4, 8]
    assert sort_array([7, 3, 15, 31]) == [3, 7, 15, 31]
    assert sort_array([16, 32, 64, 128]) == [16, 32, 64, 128]
    assert sort_array([9, 4, 9, 4]) == [4, 4, 9, 9]
    assert sort_array([-1, -2, -3, -4]) == [-4, -3, -2, -1]
