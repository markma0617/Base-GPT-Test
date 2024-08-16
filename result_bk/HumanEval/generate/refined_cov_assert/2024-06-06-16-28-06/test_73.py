from code_73 import smallest_change

def test():
    assert smallest_change([1,2,3,5,4,7,9,6]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert smallest_change([1, 1, 1, 2, 2, 2, 1, 1]) == 4
    assert smallest_change([3, 2, 1, 1, 2, 3]) == 0
    assert smallest_change([3, 2, 1, 2, 2, 3]) == 1
    assert smallest_change([1, 2, 3, 2, 3, 2, 1]) == 0
    assert smallest_change([5, 4, 3, 2, 1]) == 2
    assert smallest_change([1, 1, 2, 2, 1, 1]) == 0
