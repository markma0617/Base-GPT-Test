from code_9 import rolling_max
def test():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 9, 9, 9, 9, 9, 9, 9, 9]
    assert rolling_max([3, 5, 2, 8, 1, 7]) == [3, 5, 5, 8, 8, 8]