from code_43 import pairs_sum_to_zero

def test():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
    assert pairs_sum_to_zero([-1, 1, 3, 2]) == True
    assert pairs_sum_to_zero([0, 5, -5, 3]) == True
    assert pairs_sum_to_zero([4, -4, 3, -3]) == True
    assert pairs_sum_to_zero([1, 2, 3, -6]) == True
    assert pairs_sum_to_zero([10, -10, 5, -5]) == True
