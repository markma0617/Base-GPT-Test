from code_100 import make_a_pile
def test():
    assert make_a_pile(0) == []
    assert make_a_pile(1) == [1]
    assert make_a_pile(3) == [3, 5, 7]