from code_121 import solution

def test():
    assert solution([5, 8, 7, 1]) == 12
    assert solution([3, 3, 3, 3, 3]) == 9
    assert solution([30, 13, 24, 321]) == 0
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 16
    assert solution([7, 12, 9, 5, 2, 6, 3]) == 16
    assert solution([1, 2, 3, 4]) == 0
    assert solution([11, 22, 33, 44, 55]) == 33
    assert solution([9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
    assert solution([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
    assert solution([1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 16
