from code_26 import remove_duplicates
def test():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([1, 1, 1, 2, 3, 4, 4, 5, 5, 5]) == [2, 3]
    assert remove_duplicates([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]