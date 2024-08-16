from code_19 import sort_numbers

def test():   
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('four six nine') == 'four six nine'
    assert sort_numbers('two seven eight') == 'two seven eight'
