from code_123 import get_odd_collatz
def test():
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(10) == [1, 5, 13, 3]
    assert get_odd_collatz(20) == [1, 5, 13, 3, 16, 10]
    assert get_odd_collatz(7) == [1, 7, 11, 17, 26, 13, 20, 10, 5]
    assert get_odd_collatz(16) == [1, 5, 13, 3, 16, 10, 8, 4, 2]