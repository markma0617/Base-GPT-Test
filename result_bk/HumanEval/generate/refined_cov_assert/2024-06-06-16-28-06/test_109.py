from code_109 import move_one_ball

def test():   
    assert move_one_ball([]) == True
    assert move_one_ball([1]) == True
    assert move_one_ball([1, 2, 3, 4, 5]) == True
    assert move_one_ball([3, 4, 5, 1, 2]) == True
    assert move_one_ball([3, 5, 4, 1, 2]) == False
    assert move_one_ball([5, 1, 2, 3, 4]) == True
    assert move_one_ball([4, 1, 2, 3, 5]) == True
    assert move_one_ball([4, 2, 3, 1, 5]) == False
    assert move_one_ball([3, 4, 5, 1, 2, 6]) == False
    assert move_one_ball([3, 1, 4, 2, 5]) == True
