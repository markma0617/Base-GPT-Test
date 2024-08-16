from code_42 import incr_list

def test():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert incr_list([]) == []
    assert incr_list([-1, 0, 1]) == [0, 1, 2]
    assert incr_list([100, 200, 300]) == [101, 201, 301]
    assert incr_list([float(-1), 0.0, 1.5]) == [float(0), 1.0, 2.5]
    assert incr_list([2 ** 10, 3 ** 5, 5 ** 2]) == [2 ** 11, 3 ** 6, 5 ** 3]
    assert incr_list([10 ** 9, -10, -10 ** 9]) == [10 ** 10, -9, -10 ** 8]
    assert incr_list([0.1, 0.2, 0.3]) == [0.2, 0.3, 0.4]
    assert incr_list([1, -1, 0]) == [2, 0, 1]
