from code_26 import remove_duplicates

def test():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([5, 5, 3, 3, 1, 1, 7]) == [7]
    assert remove_duplicates([0, 0, 0, 1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([42, 42, 6, 6, 9, 9, 1, 1]) == [42, 6, 9, 1]
    assert remove_duplicates([10, 20, 30, 40, 50, 50]) == [10, 20, 30, 40]
