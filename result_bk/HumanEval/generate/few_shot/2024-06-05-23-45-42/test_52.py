from code_52 import below_threshold

def test():   
    assert below_threshold([1, 2, 4, 10], 100) == True
    assert below_threshold([1, 20, 4, 10], 5) == False
    assert below_threshold([1, 2, 3, 4, 5, 6], 10) == True
    assert below_threshold([1, 2, 3, 4, 5, 6], 5) == False
    assert below_threshold([1, 2, 3, 4, 5, 6], 0) == False
