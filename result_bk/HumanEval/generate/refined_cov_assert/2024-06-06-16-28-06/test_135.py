from code_135 import can_arrange

def test():
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    assert can_arrange([1, 2, 3]) == -1
    assert can_arrange([5, 4, 3, 2, 1]) == 4
    assert can_arrange([3, 5, 2, 8, 4, 6]) == 2
    assert can_arrange([10, 8, 6, 5, 3, 1]) == 5
    assert can_arrange([5]) == -1
    assert can_arrange([5, 5, 5, 5, 5]) == -1
    assert can_arrange([1, 2, 3, 4, 5]) == -1
    assert can_arrange([5, 4, 3, 2, 1, 5, 4, 3, 2]) == 8
    assert can_arrange([1, 3, 2, 5, 4]) == 2
