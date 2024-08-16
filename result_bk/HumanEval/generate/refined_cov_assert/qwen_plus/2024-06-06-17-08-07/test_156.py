from code_156 import int_to_mini_roman

def test():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(12) == 'xii'
    assert int_to_mini_roman(42) == 'xlii'
    assert int_to_mini_roman(99) == 'xcix'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(999) == 'cmcmcmcmcmcmcmcmcmcmcmcm'
