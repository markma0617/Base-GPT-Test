from code_19 import sort_numbers

def test():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('seven eight two') == 'two seven eight'
    assert sort_numbers('four six nine') == 'four six nine'
