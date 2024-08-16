from code_160 import do_algebra

def test():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '-', '+'], [10, 5, 2, 3]) == 11
    assert do_algebra(['**', '//', '+'], [2, 3, 4, 2]) == 6
