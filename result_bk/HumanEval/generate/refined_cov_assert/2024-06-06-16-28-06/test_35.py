from code_35 import max_element

def test():   
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
    assert max_element([1]) == 1
    assert max_element([-1, -2, -3, -4, -5]) == -1
    assert max_element([0, 0, 0, 0, 0]) == 0
    assert max_element([-1, 0, 1]) == 1
    assert max_element([2, 4, 6, 8, 10]) == 10
    assert max_element([-10, -20, -30, -40, -5]) == -5
    assert max_element([2, 2, 2, 2, 2]) == 2
    assert max_element([1, 3, 5, 4, 2]) == 5
