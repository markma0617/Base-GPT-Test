from code_87 import get_row
def test():
    assert get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    assert get_row([], 1) == []
    assert get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]