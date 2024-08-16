from code_129 import minPath

def test():
    assert minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == [1, 2, 1]
    assert minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1) == [1]
    assert minPath([[1, 3, 2], [4, 5, 6], [7, 8, 9]], 4) == [1, 3, 1, 2]
    assert minPath([[5, 9, 3], [4, 1, 6], [2, 8, 7]], 2) == [1, 2]
    assert minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [1, 2, 1, 2, 1]
