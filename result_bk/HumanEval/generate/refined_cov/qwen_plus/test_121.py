from code_121 import solution

def test():
    assert solution([5, 8, 7, 1]) == 12
    assert solution([3, 3, 3, 3, 3]) == 9
    assert solution([30, 13, 24, 321]) == 0
    assert solution([1, 2, 3, 4, 5, 6]) == 0
    assert solution([9, 2, 7, 4, 11, 3]) == 11
