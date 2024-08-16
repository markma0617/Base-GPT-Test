from code_70 import strange_sort_list

def test():   
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([]) == []
    assert strange_sort_list([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert strange_sort_list([1, 2, 3, 4, 5, 6]) == [1, 6, 2, 5, 3, 4]
    assert strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3]
    assert strange_sort_list([-1, 0, 1, 2, 3]) == [-1, 3, 0, 2, 1]
    assert strange_sort_list([-5, -2, -1, 0, 3]) == [-5, 3, -2, 0, -1]
    assert strange_sort_list([100, 200, 300, 400, 500]) == [100, 500, 200, 400, 300]
    assert strange_sort_list([10, 20, 10, 20, 10, 20]) == [10, 20, 10, 20, 10, 20]
