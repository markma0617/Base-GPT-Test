from code_127 import is_prime
from code_127 import intersection
def test():
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((-10, -5), (-3, 0)) == "NO"
    assert intersection((7, 10), (2, 6)) == "YES"