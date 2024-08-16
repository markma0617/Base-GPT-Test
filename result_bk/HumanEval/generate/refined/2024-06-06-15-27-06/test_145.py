from code_145 import order_by_points

def test():   
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([12, 9, 34, 78]) == [9, 34, 12, 78]
