from code_9 import rolling_max
def test():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([5, 2, 9, 3, 7, 1, 4, 8]) == [5, 5, 9, 9, 9, 9, 9, 9]
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]