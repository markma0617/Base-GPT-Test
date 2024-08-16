from code_115 import max_fill

def test():
    assert max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6
    assert max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5
    assert max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0
    assert max_fill([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], 2) == 3
    assert max_fill([[0, 1, 1, 0, 0], [1, 0, 1, 0, 0]], 3) == 2
    assert max_fill([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]], 4) == 2
    assert max_fill([[0, 0, 0, 0]], 1) == 0
    assert max_fill([[1, 1, 1, 1]], 1) == 4
    assert max_fill([[1, 1, 1, 1]], 3) == 1
    assert max_fill([[0, 0, 0, 0, 0, 0, 0]], 7) == 0
