from code_123 import get_odd_collatz

def test():
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(2) == []
    assert get_odd_collatz(3) == [1, 5]
    assert get_odd_collatz(4) == [3, 5]
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(6) == [1, 5]
    assert get_odd_collatz(7) == [1, 5, 7]
    assert get_odd_collatz(8) == [1, 5, 7]
    assert get_odd_collatz(9) == [1, 5, 7]
    assert get_odd_collatz(10) == [1, 5, 7]
