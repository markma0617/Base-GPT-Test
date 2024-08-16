from code_34 import unique
def test():   
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert unique([1, 1, 1, 1, 1]) == [1]
    assert unique([]) == []
    assert unique([7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7]
    assert unique([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert unique([2, 2, 2, 2]) == [2]
    assert unique([3]) == [3]
    assert unique([0, 0, 0, 0, 0]) == [0]
    assert unique([5, 5, 5, 5, 5, 5, 5, 5]) == [5]
    assert unique([99, 88, 77, 66, 55]) == [55, 66, 77, 88, 99]