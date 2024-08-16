from code_9 import rolling_max
def test():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([5, 3, 6, 2, 8, 1]) == [5, 5, 6, 6, 8, 8]
    assert rolling_max([10, 9, 8, 7, 6, 5]) == [10, 10, 10, 10, 10, 10]