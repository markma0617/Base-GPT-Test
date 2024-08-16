from code_122 import add_elements

def test():
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert add_elements([100, 10, 1000, 99, 888, 777, 66, 55], 7) == 366
    assert add_elements([1, 2, 3, 4, 5], 3) == 6
    assert add_elements([99, 88, 77, 66, 55, 44, 33, 22, 11], 6) == 220
    assert add_elements([10, 20, 30, 40, 50, 60], 4) == 100
