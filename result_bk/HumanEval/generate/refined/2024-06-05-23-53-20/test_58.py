from code_58 import common
def test():
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert common([1, 2, 3, 4, 5], [6, 7, 8, 9]) == []