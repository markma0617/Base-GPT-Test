from code_70 import strange_sort_list

def test():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([]) == []

    assert strange_sort_list([3, 7, 2, 8, 1]) == [1, 8, 2, 7, 3]
    assert strange_sort_list([9, 5, 2, 9, 3, 6, 1]) == [1, 9, 2, 9, 3, 6, 5]
    assert strange_sort_list([2, 3, 5, 7, 9, 11]) == [2, 11, 3, 9, 5, 7]
