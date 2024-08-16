from code_121 import solution

def test():
    assert solution([5, 8, 7, 1]) == 12
    assert solution([3, 3, 3, 3, 3]) == 9
    assert solution([30, 13, 24, 321]) == 0
    assert solution([1, 2, 3, 4, 5, 6]) == 0
    assert solution([9, 12, 5, 17, 22, 7]) == 12
    assert solution([2, 5, 3, 7, 8, 9]) == 12
    assert solution([11, 22, 33, 44, 55, 66]) == 0
    assert solution([0, 1, 2, 3, 4, 5]) == 5
    assert solution([4, 6, 8, 10, 12, 13]) == 13
    assert solution([31, 2, 15, 4, 17, 6]) == 15 + 17
