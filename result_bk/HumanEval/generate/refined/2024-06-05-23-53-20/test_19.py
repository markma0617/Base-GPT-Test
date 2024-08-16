from code_19 import sort_numbers

def test():   
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('two six eight') == 'two six eight'
    assert sort_numbers('seven zero four') == 'zero four seven'
