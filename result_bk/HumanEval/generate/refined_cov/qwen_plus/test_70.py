from code_70 import strange_sort_list
def test(): 
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([]) == []
    assert strange_sort_list([3, 1, 5, 2, 6]) == [1, 6, 3, 5, 2]
    assert strange_sort_list([9, 7, 5, 3, 1]) == [1, 9, 3, 7, 5]