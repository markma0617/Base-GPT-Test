from code_20 import find_closest_elements

def test():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0]) == (3.9, 4.0)
    assert find_closest_elements([1.0, 2.0, 4.0, 6.0, 8.0]) == (2.0, 4.0)
    assert find_closest_elements([5.0, 10.0, 15.0, 20.0, 25.0]) == (15.0, 20.0)
