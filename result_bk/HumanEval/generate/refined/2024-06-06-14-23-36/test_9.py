from code_9 import rolling_max

def test():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([5, 3, 8, 2, 5, 7, 9]) == [5, 5, 8, 8, 8, 9, 9]
    assert rolling_max([10, 7, 6, 12, 9, 15]) == [10, 10, 10, 12, 12, 15]
