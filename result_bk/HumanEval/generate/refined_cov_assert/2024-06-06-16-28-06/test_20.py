from code_20 import find_closest_elements

def test():   
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.9, 5.0)
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0, 2.7]) == (2.7, 2.0)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([5.0, 5.0, 5.0, 5.0, 5.0, 5.0]) == (5.0, 5.0)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 0.0]) == (0.0, 1.0)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) == (5.0, 6.0)
    assert find_closest_elements([1.0, 2.0, 2.1, 2.2, 3.0, 4.0]) == (2.0, 2.1)
    assert find_closest_elements([1.0, 1.1, 1.2, 1.3, 1.4, 1.5]) == (1.0, 1.1)
