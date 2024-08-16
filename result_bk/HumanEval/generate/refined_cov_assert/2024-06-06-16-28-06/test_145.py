from code_145 import order_by_points

def test():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([100, 3, 71, -93, -9]) == [-9, 100, 3, 71, -93]
    assert order_by_points([12, -45, 67, 89, 100]) == [100, 12, 67, 89, -45]
    assert order_by_points([7, -5, 3, 0, 10]) == [0, 3, -5, 7, 10]
    assert order_by_points([-9, -1, -8, -99, 0]) == [-9, -99, -1, -8, 0]
    assert order_by_points([111, 222, 333, 444, 555]) == [111, 222, 333, 444, 555]
    assert order_by_points([9, 99, 999, 9999, 99999]) == [9, 99, 999, 9999, 99999]
    assert order_by_points([0, 1, 10, 100, 1000]) == [0, 1, 10, 100, 1000]
    assert order_by_points([-1, -10, -100, -1000, -10000]) == [-1, -10, -100, -1000, -10000]
