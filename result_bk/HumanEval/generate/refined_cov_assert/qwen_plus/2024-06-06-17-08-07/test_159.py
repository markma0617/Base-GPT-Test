from code_159 import eat

def test():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]
    assert eat(0, 0, 1000) == [0, 1000]
    assert eat(500, 500, 1000) == [1000, 0]
    assert eat(750, 250, 1000) == [1000, 0]
    assert eat(999, 1, 1000) == [1000, 0]
    assert eat(100, 900, 500) == [600, 0]
    assert eat(50, 500, 450) == [500, 0]
