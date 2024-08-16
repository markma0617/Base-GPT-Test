from code_85 import add

def test():
    assert add([4, 2, 6, 7]) == 2
    assert add([1, 2, 3, 4, 5]) == 4
    assert add([0, 2, 4, 6, 8]) == 0
    assert add([10, 9, 8, 7, 6, 5]) == 18
    assert add([3, 2, 1, 0]) == 0
    assert add([1, 3, 5, 7, 9]) == 0
    assert add([2, 4, 6]) == 6
    assert add([100, 50, 30, 70, 90]) == 120
    assert add([5, 10, 15, 20, 25]) == 30
    assert add([33, 22, 11]) == 22
