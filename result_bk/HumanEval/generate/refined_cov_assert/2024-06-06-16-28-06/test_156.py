from code_156 import int_to_mini_roman
def test():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(999) == 'cmxcix'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(399) == 'cccxcix'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(4) == 'iv'