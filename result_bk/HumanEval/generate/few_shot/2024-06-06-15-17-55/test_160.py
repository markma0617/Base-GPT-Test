from code_160 import do_algebra

def test():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '//'], [2, 3, 7]) == 4
    assert do_algebra(['**', '+', '-'], [2, 4, 3, 5]) == 14
