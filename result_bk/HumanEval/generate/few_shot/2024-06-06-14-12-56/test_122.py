from code_122 import add_elements

def test():   
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert add_elements([1, 22, 333, 4444, 55, 666, 7777, 88, 999], 6) == 1056
    assert add_elements([10, 20, 30, 40, 50, 60, 70, 80, 90], 9) == 450
