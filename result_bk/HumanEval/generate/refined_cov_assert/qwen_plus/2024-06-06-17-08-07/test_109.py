from code_109 import move_one_ball

def test():
    assert move_one_ball([]) == True
    assert move_one_ball([1, 2, 3, 4, 5]) == True
    assert move_one_ball([5, 4, 3, 2, 1]) == True
    assert move_one_ball([3, 4, 5, 1, 2]) == True
    assert move_one_ball([3, 5, 4, 1, 2]) == False
    assert move_one_ball([1, 3, 2, 5, 4]) == True
    assert move_one_ball([4, 1, 3, 2, 5]) == False
    assert move_one_ball([2, 1, 3, 5, 4]) == True
    assert move_one_ball([5, 4, 3, 2, 1, 6]) == False
    assert move_one_ball([1, 2, 3, 4, 5, 6]) == True
