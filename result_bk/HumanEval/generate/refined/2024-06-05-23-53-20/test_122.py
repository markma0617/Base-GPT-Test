from code_122 import add_elements
def test():
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert add_elements([12, 45, 67, 89], 2) == 57
    assert add_elements([10, 20, 30, 40, 50], 3) == 60