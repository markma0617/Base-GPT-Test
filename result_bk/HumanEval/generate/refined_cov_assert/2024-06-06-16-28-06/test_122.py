from code_122 import add_elements

def test():
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert add_elements([10, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 90000000], 3) == 330
    assert add_elements([11, 22, 33, 44, 55, 66, 77, 88, 99], 5) == 198
    assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 45
    assert add_elements([11, 22, 33, 44, 55, 66, 77, 88, 99], 1) == 11
    assert add_elements([111, 222, 333, 444, 555, 666, 777, 888, 999], 9) == 999
    assert add_elements([11, 22, 33, 44, 55, 66, 77, 88, 99], 9) == 495
    assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 1
    assert add_elements([111, 222, 333, 444, 555, 666, 777, 888, 999], 4) == 999
    assert add_elements([11, 22, 33, 44, 55, 66, 77, 88, 99], 3) == 66
