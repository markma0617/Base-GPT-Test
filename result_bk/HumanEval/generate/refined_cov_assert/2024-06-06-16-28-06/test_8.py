from code_8 import sum_product

def test():
    assert sum_product([]) == (0, 1)
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([5, 6, 7]) == (18, 210)
    assert sum_product([-1, -2, -3]) == (-6, -6)
    assert sum_product([0, 0, 0, 0]) == (0, 0)
    assert sum_product([10]) == (10, 10)
    assert sum_product([-1, 2, -3, 4]) == (2, 24)
    assert sum_product([1, 1, 1, 1, 1, 1, 1, 1]) == (8, 1)
    assert sum_product([2, 2, 2, 2, 2]) == (10, 32)
    assert sum_product([0, 1, 2, 3, 4, 5]) == (15, 0)
