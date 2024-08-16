from code_85 import add

def test():   
    assert add([4, 2, 6, 7]) == 2
    assert add([1, 3, 5, 7]) == 0
    assert add([0, 1, 2, 3, 4, 5, 6]) == 4
    assert add([10, 20, 30, 40, 50]) == 20
