from code_35 import max_element

def test():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
    assert max_element([-10, -9, -8, -7]) == -7
    assert max_element([0]) == 0
    assert max_element([]) == None
