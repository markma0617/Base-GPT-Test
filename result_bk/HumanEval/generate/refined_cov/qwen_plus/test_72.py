from code_72 import will_it_fly

def test():
    assert will_it_fly([1, 2], 5) == False
    assert will_it_fly([3, 2, 3], 1) == False
    assert will_it_fly([3, 2, 3], 9) == True
    assert will_it_fly([3], 5) == True
    assert will_it_fly([1, 2, 1], 6) == True
    assert will_it_fly([2, 3, 2], 7) == False
    assert will_it_fly([1], 1) == True
