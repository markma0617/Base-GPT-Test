from code_122 import add_elements

def test():
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert add_elements([100, 200, 300, 400, 500], 3) == 100
    assert add_elements([1, 2, 3, 4, 5], 5) == 1 + 2
    assert add_elements([999, 1000, 1001, 10, 11], 2) == 10
    assert add_elements([123, 456, 789, 1, 2, 3], 6) == 1 + 2
    assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 1
    assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 1 + 2 + 3 + 4 + 5
    assert add_elements([100, 20, 3, 4, 5, 6, 7, 8, 9], 1) == 100
    assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 111], 10) == 1 + 2 + 3 + 4 + 5 + 6
    assert add_elements([1000, 2000, 3000], 3) == 0
