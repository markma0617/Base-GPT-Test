from code_8 import sum_product
def test():
    assert sum_product([]) == (0, 1)
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([-1, -2, 3, 4, 5]) == (9, -120)
    assert sum_product([0, 0, 0, 0]) == (0, 0)
    assert sum_product([2, 2, 2, 2, 2]) == (10, 32)