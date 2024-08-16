from code_19 import sort_numbers
def test():   
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('two four six') == 'two four six'
    assert sort_numbers('seven nine eight') == 'eight nine seven'
    assert sort_numbers('five zero one') == 'zero one five'
    assert sort_numbers('two two three') == 'two two three'