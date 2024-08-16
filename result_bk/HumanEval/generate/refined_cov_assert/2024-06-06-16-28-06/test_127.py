from code_127 import intersection

def test():   
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((1, 3), (2, 4)) == "NO"
    assert intersection((0, 0), (1, 1)) == "NO"
    assert intersection((5, 8), (3, 6)) == "YES"
    assert intersection((10, 15), (20, 25)) == "NO"
    assert intersection((-10, 0), (-5, 5)) == "YES"
    assert intersection((1, 3), (4, 6)) == "NO"
    assert intersection((13, 17), (10, 20)) == "YES"
