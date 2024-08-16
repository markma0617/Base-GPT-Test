from code_135 import can_arrange

def test():   
    assert can_arrange([1,2,4,3,5]) == 3
    assert can_arrange([1,2,3]) == -1
    assert can_arrange([5,4,3,2,1]) == 4
    assert can_arrange([5,4,3,2,3]) == 4
    assert can_arrange([1, 5, 3, 4, 2]) == 3
