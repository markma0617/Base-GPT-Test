from code_35 import max_element

def test():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
    assert max_element([-10, -9, -8]) == -8
    assert max_element([0]) == 0
    assert max_element([]) == None
    assert max_element([1.5, 2.7, 3.2]) == 3.2
    assert max_element([float('-inf'), float('inf')]) == float('inf')
    assert max_element(['c', 'a', 'z']) == 'z'
    assert max_element([True, False, 1, 0]) == 1
    assert max_element([{'value': 3}, {'value': 1}, {'value': 2}]) == {'value': 3}
