from code_156 import int_to_mini_roman

def test():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(1) == 'i'
