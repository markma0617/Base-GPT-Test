from code_3 import below_zero
def test():
    assert below_zero([1, 2, 3]) == False
    assert below_zero([1, 2, -4, 5]) == True
    assert below_zero([5, -3, 2, 1, -10, 8]) == True
    assert below_zero([10, 20, 30, -60, 50]) == True
    assert below_zero([100, -50, 20, 30, 40, -100]) == True