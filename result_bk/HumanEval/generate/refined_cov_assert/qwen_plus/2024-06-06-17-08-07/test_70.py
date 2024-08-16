from code_70 import strange_sort_list

def test():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([]) == []
    assert strange_sort_list([9, 1, 6, 3, 7]) == [1, 9, 3, 6, 7]
    assert strange_sort_list([2, 1, 4, 3]) == [1, 4, 2, 3]
    assert strange_sort_list([3, 1, 2, 5, 4]) == [1, 5, 2, 4, 3]
    assert strange_sort_list([-1, -5, -3, -2]) == [-5, -1, -3, -2]
    assert strange_sort_list([10, 20, 30, 40]) == [10, 40, 20, 30]
    assert strange_sort_list([1, 10, 2, 9, 3, 8]) == [1, 10, 2, 9, 3, 8]
    assert strange_sort_list([0, -1, 1]) == [-1, 1, 0]
