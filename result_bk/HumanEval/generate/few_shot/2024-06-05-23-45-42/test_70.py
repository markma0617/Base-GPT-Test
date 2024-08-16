from code_70 import strange_sort_list

def test():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([]) == []
    assert strange_sort_list([5, 3, 1, 2, 4, 6]) == [1, 6, 2, 5, 3, 4]
    assert strange_sort_list([-2, 3, 0, -5, 9]) == [-5, 9, -2, 3, 0]
