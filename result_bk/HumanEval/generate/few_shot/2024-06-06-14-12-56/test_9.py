from code_9 import rolling_max

def test():   
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]
    assert rolling_max([1, 3, 5, 2, 4, 6]) == [1, 3, 5, 5, 5, 6]
    assert rolling_max([10, 20, 15, 30, 25, 35, 20]) == [10, 20, 20, 30, 30, 35, 35]
    assert rolling_max([7, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 7]
