from code_97 import multiply

def test():
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72
    assert multiply(2020, 1851) == 0
    assert multiply(14, -15) == 20
    assert multiply(99, 88) == 72
    assert multiply(123, 456) == 18
    assert multiply(-77, -66) == 42
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0
    assert multiply(101, 202) == 2
