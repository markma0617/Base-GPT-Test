from code_109 import move_one_ball

def test():
    assert move_one_ball([3, 4, 5, 1, 2]) == True
    assert move_one_ball([3, 5, 4, 1, 2]) == False
