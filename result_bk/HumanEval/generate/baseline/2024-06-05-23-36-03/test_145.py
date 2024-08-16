from code_145 import order_by_points
def test_order_by_points():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([123, 456, -789, -321, 0]) == [0, -321, 123, -789, 456]
    assert order_by_points([99, -99, 9, -9]) == [-9, 9, -99, 99]
    assert order_by_points([100, 101, 102, 103, 104]) == [100, 101, 102, 103, 104]
    assert order_by_points([-100, -101, -102, -103, -104]) == [-100, -101, -102, -103, -104]