from code_19 import sort_numbers
def test():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('zero two four eight') == 'zero two four eight'
    assert sort_numbers('seven six nine') == 'six seven nine'