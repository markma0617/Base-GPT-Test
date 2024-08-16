from code_97 import multiply

def test():
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72
    assert multiply(2020, 1851) == 0
    assert multiply(14,-15) == 20
    assert multiply(0, 0) == 0
    assert multiply(10, 0) == 0
    assert multiply(0, 10) == 0
    assert multiply(10, 10) == 0
    assert multiply(-10, -10) == 0
    assert multiply(-10, 10) == 0
