from code_40 import triples_sum_to_zero

def test():
    assert triples_sum_to_zero([1, 3, 5, 0]) == False
    assert triples_sum_to_zero([1, 3, -2, 1]) == True
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert triples_sum_to_zero([1]) == False
    assert triples_sum_to_zero([0, 0, 0]) == True
    assert triples_sum_to_zero([-1, 0, 1, 2, -1, -4]) == True
    assert triples_sum_to_zero([5, -5, 1, 2, 3]) == True
    assert triples_sum_to_zero([1, 2, 3, 4, 5]) == False
    assert triples_sum_to_zero([0, 1, 2, 3, 4, -7]) == True
