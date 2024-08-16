from code_123 import get_odd_collatz

def test():   
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(10) == [1, 5]
    assert get_odd_collatz(20) == [1, 5, 13, 21, 53]
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(3) == [1, 3, 5, 19, 9]
