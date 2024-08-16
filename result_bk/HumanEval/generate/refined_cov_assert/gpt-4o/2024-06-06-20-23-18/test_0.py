from code_0 import has_close_elements

def test():   
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
    assert has_close_elements([1.0, 1.5, 2.5], 0.4) == True
    assert has_close_elements([1.0, 2.0, 3.0], 1.1) == True
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([], 0.5) == False
    assert has_close_elements([1.0], 0.5) == False
