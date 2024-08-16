from code_19 import sort_numbers

def test():   
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('seven two eight') == 'two seven eight'
    assert sort_numbers('nine zero six two') == 'zero two six nine'
    assert sort_numbers('five four one') == 'one four five'
    assert sort_numbers('eight') == 'eight'
