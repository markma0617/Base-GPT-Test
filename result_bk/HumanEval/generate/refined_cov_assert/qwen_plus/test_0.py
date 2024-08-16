from code_0 import has_close_elements

def test():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.99, 4.01, 5.0], 0.1) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.0) == False
    assert has_close_elements([1.0, 1.1, 1.2, 1.3, 1.4], 0.2) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 1.5) == False
    assert has_close_elements([1.0, 1.01, 1.02, 1.03, 1.04], 0.005) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.55) == False
    assert has_close_elements([1.0, 2.0, 3.1, 4.0, 5.0], 0.1) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], 2.0) == False
