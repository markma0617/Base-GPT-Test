from code_70 import strange_sort_list
def test():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([]) == []
    assert strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3]
    assert strange_sort_list([-1, -2, -3, -4]) == [-4, -1, -3, -2]