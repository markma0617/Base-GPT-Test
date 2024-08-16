from code_35 import max_element
def test():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
    assert max_element([10, 5, 20, 30, 15]) == 30