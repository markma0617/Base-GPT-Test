from code_90 import next_smallest

def test():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([3, 1, 2, 3, 4]) == 2
    assert next_smallest([4, 4, 3, 2, 1]) == 2
    assert next_smallest([-1, 0, 1]) == 0
    assert next_smallest([10, 20, 30, 15]) == 15
    assert next_smallest([100, 200, 100, 300]) == None
    assert next_smallest([10, 9, 8, 7, 6]) == 7
