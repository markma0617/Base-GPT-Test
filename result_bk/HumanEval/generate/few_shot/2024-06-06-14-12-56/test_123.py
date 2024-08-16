from code_123 import get_odd_collatz

def test():
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(10) == [1, 5, 7, 9]
    assert get_odd_collatz(20) == [1, 5, 7, 9, 11, 13, 15, 17, 19]
    assert get_odd_collatz(50) == [1, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
