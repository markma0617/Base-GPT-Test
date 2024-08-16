from code_3 import below_zero

def test():
    assert below_zero([1, 2, 3]) == False
    assert below_zero([1, 2, -4, 5]) == True
    assert below_zero([0, 0, 0, 0, 0, 0]) == False
