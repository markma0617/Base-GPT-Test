from code_86 import anti_shuffle

def test():
    assert anti_shuffle('Hi') == 'Hi'
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
    assert anti_shuffle('Python Programming') == 'Pyhon gnimmargorP'
    assert anti_shuffle('A quick brown dog jumps over the lazy fox') == 'A eijmpqkuo  bdgolnorswv'
    assert anti_shuffle('SpaceX launches rockets to Mars') == 'AceSX lgnhruotw to Mras'
    assert anti_shuffle('The cat in the hat') == 'The cainht ot hte'
    assert anti_shuffle('12345abcde') == '12345abcde'
    assert anti_shuffle('') == ''
    assert anti_shuffle('   ') == '   '
