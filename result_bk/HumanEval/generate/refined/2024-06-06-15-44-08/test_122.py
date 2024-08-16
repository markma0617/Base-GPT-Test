from code_122 import add_elements

def test():   
    assert add_elements([111,21,3,4000,5,6,7,8,9], 4) == 24
    assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 15
    assert add_elements([12, 34, 56, 78, 90], 3) == 102
