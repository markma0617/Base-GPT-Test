from code_72 import will_it_fly
def test():
    assert will_it_fly([1, 2], 5) == False
    assert will_it_fly([3, 2, 3], 1) == False
    assert will_it_fly([3, 2, 3], 9) == True