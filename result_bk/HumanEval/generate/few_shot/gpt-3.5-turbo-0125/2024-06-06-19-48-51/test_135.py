from code_135 import can_arrange

def test():   
    assert can_arrange([1,2,4,3,5]) == 3
    assert can_arrange([1,2,3]) == -1
