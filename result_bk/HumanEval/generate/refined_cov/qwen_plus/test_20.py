from code_20 import find_closest_elements

def test():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([1.0, 2.0, 3.9, 4.1, 5.0]) == (3.9, 4.1)
    assert find_closest_elements([1.0, 2.0, 7.0, 4.0, 5.0]) == (2.0, 4.0)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.1, 5.9]) == (5.1, 5.9)
