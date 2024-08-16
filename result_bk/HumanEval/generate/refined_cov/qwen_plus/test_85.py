from code_85 import add

def test():
    assert add([4, 2, 6, 7]) == 2
    assert add([1, 2, 3, 4, 5, 6]) == 4
    assert add([0, 1, 2, 3, 4, 5]) == 0
