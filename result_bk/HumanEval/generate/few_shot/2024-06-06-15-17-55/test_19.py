from code_19 import sort_numbers
def test():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('four six two') == 'two four six'
    assert sort_numbers('eight zero nine') == 'zero eight nine'
    assert sort_numbers('five three seven') == 'three five seven'
    assert sort_numbers('one four six') == 'one four six'