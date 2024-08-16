from code_85 import add

def test():
    assert add([4, 2, 6, 7]) == 2
    assert add([1, 3, 5, 7, 9]) == 0
    assert add([2, 4, 6, 8, 10, 12, 14]) == 20
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 12
