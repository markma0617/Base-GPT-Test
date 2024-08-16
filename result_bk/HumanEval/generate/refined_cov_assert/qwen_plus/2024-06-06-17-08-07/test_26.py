from code_26 import remove_duplicates

def test():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([1, 2, 3, 3, 4]) == [1, 2, 4]
    assert remove_duplicates([1, 2, 2, 2, 3, 4]) == [1, 3, 4]
    assert remove_duplicates([1, 2, 3, 4, 4, 5, 5]) == [1, 2, 3]
    assert remove_duplicates([1, 2, 2, 3, 3, 4, 4]) == [1]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([1, 1, 1, 1]) == []
    assert remove_duplicates([1, 2, 2, 3, 3]) == [1]
    assert remove_duplicates([1, 2, 3, 4, 4, 5, 5, 6, 6, 7]) == [1, 2, 3, 7]
