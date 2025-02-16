from code_0 import has_close_elements

def test():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.1, 4.0, 5.0], 0.2) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 0.0) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.5], 0.5) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.1], 0.1) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.01) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 1.0) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.01], 0.001) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 0.9) == False
