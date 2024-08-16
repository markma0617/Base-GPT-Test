from code_55 import fib

def test():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(8) == 21
    assert fib(10) == 55
    assert fib(20) == 6765
    assert fib(30) == 832040
