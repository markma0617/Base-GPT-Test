from code_145 import digits_sum
from code_145 import order_by_points

def test():   
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
