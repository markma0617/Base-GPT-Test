from code_52 import below_threshold
def test():
    assert below_threshold([1, 2, 4, 10], 100) == True
    assert below_threshold([1, 20, 4, 10], 5) == False
    assert below_threshold([0, 0.1, 0.2, 0.3], 0.5) == True