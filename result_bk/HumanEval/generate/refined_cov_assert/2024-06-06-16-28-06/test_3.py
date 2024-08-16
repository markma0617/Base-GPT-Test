from code_3 import below_zero

def test():
    assert below_zero([1, 2, 3]) == False
    assert below_zero([1, 2, -4, 5]) == True
    assert below_zero([-100, 200, 300, -400]) == True
    assert below_zero([100, 200, 300, 400]) == False
    assert below_zero([0, 0, 0, 0, 0, -1]) == True
    assert below_zero([0, 0, 0, 0, 0, 0]) == False
    assert below_zero([10, -10, 10, -10, 10]) == True
    assert below_zero([1, 2, 3, -6, 4, 5, -15]) == True
    assert below_zero([-1, -2, -3, -4, 10]) == True
    assert below_zero([1, 2, 3, 4, 5, 6]) == False
