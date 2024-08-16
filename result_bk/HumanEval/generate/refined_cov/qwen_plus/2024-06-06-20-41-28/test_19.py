from code_19 import sort_numbers

def test():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('nine eight seven six five four three two one zero') == '零 one two three four five six seven eight nine'
    assert sort_numbers('random five seven two') == 'two five seven'
