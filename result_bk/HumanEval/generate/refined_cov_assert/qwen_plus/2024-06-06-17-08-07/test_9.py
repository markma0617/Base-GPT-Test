from code_9 import rolling_max

def test():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([5, 3, 7, 2, 8, 1, 9]) == [5, 5, 7, 7, 8, 8, 9]
    assert rolling_max([10, 9, 8, 7, 6, 5]) == [10, 10, 10, 10, 10, 10]
    assert rolling_max([1, -1, 0, -2, 3]) == [1, 1, 1, 1, 3]
    assert rolling_max([]) == []
    assert rolling_max([-1, -2, -3]) == [-1, -1, -1]
    assert rolling_max([4, 2, 4, 1, 5, 3]) == [4, 4, 4, 4, 5, 5]
    assert rolling_max([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert rolling_max([3, 2, 1, 2, 0]) == [3, 3, 3, 3, 3]
    assert rolling_max([0, -1, -2, -1]) == [0, 0, 0, 0]
