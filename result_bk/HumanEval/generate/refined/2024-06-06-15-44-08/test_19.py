from code_19 import sort_numbers
def test():   
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('five two eight zero') == 'zero two five eight'
    assert sort_numbers('six seven three nine') == 'three six seven nine'