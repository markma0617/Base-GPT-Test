from code_127 import intersection

def test():
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((3, 5), (2, 4)) == "NO"
    assert intersection((-2, 2), (1, 3)) == "NO"
    assert intersection((-4, -1), (-3, 1)) == "YES"
