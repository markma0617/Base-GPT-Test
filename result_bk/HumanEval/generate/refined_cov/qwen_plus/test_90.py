from code_90 import next_smallest

def test():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([3, 1, 2, 5, 4]) == 2
    assert next_smallest([4, 4, 4, 4]) == None
