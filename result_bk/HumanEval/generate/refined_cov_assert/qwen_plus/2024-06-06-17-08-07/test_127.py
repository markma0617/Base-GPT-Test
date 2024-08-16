from code_127 import intersection

def test():
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((3, 5), (2, 4)) == "NO"
    assert intersection((0, 5), (3, 7)) == "NO"
    assert intersection((-2, 0), (0, 2)) == "YES"
    assert intersection((1, 1), (1, 1)) == "NO"
    assert intersection((0, 0), (0, 0)) == "NO"
    assert intersection((10, 12), (11, 13)) == "YES"
    assert intersection((-5, -3), (-7, -4)) == "NO"
