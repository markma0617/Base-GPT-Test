from code_123 import get_odd_collatz

def test():
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(2) == []
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(6) == []
    assert get_odd_collatz(7) == [1, 7]
    assert get_odd_collatz(8) == []
    assert get_odd_collatz(10) == []
    assert get_odd_collatz(15) == [1, 15, 46]
    assert get_odd_collatz(32) == []
    assert get_odd_collatz(93) == [1, 93, 280, 140, 70, 35]
