from code_53 import add

def test():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
    assert add(-1, 4) == 3
    assert add(0, 0) == 0
    assert add(100, 200) == 300
    assert add(-5, 15) == 10
    assert add(10, -5) == 5
    assert add(-10, -10) == -20
    assert add(1000, 2000) == 3000
    assert add(-100, -200) == -300
