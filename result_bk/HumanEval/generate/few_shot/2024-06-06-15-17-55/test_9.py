from code_9 import rolling_max

def test():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([5, 3, 1, 2, 4, 6, 5]) == [5, 5, 5, 5, 5, 6, 6]
    assert rolling_max([10, 9, 8, 7, 6, 5, 4, 3]) == [10, 10, 10, 10, 10, 10, 10, 10]
    assert rolling_max([1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1]
