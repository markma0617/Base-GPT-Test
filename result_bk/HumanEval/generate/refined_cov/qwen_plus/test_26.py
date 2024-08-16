from code_26 import remove_duplicates

def test():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([5, 5, 3, 3, 1, 1, 2, 2]) == [5, 3, 1, 2]
    assert remove_duplicates([1, 2, 3, 4, 5, 5, 5]) == [1, 2, 3, 4]
