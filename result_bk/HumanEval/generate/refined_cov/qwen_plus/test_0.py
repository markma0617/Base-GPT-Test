from code_0 import has_close_elements

def test():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.2) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.9) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.9], 0.1) == True