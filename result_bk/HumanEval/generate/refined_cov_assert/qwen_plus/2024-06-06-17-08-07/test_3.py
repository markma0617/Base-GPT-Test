from code_3 import below_zero

def test():
    assert below_zero([1, 2, 3]) == False
    assert below_zero([1, 2, -4, 5]) == True
    assert below_zero([5, -3, -2, 7]) == True
    assert below_zero([10, -20, 30, -40, 50]) == True
    assert below_zero([1, 1, 1, 1, 1]) == False
    assert below_zero([-1, -2, -3, -4, -5]) == True
    assert below_zero([0, 0, 0, 0, 0]) == False
    assert below_zero([100, -99]) == False
    assert below_zero([1, -1, 1, -1, 1]) == True
    assert below_zero([2, -1, 3, -2, 1]) == False
