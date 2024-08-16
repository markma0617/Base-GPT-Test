from code_160 import do_algebra

def test():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['-', '*', '+'], [7, 3, 2, 4]) == 13
    assert do_algebra(['*', '+'], [1, 2, 3]) == 7
