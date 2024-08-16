from code_46 import fib4
def test(): 
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 2
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(10) == 136
    assert fib4(15) == 2298
    assert fib4(20) == 61232