from code_159 import eat

def test():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]
    assert eat(0, 0, 0) == [0, 0]
    assert eat(0, 1, 0) == [1, 0]
    assert eat(0, 0, 1) == [0, 0]
    assert eat(1000, 1000, 1000) == [2000, 0]
    assert eat(500, 500, 1000) == [1000, 500]
    assert eat(1000, 0, 1000) == [1000, 1000]
