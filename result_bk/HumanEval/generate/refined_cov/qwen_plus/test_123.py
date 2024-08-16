from code_123 import get_odd_collatz

def test():
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(8) == [1]
    assert get_odd_collatz(27) == [1, 82, 247, 742, 2227, 6682, 20047]
    assert get_odd_collatz(100) == [1]
