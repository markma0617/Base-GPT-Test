from code_87 import get_row
def test():
    assert get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    assert get_row([], 1) == []

    assert get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]

    assert get_row([[1, 2], [3, 4]], 5) == []

    assert get_row([[1, 1, 1], [2, 2, 2]], 1) == [(0, 2), (0, 1), (0, 0)]

    assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [(1, 1)]

    assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9) == [(2, 2)]

    assert get_row([[1, 2, 3], [3, 2, 1]], 3) == [(0, 2), (1, 0)]

    assert get_row([[1, 2], [2, 1]], 2) == [(0, 1), (1, 0)]

    assert get_row([[1]], 1) == [(0, 0)]