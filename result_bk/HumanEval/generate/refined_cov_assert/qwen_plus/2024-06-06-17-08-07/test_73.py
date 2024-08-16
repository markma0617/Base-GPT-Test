from code_73 import smallest_change

def test():
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert smallest_change([1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 4, 5, 6, 7]) == 3
    assert smallest_change([1, 2, 2, 1, 3, 3]) == 2
    assert smallest_change([1, 2, 3, 4, 5, 4, 3, 2, 1, 2]) == 3
    assert smallest_change([1, 2, 3, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 4, 3, 2, 1, 5]) == 1
    assert smallest_change([1, 2, 3, 4, 4, 3, 2, 1]) == 0
