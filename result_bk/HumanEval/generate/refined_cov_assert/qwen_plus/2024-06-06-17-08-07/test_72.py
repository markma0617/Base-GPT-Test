from code_72 import will_it_fly

def test():
    assert will_it_fly([1, 2], 5) == False
    assert will_it_fly([3, 2, 3], 1) == False
    assert will_it_fly([3, 2, 3], 9) == True
    assert will_it_fly([3], 5) == True
    assert will_it_fly([1, 1], 2) == True
    assert will_it_fly([2, 1], 2) == False
    assert will_it_fly([2, 2, 2], 6) == True
    assert will_it_fly([2, 2, 3], 7) == False
    assert will_it_fly([1, 1, 1, 1], 4) == True
    assert will_it_fly([1, 2, 1, 3], 8) == False
