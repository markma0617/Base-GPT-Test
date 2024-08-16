from code_72 import will_it_fly

def test():
    assert will_it_fly([1, 2], 5) == False
    assert will_it_fly([3, 2, 3], 1) == False
    assert will_it_fly([3, 2, 3], 9) == True
    assert will_it_fly([3], 5) == True
    assert will_it_fly([1, 1, 1, 1, 1, 1], 6) == True
    assert will_it_fly([4, 1, 4], 8) == False
    assert will_it_fly([4, 1, 4], 9) == True
    assert will_it_fly([3, 3, 3, 3, 3], 17) == False
    assert will_it_fly([3, 3, 3, 3, 3], 18) == True
    assert will_it_fly([], 0) == True
