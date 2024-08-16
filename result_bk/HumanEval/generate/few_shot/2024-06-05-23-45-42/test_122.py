from code_122 import add_elements
def test():
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert add_elements([-100, 50, 300, 45, 2, 75, 101], 6) == -50
    assert add_elements([11, 22, 33, 44, 55, 66, 77, 88, 99], 5) == 220
    assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 45
    assert add_elements([100, 200, 300, 400, 500, 600, 700, 800, 900], 3) == 600