from code_0 import has_close_elements
def test():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
    assert has_close_elements([5.5, 6.0, 7.0, 9.2], 0.1) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], 0.9) == True