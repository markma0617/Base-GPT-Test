from code_39 import prime_fib

def test():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) == 211
    assert prime_fib(7) == 1597
    assert prime_fib(8) == 2584
    assert prime_fib(9) == 6103515625
    assert prime_fib(10) == 100590803329501761
