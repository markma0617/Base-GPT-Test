from code_145 import order_by_points

def test():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([12, 34, -56, 78, -90]) == [-90, 12, 34, -56, 78]
    assert order_by_points([4, 13, -22, 0, 9]) == [0, 4, 9, 13, -22]
    assert order_by_points([123, 321, -456, -987, 654]) == [-987, -456, 123, 321, 654]
