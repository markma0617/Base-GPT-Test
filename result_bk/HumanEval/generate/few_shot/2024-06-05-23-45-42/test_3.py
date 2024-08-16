from code_3 import below_zero
def test():   
    assert below_zero([1, 2, 3]) == False
    assert below_zero([1, 2, -4, 5]) == True
    assert below_zero([100, -50, 20, -200]) == True
    assert below_zero([10, 20, 30, -100, 40, 50]) == True
    assert below_zero([10, 10, 5, 10]) == False