from code_129 import minPath

def test():
    assert minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == [1, 2, 1]
    assert minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1) == [1]
    assert minPath([[1, 4, 2], [3, 5, 7], [8, 9, 6]], 4) == [1, 2, 1, 2]
    assert minPath([[2, 1, 3], [4, 5, 6], [7, 8, 9]], 2) == [2, 1]
    assert minPath([[9, 8, 7], [6, 5, 4], [3, 2, 1]], 5) == [1, 2, 1, 2, 1]
