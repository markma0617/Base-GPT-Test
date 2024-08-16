from code_122 import add_elements
def test():
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert add_elements([1, 22, 333, 4444, 55555], 3) == 356
    assert add_elements([11, 222, 3333, 4444, 5555], 5) == 946