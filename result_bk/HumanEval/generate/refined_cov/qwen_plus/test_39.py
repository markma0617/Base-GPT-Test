from code_39 import prime_fib

def test():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) == 21
    assert prime_fib(10) == 151
    assert prime_fib(20) == 1597