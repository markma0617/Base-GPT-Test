from code_85 import add

def test():
    assert add([4, 2, 6, 7]) == 2
    assert add([1, 3, 5, 7, 9]) == 0
    assert add([2, 4, 6, 8]) == 10
    assert add([1, 2, 3, 4, 5, 6, 7, 8]) == 14
    assert add([10, 20, 30, 40, 50]) == 60
    assert add([11, 22, 33, 44, 55]) == 0
    assert add([0, 0, 0, 0, 0, 0, 0, 1]) == 0
    assert add([9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert add([2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36
