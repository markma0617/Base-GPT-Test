from code_145 import order_by_points

def test():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([10, 91, -2, 23, -31]) == [-2, 10, 23, -31, 91]
    assert order_by_points([-99, 9, 99, -9]) == [-9, 9, -99, 99]
    assert order_by_points([123, -456, 78, -901, 234]) == [78, -456, 123, -901, 234]
