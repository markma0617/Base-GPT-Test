from code_145 import order_by_points

def test():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([123, 45, -67, 8910, -1234]) == [-67, 45, 123, -1234, 8910]
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]
    assert order_by_points([1, 1, 2, 2, 3, 3]) == [1, 1, 2, 2, 3, 3]
    assert order_by_points([10, -20, 30, -40]) == [-40, -20, 10, 30]
    assert order_by_points([1, 11, 2, 22, 3, 33]) == [1, 2, 3, 11, 22, 33]
    assert order_by_points([1, -1, 2, -2, 3, -3]) == [-3, -2, -1, 1, 2, 3]
    assert order_by_points([12, -34, 56, -78, 90]) == [-34, -78, 12, 56, 90]
    assert order_by_points([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
