from code_19 import sort_numbers

def test():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('two seven eight zero') == 'zero two seven eight'
    assert sort_numbers('four six five') == 'four five six'
    assert sort_numbers('eight one four nine') == 'one four eight nine'
    assert sort_numbers('zero five two') == 'zero two five'
