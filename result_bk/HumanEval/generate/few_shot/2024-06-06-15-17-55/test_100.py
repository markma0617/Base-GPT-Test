from code_100 import make_a_pile

def test():   
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
