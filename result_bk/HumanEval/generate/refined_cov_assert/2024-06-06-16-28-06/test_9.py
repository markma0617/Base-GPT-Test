from code_9 import rolling_max
def test():
    assert rolling_max([]) == []
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]
    assert rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]
    assert rolling_max([-1, 0, -2, 4, 3]) == [-1, 0, 0, 4, 4]
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([5, 3, 1, 2, 4]) == [5, 5, 5, 5, 5]
    assert rolling_max([5, 3, 7, 2, 4]) == [5, 5, 7, 7, 7]
    assert rolling_max([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert rolling_max([-1, -2, -3, -1, -4, -5]) == [-1, -1, -1, -1, -1, -1]