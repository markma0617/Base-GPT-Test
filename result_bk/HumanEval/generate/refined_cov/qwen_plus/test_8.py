from code_8 import sum_product
def test():
    assert sum_product([]) == (0, 1)
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([-1, 2, -3, 4]) == (-6, -24)
    assert sum_product([0, 1, 2, 3]) == (0, 0)
    assert sum_product([5]) == (5, 5)